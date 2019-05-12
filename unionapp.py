"""
    作者：rainboysd
    日期：2019年4月29日
    功能：手机营业厅app信息
    版本：1.0
"""
import baseapp
import time

class UnionApp(baseapp.BaseApp):
    def union_day(self):
        '''
    天天抽奖图标
    '''
        d = self.conn
        #天天抽奖图标 
        while (not d(resourceId="adUrl").exists()):
            print("{} {} waiting".format(self.__class__.__name__,"天天抽奖图标"))   
            time.sleep(3)
            pass    
        d(resourceId="adUrl").click()
        for i in range(3):            
            #开始抽奖图标
            while not d(resourceId="zhuanpan_2").exists() and not d(resourceId="zhuanpan_1").exists():                
                print("{} {} waiting".format(self.__class__.__name__,"天天抽奖zhuanpan"))  
                time.sleep(2)
                pass
            if d(resourceId="zhuanpan_2").exists():
                start = d(resourceId="zhuanpan_2").sibling(className="android.view.View")
                start[1].click()
                print("{}签到成功".format(self.__class__.__name__))
                time.sleep(3) 
            elif d(resourceId="zhuanpan_1").exists():
                start = d(resourceId="zhuanpan_2").sibling(className="android.view.View")
                start[1].click()
                print("{}签到成功".format(self.__class__.__name__))
            else:
                print("{}天天抽奖未知情况".format(self.__class__.__name__))

            #关闭按钮 
            if d(text=u"tt_guanbi_icon").exists():
                d(text=u"tt_guanbi_icon").click()
        time.sleep(3) 
        d.press("back")    
        d.press("back")  
        pass


    def union_tree(self):
        '''
        种树
        '''
        d = self.conn
        # 等待按钮出现
        obj = d(text="沃之树")
        self.waiting_click(obj,"沃之树")
        d.click(709, 1530)
        print("{}完成浇水".format(self.__class__.__name__))
        time.sleep(3)        
        pass


    def sign(self):
        '''
        手机营业厅签到 
        '''
        d  = self.conn
        # 等待按钮出现
        while not d(resourceId="com.sinovatech.unicom.ui:id/home_header_long_qiandao_image").exists:
            print("{} {} waiting".format(self.__class__.__name__,"签到图标"))           
            time.sleep(3)            
            pass
        #签到
        d(resourceId="com.sinovatech.unicom.ui:id/home_header_long_qiandao_image").click()
        time.sleep(4)
        # 天天抽奖图标 
        self.union_day()        
        #种树
        self.union_tree()
        time.sleep(3)  
        pass  
    
    pass

if __name__ == "__main__":
    # 联通手机营业厅
    app_name = "com.sinovatech.unicom.ui"
    app = UnionApp(app_name)
    app.run()

   
