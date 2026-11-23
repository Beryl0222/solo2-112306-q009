# 动作头混合权重

本项目面向机器人与机器学习工程中的动作头混合权重数据准备。示例资料均为本地合成记录，用来说明输入对象、版本字段及读取边界。数值口径、字段含义与设备约束见[资料格式](资料格式.md)。

Python 3.11 或更新版本可用于开发。在 Linux 环境中创建虚拟环境并安装项目后，可运行 `python3 -m venv .venv`、`. .venv/bin/activate` 和 `python -m pip install -e .`。随后用 `python3 -m unittest discover -s tests` 检查资料清单和 JSON 文件。运行依赖固定在 `pyproject.toml`，目前使用 NumPy 的 CPU 数组能力；资料检查可离线执行。

`fixtures/manifest.json` 描述本项目样例集合。`primary.json` 与 `revision.json` 是一组初始采集记录及其后续事件，可用于查看字段和版本关系。Python 包位于 `src/orthogonal_mix/`。
