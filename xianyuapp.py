"""
    作者：rainboysd
    日期：2019年4月29日
    功能：闲鱼app信息
    版本：1.0
"""
import baseapp
import time

class XianYuApp(baseapp.BaseApp):
    def sign(self):
        # 等待按钮出现
        while not self.conn(text="闲鱼币").exists:
            print("{} waiting".format("闲鱼币"))           
            time.sleep(3)            
            pass
        self.conn(text="闲鱼币").click() 
        #如果马上签到和已签到都不存在，等待
        while not self.conn(description=u"马上签到").exists and not self.conn(description=u"已签到").exists :           
            time.sleep(3)            
            pass
        #等待签到按钮变化完成
        time.sleep(3)
         #出现马上签到按钮进行签到,否则不做任何操作
        if self.conn(description=u"马上签到").exists:
            self.conn(description=u"马上签到").click()
            print("{}签到成功".format(self.__class__.__name__))
            pass
        else:
            print("{}已经完成签到".format(self.__class__.__name__))
            pass
        time.sleep(3)
        pass
    
    pass

if __name__ == "__main__":
    app_name = "com.taobao.idlefish"
    app = XianYuApp(app_name)
    app.run()
