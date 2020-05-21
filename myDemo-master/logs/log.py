import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
import logging
import time
class MyLog(object):
    def __init__(self,logger_name):
        # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)
            # 创建日志名称
            now=time.strftime('%Y_%m_%d')
            # 日志存放路径
            all_log_name = setting.ALL_LOG_DIR+'/'+now+'.log'
            error_log_name=setting.ERROR_LOG_DIR+'/'+now+'.log'
            # 创建一个handler 写入所有日志
            fh = logging.FileHandler(all_log_name,encoding='utf-8')
            fh.setLevel(logging.INFO)
            # 创建一个handler 写入错误日志
            eh = logging.FileHandler(error_log_name,encoding='utf-8')
            eh.setLevel(logging.ERROR)
            # 创建一个handler 控制台输出
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)

            # 创建输出日志的格式
            # 时间-日志器名称-日志级别-日志信息
            all_log_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
            # 时间-日志器名称-日志级别-文件名-函数名-行号-日志信息
            error_log_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(funcName)s-%(lineno)s-%(message)s')

            # 输出形式添加
            fh.setFormatter(all_log_formatter)
            eh.setFormatter(error_log_formatter)
            sh.setFormatter(all_log_formatter)

            #给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(eh)
            self.logger.addHandler(sh)
    def getLog(self):
        return self.logger




