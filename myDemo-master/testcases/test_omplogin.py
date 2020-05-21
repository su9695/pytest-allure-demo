import pytest
from data import reExcelData
from selenium import webdriver
from logs import log
from pages import ompLogin
import os
import sys
import allure
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

oRdExcel = reExcelData.RdExcel().getSheetData('omploginWx')
logger = log.MyLog('omplogin').getLog()


@pytest.mark.usefixtures('open_url')
@allure.feature('omplogin')
class Test_omplogin(object):
    @pytest.mark.usefixtures('refresh_page')
    @pytest.mark.parametrize('getOMPData', oRdExcel, indirect=True)
    def test_1(self, open_url, getOMPData):
        try:
            omp = ompLogin.OmpLoginPage(open_url)
            omp.oLogin(getOMPData['username'],
                       getOMPData['password'], getOMPData['checkcode'])
            assert omp.getMsg() == getOMPData['expected']
            omp.screenshot(omp.getMsg())
            logger.info('预期结果{0}和实际提示{1}=>一致'.format(
                omp.getMsg(), getOMPData['expected']))
        except:
            omp.screenshot(omp.getMsg())
            logger.error('预期结果{0}和实际提示{1}=>不一致！！！'.format(
                omp.getMsg(), getOMPData['expected']))


if __name__ == "__main__":
    pytest.main(['-s', 'myDemo-master/testcases/test_omplogin.py', '--html='])
