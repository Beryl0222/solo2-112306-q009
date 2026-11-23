# 动作头混合权重

本项目面向机器人与机器学习工程中的动作头混合权重数据准备。示例资料均为本地合成记录，用来说明输入对象、版本字段及读取边界。数值口径、字段含义与设备约束见[资料格式](资料格式.md)。

Python 3.11 或更新版本可用于开发。在 Linux 环境中用 `python3 -m venv .venv` 创建虚拟环境，再用 `. .venv/bin/activate` 激活。运行 `python -m pip install -r requirements-build.txt` 安装固定版本的构建工具，然后用 `python -m pip install --no-build-isolation -e .` 安装项目。运行 `python -m unittest discover -s tests` 检查资料。需要分发时，用 `python -m build --wheel --no-isolation` 构建 wheel。运行依赖固定在 `pyproject.toml`，目前使用 NumPy 的 CPU 数组能力；资料检查可离线执行。

`fixtures/manifest.json` 描述本项目样例集合。`primary.json` 与 `revision.json` 是一组初始采集记录及其后续事件，可用于查看字段和版本关系。Python 包位于 `src/orthogonal_mix/`。
