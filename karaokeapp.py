"""
    作者：rainboysd
    日期：2019年4月29日
    功能：全面k歌app信息
    版本：1.0
"""
import baseapp
import time
import util

class KaraokeApp(baseapp.BaseApp):
    def sign(self): 
        d = self.conn
        while not d(text=u"我的").exists:
            print("{} waiting".format("我的")) 
            time.sleep(3)
            pass
        #右下角"我的"图标不好定位，之间用屏幕像素定位，
        bounds = {'bottom': 1797, 'left': 864, 'right': 1080, 'top': 1674}
        self.click_bounds(bounds)
        #“任务中心” 
        while not d(resourceId="com.tencent.karaoke:id/e1h").exists:
            print("{} waiting".format("任务中心图标")) 
            time.sleep(3)
            pass
        d(resourceId="com.tencent.karaoke:id/e1h").click()
        while not d(resourceId="com.tencent.karaoke:id/c9v").exists:
            print("{} waiting".format("任务中心主界面")) 
            time.sleep(3)
            pass
        #如果存在view实例29，则推定七天签到图标存在(如果签到了，界面不会显示)，说明未签到，
        if len(d(className="android.view.View"))>25:                
            # “立即签到” 边界
            bounds = {'bottom': 657, 'left': 720, 'right': 1005, 'top': 567}
            self.click_bounds(bounds)
            print("{}签到成功".format(self.__class__.__name__))
            time.sleep(3)
        else :
            print("{}已经完成签到".format(self.__class__.__name__))
            pass
       
        pass      
    
    pass

if __name__ == "__main__":
    #全民k歌
    app_name = "com.tencent.karaoke"    
    app = KaraokeApp(app_name)
    app.run()
   