"""
    作者：rainboysd
    日期：2019年4月29日
    功能：云闪付app信息
    版本：1.0
"""
import baseapp
import time

class YunShanFuApp(baseapp.BaseApp):
    def sign(self): 
        d = self.conn
        # 等待按钮出现
        while not d(resourceId="com.unionpay:id/frog_float_gif").exists:
            print("{} waiting".format("签到图标"))           
            time.sleep(3)            
            pass
        d(resourceId="com.unionpay:id/frog_float_gif").click()
        #如果"签到"和"今日已签"到都不存在，等待
        while not self.conn(text=u"今日已签到").exists and not self.conn(text="签到").exists :           
            time.sleep(3)            
            pass
        #如果已经签到输出，否则签到
        if d(text=u"今日已签到").exists:
            print("{}已经完成签到".format(self.__class__.__name__))
            pass
        else:
            d(text="签到").click()            
            print("{}签到成功".format(self.__class__.__name__))
            pass 
        time.sleep(3)
        pass      
    
    pass

if __name__ == "__main__":
    app_name = "com.unionpay"
    app = YunShanFuApp(app_name)
    app.run()
