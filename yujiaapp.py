"""
    作者：rainboysd
    日期：2019年4月29日
    功能：我家瑜伽app信息
    版本：1.0
"""
import baseapp
import time

class YuJiaApp(baseapp.BaseApp):
    def sign(self): 
        
        #如果"签到"和弹出的签到图标到都不存在，等待
        while not self.conn(resourceId="cn.org.rar.iwantyoga:id/imageView2").exists and not self.conn(resourceId="cn.org.rar.iwantyoga:id/new_sign").exists:           
            time.sleep(3)            
            pass
        #如果出现签到图标，说明已经签过到了
        if self.conn(resourceId="cn.org.rar.iwantyoga:id/new_sign").exists:
            print("{}已经完成签到".format(self.__class__.__name__))
            pass
        else:#签到
            self.conn(resourceId="cn.org.rar.iwantyoga:id/imageView2").click()
            print("{}签到成功".format(self.__class__.__name__))
            pass        
        time.sleep(3)
        pass      
    
    pass

if __name__ == "__main__":
    app_name = "cn.org.rar.iwantyoga"
    app = YuJiaApp(app_name)
    app.run()
