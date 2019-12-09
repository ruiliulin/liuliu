import tkinter
import time
import configparser


class Actor():
    def __init__(self, root, canvas, position, x, y, tags, w, h, play):
        '''
        :param root:
        :param canvas:
        :param position: 锚点
        :param x:
        :param y:
        :param tags:给每个图片定义的标签，便于使用
        :param w:
        :param h:
        :param play: 是否播放死亡动画
        '''
        #