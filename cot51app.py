"""
    作者：rainboysd
    日期：2019年4月29日
    功能：Cot51app信息
    版本：1.0
"""
import baseapp
import time

class Cot51App(baseapp.BaseApp):
    def sign(self): 
        d = self.conn
        while not d(resourceId="com.cto51.student:id/featured_rl_nav_gift").exists:
            print("{} waiting...".format("每日有礼图标"))
            time.sleep(3)
            pass
        d(resourceId="com.cto51.student:id/featured_rl_nav_gift").click()
        # d(resourceId="com.cto51.student:id/web_view")
        while not  d(resourceId="SignBtn").exists:
            print("{} waiting...".format("签到图标"))
            time.sleep(3)
            pass
        d(resourceId="SignBtn").click()
        time.sleep(2)
        d(text=u"确定").click()
        pass      
    
    pass

if __name__ == "__main__":
    #cot51
    app_name = "com.cto51.student"    
    app = Cot51App(app_name)
    app.run()
   