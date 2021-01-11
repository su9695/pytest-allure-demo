import os,sys
BASIC_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASIC_DIR)

# pages页面目录
PAGES_DIR = os.path.join(BASIC_DIR,'pages')

# data 数据源目录
DATA_DIR = os.path.join(BASIC_DIR,'data')
TESTDATA_EXCEL_PATH =DATA_DIR+'/testData.xlsx'

# logs 日志大目录
LOGS_DIR = os.path.join(BASIC_DIR,'logs')
# 所有日志信息
ALL_LOG_DIR = os.path.join(LOGS_DIR,'all_log')
ERROR_LOG_DIR=os.path.join(LOGS_DIR,'error_log')

# testcases测试用例目录 
TESTCASES_DIR = os.path.join(BASIC_DIR,'testcases')

# scrrenshots截图目录
SCREENSHOT_DIR = os.path.join(BASIC_DIR, 'screenshots')

# reports报告目录
REPORTS_DIR = os.path.join(BASIC_DIR, 'reports')

# 测试地址
OMP = 'http://omp.888ly.cn'
OBP = 'http://obp.888ly.cn'
OSP = 'http://osp.888ly.cn'
