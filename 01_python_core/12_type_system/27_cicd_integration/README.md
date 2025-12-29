# CI/CD 集成

将类型检查自动化是确保代码库长期保持高质量的关键。本章节介绍如何将 mypy 和 pyright 集成到常见的自动化流程中。

## 目录

- [01_github_actions.py - GitHub Actions](01_github_actions.py)：展示如何在 GitHub 的 CI 流程中配置自动类型检查。
- [02_pre_commit.py - pre-commit 集成](02_pre_commit.py)：展示如何配置 git 钩子，在代码提交前强制执行类型检查。
- [03_makefile.py - 本地 Makefile](03_makefile.py)：展示如何通过一个简单的 `make` 命令统一本地的检查流程。

## 自动化价值

1. **防患未然**：防止包含类型错误的 PR 被合并到主分支。
2. **强制规范**：确保团队所有成员都遵循相同的类型检查规则。
3. **减少人工审查**：机器能处理的错误，就不需要浪费 Code Review 的时间。

## 学习建议

- 推荐使用 `pre-commit`，因为它能在错误发生的第一时间（本地提交时）就给出反馈，比等待 CI 运行更高效。
- 在 CI 中，确保使用的 Python 版本和依赖与开发环境完全一致。
