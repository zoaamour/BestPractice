import copy
import datetime
import hdf5storage
import mat73
import numpy as np
import os
import pandas as pd
from pylru import lrudecorator

from util.ConstUtil import GLOBAL_CONFIG


class DataAPI():
    def __init__(self):
        self.cache = {}

    def getDateList(self):
        date_list_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "dateList.mat")
        if date_list_path not in self.cache:
            date_list = hdf5storage.loadmat(date_list_path)['dateList'][:, 0]
            date_list = [datetime.datetime.strptime(str(int(x)), "%Y%m%d").date() for x in date_list]
            self.cache[date_list_path] = date_list
        return copy.deepcopy(self.cache[date_list_path])

    def getDateList_num(self):
        date_list_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "dateList.mat")
        dateList_cname = 'dateList_num'
        if dateList_cname not in self.cache:
            dateList_num = hdf5storage.loadmat(date_list_path)['dateList'].astype(int)
            self.cache[dateList_cname] = dateList_num
        return copy.deepcopy(self.cache[dateList_cname])

    # @lrudecorator(1)
    # def getLatestDate(self):
    #     date_list_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "dateList.mat")
    #     date_list = hdf5storage.loadmat(date_list_path)['dateList'][:, 0]
    #     date_list = [datetime.datetime.strptime(str(int(x)), "%Y%m%d").date() for x in date_list]
    #     return date_list[-1]
    #
    # @lrudecorator(1)
    # def getStkList(self):
    #     stk_list_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "stkList.mat")
    #     stk_list = hdf5storage.loadmat(stk_list_path)['stkList'][0]
    #     stk_list = np.array([x[0][0] for x in stk_list])
    #     return stk_list

    @lrudecorator(1)
    def getStkList_num(self):
        stk_list_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "stkList_num.mat")
        stkList_num = hdf5storage.loadmat(stk_list_path)['stkList_num'][0].astype(int)
        return stkList_num

    # @lrudecorator(1)
    # def getStkChNameList(self):
    #     stk_ch_name_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "stkChName.mat")
    #     stk_ch_name = hdf5storage.loadmat(stk_ch_name_path)['stkChName'][0]
    #     stk_ch_name = np.array([x[0][0] if len(x) > 0 else "" for x in stk_ch_name])
    #     return stk_ch_name
    @lrudecorator(1)
    def getStkList(self):
        stk_list_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "stkList.mat")
        stk_list = np.array(mat73.loadmat(stk_list_path)['stkList'])
        return stk_list

    # @lrudecorator(1)
    # def getStkChNameMap(self):
    #     stk_list = self.getStkList()
    #     stk_ch_name = self.getStkChNameList()
    #     stk_ch_name_map = {}
    #     for idx, stk_ticker in enumerate(stk_list):
    #         stk_ch_name_map[stk_ticker] = stk_ch_name[idx]
    #     return stk_ch_name_map
    @lrudecorator(1)
    def getStkChNameList(self):
        stk_ch_name_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "stkChName.mat")
        stk_ch_name = np.array(mat73.loadmat(stk_ch_name_path)['stkChName'])
        return stk_ch_name

    # @lrudecorator(1)
    # def getListDate(self):
    #     list_delist_date_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "date_IPO_delist.mat")
    #     list_date = hdf5storage.loadmat(list_delist_date_path)['date_IPO_delist'][0]
    #
    #     def _f(x):
    #         return datetime.datetime.strptime(str(int(x)), "%Y%m%d").date()
    #
    #     list_date = [_f(x) for x in list_date]
    #     return list_date
    #
    # def getPoolIPOEnable(self):
    #     file_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "poolIPOEnable.mat")
    #     data = hdf5storage.loadmat(file_path)['poolIPOEnable']
    #     return data
    #
    # def getTradingStatus(self):
    #     trading_status_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "tradingStatus.mat")
    #     trading_status = hdf5storage.loadmat(trading_status_path)['tradingStatus']
    #     return trading_status
    #
    def getSignalData(self, signal_name, date_as_index=False):
        df = self._getSignalData(signal_name).copy()
        if date_as_index:
            df.set_index('TradeDate', drop=True, inplace=True)
        return df

    @lrudecorator(10000)
    def _getSignalData(self, signal_name):
        file_path = os.path.join(GLOBAL_CONFIG['PostUpdate'], "%s.csv" % signal_name)
        df = pd.read_csv(file_path)
        df.TradeDate = df.TradeDate.apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").date())
        return df
    #
    # def getPostSignal(self, signal_name, date_as_index=False):
    #     df = self._getPostSignal(signal_name).copy()
    #     if date_as_index:
    #         df.set_index('TradeDate', drop=True, inplace=True)
    #     return df
    #
    # @lrudecorator(10000)
    # def _getPostSignal(self, signal_name):
    #     file_path = os.path.join(GLOBAL_CONFIG['PostUpdateRoot'], "%s.csv" % signal_name)
    #     df = pd.read_csv(file_path)
    #     df.TradeDate = df.TradeDate.apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").date())
    #     return df
    #
    # def saveSignalData(self, data, signal_name):
    #     file_path = os.path.join(GLOBAL_CONFIG['PostUpdate'], "%s.csv" % signal_name)
    #     data.to_csv(file_path, index=False, encoding="utf_8_sig")
    #
    # def isSignalExist(self, signal_name):
    #     file_path = os.path.join(GLOBAL_CONFIG['PostUpdate'], "%s.csv" % signal_name)
    #     return os.path.exists(file_path)
    #
    # def getIndexData(self, index_ticker):
    #     file_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "%s.mat" % index_ticker)
    #     index_data = hdf5storage.loadmat(file_path)[index_ticker]
    #     return index_data
    #
    # @lrudecorator(1)
    # def getStockReturn(self):
    #     pct_change_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "pct_change.mat")
    #     pct_change = hdf5storage.loadmat(pct_change_path)['pct_change']
    #     pct_chg_data = pct_change[0][1]
    #     return pct_chg_data
    #
    # @lrudecorator(4)
    # def getSWNameInfo(self, name_type="Ticker", level=1):
    #     sw_name_info = self._getSWNameInfo()
    #     if level == 1:
    #         sw_name_info = sw_name_info[0]
    #     elif level == 2:
    #         sw_name_info = sw_name_info[1]
    #     if name_type == "Ticker":
    #         sw_names = [x[0][0][0] for x in sw_name_info]
    #     elif name_type == "ChName":
    #         sw_names = [x[1][0][0].replace('(申万)', '') for x in sw_name_info]
    #     return sw_names
    #
    # @lrudecorator(1)
    # def _getSWNameInfo(self):
    #     sw_name_info_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "industry_name_SW.mat")
    #     sw_name_info = hdf5storage.loadmat(sw_name_info_path)['industry_name'][0]
    #     return sw_name_info

    @lrudecorator(4)
    def getSWNameInfo(self, level=1, name_type="Name"):
        sw_name_info = self._getSWNameInfo()[level-1]
        sw_name_arr = np.array(sw_name_info)
        if name_type == "Ticker":
            sw_names = sw_name_arr[:,0]
        else:
            sw_names = sw_name_arr[:,1]
            # 去掉‘(申万)’
            sw_names = [x.replace('(申万)', '') for x in sw_names]
            sw_names = np.array(sw_names)
        return sw_names

    @lrudecorator(1)
    def _getSWNameInfo(self):
        sw_name_info_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "industry_name_SW.mat")
        sw_name_info = np.array(mat73.loadmat(sw_name_info_path)['industry_name'], dtype="object")
        return sw_name_info


    @lrudecorator(2)
    def getSWIndexInfo(self, level):
        sw_info = self._getSWIndexInfo()
        if level == 1:
            sw_info = sw_info[0].astype(int)
        elif level == 2:
            sw_info = sw_info[1].astype(int)
        return sw_info

    @lrudecorator(1)
    def _getSWIndexInfo(self):
        sw_info_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "IndustryIndex_SW_block.mat")
        sw_info = hdf5storage.loadmat(sw_info_path)["IndustryIndex_SW_block"][0]
        return sw_info

    @lrudecorator(1)
    def getTradeStatus(self):
        status_file_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "status.mat")
        status = hdf5storage.loadmat(status_file_path)['status']
        return status

    @lrudecorator(1)
    def getRawBaseData(self):
        raw_base_file_path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "rawBaseData.mat")
        raw_base_data = hdf5storage.loadmat(raw_base_file_path)['rawBaseData'][0]
        return raw_base_data

    @lrudecorator(100)
    def getReportEndDate(self, report_index):
        start_year = 2005
        year_addon = report_index // 4
        remaing_addon = report_index % 4
        report_year = start_year + year_addon
        if remaing_addon == 0:
            report_date = datetime.date(report_year, 3, 31)
        elif remaing_addon == 1:
            report_date = datetime.date(report_year, 6, 30)
        elif remaing_addon == 2:
            report_date = datetime.date(report_year, 9, 30)
        elif remaing_addon == 3:
            report_date = datetime.date(report_year, 12, 31)
        else:
            raise Exception("Check the input report index")
        return report_date


GLOBAL_DATA_API = DataAPI()
