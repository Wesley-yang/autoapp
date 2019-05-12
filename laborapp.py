"""
    作者：rainboysd
    日期：2019年4月29日
    功能：齐鲁总工会app信息
    版本：1.0
"""
import baseapp
import time

class LaborApp(baseapp.BaseApp):
    def sign(self): 
        d = self.conn
        #主界面签到按钮
        d(resourceId="com.inspur.vista.labor:id/ll_sign_in").click()
       
        while not d(resourceId="com.inspur.vista.labor:id/tv_sign_in").exists:
            time.sleep(3)
            pass
        btnsign = d(resourceId="com.inspur.vista.labor:id/tv_sign_in")
        if btnsign.info['text'] =="立即签到":
            btnsign.click()
            print("{}签到成功".format(self.__class__.__name__))
        else:
            print("{}已经完成签到".format(self.__class__.__name__))
            pass
        pass      
    
    pass

if __name__ == "__main__":
    #齐鲁总工会
    app_name = "com.inspur.vista.labor"    
    app = LaborApp(app_name)
    app.run()
   
