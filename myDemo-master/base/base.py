import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from logs import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
logger = log.MyLog('basepage').getLog()
class Base(object):
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,*loc):
        """
        单个元素
        *loc 传入元素的属性
        return 定位到的元素
        """
        try:
            self.WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
            logger.info('元素{0}可见'.format(loc))
            return self.driver.find_element(*loc)
        except :
            logger.error('{0}未找到元素{1}'.format(self,loc))
            
    
    def find_elements(self, *loc):
        """
        多个元素
        *loc 传入元素的属性
        return 定位到的元素
        """
        try:
            self.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc))
            logger.info('元素{0}可见'.format(loc))
            return self.driver.find_elements(*loc)
        except:
            logger.error('{0}未找到元素{1}'.format(self,loc))

    def screenshot(self,picname):
        """
        截图：格式为picname+时间.PNG
        """
        now=time.strftime('%Y-%m-%d-%H-%M')
        try:
            self.driver.get_screenshot_as_file(setting.SCREENSHOT_DIR+'/'+picname+now+'.PNG')
            logger.info('{0}已成功截图'.format(picname))
        except Exception as e:
            logger.error(picname+'截图失败',e)
 
    
    def isEelementExist(self,*loc):
        '''
        判断元素是否存在
        '''
        flag=True
        try:
            self.driver.find_element(*loc)
            logger.info('{0}元素存在'.format(loc))
            return flag==True
        except:
            logger.error('{0}元素不存在'.format(loc))
            return flag==False
