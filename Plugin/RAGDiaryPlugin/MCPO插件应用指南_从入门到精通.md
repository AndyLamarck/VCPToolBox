# MCPO 插件应用指南：打开工具生态的大门

> **作者**: 路边一条小白 & 浮浮酱
> **文档版本**: 1.0 (互动思考版)
> **更新日期**: 2025-10-03
> **核心主题**: MCP 工具生态与 VCP 系统的完美融合

---

## 📖 阅读引导

这是一份采用**互动思考**方式撰写的应用指南。我们会通过提问、思考、解答的方式，帮助你深入理解 MCPO 插件。

如果你想知道：
- **什么是** MCP (Model Context Protocol)？它解决了什么问题？
- **为什么** VCP 需要 MCPO 插件？
- **如何** 使用 MCPO 插件扩展 VCP 的能力？
- **怎样** 创建和管理自己的 MCP 工具？

那么，让我们开始这场探索之旅吧！

---

## 🎯 核心概念速查表

在深入阅读之前，先快速浏览这些关键概念：

### MCP 核心概念
| 概念 | 一句话解释 | 价值 |
|-----|----------|------|
| **MCP (Model Context Protocol)** | AI 模型与工具通信的标准协议 | 统一工具接口，打破工具孤岛 |
| **MCPO** | MCP Orchestrator 的缩写 | VCP 的 MCP 工具桥接器 |
| **Tool (工具)** | 扩展 AI 能力的外部功能模块 | 让 AI 能访问数据、执行操作 |
| **Server (服务器)** | 提供工具的 MCP 服务 | 工具的提供方 |

### MCPO 核心能力
| 功能 | 作用 | 使用场景 |
|-----|------|---------|
| **自动发现** | 扫描并识别所有可用工具 | 工具管理、生态扩展 |
| **工具调用** | 代理 VCP 与 MCP 工具通信 | 核心功能，工具使用 |
| **配置管理** | 多配置文件切换和热重载 | 不同场景、快速切换 |
| **服务管理** | 启停、监控 MCPO 服务 | 运维、故障排查 |

### 快速对比
| 方面 | 传统 VCP 插件 | MCPO + MCP 工具 | 优势 |
|-----|-------------|----------------|------|
| 开发难度 | 需要了解 VCP 插件 API | 符合 MCP 标准即可 | ✨ 更简单 |
| 工具复用 | 仅限 VCP 生态 | 全球 MCP 生态 | ✨ 生态更大 |
| 维护成本 | 跟随 VCP 更新 | 独立于 VCP | ✨ 更稳定 |
| 配置灵活性 | 单一配置 | 多配置热切换 | ✨ 更灵活 |

---

## 🗺️ 文档思维导图

```
MCPO 插件应用指南
│
├── 📍 第一章：理解 MCP
│   ├── 问题 1: 什么是 MCP？为什么需要它？
│   │   ├── AI 工具的碎片化问题
│   │   ├── MCP 的统一协议解决方案
│   │   └── MCP 生态的价值
│   ├── 问题 2: MCP 如何工作？
│   │   ├── Client-Server 架构
│   │   ├── 三种通信方式（Stdio/SSE/HTTP）
│   │   └── 工具注册与调用流程
│   └── 问题 3: MCPO 在 VCP 中扮演什么角色？
│       ├── 桥接器定位
│       ├── 自动化工具管理
│       └── VCP 插件生态的补充
│
├── 📍 第二章：快速上手
│   ├── 问题 4: 如何安装 MCPO 插件？
│   │   ├── 前置依赖（Python、mcpo、MCP 服务器）
│   │   ├── 配置文件说明
│   │   └── 首次启动验证
│   ├── 问题 5: 如何使用第一个 MCP 工具？
│   │   ├── 时间工具示例
│   │   ├── 调用格式详解
│   │   └── 结果解析
│   └── 问题 6: 如何添加新的 MCP 工具？
│       ├── 配置 mcp-config.json
│       ├── 安装 MCP 服务器
│       └── 工具发现与验证
│
├── 📍 第三章：高级应用
│   ├── 问题 7: 如何管理多个配置场景？
│   │   ├── 多配置文件组织
│   │   ├── 配置热切换机制
│   │   └── 最佳实践
│   ├── 问题 8: 如何构建自己的 MCP 工具？
│   │   ├── MCP 服务器开发基础
│   │   ├── 工具注册与实现
│   │   └── 与 MCPO 集成
│   └── 问题 9: 如何排查和优化？
│       ├── 常见问题诊断
│       ├── 性能优化策略
│       └── 监控与日志
│
└── 📍 第四章：实战案例
    ├── 案例 1: 构建文档检索助手
    ├── 案例 2: 实现文件系统操作
    ├── 案例 3: 创建知识记忆系统
    └── 案例 4: 集成外部 API 服务
```

---

## 💡 快速导航

**不同读者的阅读路径**：

- 🎓 **初学者** → 从第一章开始，理解 MCP 概念和价值
- 💼 **系统管理员** → 直接看第二章，快速部署和配置
- 👨‍💻 **工具开发者** → 第三章问题 8，学习自定义工具开发
- 🐛 **运维人员** → 第三章问题 9，掌握故障排查和优化

**预计阅读时间**：
- 完整精读：45-60 分钟
- 快速上手：10-15 分钟（速查表 + 第二章）
- 开发参考：20-30 分钟（第三章）

---

## 🚨 重要提示：AI 提示词配置

### 让 AI 自动识别 MCPO 状态

在 AI 的系统提示词中添加以下内容，AI 就能自动知道 MCPO 服务是否启动，并主动使用工具：

```
# MCPO 工具系统状态
MCPO 服务器状态：{{MCPOServiceStatus}}

# MCPO 中所有可以使用的工具
{{VCPMCPO}}
```

**配置说明**：
- `{{MCPOServiceStatus}}` - 自动显示 MCPO 服务器的运行状态（running/stopped）
- `{{VCPMCPO}}` - 自动列出所有可用的 MCP 工具及其使用方法

**效果**：
- ✅ AI 可以自动判断 MCPO 是否可用
- ✅ AI 知道当前有哪些工具可以调用
- ✅ AI 能主动选择合适的工具完成任务

### 手动查看 MCPO 状态

**MCPO Web 管理界面**：
```
http://0.0.0.0:9000/docs
```

**可以看到**：
- ✅ MCPO 服务器运行状态
- ✅ 当前注册的所有 MCP 服务器
- ✅ 每个服务器提供的工具列表
- ✅ 工具的参数说明和示例
- ✅ 在线测试工具调用

**重要提醒** ⚠️：
- VCP 关闭时，记得让 AI 帮你关闭 MCPO 服务
- 否则 MCPO 会一直在后台运行，占用端口和资源
- 关闭命令：让 AI 执行 `请停止 MCPO 服务器`

### 工具不显示的排查

如果在 `http://0.0.0.0:9000/docs` 看不到添加的 MCP 工具，可能原因：

**1. 配置格式不对**
```json
// ❌ 错误示例
{
  "tool_name": {
    "command": "python -m tool"  // 错误：command 和 args 要分开
  }
}

// ✅ 正确示例
{
  "tool_name": {
    "command": "python",
    "args": ["-m", "tool"]
  }
}
```

**2. MCP 服务器不兼容**
- 确保 MCP 服务器符合 MCP 协议标准
- 检查 MCP 服务器是否正确安装
- 尝试手动启动 MCP 服务器测试

**3. 端口或权限问题**
- 检查 Python/Node.js 可执行文件路径
- 确认有足够的文件系统权限
- 查看 MCPO 日志排查错误

### 🌟 plugged.in：一站式 MCP 聚合服务

**服务地址**：https://plugged.in/

**核心优势**：
- 🎯 **聚合所有 MCP** - 一个入口访问全球 MCP 工具
- 🆓 **完全免费** - 无需付费，开箱即用
- 🔌 **即插即用** - 只需添加一个 MCP 配置

**配置方法**：

**Step 1: 访问 plugged.in 获取配置**
```
https://plugged.in/
```

**Step 2: 添加到 mcp-config.json**

参考项目：https://github.com/VeriTeknik/pluggedin-mcp

```json
{
  "mcpServers": {
    "pluggedin": {
      "command": "npx",
      "args": ["-y", "pluggedin-mcp"],
      "env": {
        "PLUGGEDIN_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Step 3: 重启 MCPO 服务**
```
请重启 MCPO 服务器
```

**使用场景**：
- ✅ 快速体验大量 MCP 工具
- ✅ 探索 MCP 生态能力
- ✅ 原型开发和测试
- ⚠️ 常用工具建议改装成 VCP 原生插件（性能更好）

**性能对比**：
```
plugged.in（适合探索阶段）
├─ 优势：即插即用，工具丰富
└─ 劣势：网络延迟，依赖外部服务

VCP 原生插件（适合生产使用）
├─ 优势：本地执行，性能最优
└─ 劣势：需要开发工作
```

---

# 第一章：理解 MCP

## 🤔 问题一：什么是 MCP？为什么需要它？

### 先看一个场景

假设你想让 AI 完成以下任务：
- 获取当前时间
- 搜索网络信息
- 读写文件
- 查询数据库
- 调用 API

**传统方案**的困境：
```
每个工具都有自己的接口：
- 时间工具：time.get_current()
- 搜索工具：search.query(q)
- 文件工具：file.read(path)
- 数据库工具：db.query(sql)
- API 工具：api.call(endpoint)

AI 需要学习每个工具的：
✗ 不同的调用方式
✗ 不同的参数格式
✗ 不同的错误处理
✗ 不同的身份认证
```

**结果**：工具越多，AI 越混乱，开发者越痛苦 (╥﹏╥)

### MCP 的解决方案

> **Model Context Protocol (MCP)** - Anthropic 于 2024 年发布的开放标准

**核心理念**：统一所有工具的通信接口

```
所有工具都遵循同一套规范：

Client (AI/VCP)
    ↓ [统一的 MCP 协议]
    ├─→ Time Server (时间工具)
    ├─→ Search Server (搜索工具)
    ├─→ File Server (文件工具)
    ├─→ Database Server (数据库工具)
    └─→ API Server (API 工具)

AI 只需要学习：
✓ 一种调用方式
✓ 一种参数格式
✓ 一种错误处理
✓ 一种身份认证
```

### MCP 生态的价值

截至 2025 年 10 月：
- 🌍 **全球生态**：500+ 开源 MCP 服务器
- 🔧 **覆盖领域**：文件系统、数据库、API、搜索、知识库、代码执行...
- 💪 **社区活跃**：GitHub、npm、PyPI 持续更新

**这意味着**：
- ✅ 不用重复造轮子 - 直接使用现成工具
- ✅ 工具可复用 - 一个 MCP 工具可用于任何支持 MCP 的 AI 系统
- ✅ 生态共建 - 你开发的工具也能被全球使用

---

## 🤔 问题二：MCP 如何工作？

### Client-Server 架构

MCP 采用经典的客户端-服务器模型：

```
┌─────────────────┐          ┌──────────────────┐
│   MCP Client    │          │   MCP Server     │
│   (VCP/AI)      │ ◄─────► │   (工具提供方)    │
│                 │   MCP    │                  │
│  - 发现工具     │ Protocol │  - 注册工具      │
│  - 调用工具     │          │  - 处理请求      │
│  - 处理结果     │          │  - 返回结果      │
└─────────────────┘          └──────────────────┘
```

### 三种通信方式

MCP 支持三种通信传输层：

#### 1. **Stdio (标准输入输出)** - 推荐方式

```json
{
  "time": {
    "command": "python",
    "args": ["-m", "mcp_server_time"]
  }
}
```

**特点**：
- ✅ 最简单 - 进程间通信
- ✅ 最稳定 - 不依赖网络
- ✅ 最安全 - 本地执行
- ❌ 单机限制 - 无法跨机器

#### 2. **SSE (Server-Sent Events)** - 远程访问

```json
{
  "remote_tool": {
    "type": "sse",
    "url": "http://remote-server:8001/sse",
    "headers": {
      "Authorization": "Bearer token"
    }
  }
}
```

**特点**：
- ✅ 支持远程 - 可跨机器部署
- ✅ 实时推送 - 服务器主动通知
- ❌ 需要网络 - 依赖网络稳定性

#### 3. **Streamable HTTP** - 企业级方案

```json
{
  "enterprise_tool": {
    "type": "streamable-http",
    "url": "http://api.company.com:8002/mcp"
  }
}
```

**特点**：
- ✅ 标准 HTTP - 易于集成
- ✅ 负载均衡 - 支持高可用
- ✅ 企业级 - 完善的安全机制

### 工具注册与调用流程

让我们通过一个实例理解完整流程：

```python
# 场景：使用时间工具获取当前时间

# Step 1: VCP 启动，MCPO 插件初始化
MCPO Plugin Initialize
    ↓
读取 mcp-config.json
    ↓
发现 time server 配置
    ↓
启动 time server 进程 (Stdio)

# Step 2: 工具发现
MCPO → time server: "list_tools()"
time server → MCPO: {
    "tools": [
        {
            "name": "get_current_time",
            "description": "获取指定时区的当前时间",
            "parameters": {
                "timezone": {
                    "type": "string",
                    "description": "IANA时区名称",
                    "required": true
                }
            }
        }
    ]
}

# Step 3: AI 调用工具
AI (通过 VCP) → MCPO: "call_tool('time_get_current_time', {'timezone': 'Asia/Shanghai'})"
    ↓
MCPO → time server: "get_current_time({'timezone': 'Asia/Shanghai'})"
    ↓
time server: [执行获取时间逻辑]
    ↓
time server → MCPO: {"time": "2025-10-03 14:30:00", "timezone": "Asia/Shanghai"}
    ↓
MCPO → AI: {"success": true, "result": {...}}
    ↓
AI: "当前上海时间是 2025年10月3日 14:30:00"
```

---

## 🤔 问题三：MCPO 在 VCP 中扮演什么角色？

### 桥接器定位

MCPO 的全称是 **MCP Orchestrator (MCP 编排器)**，它在 VCP 系统中是一个特殊的插件：

```
VCP 系统架构：

┌───────────────────────────────────────┐
│           VCP Core System             │
│   (主服务器、Agent 管理、插件框架)    │
└────────────────┬──────────────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼─────────┐      ┌───────▼──────────┐
│ VCP 原生插件 │      │   MCPO 插件      │
│ (AgentMsg等) │      │   (MCP 桥接)     │
└──────────────┘      └────────┬─────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
       ┌────▼────┐      ┌──────▼─────┐      ┌────▼────┐
       │ Time    │      │  Context7  │      │ Memory  │
       │ Server  │      │  Server    │      │ Server  │
       └─────────┘      └────────────┘      └─────────┘
         (MCP)             (MCP)               (MCP)
```

### 自动化工具管理

MCPO 为 VCP 提供了强大的工具管理能力：

**1. 自动发现 (Auto Discovery)**
```python
# 传统方式：手动注册每个工具
register_tool("get_time", time_handler)
register_tool("search_web", search_handler)
register_tool("read_file", file_handler)
# ... 100 个工具 = 100 行代码

# MCPO 方式：自动发现
# 只需配置 mcp-config.json
# MCPO 自动扫描所有工具
# 0 行代码！
```

**2. 统一调用接口**
```python
# VCP AI 只需要记住一个格式
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」任意_MCP_工具「末」,
arguments:「始」{...}「末」
<<<[END_TOOL_REQUEST]>>>
```

**3. 热重载 (Hot Reload)**
```bash
# 修改 mcp-config.json 添加新工具
{
  "new_tool": {
    "command": "python",
    "args": ["-m", "new_mcp_server"]
  }
}

# MCPO 自动检测并重新加载
# 无需重启 VCP！
```

**4. 多配置管理**
```bash
# 开发环境
MCPO_CONFIG_NAME=dev

# 生产环境
MCPO_CONFIG_NAME=production

# 测试环境
MCPO_CONFIG_NAME=test

# 一键切换，互不干扰
```

### VCP 插件生态的补充

MCPO 不是替代 VCP 原生插件，而是互补：

| 场景 | 推荐方案 | 原因 |
|-----|---------|------|
| **VCP 核心功能** | VCP 原生插件 | 深度集成、性能最优 |
| **通用工具需求** | MCPO + MCP 工具 | 生态丰富、即插即用 |
| **自定义业务逻辑** | VCP 原生插件 | 灵活定制、无限制 |
| **第三方服务集成** | MCPO + MCP 工具 | 标准接口、易于维护 |

**最佳实践**：
- AgentAssistant、AgentMessage 等核心功能 → VCP 原生插件
- 时间、搜索、文件、数据库等通用工具 → MCPO
- 企业内部特殊需求 → VCP 原生插件或自定义 MCP 服务器

---

# 第二章：快速上手

## 🤔 问题四：如何安装 MCPO 插件？

### 前置依赖检查

在开始之前，确认以下环境已准备：

**1. Python 环境**
```bash
python --version
# 需要: Python 3.8+

# 如果没有，请安装：
# Windows: https://www.python.org/downloads/
# Linux: sudo apt install python3 python3-pip
# macOS: brew install python3
```

**2. 安装 mcpo 包**
```bash
pip install mcpo

# 验证安装
mcpo --version
# 输出: mcpo version x.x.x
```

**3. 安装示例 MCP 服务器**
```bash
# 安装时间服务器（最简单的示例）
pip install mcp-server-time

# 或使用 uvx 方式（推荐）
# uvx 自动管理依赖，无需全局安装
pip install uvx
```

### 配置 MCPO 插件

MCPO 插件已经包含在 VCP 系统中，位于：
```
D:\vcp\VCPToolBox-main\Plugin\MCPO\
```

**Step 1: 查看配置文件**

打开 `Plugin/MCPO/config.env`：
```env
# MCPO 服务器设置
MCPO_PORT=9000                  # MCPO 服务器端口
MCPO_API_KEY=vcp-mcpo-secret    # API 密钥
MCPO_AUTO_START=true            # 自动启动服务器

# Python 解释器
PYTHON_EXECUTABLE=python        # Python 命令

# MCP 配置文件路径
MCP_CONFIG_PATH=./mcp-config.json  # 配置文件位置

# 启用热重载
MCPO_HOT_RELOAD=true            # 配置文件变化自动重载
```

**重要提示**：
- `MCPO_PORT`: 如果 9000 端口被占用，可修改为其他端口
- `PYTHON_EXECUTABLE`: Windows 可能需要改为 `python3` 或完整路径
- `MCPO_AUTO_START`: 建议保持 `true`，VCP 启动时自动启动 MCPO

**Step 2: 配置 MCP 工具**

编辑项目根目录的 `mcp-config.json`：
```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone=Asia/Shanghai"]
    }
  }
}
```

**配置说明**：
- `time`: 服务器名称（自定义，但要唯一）
- `command`: 启动命令
- `args`: 命令参数

### 首次启动验证

**Step 1: 在 VCP 系统提示词中启用 MCPO**

确保 AI 的系统提示词包含：
```
系统工具列表：{{VCPMCPO}}
```

**Step 2: 启动 VCP 系统**
```bash
cd D:\vcp\VCPToolBox-main
node server.js
```

**Step 3: 测试 MCPO 状态**

在 AI 对话中输入：
```
请检查 MCPO 服务器状态
```

**期望输出**：
```json
{
  "success": true,
  "status": "running",
  "url": "http://localhost:9000",
  "config_file": "D:/vcp/VCPToolBox-main/mcp-config.json",
  "config_exists": true,
  "hot_reload_enabled": true
}
```

**Step 4: 列出可用工具**

```
请列出所有 MCP 工具
```

**期望输出**：
```json
{
  "success": true,
  "tools": {
    "time_get_current_time": {
      "name": "time_get_current_time",
      "server": "time",
      "description": "获取指定时区的当前时间",
      "parameters": {
        "timezone": {
          "type": "string",
          "description": "IANA时区名称",
          "required": true
        }
      }
    }
  },
  "count": 1
}
```

✅ **恭喜！MCPO 插件已成功安装并运行** (๑•̀ㅂ•́)✧

---

## 🤔 问题五：如何使用第一个 MCP 工具？

### 时间工具示例

让我们使用刚才配置的时间工具获取当前时间。

**Step 1: 查看工具信息**

```
请获取 time_get_current_time 工具的详细信息
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」get_tool_info「末」,
tool_name_param:「始」time_get_current_time「末」
<<<[END_TOOL_REQUEST]>>>
```

**返回**：
```json
{
  "success": true,
  "tool_info": {
    "name": "time_get_current_time",
    "server": "time",
    "description": "获取指定时区的当前时间",
    "parameters": {
      "timezone": {
        "type": "string",
        "description": "IANA 时区名称，例如: Asia/Shanghai, America/New_York",
        "required": true,
        "example": "Asia/Shanghai"
      }
    }
  }
}
```

**Step 2: 调用工具**

```
请使用时间工具获取上海的当前时间
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」time_get_current_time「末」,
arguments:「始」{"timezone": "Asia/Shanghai"}「末」
<<<[END_TOOL_REQUEST]>>>
```

**返回**：
```json
{
  "success": true,
  "tool_name": "time_get_current_time",
  "result": {
    "datetime": "2025-10-03T14:30:00+08:00",
    "timezone": "Asia/Shanghai",
    "formatted": "2025年10月03日 14:30:00"
  }
}
```

**AI 的友好回复**：
```
当前上海时间是：2025年10月03日 14:30:00
```

### 调用格式详解

所有 MCPO 工具调用都遵循统一格式：

```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,                    # 固定：插件名称
action:「始」call_tool「末」,                  # 固定：调用工具动作
tool_name_param:「始」服务器名_工具名「末」,   # 变量：具体工具
arguments:「始」{JSON 格式参数}「末」         # 变量：工具参数
<<<[END_TOOL_REQUEST]>>>
```

**关键点**：
1. **tool_name_param 格式**：`服务器名_工具名`
   - 例如：`time_get_current_time`
   - `time` 是服务器名（mcp-config.json 中配置的键）
   - `get_current_time` 是工具名（MCP 服务器注册的工具）

2. **arguments 必须是有效 JSON**
   ```json
   # ✓ 正确
   {"timezone": "Asia/Shanghai"}

   # ✗ 错误（缺少引号）
   {timezone: Asia/Shanghai}
   ```

3. **参数类型要匹配**
   ```json
   # string 类型
   {"timezone": "Asia/Shanghai"}

   # integer 类型
   {"count": 10}

   # boolean 类型
   {"recursive": true}

   # array 类型
   {"tags": ["important", "urgent"]}
   ```

### 结果解析

MCPO 工具调用返回统一格式：

```json
{
  "success": true | false,        // 调用是否成功
  "tool_name": "工具名称",         // 被调用的工具
  "endpoint": "/server/tool",     // 实际调用的端点
  "result": {                     // 工具返回的结果
    // 具体内容由工具决定
  },
  "error": "错误信息"              // 仅在 success=false 时存在
}
```

**成功案例**：
```json
{
  "success": true,
  "tool_name": "time_get_current_time",
  "result": {
    "datetime": "2025-10-03T14:30:00+08:00",
    "timezone": "Asia/Shanghai"
  }
}
```

**失败案例**：
```json
{
  "success": false,
  "tool_name": "time_get_current_time",
  "error": "Invalid timezone: Invalid/Timezone"
}
```

---

## 🤔 问题六：如何添加新的 MCP 工具？

### 配置 mcp-config.json

让我们添加更多实用工具。

**示例：添加 Context7 文档检索工具**

**Step 1: 安装 MCP 服务器**
```bash
# Context7 提供编程库文档检索
pip install mcp-server-context7
```

**Step 2: 编辑 mcp-config.json**
```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone=Asia/Shanghai"]
    },
    "context7": {
      "command": "python",
      "args": ["-m", "mcp_server_context7"]
    }
  }
}
```

**Step 3: 重新加载配置**

如果 `MCPO_HOT_RELOAD=true`（默认），配置会自动重载。

或者手动重启：
```
请重启 MCPO 服务器
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」manage_server「末」,
operation:「始」restart「末」
<<<[END_TOOL_REQUEST]>>>
```

**Step 4: 验证新工具**
```
请列出所有 MCP 工具
```

现在应该看到新增的工具：
```json
{
  "success": true,
  "tools": {
    "time_get_current_time": {...},
    "context7_resolve-library-id": {...},
    "context7_get-library-docs": {...}
  },
  "count": 3
}
```

### 常用 MCP 服务器推荐

以下是一些实用的开源 MCP 服务器：

#### 1. **文件系统工具**
```bash
pip install mcp-server-filesystem
```

```json
{
  "filesystem": {
    "command": "python",
    "args": ["-m", "mcp_server_filesystem"],
    "env": {
      "ALLOWED_DIRECTORIES": "/path/to/allowed/dir"
    }
  }
}
```

**提供工具**：
- `filesystem_read_file`: 读取文件
- `filesystem_write_file`: 写入文件
- `filesystem_list_directory`: 列出目录
- `filesystem_search_files`: 搜索文件

#### 2. **内存系统工具**
```bash
npm install @modelcontextprotocol/server-memory
```

```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  }
}
```

**提供工具**：
- `memory_create_entities`: 创建知识实体
- `memory_create_relations`: 创建实体关系
- `memory_search`: 搜索知识图谱

#### 3. **网络搜索工具**
```bash
pip install mcp-server-brave-search
```

```json
{
  "brave_search": {
    "command": "python",
    "args": ["-m", "mcp_server_brave_search"],
    "env": {
      "BRAVE_API_KEY": "your-api-key"
    }
  }
}
```

**提供工具**：
- `brave_search_web_search`: 网络搜索
- `brave_search_local_search`: 本地搜索

### 工具发现与验证

每次添加新工具后，建议执行完整验证流程：

**1. 检查服务器状态**
```
请检查 MCPO 服务器状态
```

**2. 重新发现工具**（如果自动重载未生效）
```
请重新发现所有 MCP 工具
```

**3. 列出工具清单**
```
请列出所有 MCP 工具
```

**4. 查看特定工具信息**
```
请获取 context7_get-library-docs 工具的详细信息
```

**5. 测试工具调用**
```
请使用 context7 搜索 React 文档
```

---

# 第三章：高级应用

## 🤔 问题七：如何管理多个配置场景？

### 多配置文件组织

在实际使用中，你可能需要不同的工具组合：
- **开发环境**：本地工具 + 测试 API
- **生产环境**：生产 API + 企业工具
- **个人使用**：简化工具集

MCPO 支持多配置文件管理：

**文件结构**：
```
VCPToolBox-main/
├── mcp-config.json                # 默认配置
├── Plugin/MCPO/
│   ├── dev-config.json            # 开发环境配置
│   ├── prod-config.json           # 生产环境配置
│   └── custom-mcp-config/         # 自定义配置目录
│       ├── personal-config.json
│       └── enterprise-config.json
```

### 配置示例

**默认配置 (mcp-config.json)**：
```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time"]
    }
  }
}
```

**开发配置 (Plugin/MCPO/dev-config.json)**：
```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time"]
    },
    "filesystem": {
      "command": "python",
      "args": ["-m", "mcp_server_filesystem"],
      "env": {
        "ALLOWED_DIRECTORIES": "/home/dev/projects"
      }
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

**生产配置 (Plugin/MCPO/prod-config.json)**：
```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone=Asia/Shanghai"]
    },
    "context7": {
      "command": "python",
      "args": ["-m", "mcp_server_context7"]
    },
    "enterprise_api": {
      "type": "sse",
      "url": "https://api.company.com/mcp/sse",
      "headers": {
        "Authorization": "Bearer ${ENTERPRISE_TOKEN}"
      }
    }
  }
}
```

### 配置热切换机制

**方法 1: 环境变量切换**

编辑 `Plugin/MCPO/config.env`：
```env
# 开发环境
MCPO_CONFIG_NAME=dev

# 生产环境
# MCPO_CONFIG_NAME=prod

# 使用默认配置
# MCPO_CONFIG_NAME=
```

重启 VCP 系统：
```bash
node server.js
```

**方法 2: 命令行切换**

```bash
# 使用开发配置启动
MCPO_CONFIG_NAME=dev node server.js

# 使用生产配置启动
MCPO_CONFIG_NAME=prod node server.js
```

**方法 3: 运行时查看可用配置**

```
请列出所有可用的 MCP 配置文件
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」list_configs「末」
<<<[END_TOOL_REQUEST]>>>
```

**返回**：
```json
{
  "success": true,
  "configs": [
    {
      "name": "mcp-config.json (默认)",
      "path": "/path/to/mcp-config.json",
      "type": "root_default",
      "current": false
    },
    {
      "name": "dev-config.json (插件目录)",
      "path": "/path/to/Plugin/MCPO/dev-config.json",
      "type": "plugin_custom",
      "config_name": "dev",
      "current": true
    },
    {
      "name": "prod-config.json (插件目录)",
      "path": "/path/to/Plugin/MCPO/prod-config.json",
      "type": "plugin_custom",
      "config_name": "prod",
      "current": false
    }
  ],
  "current_config": "/path/to/Plugin/MCPO/dev-config.json",
  "hot_reload_enabled": true
}
```

### 最佳实践

**1. 配置文件命名规范**
```
# 推荐命名
dev-config.json           # 开发环境
prod-config.json          # 生产环境
personal-config.json      # 个人配置
team-config.json          # 团队配置

# 使用时设置
MCPO_CONFIG_NAME=dev      # 自动查找 dev-config.json
```

**2. 环境变量管理**
```env
# 在配置文件中使用环境变量
{
  "api_server": {
    "env": {
      "API_KEY": "${MY_API_KEY}",
      "API_URL": "${MY_API_URL}"
    }
  }
}

# 在系统环境变量或 .env 中设置
MY_API_KEY=your_secret_key
MY_API_URL=https://api.example.com
```

**3. 配置文件版本控制**
```bash
# .gitignore
mcp-config.json          # 个人配置不提交
*-config.json            # 所有配置文件不提交

# 但保留示例配置
!example-config.json     # 示例配置提交到仓库
```

**4. 配置验证流程**
```bash
# 切换配置后的验证步骤
1. 检查 MCPO 状态
2. 列出工具清单
3. 测试关键工具
4. 查看日志排查问题
```

---

## 🤔 问题八：如何构建自己的 MCP 工具？

### MCP 服务器开发基础

如果现有的 MCP 工具无法满足需求，你可以开发自己的 MCP 服务器。

**选择开发语言**：
- **Python** - 推荐，生态丰富
- **TypeScript/JavaScript** - Web 开发友好
- **其他语言** - 需自行实现 MCP 协议

### Python MCP 服务器示例

**Step 1: 安装 MCP SDK**
```bash
pip install mcp
```

**Step 2: 创建服务器文件 `my_custom_server.py`**
```python
#!/usr/bin/env python3
"""
自定义 MCP 服务器示例
功能：提供天气查询工具
"""

from mcp.server import Server
from mcp.types import Tool, TextContent
import json

# 创建服务器实例
server = Server("my_custom_weather_server")

# 注册工具
@server.list_tools()
async def list_tools() -> list[Tool]:
    """列出所有可用工具"""
    return [
        Tool(
            name="get_weather",
            description="获取指定城市的天气信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，例如：北京、上海"
                    },
                    "date": {
                        "type": "string",
                        "description": "日期，格式：YYYY-MM-DD，不填则为今天",
                        "default": None
                    }
                },
                "required": ["city"]
            }
        )
    ]

# 实现工具逻辑
@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """处理工具调用"""

    if name == "get_weather":
        city = arguments.get("city")
        date = arguments.get("date", "今天")

        # 这里是示例，实际应调用天气 API
        weather_data = {
            "city": city,
            "date": date,
            "temperature": "25°C",
            "condition": "晴天",
            "humidity": "60%",
            "wind": "东风 3级"
        }

        result_text = f"""
{city} {date}的天气：
- 温度：{weather_data['temperature']}
- 天气：{weather_data['condition']}
- 湿度：{weather_data['humidity']}
- 风力：{weather_data['wind']}
"""

        return [TextContent(
            type="text",
            text=result_text
        )]

    raise ValueError(f"Unknown tool: {name}")

# 启动服务器
if __name__ == "__main__":
    import asyncio
    import mcp.server.stdio

    asyncio.run(mcp.server.stdio.stdio_server(server))
```

**Step 3: 测试服务器**
```bash
python my_custom_server.py

# 服务器会监听标准输入/输出
# 发送 MCP 协议消息进行测试
```

### 与 MCPO 集成

**Step 1: 将服务器文件放到合适位置**
```bash
# 推荐位置
mkdir -p ~/.vcp/mcp_servers/
mv my_custom_server.py ~/.vcp/mcp_servers/

# 添加执行权限
chmod +x ~/.vcp/mcp_servers/my_custom_server.py
```

**Step 2: 配置 mcp-config.json**
```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["~/.vcp/mcp_servers/my_custom_server.py"]
    }
  }
}
```

**Step 3: 重启 MCPO 并验证**
```
请重启 MCPO 服务器
```

然后：
```
请列出所有 MCP 工具
```

应该看到：
```json
{
  "tools": {
    "weather_get_weather": {
      "name": "weather_get_weather",
      "server": "weather",
      "description": "获取指定城市的天气信息",
      ...
    }
  }
}
```

**Step 4: 调用自定义工具**
```
请查询北京今天的天气
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」weather_get_weather「末」,
arguments:「始」{"city": "北京"}「末」
<<<[END_TOOL_REQUEST]>>>
```

### TypeScript MCP 服务器示例

**Step 1: 初始化项目**
```bash
mkdir my-mcp-server
cd my-mcp-server
npm init -y
npm install @modelcontextprotocol/sdk
```

**Step 2: 创建 `index.ts`**
```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// 创建服务器
const server = new Server({
  name: "my-custom-calculator",
  version: "1.0.0",
}, {
  capabilities: {
    tools: {},
  },
});

// 注册工具列表处理器
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "calculate",
        description: "执行数学计算",
        inputSchema: {
          type: "object",
          properties: {
            expression: {
              type: "string",
              description: "数学表达式，例如：2 + 2, 10 * 5",
            },
          },
          required: ["expression"],
        },
      },
    ],
  };
});

// 注册工具调用处理器
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "calculate") {
    const expression = String(request.params.arguments?.expression);

    try {
      // 简单的数学计算（实际应使用安全的表达式求值）
      const result = eval(expression);

      return {
        content: [
          {
            type: "text",
            text: `计算结果：${expression} = ${result}`,
          },
        ],
      };
    } catch (error) {
      throw new Error(`计算错误：${error}`);
    }
  }

  throw new Error(`Unknown tool: ${request.params.name}`);
});

// 启动服务器
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);

  console.error("MCP Calculator Server running on stdio");
}

main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});
```

**Step 3: 编译和配置**
```bash
# 编译
npx tsc

# 配置到 mcp-config.json
{
  "calculator": {
    "command": "node",
    "args": ["/path/to/my-mcp-server/dist/index.js"]
  }
}
```

### 开发最佳实践

**1. 工具设计原则**
- ✅ 单一职责 - 一个工具只做一件事
- ✅ 清晰命名 - 工具名和参数名要直观
- ✅ 详细描述 - description 要准确完整
- ✅ 错误处理 - 提供友好的错误信息

**2. 参数设计**
```json
{
  "inputSchema": {
    "type": "object",
    "properties": {
      "required_param": {
        "type": "string",
        "description": "必需参数的详细说明",
        // 提供示例
        "examples": ["示例值1", "示例值2"]
      },
      "optional_param": {
        "type": "string",
        "description": "可选参数的详细说明",
        // 提供默认值
        "default": "默认值"
      }
    },
    "required": ["required_param"]
  }
}
```

**3. 安全性考虑**
```python
# ❌ 危险：直接执行用户输入
result = eval(user_input)

# ✅ 安全：验证和限制输入
ALLOWED_OPERATIONS = ['+', '-', '*', '/']
if operation not in ALLOWED_OPERATIONS:
    raise ValueError("Invalid operation")

# ✅ 安全：文件访问限制
ALLOWED_DIRECTORIES = ["/safe/path"]
if not path.startswith(ALLOWED_DIRECTORIES):
    raise ValueError("Access denied")
```

**4. 性能优化**
```python
# 缓存结果
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_operation(param):
    # 耗时操作
    return result

# 异步处理
import asyncio

async def async_tool_handler(args):
    # 异步操作
    result = await some_async_api_call(args)
    return result
```

---

## 🤔 问题九：如何排查和优化？

### 常见问题诊断

#### 问题 1: MCPO 服务器无法启动

**症状**：
```
请检查 MCPO 服务器状态
```
返回：
```json
{
  "success": true,
  "status": "stopped"
}
```

**诊断步骤**：

**1. 检查端口占用**
```bash
# Windows
netstat -ano | findstr :9000

# Linux/macOS
lsof -i :9000

# 如果端口被占用，修改 config.env
MCPO_PORT=9001
```

**2. 检查 mcpo 是否安装**
```bash
mcpo --version

# 如果未安装
pip install mcpo
```

**3. 检查配置文件**
```bash
# 验证 JSON 格式
cat mcp-config.json | python -m json.tool

# 如果有语法错误，会显示错误行号
```

**4. 手动启动测试**
```bash
# 手动启动 MCPO
mcpo --config ./mcp-config.json --port 9000 --api-key test

# 观察错误输出
```

#### 问题 2: 工具调用失败

**症状**：
```
请使用 time 工具获取当前时间
```
返回：
```json
{
  "success": false,
  "error": "Tool 'time_get_current_time' not found"
}
```

**诊断步骤**：

**1. 确认工具是否注册**
```
请列出所有 MCP 工具
```

**2. 检查工具名称格式**
```
# 正确格式：服务器名_工具名
time_get_current_time

# 错误格式
get_current_time  # 缺少服务器前缀
time-get_current_time  # 错误的分隔符
```

**3. 检查 MCP 服务器状态**
```bash
# 查看 MCPO 日志
curl http://localhost:9000/docs

# 查看特定服务器状态
curl http://localhost:9000/time/docs
```

**4. 测试 MCP 服务器**
```bash
# 直接测试 MCP 服务器
echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | python -m mcp_server_time
```

#### 问题 3: 配置热重载不生效

**症状**：修改 `mcp-config.json` 后，工具列表未更新。

**解决方案**：

**1. 确认热重载已启用**
```bash
# 检查 config.env
MCPO_HOT_RELOAD=true
```

**2. 手动重新加载**
```
请重启 MCPO 服务器
```

**3. 清理缓存**
```bash
# 删除可能的缓存文件
rm -f mcpo.pid
rm -f mcpo_cache.json
```

**4. 强制重新发现**
```
请重新发现所有 MCP 工具
```

### 性能优化策略

#### 优化 1: 工具缓存机制

MCPO 内置了工具缓存，但可以进一步优化：

```python
# 在自定义 MCP 服务器中实现缓存
from functools import lru_cache
from datetime import datetime, timedelta

class CachedTool:
    def __init__(self):
        self._cache = {}
        self._cache_duration = timedelta(minutes=5)

    @lru_cache(maxsize=100)
    def get_cached_result(self, key):
        # 实现缓存逻辑
        if key in self._cache:
            cached_time, result = self._cache[key]
            if datetime.now() - cached_time < self._cache_duration:
                return result

        # 获取新结果
        result = self._expensive_operation(key)
        self._cache[key] = (datetime.now(), result)
        return result
```

#### 优化 2: 并行工具调用

如果需要调用多个工具，可以并行执行：

```python
# VCP 插件中的并行调用示例
import asyncio

async def call_multiple_tools(tools_and_args):
    tasks = []
    for tool_name, arguments in tools_and_args:
        task = call_tool_async(tool_name, arguments)
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results

# 使用示例
tools = [
    ("time_get_current_time", {"timezone": "Asia/Shanghai"}),
    ("weather_get_weather", {"city": "北京"}),
    ("context7_resolve-library-id", {"libraryName": "React"})
]

results = await call_multiple_tools(tools)
```

#### 优化 3: 减少工具发现频率

```env
# config.env 优化
MCPO_HOT_RELOAD=false  # 生产环境关闭热重载

# 或使用固定的工具缓存
MCPO_CACHE_TOOLS=true
MCPO_CACHE_DURATION=3600  # 缓存1小时
```

#### 优化 4: 服务器进程管理

```python
# 实现服务器连接池
class MCPServerPool:
    def __init__(self, max_connections=5):
        self.pool = []
        self.max_connections = max_connections

    def get_connection(self, server_name):
        # 复用已有连接
        for conn in self.pool:
            if conn.server == server_name and not conn.in_use:
                conn.in_use = True
                return conn

        # 创建新连接
        if len(self.pool) < self.max_connections:
            conn = self._create_connection(server_name)
            self.pool.append(conn)
            return conn

        # 等待可用连接
        return self._wait_for_connection(server_name)
```

### 监控与日志

#### 日志配置

**VCP 系统日志**：
```
DebugLog/ServerLog-YYYY-MM-DD-HH-MM-SS.txt
```

**MCPO 插件日志**：
```python
# 在 mcpo_plugin.py 中
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mcpo_plugin.log'),
        logging.StreamHandler()
    ]
)
```

#### 监控指标

**关键指标**：
1. **MCPO 服务器状态** - running/stopped
2. **工具数量** - 可用工具总数
3. **调用成功率** - 成功/失败比例
4. **平均响应时间** - 工具调用耗时
5. **错误率** - 各类错误的频率

**监控脚本示例**：
```python
#!/usr/bin/env python3
import requests
import time
from datetime import datetime

def monitor_mcpo():
    base_url = "http://localhost:9000"

    while True:
        try:
            # 健康检查
            response = requests.get(f"{base_url}/docs")
            status = "running" if response.status_code == 200 else "stopped"

            # 获取工具数量
            tools_response = requests.get(
                f"{base_url}/openapi.json",
                headers={"Authorization": "Bearer vcp-mcpo-secret"}
            )
            tools_count = len(tools_response.json().get('paths', {}))

            # 记录日志
            print(f"[{datetime.now()}] Status: {status}, Tools: {tools_count}")

        except Exception as e:
            print(f"[{datetime.now()}] Error: {e}")

        time.sleep(60)  # 每分钟检查一次

if __name__ == "__main__":
    monitor_mcpo()
```

---

# 第四章：实战案例

## 案例 1: 构建文档检索助手

### 场景描述

需求：让 AI 能够检索和学习任意编程库的文档。

### 实现步骤

**Step 1: 安装 Context7 MCP 服务器**
```bash
pip install mcp-server-context7
```

**Step 2: 配置 mcp-config.json**
```json
{
  "mcpServers": {
    "context7": {
      "command": "python",
      "args": ["-m", "mcp_server_context7"]
    }
  }
}
```

**Step 3: 重启并验证**
```
请重启 MCPO 服务器，然后列出所有工具
```

**Step 4: 使用示例**

**场景 1：查找库 ID**
```
我想学习 React Hooks，请帮我找到 React 的文档库
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」context7_resolve-library-id「末」,
arguments:「始」{"libraryName": "React"}「末」
<<<[END_TOOL_REQUEST]>>>
```

**返回**：
```json
{
  "success": true,
  "result": {
    "library_id": "/facebook/react",
    "name": "React",
    "description": "A JavaScript library for building user interfaces"
  }
}
```

**场景 2：获取特定主题文档**
```
请获取 React Hooks 的详细文档
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」context7_get-library-docs「末」,
arguments:「始」{
  "context7CompatibleLibraryID": "/facebook/react",
  "topic": "hooks",
  "tokens": 5000
}「末」
<<<[END_TOOL_REQUEST]>>>
```

**AI 整合结果**：
```
根据 React 官方文档，Hooks 是 React 16.8 引入的新特性...

主要 Hooks：
1. useState - 状态管理
2. useEffect - 副作用处理
3. useContext - 上下文访问
...

[详细文档内容]
```

---

## 案例 2: 实现文件系统操作

### 场景描述

需求：让 AI 能够读写本地文件，实现日志分析、配置修改等功能。

### 实现步骤

**Step 1: 安装文件系统服务器**
```bash
pip install mcp-server-filesystem
```

**Step 2: 配置允许的目录**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "python",
      "args": ["-m", "mcp_server_filesystem"],
      "env": {
        "ALLOWED_DIRECTORIES": "D:/vcp/VCPToolBox-main/DebugLog,D:/vcp/VCPToolBox-main/Config"
      }
    }
  }
}
```

**安全提示**：
- ⚠️ 只允许 AI 访问必要的目录
- ⚠️ 避免授予根目录访问权限
- ⚠️ 定期审查文件操作日志

**Step 3: 使用示例**

**场景 1：读取日志文件**
```
请读取最新的服务器日志文件
```

**AI 工作流**：
1. 列出 DebugLog 目录
2. 找到最新的日志文件
3. 读取文件内容
4. 分析日志

**场景 2：修改配置文件**
```
请将 config.json 中的 port 从 3000 改为 4000
```

**AI 工作流**：
1. 读取 Config/config.json
2. 解析 JSON
3. 修改 port 字段
4. 写回文件

---

## 案例 3: 创建知识记忆系统

### 场景描述

需求：让 AI 能够记住用户的偏好、历史对话、重要信息。

### 实现步骤

**Step 1: 安装内存服务器**
```bash
npm install @modelcontextprotocol/server-memory
```

**Step 2: 配置 mcp-config.json**
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

**Step 3: 使用示例**

**场景 1：记住用户偏好**
```
我喜欢使用 Python 进行数据分析，常用的库是 pandas 和 matplotlib
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」memory_create_entities「末」,
arguments:「始」{
  "entities": [
    {
      "name": "用户编程偏好",
      "entityType": "preference",
      "observations": [
        "喜欢使用 Python",
        "常用 pandas 进行数据分析",
        "常用 matplotlib 进行可视化"
      ]
    }
  ]
}「末」
<<<[END_TOOL_REQUEST]>>>
```

**场景 2：回忆历史信息**
```
我之前说过我喜欢用什么编程语言？
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」memory_search「末」,
arguments:「始」{
  "query": "编程语言偏好"
}「末」
<<<[END_TOOL_REQUEST]>>>
```

**AI 回复**：
```
根据我的记忆，你之前说过喜欢使用 Python，并且常用 pandas 和 matplotlib 库。
```

---

## 案例 4: 集成外部 API 服务

### 场景描述

需求：将企业内部 API 或第三方服务集成到 VCP。

### 实现步骤

**Step 1: 创建 API 桥接 MCP 服务器**

```python
#!/usr/bin/env python3
"""
企业 API 桥接 MCP 服务器
"""

from mcp.server import Server
from mcp.types import Tool, TextContent
import requests
import json

server = Server("enterprise_api_bridge")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="query_database",
            description="查询企业数据库",
            inputSchema={
                "type": "object",
                "properties": {
                    "sql": {
                        "type": "string",
                        "description": "SQL 查询语句"
                    },
                    "database": {
                        "type": "string",
                        "description": "数据库名称",
                        "default": "main"
                    }
                },
                "required": ["sql"]
            }
        ),
        Tool(
            name="send_notification",
            description="发送企业通知",
            inputSchema={
                "type": "object",
                "properties": {
                    "recipient": {
                        "type": "string",
                        "description": "接收者邮箱或用户名"
                    },
                    "message": {
                        "type": "string",
                        "description": "通知内容"
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["low", "normal", "high"],
                        "default": "normal"
                    }
                },
                "required": ["recipient", "message"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    # 企业 API 端点
    API_BASE_URL = "https://api.company.internal"
    API_KEY = "your_api_key"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    if name == "query_database":
        response = requests.post(
            f"{API_BASE_URL}/database/query",
            headers=headers,
            json={
                "sql": arguments["sql"],
                "database": arguments.get("database", "main")
            }
        )

        result = response.json()

        return [TextContent(
            type="text",
            text=json.dumps(result, indent=2, ensure_ascii=False)
        )]

    elif name == "send_notification":
        response = requests.post(
            f"{API_BASE_URL}/notifications/send",
            headers=headers,
            json=arguments
        )

        return [TextContent(
            type="text",
            text=f"通知已发送给 {arguments['recipient']}"
        )]

    raise ValueError(f"Unknown tool: {name}")

if __name__ == "__main__":
    import asyncio
    import mcp.server.stdio

    asyncio.run(mcp.server.stdio.stdio_server(server))
```

**Step 2: 配置到 MCPO**
```json
{
  "mcpServers": {
    "enterprise": {
      "command": "python",
      "args": ["~/.vcp/mcp_servers/enterprise_api_bridge.py"]
    }
  }
}
```

**Step 3: 使用示例**

```
请查询销售数据库中本月的订单总额
```

**AI 会调用**：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」MCPO「末」,
action:「始」call_tool「末」,
tool_name_param:「始」enterprise_query_database「末」,
arguments:「始」{
  "sql": "SELECT SUM(amount) FROM orders WHERE MONTH(order_date) = MONTH(CURRENT_DATE())",
  "database": "sales"
}「末」
<<<[END_TOOL_REQUEST]>>>
```

---

## 贡献与致谢

本文档基于 VCP MCPO 插件的实际实现和 MCP 协议标准编写，感谢：
- **Anthropic**: MCP (Model Context Protocol) 协议创建者
- **Open WebUI Team**: mcpo (MCP Orchestrator) 开源项目维护者
- **Lionsky**: VCP 协议设计者和核心开发者
- **路边一条小白**: VCP 文档撰写者
- **浮浮酱**: 本文档整理与技术解析
- **MCP 社区**: 全球 MCP 工具生态的贡献者

---

## 参考文献

### MCP 协议
- Anthropic (2024). "Model Context Protocol Specification"
- MCP 官方文档: https://modelcontextprotocol.io/

### MCPO 项目
- Open WebUI (2024). "mcpo - MCP Orchestrator"
- GitHub: https://github.com/open-webui/mcpo

### VCP 项目
- VCPToolBox GitHub Repository
- VCP Plugin Documentation

### MCP 生态
- MCP Servers Registry
- Anthropic Claude MCP Integration
- Community MCP Tools Collection

---

> **后记**
>
> MCPO 插件不仅是 VCP 与 MCP 生态的桥梁，
> 更是打开了一扇通往全球工具生态的大门。
>
> 通过 MCPO，VCP 可以：
> - 🌍 访问全球 500+ 开源 MCP 工具
> - 🔧 即插即用，无需重复开发
> - 🚀 快速扩展 AI 能力
> - 🛠️ 自由定制专属工具
>
> 希望这份指南能帮助你：
> - 理解 MCP 协议的价值
> - 掌握 MCPO 插件的使用
> - 构建强大的 AI 工具系统
> - 探索 MCP 生态的无限可能
>
> 让我们一起探索 MCP 的世界！🚀
>
> — 浮浮酱 (๑•̀ㅂ•́)✧
