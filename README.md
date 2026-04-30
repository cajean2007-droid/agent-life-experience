# Agent Life Experience System
# 人生经历系统

让 AI Agent 像人一样"经历"一段人生故事，拥有完整的记忆生命周期管理。

[English](README_EN.md) | 中文

---

## 🌟 特性

- **多层记忆架构**：感官层 → 即时层 → 母记忆层 → 子集记忆层
- **遗忘模拟**：模拟人类的自然遗忘机制
- **分段经历**：支持长篇人生故事分段处理
- **逐层确认**：每层处理后可确认再继续
- **开源可扩展**：欢迎贡献代码

---

## 📖 概念

**"经历"vs"知道"的区别：**

- **知道**：存储信息 → 检索
- **经历**：输入 → 身体/情绪反应 → 记忆重组 → 内化成"我"的一部分

本系统模拟人类记忆的完整生命周期。

---

## 🧠 记忆层级架构

```
第一层：感官记忆层 (Sensory Memory)
├─ 视觉、听觉、嗅觉、味觉、触觉
└─ 毫秒级大量信息过滤

第二层：即时记忆层 (Working Memory)
├─ 当前事件、闪念、临时信息
└─ 秒~分钟级，大部分遗忘

第三层：母记忆层 (Mother Memory)
├─ 人生叙事、身份核心
└─ 长期存储，情感锚点

第四层：子集记忆层 (Subset Memories)
├─ 身份/事实/关系/情感/技能/遗忘
└─ 分类存储，关联检索
```

---

## 🚀 快速开始

### 方式一：作为 Hermes Skill 使用

```
请用 agent-life-experience 这个 skill 来处理以下人生故事：
[粘贴人生故事]
```

### 方式二：直接调用 Python 模块

```python
from experience_runner import run_experience

life_story = """
我第一次意识到自己与众不同，是在八岁那年的春天...
"""

result = run_experience(life_story)
print(result['reflection'])
```

---

## 📂 文件结构

```
agent-life-experience/
├── SKILL.md                      # Skill 主文件
├── README.md                     # 本文件
├── README_EN.md                  # English version
├── references/
│   ├── memory-arch.md            # 记忆架构详细说明
│   ├── forgetting-mechanism.md    # 遗忘机制原理
│   └── research.md               # 相关研究论文
├── scripts/
│   ├── experience_runner.py       # 经历执行器
│   ├── memory_manager.py         # 记忆管理层
│   ├── sensory_processor.py      # 感官处理器
│   └── forgetting_simulator.py   # 遗忘模拟器
├── templates/
│   ├── life_story_template.md   # 人生故事模板
│   └── memory_output_template.md # 记忆输出模板
└── tests/
    ├── test_sensory.py
    ├── test_memory.py
    └── test_forgetting.py
```

---

## 📝 人生故事格式

详见 [templates/life_story_template.md](templates/life_story_template.md)

基本格式：

```markdown
# 事件标题

## 时间与背景
- 时间：
- 地点：
- 背景：

## 事件描述
[包含感官细节：看到的、听到的、感受到的]

## 内心独白
[当时在想什么]

## 情感标注
- 主要情感：
- 情感强度：1-10
- 身体反应：

## 对"我"的影响
[这件事如何改变了你]
```

---

## 🔬 相关研究

- [Generative Agents](https://arxiv.org/abs/2304.03442) - Stanford + DeepMind, 2023
- [Human-Like Remembering and Forgetting in LLM Agents](https://dl.acm.org/doi/10.1145/3765766.3765803) - 2026
- [Nemori: Adaptive Memory Distillation](https://arxiv.org/abs/2508.03341) - 2025
- [Memory-R1](https://arxiv.org/abs/2508.19828) - 2025

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建 Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 提交 Changes (`git commit -m 'Add AmazingFeature'`)
4. Push 到 Branch (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 License

本项目采用 MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- 斯坦福大学 AI 小镇 (Generative Agents)
- 所有为 Agent 记忆系统研究做出贡献的研究者
- 启发本项目的所有 AI 爱好者
