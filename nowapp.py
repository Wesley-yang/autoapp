"""
    作者：rainboysd
    日期：2019年4月29日
    功能：腾讯now直播app信息
    版本：1.0
"""
import baseapp
import time
import util

class NowApp(baseapp.BaseApp):
    def sign(self):
        d = self.conn
        #主界面领红包图标
        obj =  d(resourceId="com.tencent.now:id/b7k")
        self.waiting_click(obj,"主界面领红包图标")
        
        # 领红包
        obj = d(resourceId="com.tencent.now:id/qa")
        self.waiting_click(obj,"领红包")
        # 分享
        # time.sleep(3)
        # d(className="android.view.View", instance=7).click()
        # time.sleep(3)
        # d.press("back")
        # time.sleep(3)
        # d(scrollable=True).scroll()
        # time.sleep(3)
        obj = d(text=u"立即提现")
        self.waiting(obj,"立即提现")
        bounds = {'bottom': 1640, 'left': 420, 'right': 650, 'top': 500}
        x,y = util.createPosition(bounds)
        d.swipe(x,y,x,y-500)
        time.sleep(2)
        obj = d(text=u"领取")
        if  obj.exists:
            d(text=u"领取").click()
            print("{}领取成功".format(self.__class__.__name__))
        else:
            print("{}已经领取".format(self.__class__.__name__))     
            pass              
        time.sleep(3)
        d.press("back")  
        pass
    
    pass

if __name__ == "__main__":
    # 腾讯now直播
    app_name = "com.tencent.now"
    app = NowApp(app_name)
    app.run()
