# AI Desktop Pet (Agent-Driven)

这是一个基于 Python (PyQt5) 和大语言模型（LLM）驱动的 PC 端智能桌面宠物脚手架。
宠物具备透明悬浮、鼠标拖拽交互以及与云端 AI Agent 引擎进行自然语言对话的基础能力。

## 核心架构
- **UI 层 (PyQt5)**: 实现无边框、透明背景的异形窗口，支持拖拽和右键菜单。
- **Agent 大脑层**: 封装大语言模型 API（如 MiMo），处理多轮对话与意图识别。
- **状态机**: 管理宠物的闲置 (Idle)、思考 (Thinking)、互动 (Interacting) 状态。

## 快速启动
1. 安装依赖: `pip install -r requirements.txt`
2. 准备素材: 在 `assets/` 目录下放置您的宠物 GIF 动图 (默认需要 `idle.gif` 和 `thinking.gif`)。
3. 配置环境: 在根目录创建 `.env` 文件配置 API Key。
4. 启动应用: `python main.py`
