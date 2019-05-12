"""
    作者：rainboysd
    日期：2019年4月29日
    功能：常用工具信息
    版本：1.0
"""
import random


def createPosition(bounds):
    '''
    根据输入的界面元素边界，产生随机点击位置,主要集中在中心位置
    获取元素中心点，然后从中心点，随机方向，随机距离增减
    '''
    bottom = bounds['bottom']
    left = bounds['left']
    right = bounds['right']
    top = bounds['top']
    #获取一半的大小
    width = int((right - left)/2)
    hight = int((bottom - top)/2)
    #得到中心点
    x_center = left + width
    y_center =top + hight
    #产生随机距离
    x_step = random.randint(0,(int(width/2)))
    y_step = random.randint(0,(int(hight/2)))
    #随机方向增减
    xflag = random.randint(-1,1)
    yflag = random.randint(-1,1)
    x = x_center + xflag * x_step
    y = y_center + yflag * y_step
    return x,y
