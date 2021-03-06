# thu_resilience

Version: 1.0

Last update: 2019-09-27

Description: 校园韧性评估系统平台（GUI）

## 环境要求

- 常用运行时库
  - DirectX
  - Microsoft Visual C++
- 商用软件
  - MATLAB（已测试2018b版本）
- 硬件要求
  - Windows 64位操作系统
  - 建筑模块采用并行算法（默认4线程），提高CPU线程数有利于提高建筑模块计算速度，可联系开发者修改并行设置
  - 建筑模块对内存要求较大，1000栋建筑推荐内存64GB

## 使用说明

运行thu_resilience.exe

### 菜单栏

#### 文件

- 退出：关闭程序

#### 查看

- 结果文件夹：打开结果文件夹`/results`

#### 帮助

- 文档
  - 使用说明
  - 建筑
  - 交通
  - 生命线
  - 韧性指标
- 版本信息

### 建筑系统

按顺序点击即可，可点击查看示例文件格式

### 交通系统

按顺序点击即可，可点击查看示例文件格式

测试时可先用迭代次数较少的`交通模拟（20次）`，耗时较短

### 生命线系统

按顺序点击即可，可点击查看示例文件

输入文件共20个

### 韧性评价指标

按顺序点击即可，要求建筑、交通和生命线模块已完成计算且提取结果

## 文件说明

- 界面：`/GUI`
- 核心模块
  - 建筑：`/building`
  - 交通：`/transport`
  - 生命线：`/lifeline`
  - 韧性指标：`/criteria`
- 文档： `/doc`
- 示例文件：`/demo`

- 结果文件：`/results`

## TODO

