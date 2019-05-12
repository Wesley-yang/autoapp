
import uiautomator2 as u2
import util
import time

addr = '192.168.0.103'
d= u2.connect(addr)
obj = d(resourceId="com.alipay.mobile.cardbiz:id/interact_text")
while not obj.exists:
    fbounds = {'bottom': 1500, 'left': 0, 'right': 1080, 'top': 300}
    x,y = util.createPosition(fbounds)
    d.swipe(x,y,x,y-200)
    print("{} {} waiting".format("alipayapp","立即领取"))
    time.sleep(3)
    pass 