"""
    作者：rainboysd
    日期：2019年4月29日
    功能：模型app信息
    版本：1.0
"""
import baseapp
import time

class ModelApp(baseapp.BaseApp):
    def sign(self): 
        pass      
    
    pass

if __name__ == "__main__":
    #
    app_name = "com.taobao.idlefish"    
    app = ModelApp(app_name)
    app.run()
   