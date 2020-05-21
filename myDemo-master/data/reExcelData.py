import xlrd 
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
class RdExcel(object):
    oData=xlrd.open_workbook(setting.TESTDATA_EXCEL_PATH)
    oSheets=oData.sheet_names()  # 获取所有的sheet名称,返回list
    # 存放所有sheet下的数据
    sheetDict={}  
    # 遍历每个sheet
    for sheetname in oSheets:
        # 根据sheet名称打开
        sheetTable = oData.sheet_by_name(sheetname) 
        # 每个sheet下的总行数
        oRows=sheetTable.nrows
        # 每个sheet下的总列数
        oCols=sheetTable.ncols
        # 获取第一行表头作为下个字典的key
        keys = sheetTable.row_values(0) 
        # 存放每个sheet下的数据
        dataList=[]
        j=1
        for k in range(oRows-1):# 不算第一行key
            values=sheetTable.row_values(j) # 从第一行开始
            # 该字典用于存放每一行的值
            dict={} 
            for x in range(oCols):# 总列数
                dict[keys[x]]=values[x] # K：V  第X列的表头：第X列的值
            j+=1
            dataList.append(dict) 
        sheetDict[sheetname] = dataList
    def getSheetData(self,sheetname):
        # 根据sheet名称返回每个sheet下的内容
        return self.sheetDict[sheetname]


test1 = RdExcel()
print(test1.getSheetData('omploginYx'))
    


