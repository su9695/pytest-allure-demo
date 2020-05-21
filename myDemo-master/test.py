import time 
from config import setting
now=time.strftime('%Y-%m')
def aaa(picname):
    print(setting.SCREENSHOT_DIR+'/'+picname+now+'.PNG')

aaa('ssss')

