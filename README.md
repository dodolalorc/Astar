# AStar 可视化项目

一个基于 PyScript + p5.js 的 A\* 路径搜索可视化小项目。
项目会随机生成网格地图（包含可通行与障碍格），再在画布中展示起点、终点、探索过程和最终路径。

## 功能概览

- 随机生成网格地图
- 随机生成起点与终点
- 构建网格图邻接关系
- 可视化展示搜索探索过程
- 高亮显示最终路径（若存在）

## 技术栈

- Python 3.12
- PyScript
- p5.js
- proceso
- Poetry（可选，用于依赖管理）

## 项目结构

```text
.
├── pyproject.toml
├── poetry.lock
└── astar/
    ├── index.html          # Web 入口
    ├── style.css           # 页面样式
    ├── pyscript.toml       # PyScript 配置
    ├── main.py             # 主流程与可视化逻辑
    ├── graph.py            # 图结构（顶点、邻接关系）
    ├── point.py            # 点/网格单元定义
    ├── search.py           # 搜索模块
    └── debugger.py         # 调试入口
```

## 环境准备

### 方式一：仅运行前端可视化（推荐）

本项目主要通过浏览器运行 PyScript，不依赖本地 Python 执行主逻辑。

1. 进入目录

```bash
cd astar
```

2. 启动静态服务器（任选一种）

```bash
python -m http.server 8000
```

3. 浏览器访问

```text
http://localhost:8000
```

### 方式二：使用 Poetry 安装依赖

如果你需要在本地 Python 环境中做调试，可在仓库根目录安装依赖：

```bash
poetry install
```

## 运行说明

- 打开页面后，会自动加载 main.py。
- 程序初始化网格、障碍、起点和终点。
- 鼠标按下后开始播放搜索过程。
- 若存在路径，会逐帧显示探索与路径信息；若不存在，显示 No solution。

## 主要可调参数

可在 astar/main.py 中调整：

- WIDTH, HEIGHT：画布大小
- ROWS, COLUMNS：网格行列数
- CELL_SIZE：网格大小
- 各类颜色常量：起点、终点、路径、探索区样式
- frame_rate：动画速度

## 已知问题

- 当前代码中 main.py 和 debugger.py 引用了 A_Star 类，但 search.py 里暂未看到对应实现。
- 若运行时报导入或属性错误，请先补齐 search.py 中的 A\* 搜索实现。

## 后续改进建议

- 增加手动设置起点/终点与障碍物的交互
- 支持对比 Dijkstra、BFS、Greedy Best-First 等算法
- 增加权重地图与对角线移动
- 输出更详细的性能指标（节点展开数、耗时等）

## License

仅用于学习与演示。
