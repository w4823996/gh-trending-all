# 📦 发布指南

## 版本号规则

采用语义化版本 (SemVer):
- 主版本号: 不兼容的 API 更改
- 次版本号: 向后兼容的功能新增
- 修订号: 向后兼容的问题修复

## 发布步骤

### 1. 更新版本号

```bash
# 编辑 gh_trending_all.py 中的版本号
# 或使用 bump2version 工具
pip install bump2version
bump2version patch  # 1.0.0 -> 1.0.1
bump2version minor  # 1.0.0 -> 1.1.0
bump2version major  # 1.0.0 -> 2.0.0
```

### 2. 运行测试

```bash
python -m pytest test_gh_trending.py -v
```

### 3. 提交更改

```bash
git add .
git commit -m "Release v1.0.1"
git tag -a v1.0.1 -m "Version 1.0.1"
git push origin main
git push origin v1.0.1
```

### 4. 创建 GitHub Release

1. 访问 https://github.com/w4823996/gh-trending-all/releases/new
2. 选择标签版本
3. 填写发布说明
4. 点击 "Publish release"

### 5. PyPI 发布 (可选)

```bash
# 安装构建工具
pip install build twine

# 构建包
python -m build

# 上传到 PyPI
twine upload dist/*
```

## 测试流程

```bash
# 运行所有测试
python -m pytest test_gh_trending.py -v

# 运行特定测试
python -m pytest test_gh_trending.py::test_fetch_github_trending -v

# 生成覆盖率报告
pip install pytest-cov
pytest --cov=gh_trending_all --cov-report=html
```

## 检查清单

- [ ] 所有测试通过
- [ ] 版本号已更新
- [ ] README.md 已更新 (如有 API 变更)
- [ ] CHANGELOG.md 已更新
- [ ] 代码已提交并推送
- [ ] GitHub Release 已创建
