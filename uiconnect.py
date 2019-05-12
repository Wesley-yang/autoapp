"""
    作者：rainboysd
    日期：2019年4月29日
    功能：通用conn信息
    版本：1.0
"""

import uiautomator2 as u2
g_addr = '192.168.0.103'
def getconn(addr=g_addr):
    conn = u2.connect(addr)
    return conn