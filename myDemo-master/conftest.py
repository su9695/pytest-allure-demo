import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting

import pytest
from selenium import webdriver
@pytest.fixture(scope='class')
def open_url():
    driver=webdriver.Chrome(executable_path=setting.Driver_PATH )
    driver.get(setting.OMP)
    yield driver
    driver.quit()
@pytest.fixture
def refresh_page(open_url):
    yield
    open_url.refresh()

@pytest.fixture()
def getOMPData(request):
    param=request.param
    return param
