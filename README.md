# 📊 gh-trending-all

> 一个命令查看 GitHub + Hacker News 热榜，发现趋势和有趣项目。

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ 功能特性

- 🔥 一键查看 GitHub Trending 热门仓库
- 🐍 支持按编程语言筛选 (Python, JavaScript, Rust...)
- 📅 支持时间范围过滤 (日/周/月)
- 💾 支持导出 JSON/CSV 格式
- 🎨 彩色终端输出，赏心悦目
- ⚡ 无需 API Key，直接使用 GitHub 搜索 API

## 🚀 快速开始

### 安装

```bash
# 方式1: 直接下载
pip install requests
python gh_trending_all.py

# 方式2: 克隆仓库
git clone https://github.com/w4823996/gh-trending-all.git
cd gh-trending-all
pip install requests
python gh_trending_all.py
```

### 使用方法

```bash
# 基本用法 - 查看今日热榜
python gh_trending_all.py

# 按语言筛选
python gh_trending_all.py -l python
python gh_trending_all.py -l javascript
python gh_trending_all.py -l rust

# 按时间范围
python gh_trending_all.py -s weekly    # 本周
python gh_trending_all.py -s monthly   # 本月

# 组合使用
python gh_trending_all.py -l python -s weekly -n 20

# 导出数据
python gh_trending_all.py --export json
python gh_trending_all.py --export csv

# 隐藏 URL 显示
python gh_trending_all.py --no-url
```

## 📖 命令行参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `-l, --language` | 按语言筛选 | `-l python` |
| `-s, --since` | 时间范围 | `-s weekly` |
| `-n, --number` | 显示数量 | `-n 20` |
| `--export` | 导出格式 | `--export json` |
| `--no-url` | 隐藏 URL | `--no-url` |
| `-v, --version` | 显示版本 | `-v` |

## 🎯 支持的编程语言

- Python, JavaScript, TypeScript
- Rust, Go, Java
- C++, C#, Ruby
- 以及任何 GitHub 支持的语言

## 📝 示例输出

```
╔═══════════════════════════════════════════════════════════════╗
║                    📊 gh-trending-all v1.0                    ║
║               聚合查看 GitHub + HN + Reddit 热榜              ║
╚═══════════════════════════════════════════════════════════════╝

============================================================
🔥 GitHub Trending (热门仓库)
============================================================

1. ⭐ microsoft/TypeScript
   📝 TypeScript is JavaScript with syntax for types.
   💬 语言: TypeScript | ⭐ 102k | 🍴 14.2k
   🔗 https://github.com/microsoft/TypeScript

2. ⭐ getcursor/cursor
   📝 The AI Code Editor
   💬 语言: TypeScript | ⭐ 52k | 🍴 6.8k
   🔗 https://github.com/getcursor/cursor
```

## 🛠️ 开发

```bash
# 克隆项目
git clone https://github.com/w4823996/gh-trending-all.git

# 安装依赖
pip install requests

# 运行
python gh_trending_all.py
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- GitHub API 提供的数据
- 所有 Star 和 Contributors

---

**如果这个工具对你有帮助，欢迎给我一个 ⭐ Star！**

[![Star](https://img.shields.io/github/stars/w4823996/gh-trending-all?style=social)](https://github.com/w4823996/gh-trending-all)
