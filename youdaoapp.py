"""
    作者：rainboysd
    日期：2019年4月29日
    功能：有道云笔记app信息
    版本：1.0
"""
import baseapp
import time

class YouDaoNoteApp(baseapp.BaseApp):
    def sign(self): 
        d = self.conn
        # 等待按钮出现
        obj = d(text="我的")
        self.waiting_click(obj,"我的")
        d(text="签到").click()        
        print("{}签到成功".format(self.__class__.__name__))
        time.sleep(3)        
        pass      
    
    pass

if __name__ == "__main__":
    app_name = "com.youdao.note"
    app = YouDaoNoteApp(app_name)
    app.run()
