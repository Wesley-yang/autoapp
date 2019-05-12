"""
    作者：rainboysd
    日期：2019年4月30日
    功能：main主程序信息
    版本：1.0
"""
from xianyuapp  import XianYuApp
from yunshanfuapp import YunShanFuApp
from youdaoapp import YouDaoNoteApp
from yujiaapp import YuJiaApp
from unionapp import UnionApp
from nowapp import NowApp
from baidu.yueduapp import YueDuApp
from baidu.zhidaoapp import ZhiDaoApp
from laborapp import LaborApp
from cot51app import Cot51App
from karaokeapp import KaraokeApp


if __name__ == '__main__':
    # #齐鲁总工会
    # app_name = "com.inspur.vista.labor"    
    # app = LaborApp(app_name)
    # app.run()
    # # 闲鱼1
    # app_name = "com.taobao.idlefish"
    # app = XianYuApp(app_name)
    # app.run()
    # # 云闪付
    # app_name = "com.unionpay"
    # app = YunShanFuApp(app_name)
    # app.run()
    # # 有道笔记
    # app_name = "com.youdao.note"
    # app = YouDaoNoteApp(app_name)
    # app.run()
    # # 瑜伽
    # app_name = "cn.org.rar.iwantyoga"
    # app = YuJiaApp(app_name)
    # app.run()
    # #cot51
    # app_name = "com.cto51.student"    
    # app = Cot51App(app_name)
    # app.run()
    # #全民k歌
    # app_name = "com.tencent.karaoke"    
    # app = KaraokeApp(app_name)
    # app.run()
    # # 联通手机营业厅
    # app_name = "com.sinovatech.unicom.ui"
    # app = UnionApp(app_name)
    # app.run()
    # 腾讯now直播
    app_name = "com.tencent.now"
    app = NowApp(app_name)
    app.run()
    # 百度阅读
    app_name = "com.baidu.yuedu"    
    app = YueDuApp(app_name)
    app.run()

    #百度知道
    app_name = "com.baidu.iknow"    
    app = ZhiDaoApp(app_name)
    app.run()
    pass
   