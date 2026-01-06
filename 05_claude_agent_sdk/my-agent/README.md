# Claude Agent SDK - my-agent

基于 Claude Agent SDK 的示例代理项目。

## 📋 快速开始

### 1. 配置认证信息

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，配置以下之一：
```

**方式 1: 使用官方 Anthropic API**
```bash
ANTHROPIC_API_KEY=your-api-key-here
```
从 [Anthropic Console](https://console.anthropic.com/) 获取 API 密钥。

**方式 2: 使用自定义 API 代理或网关**
```bash
ANTHROPIC_BASE_URL=https://your-api-gateway.com/api
ANTHROPIC_AUTH_TOKEN=your-auth-token-here
```
如果你使用第三方 API 服务或企业内部的 API 网关。

### 2. 运行代理

```bash
# 运行标准版本
uv run python agent.py

# 运行调试版本（显示详细信息）
uv run python agent_debug.py
```

## 📁 文件说明

- `agent.py` - 主代理脚本
- `agent_debug.py` - 带详细调试信息的版本
- `utils.py` - 示例工具函数（包含一些故意的 bug 供代理修复）
- `.env.example` - 环境变量模板
- `.env` - 实际的环境变量文件（不提交到 Git）

## 🔧 功能说明

这个代理会：
1. 读取 `utils.py` 文件
2. 分析代码中可能导致崩溃的 bug
3. 自动修复发现的问题
4. 显示修复过程和结果

## 🐛 utils.py 中的已知问题

代理应该能够发现并修复以下问题：

1. `calculate_average()` - 除零错误（当 numbers 为空列表时）
2. `get_user_name()` - KeyError（当 user 为 None 或缺少 "name" 键时）

## 🔒 安全注意事项

- ⚠️  **永远不要将 `.env` 文件提交到 Git**
- ✅ 已在 `.gitignore` 中排除 `.env` 文件
- ✅ 使用 `.env.example` 作为模板
- ✅ API 密钥将被部分隐藏显示（前 10 位和后 4 位）

## 📚 更多信息

- [Claude Agent SDK 文档](https://platform.claude.com/docs/zh-CN/agent-sdk/overview)
- [项目 README](../../README.md)
