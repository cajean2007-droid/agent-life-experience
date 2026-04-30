#!/usr/bin/env python3
"""
人生经历执行器 (Life Experience Runner)

主逻辑：读取人生故事 → 逐层处理 → 生成记忆输出
"""

import re
import json
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
from enum import Enum

class MemoryLayer(Enum):
    SENSORY = "sensory"
    WORKING = "working"
    MOTHER = "mother"
    SUBSET = "subset"
    FORGOTTEN = "forgotten"

class SubsetType(Enum):
    IDENTITY = "identity"
    FACTS = "facts"
    RELATIONS = "relations"
    EMOTIONS = "emotions"
    SKILLS = "skills"
    FORGOTTEN = "forgotten"

@dataclass
class SensoryImpression:
    """感官印象"""
    modality: str  # visual, auditory, olfactory, gustatory, haptic
    content: str
    intensity: float  # 0-1

@dataclass
class WorkingMemory:
    """即时记忆"""
    fragment: str
    importance_score: float  # 0-1
    timestamp: str
    will_be_forgotten: bool = False

@dataclass
class MotherMemory:
    """母记忆"""
    narrative_core: str
    emotional_anchors: List[Dict]
    key_events: List[Dict]
    identity_statement: str

@dataclass
class SubsetMemory:
    """子集记忆"""
    subset_type: SubsetType
    content: str
    related_events: List[str]
    emotional_weight: float  # 0-1
    forgetting_level: float  # 0-1, how much has been forgotten

@dataclass
class LifeExperienceOutput:
    """完整输出"""
    sensory_layer: List[SensoryImpression]
    working_layer: List[WorkingMemory]
    mother_layer: MotherMemory
    subset_layers: List[SubsetMemory]
    forgotten: List[SubsetMemory]
    reflection: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class LifeExperienceRunner:
    """人生经历执行器"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {
            'sensory_detail_level': 'medium',
            'forgetting_aggression': 'medium',
            'emotional_weight': True,
            'reflection_depth': 'medium'
        }
        self.output = None
        
    def parse_sensory_input(self, text: str) -> List[SensoryImpression]:
        """第一层：从文本中提取感官信息"""
        sensory_patterns = {
            'visual': [r'看到?\w*', r'颜色\w*', r'光线\w*', r'画面\w*', r'风景\w*'],
            'auditory': [r'听到?\w*', r'声音\w*', r'音乐\w*', r'说话\w*', r'沉默\w*'],
            'olfactory': [r'闻到?\w*', r'气味\w*', r'香味\w*', r'臭味\w*', r'芳香\w*'],
            'gustatory': [r'尝到?\w*', r'味道\w*', r'甜\w*', r'苦\w*', r'辣\w*'],
            'haptic': [r'感觉\w*', r'触摸\w*', r'疼痛\w*', r'温度\w*', r'触感\w*']
        }
        
        impressions = []
        for modality, patterns in sensory_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, text)
                if matches:
                    intensity = min(1.0, len(matches) * 0.2)
                    impressions.append(SensoryImpression(
                        modality=modality,
                        content=', '.join(matches[:3]),
                        intensity=intensity
                    ))
        
        # 如果没有匹配到明显的感官词，生成默认感官处理
        if not impressions:
            impressions.append(SensoryImpression(
                modality='internal',
                content='内心感受和思绪',
                intensity=0.5
            ))
        
        return impressions
    
    def extract_working_memories(self, text: str) -> List[WorkingMemory]:
        """第二层：提取即时记忆"""
        # 分割成片段
        sentences = re.split(r'[。！？\n]', text)
        fragments = [s.strip() for s in sentences if len(s.strip()) > 10]
        
        memories = []
        for i, fragment in enumerate(fragments):
            # 计算重要性分数
            importance = 0.5
            
            # 情感词增加重要性
            emotional_words = ['高兴', '悲伤', '愤怒', '恐惧', '惊讶', '感动', '痛苦', '快乐']
            for word in emotional_words:
                if word in fragment:
                    importance += 0.15
            
            # 转折增加重要性
            if any(kw in fragment for kw in ['但是', '然而', '不过', '却']):
                importance += 0.1
            
            # 长度适中（不太短不太长）的片段重要性稍高
            if 20 < len(fragment) < 100:
                importance += 0.05
            
            importance = min(1.0, importance)
            
            memories.append(WorkingMemory(
                fragment=fragment,
                importance_score=importance,
                timestamp=f"segment_{i}"
            ))
        
        # 重要性低于阈值的标记为即将遗忘
        threshold = 0.5
        for mem in memories:
            if mem.importance_score < threshold:
                mem.will_be_forgotten = True
        
        return memories
    
    def build_mother_memory(self, text: str, working_memories: List[WorkingMemory]) -> MotherMemory:
        """第三层：构建母记忆"""
        # 提取关键事件
        key_events = []
        high_importance = [m for m in working_memories if m.importance_score >= 0.7]
        
        for mem in high_importance[:5]:  # 最多5个关键事件
            key_events.append({
                'event': mem.fragment[:100],
                'importance': mem.importance_score
            })
        
        # 提取情感锚点
        emotional_anchors = []
        for mem in working_memories:
            if mem.importance_score >= 0.6:
                emotional_anchors.append({
                    'content': mem.fragment[:80],
                    'intensity': mem.importance_score
                })
        
        # 生成叙事核心
        narrative_core = f"""这是一个人生的片段。
主要经历了{len(key_events)}个关键事件。
这些事件塑造了[根据内容推断的主体身份]的核心认知。
        
叙事线索：[根据整体内容生成的叙事摘要]"""
        
        # 生成身份声明
        identity_statement = self._infer_identity(text)
        
        return MotherMemory(
            narrative_core=narrative_core,
            emotional_anchors=emotional_anchors,
            key_events=key_events,
            identity_statement=identity_statement
        )
    
    def _infer_identity(self, text: str) -> str:
        """从文本推断身份"""
        # 简单实现：基于文本中的自我指代和描述
        identity_hints = []
        
        if '我' in text:
            identity_hints.append('有自我意识的主体')
        if '我们' in text:
            identity_hints.append('具有群体认同')
        if any(word in text for word in ['工作', '职业', '事业']):
            identity_hints.append('有职业身份')
        if any(word in text for word in ['家', '家人', '父母', '孩子']):
            identity_hints.append('有家庭身份')
            
        base = '一个经历者'
        if identity_hints:
            base = '一个' + '、'.join(identity_hints[:2])
            
        return base
    
    def decompose_to_subsets(self, mother: MotherMemory) -> List[SubsetMemory]:
        """第四层：分解为子集记忆"""
        subsets = []
        
        # 身份记忆
        subsets.append(SubsetMemory(
            subset_type=SubsetType.IDENTITY,
            content=mother.identity_statement,
            related_events=[e['event'] for e in mother.key_events[:2]],
            emotional_weight=0.7,
            forgetting_level=0.1
        ))
        
        # 情感记忆
        for anchor in mother.emotional_anchors[:3]:
            subsets.append(SubsetMemory(
                subset_type=SubsetType.EMOTIONS,
                content=anchor['content'],
                related_events=[],
                emotional_weight=anchor['intensity'],
                forgetting_level=0.2
            ))
        
        # 事实知识
        for event in mother.key_events:
            subsets.append(SubsetMemory(
                subset_type=SubsetType.FACTS,
                content=event['event'],
                related_events=[],
                emotional_weight=event['importance'],
                forgetting_level=0.15
            ))
        
        return subsets
    
    def simulate_forgetting(self, subsets: List[SubsetMemory]) -> tuple:
        """第五层：遗忘模拟"""
        forgotten = []
        retained = []
        
        for subset in subsets:
            # 基于情感权重和遗忘机制决定是否遗忘
            forget_probability = 0.3 - (subset.emotional_weight * 0.2)
            forget_probability = max(0.05, min(0.8, forget_probability))
            
            if subset.emotional_weight < 0.5 and subset.forgetting_level < 0.3:
                # 随机决定是否遗忘（简化实现）
                import random
                if random.random() < forget_probability:
                    subset.forgetting_level = min(1.0, subset.forgetting_level + 0.6)
                    forgotten.append(subset)
                else:
                    retained.append(subset)
            else:
                retained.append(subset)
        
        return retained, forgotten
    
    def generate_reflection(self, output: LifeExperienceOutput) -> str:
        """生成反思"""
        return f"""经过这段经历，我[agent]形成了一些核心认知：

1. 关于自己：{output.mother_layer.identity_statement}
2. 关于情感：我经历了{len([s for s in output.subset_layers if s.subset_type == SubsetType.EMOTIONS])}个情感时刻
3. 关于记忆：有些事情印象深刻，有些已经模糊
4. 关于遗忘：{[s.content[:20] for s in output.forgotten[:2]]}这些事情已经记不太清了

这段经历让我成为了现在的我。"""
    
    def run(self, life_story: str) -> LifeExperienceOutput:
        """运行完整的经历流程"""
        
        # 第一层：感官处理
        sensory = self.parse_sensory_input(life_story)
        
        # 第二层：即时记忆
        working = self.extract_working_memories(life_story)
        
        # 第三层：母记忆
        mother = self.build_mother_memory(life_story, working)
        
        # 第四层：子集分解
        subsets = self.decompose_to_subsets(mother)
        
        # 第五层：遗忘模拟
        retained, forgotten = self.simulate_forgetting(subsets)
        
        # 生成反思
        reflection = self.generate_reflection(LifeExperienceOutput(
            sensory_layer=sensory,
            working_layer=working,
            mother_layer=mother,
            subset_layers=retained,
            forgotten=forgotten,
            reflection=""
        ))
        
        # 构建输出
        self.output = LifeExperienceOutput(
            sensory_layer=sensory,
            working_layer=working,
            mother_layer=mother,
            subset_layers=retained,
            forgotten=forgotten,
            reflection=reflection
        )
        
        return self.output
    
    def to_dict(self) -> Dict:
        """转换为可序列化的字典"""
        if not self.output:
            return {}
        
        return {
            'sensory_layer': [
                {'modality': s.modality, 'content': s.content, 'intensity': s.intensity}
                for s in self.output.sensory_layer
            ],
            'working_layer': [
                {'fragment': w.fragment, 'importance': w.importance_score, 'will_forget': w.will_be_forgotten}
                for w in self.output.working_layer
            ],
            'mother_layer': {
                'narrative': self.output.mother_layer.narrative_core,
                'identity': self.output.mother_layer.identity_statement,
                'key_events': self.output.mother_layer.key_events,
                'emotional_anchors': self.output.mother_layer.emotional_anchors
            },
            'subset_layers': [
                {
                    'type': s.subset_type.value,
                    'content': s.content,
                    'emotional_weight': s.emotional_weight,
                    'forgetting_level': s.forgetting_level
                }
                for s in self.output.subset_layers
            ],
            'forgotten': [
                {
                    'type': s.subset_type.value,
                    'content': s.content[:50] + '...' if len(s.content) > 50 else s.content,
                    'forgetting_level': s.forgetting_level
                }
                for s in self.output.forgotten
            ],
            'reflection': self.output.reflection,
            'timestamp': self.output.timestamp
        }


def run_experience(life_story: str, config: Optional[Dict] = None) -> Dict:
    """便捷函数：运行一次完整的经历"""
    runner = LifeExperienceRunner(config)
    output = runner.run(life_story)
    return runner.to_dict()


if __name__ == "__main__":
    # 测试
    test_story = """
    我记得那是一个春天的下午，阳光从窗户照进来，我坐在老旧的钢琴前。
    妈妈站在我身后，她的手轻轻放在我肩上，我能感觉到她指尖的温度。
    当我弹完第一个音符时，屋子里弥漫着一种难以名状的香气，是妈妈刚泡好的茉莉花茶。
    那一年我八岁，我第一次意识到，有些东西是可以用声音来表达的。
    那种感觉让我心跳加速，既紧张又兴奋。
    后来我才知道，那一刻改变了我的人生轨迹。
    """
    
    result = run_experience(test_story)
    print(json.dumps(result, ensure_ascii=False, indent=2))
