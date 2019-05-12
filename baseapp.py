"""
    作者：rainboysd
    日期：2019年4月29日
    功能：通用app信息
    版本：1.0
"""
import uiconnect
import util
import time
g_timeout = 3
g_bounds_content = {'bottom': 1500, 'left': 0, 'right': 1080, 'top': 300}
class BaseApp():
   
    def __init__(self,app_name): 
        self.conn = uiconnect.getconn()
        self.app_name = app_name
        pass
    
    def start(self):
        self.conn.app_start(self.app_name)
        pass

    def waiting(self,obj,desc,timeout=g_timeout):
        '''
        等待提示信息        
        '''
        while not obj.exists:
            print("{} {} waiting".format(self.__class__.__name__,desc))
            time.sleep(timeout)
            pass 
        pass

    def waiting_click(self,obj,desc,timeout=g_timeout):
        '''
        等待对象出现，并点击      
        '''
        self.waiting(obj,desc,timeout)
        obj.click()
        time.sleep(timeout)
        pass
    
    def find_swipe(self,obj,desc,timeout = g_timeout):
        '''
        向下滑动屏幕查找目标
        '''
        d = self.conn
        while not obj.exists:
            fbounds = {'bottom': 1500, 'left': 0, 'right': 1080, 'top': 300}
            x,y = util.createPosition(fbounds)
            d.swipe(x,y,x,y-200)
            print("{} {} waiting".format(self.__class__.__name__,desc))
            time.sleep(timeout)
            pass 
        pass


    def stop(self):
        self.conn.press("back")
        self.conn.press("back")
        # 如果有退出按钮，点击，否则直接停止app
        if self.conn(resourceId="android:id/button1").exists:
            #51cot学院中的
            self.conn(resourceId="android:id/button1").click()
        else:
            self.conn.app_stop(self.app_name)
            pass
        
        pass

    
    def sign(self):
        pass
    

    def brows(self):
        pass

    def info(self):
        print(self.conn.info)
        pass

    def click_bounds(self,bounds):
        '''
        根据输入的界面元素边界，产生随机点击位置,并点击
        主要集中在中心位置
        获取元素中心点，然后从中心点，随机方向，随机距离增减
        '''
        x,y = util.createPosition(bounds)
        self.conn.click(x,y)
        pass

    def run(self):
        try:                  
            self.info()
            self.start()
            self.sign()       
        except Exception as e:
            print(e.args)
        finally:
            self.stop()
            pass
        pass
    pass

    