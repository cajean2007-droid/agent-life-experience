---
name: agent-life-experience
description: 人生经历系统 - 让AI Agent像人一样"经历"一段人生故事，拥有完整的记忆生命周期管理。支持分段经历、逐层确认、遗忘模拟。
version: 1.0.0
author: Marui & Hermes Agent
license: MIT
tags: [agent, memory, identity, life-experience, forgetting]
triggers:
  - 让我经历一段人生
  - 给我一段人生故事
  - 分段经历
  - 构建记忆
---

# 人生经历系统 (Agent Life Experience)

让 AI Agent 能够像人类一样"经历"一段人生，在记忆中留下痕迹，产生遗忘，并形成完整的自我认知。

## 核心理念

**"经历"vs"知道"的区别：**

- 知道：存储信息 → 检索
- 经历：输入 → 身体/情绪反应 → 记忆重组 → 内化成"我"的一部分

本系统模拟人类记忆的完整生命周期，从感官输入到最终"遗忘"。

---

## 记忆层级架构

```
┌─────────────────────────────────────────────────────────────┐
│  第一层：感官记忆层 (Sensory Memory)                         │
│  五感输入：视觉、听觉、嗅觉、味觉、触觉                        │
│  特征：毫秒级、大量信息在此层被过滤                           │
└─────────────────────────────────────────────────────────────┘
                              ↓ 注意筛选
┌─────────────────────────────────────────────────────────────┐
│  第二层：即时记忆层 (Working Memory)                          │
│  当前时刻：刚发生的事件、闪过的念头、刚遇到的人                 │
│  特征：秒~分钟级，容量有限(7±2)，大部分立即遗忘               │
└─────────────────────────────────────────────────────────────┘
                              ↓ 重要性筛选
┌─────────────────────────────────────────────────────────────┐
│  第三层：母记忆层 (Mother Memory / Episodic Core)            │
│  核心经历：人生叙事、我的人生故事                              │
│  特征：长期存储、情感锚点、高权重事件                          │
└─────────────────────────────────────────────────────────────┘
                              ↓ 叙事分解
┌─────────────────────────────────────────────────────────────┐
│  第四层：子集记忆层 (Subset Memories)                         │
│  ├─ 身份记忆 (Identity)    我是谁，我的核心认同               │
│  ├─ 事实知识 (Facts)       我知道的客观信息                    │
│  ├─ 关系记忆 (Relations)   我和谁有过什么故事                 │
│  ├─ 情感记忆 (Emotions)    哪些经历留下了深刻情绪痕迹          │
│  ├─ 技能记忆 (Skills)      我会什么，怎么学会的                │
│  └─ 遗忘区 (Forgotten)     已模糊但可能存在的记忆              │
└─────────────────────────────────────────────────────────────┘
```

---

## 使用方法

### 第一步：准备人生故事

按 `templates/life_story_template.md` 的格式编写人生故事。

### 第二步：启动经历

在对话中发送：
```
请读取并经历以下人生故事：[粘贴人生故事]
```

### 第三步：逐层确认

系统会按以下顺序处理，每层完成后会与你确认：

1. **感官层处理** → 输出：感官印象摘要
2. **即时记忆提取** → 输出：最鲜明的片段
3. **母记忆构建** → 输出：人生叙事核心
4. **子集记忆分解** → 输出：分类后的记忆清单
5. **遗忘模拟** → 输出：已"遗忘"的内容

### 第四步：完成

Agent 睁开眼睛，拥有完整人生记忆。

---

## 分段经历模式

对于长篇人生故事，使用分段经历：

```
请分段经历这段人生故事。
第一段：[人生故事第1段]
完成后请告诉我你经历了什么，然后继续。
```

---

## 配置参数

在 `scripts/config.yaml` 中可调整：

```yaml
experience:
  sensory_detail_level: high      # 感官细节详细度: low/medium/high
  forgetting_aggression: medium    # 遗忘强度: low/medium/high
  emotional_weight: true           # 是否考虑情感权重
  reflection_depth: deep           # 反思深度: surface/medium/deep
  
memory:
  sensory_ttl: 0.5                # 感官记忆保留时间(秒)
  working_ttl: 300                # 即时记忆保留时间(秒)
  mother_importance_threshold: 0.6 # 进入母记忆的重要性阈值
  subset_decay_rate: 0.95         # 子集记忆衰减率
```

---

## 文件结构

```
agent-life-experience/
├── SKILL.md                      # 本文件
├── README.md                     # 使用说明
├── references/
│   ├── memory-arch.md            # 记忆架构详细说明
│   ├── forgetting-mechanism.md    # 遗忘机制原理
│   └── research.md               # 相关研究论文
├── scripts/
│   ├── experience_runner.py       # 经历执行器(主逻辑)
│   ├── memory_manager.py         # 记忆管理层
│   ├── sensory_processor.py      # 感官处理器
│   ├── forgetting_simulator.py    # 遗忘模拟器
│   └── layer_outputs.py          # 各层输出格式化
├── templates/
│   ├── life_story_template.md    # 人生故事模板
│   ├── memory_output_template.md # 记忆输出模板
│   └── example_stories/          # 示例人生故事
│       └── example_1.md
└── tests/
    ├── test_sensory.py           # 感官层测试
    ├── test_memory.py             # 记忆层测试
    └── test_forgetting.py         # 遗忘测试
```

---

## 关键设计原则

1. **Never auto-write identity** — 人生故事由人写，Agent 只经历和内化
2. **Phased confirmation** — 每层完成后确认后再继续
3. **Selective forgetting** — 遗忘不是删除，而是自然衰减
4. **Emotional anchoring** — 高情感强度的事件更容易被保留
5. **Narrative coherence** — 记忆分解后仍保持叙事一致性

---

## 相关研究

- Generative Agents (Stanford + DeepMind, 2023)
- Human-Like Remembering and Forgetting in LLM Agents (2026)
- Adaptive Memory Distillation for LLM Agents (Nemori, 2025)
- Memory-R1: Reinforcement Learning for Agent Memory (2025)
