import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logs import log
from base.base import *
from selenium.webdriver.common.by import By
logger=log.MyLog('OMPLoginPage').getLog()
class OmpLoginPage(Base):
    # 登陆页面的元素
    # 用户名
    username = (By.ID,'txtAccount')
    # 密码
    password = (By.ID, 'txtPassword')
    # 验证码
    checkcode = (By.ID, 'txtCheckCode')
    # 登陆按钮
    btnLogin = (By.ID, 'btnLogin')
    # 错误提示语句
    errshow = (By.CLASS_NAME,'errshow')
    # 登陆成功后的退出按钮
    exit_btn = (By.CLASS_NAME, 'exit-opts')

    def set_username(self,username):
        '''
        登陆用户名输入
        '''
        self.driver.find_element(*OmpLoginPage.username).send_keys(username)
    
    def set_password(self,password):
        '''
        密码输入
        '''
        self.driver.find_element(*OmpLoginPage.password).send_keys(password)

    def set_checkcode(self,checkcode):
        '''
        验证码输入
        '''
        self.driver.find_element(*OmpLoginPage.checkcode).send_keys(checkcode)
    
    def btnLogin_click(self):
        '''
        点击登陆按钮
        '''
        self.driver.find_element(*OmpLoginPage.btnLogin).click()
    
    def getMsg(self):
        '''
        获取登陆时的提示内容
        '''
        return self.driver.find_element(*OmpLoginPage.errshow).text
    
    def ifLogin(self):
        '''
        判断登陆成功后，退出按钮是否存在
        '''
        try:
            OmpLoginPage.isEelementExist(*OmpLoginPage.exit_btn)
            return True
        except:
            logger.error('{0}元素不存在，登陆不成功'.format(OmpLoginPage.exit_btn))
            return False

    def oLogin(self,username,password,checkcode):
        '''
        登陆操作
        '''
        self.set_username(username)
        self.set_password(password)
        self.set_checkcode(checkcode)
        self.btnLogin_click()
        time.sleep(2)



