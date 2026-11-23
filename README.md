# 动作头混合权重

本项目面向机器人与机器学习工程中的动作头混合权重数据准备。示例资料均为本地合成记录，用来说明输入对象、版本字段及读取边界。仓库不包含该业务算子或计算结果的实现。

Python 3.11 或更新版本可用于开发。安装项目依赖后，可运行 `python3 -m unittest discover -s tests` 检查资料清单和 JSON 文件。运行依赖固定在 `pyproject.toml`，目前使用 NumPy 的 CPU 数组能力；测试不下载模型或访问网络。

`fixtures/manifest.json` 描述本项目样例集合。`primary.json` 与 `revision.json` 是两组独立合成记录，可用于查看字段和版本关系。应用代码位于 `src/orthogonal_mix/`。项目使用者围绕资料读取与后续计算维护模型工程。
