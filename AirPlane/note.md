# 飞机大战


# v1
- 主要作为技术验证
- 画出一个舞台，包括背景，包括一个小飞机

# v2
- 小蜜蜂会动，从上往下慢慢飞
- 能控制小蜜蜂左右移动
- 入场算法:
    - y轴要求是负数，这样会形成慢慢入场的效果，y = 0 - bee.height
    - x轴是要求一定的富余，即要求蜜蜂等移动物体不能紧紧的贴着边缘，而应该富余出来一些空隙
        - 基本上x轴的值是50起，最右边的计算方式应该是 world.width - bee.width - 50
- 移动速度问题
    - 包含x，y两个值
    - 对于绝大多数物体，只考虑y的值
    - 但是，蜜蜂和英雄是特例
    - 蜜蜂是从上向下移动的同时具有横向运动
    - 英雄的移动由上下左右键盘控制
    - 速度应该是一个tuple=(x, y)
- 方向问题
    - 具体移动方向由x, y控制
    - 值只能是-1, 0, 1三个就好
    - 应该是一个tuple
    - 例如(-1, 0)表示水平向左移动
    - 例如(0, 1)表示垂直向下移动
   
# v3
- 重构代码，使用oop方法
    - 世界的构成
        - 小飞机
        - 大飞机
        - 子弹
        - 英雄级
        - 天空
    - 配置文件
        - 可以通过一次性的配置来让程序正确运行
        - 降低了代码软件工程方面的成本
        - python的配置文件包：configparser
            - 以前叫ConfigParser
            - 配置文件一般以cfg或ini结尾
            - 语法：
                - 中括号：表示的是section
                - 每个section下是键值对，用等号或者冒号连接
            - get(section_name, key_name)返回相应的值
            - getint(section_name, key_name)返回相应的整数值
- 在oop的基础上再创建小飞机，蜜蜂等等，相对简单很多
- 程序可以正常生产飞行物，包括英雄级，子弹，云层
- BaseClass
    - 图片，以及一些功能
    - 位置，初始时飞进画布（x, 0-height）
    - 移动
- SubClass
    - Bee
    - SmallPlane
    - BigPlane
    - Bullet
    - Hero
    - Sky
    
# v4 
- 实现碰撞检测
- 碰撞检测算法是游戏的通用算法，必须掌握
- 一旦发生碰撞
    - 生命值会发生改变
    - 生命状态发生改变
        - LIFE_STATUS_LIVE
        - LIFE_STATUS_DEAD：已经发生碰撞，播放死亡动画
        - LIFE_STATUS_REMOVE：可以移除
    - 如果生命状态为DEAD，则播放死亡动画
- 在处理小飞机的时候：
    - 初始化的时候把五张图片全部初始化完毕，放入list中
    - 考虑到资源消耗，图片保存成类变量（所谓静态变量）
    - 正常播放的是第一张图片，一旦中弹，则连续播放其余的四张图片
- 游戏状态
    - READY：游戏还未开始，准备图片
    - RUNNING：正常游戏运行中
    - DONE：游戏结束停止运行，显示结束图片
- 游戏分数
    - 一个变量，每次碰撞后检查身份，如果是子弹击中敌人，则根据敌人类型更改分数
    - 把分数显示在屏幕上
    

    