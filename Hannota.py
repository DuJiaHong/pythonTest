#!/bin/python3
"""
    汉诺塔游戏（递归算法）
        汉诺塔问题是一个经典的问题。汉诺塔（Hanoi Tower），又称河内塔，源于印度一个古老传说。大梵天创造世
    界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着N片黄金圆盘。大梵天命令婆罗门把圆盘从下面
    开始按大小顺序重新摆放在另一根柱子上。并且规定，任何时候，在小圆盘上都不能放大圆盘，且在三根柱子之间一次
    只能移动一个圆盘。问应该如何操作？
        试想一下，如果我们要将最大的圆盘移动到最右边的柱子上。我们需要把除此圆盘的其他圆盘先移动到中间的柱子上。
    因此这个问题就变成了如何将 N-1 个圆盘移动到中间的柱子上。很容易我们就想到了递归的方法。

    1 层时  1次
    A -> C
    2 层时  2次
    A -> B
    A -> C
    B -> C
    3层时   7次
    A -> C
    A -> B
    C -> B
    A -> C
    B -> A
    B -> C
    A -> C
    ...
    根据上面总结 汉诺塔最优次数为(2^N-1)
"""
# 接收用户输入汉诺塔圆盘个数
Number = input("请用户输入圆盘个数")
# Times 记录移动次数
Times = 0;
# 定义交换函数
def handel(height, a="a", b="b", c="c"):
    # print("总共高度%s" % height)
    global Times
    if height == 1:
        Times += 1
        print(a, "->",c)
    else:
        Times += 1
        # 处理a -> c, a -> b, c -> b
        handel(height-1,a,c,b) 
        # 
        print(a, "->", c)
        # 处理b -> a, b -> c, a -> c
        handel(height-1,b,a,c)

if __name__ == "__main__":
    handel(int(Number))
    print("一共移动了%d次" %Times)


