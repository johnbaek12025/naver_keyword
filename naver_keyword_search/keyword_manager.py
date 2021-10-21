import datetime
import logging
import time
import matplotlib.pyplot as plt
from operator import itemgetter
# from future.utils import iteritems

from datetime import datetime
from matplotlib import font_manager
from matplotlib.gridspec import GridSpec

# from cm import to_int, create_dir, mod_josa, int_to_kor_str
from naver_keyword_search.ftp_manager import FTPManager
from naver_keyword_search.query_manager import DBManager
from naver_keyword_search.socket_manager import SocketManager
from naver_keyword_search.api_manager import Naver_api
import requests
from functools import wraps
from itertools import groupby

logger = logging.getLogger(__name__)
url = ("https://openapi.naver.com/v1/search/{kind}.json?query={{sent}}"
                    "&display=5&start=1&sort=date")

def get_value(k):
    return k['ISSN']

class CMException(Exception):

    def __init__(self, error_msg):
        super().__init__(error_msg)


class KeywordManager(object):

    def __init__(self):
        logger.info("RMManager started")
        # FIXME: test_ 를 지워주세요
        # self.news_code = 'test_NG_BUY09'
        # self.tag_code = 'T00195'
        # self.result_base_path = '../images'
        # self.ftp_path = '/ref/rassiro/img/chart/NG_BUY09_chart'
        self.newsuser_dbmgr = None
        self.rcteam_dbmgr = None
        self.kind = ['news', 'blog', 'cafearticle', 'webkr']
        self.url = [url.format(kind=i) for i in self.kind]
        # self.smgr = None
        # self.fmgr = None
        self.today = datetime.today().strftime("%Y%m%d")
        self.now_time = datetime.today().strftime("%H%M%S")
        # 차트를 위한 폰트 설정
        # font_name = font_manager.FontProperties(
        #     fname="c:/Windows/Fonts/malgun.ttf").get_name()
        # plt.rc('font', family=font_name)
        # 차트에서 음수 표시가 안드는 것을 방지
        # plt.rcParams['axes.unicode_minus'] = False

    def run(self, config_dict, L=[]):
        try:            
            self.connect(config_dict)                        
            get_keyword = self.rcteam_dbmgr.get_data_list()
            api_key = config_dict['naver_key']            
            a = Naver_api(get_keyword, api_key, self.url, self.kind)
            result = a.manipulate()
            data = {}
            j = 0
            for r in result:                
                if not r:
                    continue                
                for row in r:                    
                    key = f"{row['IS_STR']}_{row['CODE']}"                    
                    try:
                        l = data[key]
                    except Exception as err:
                        # print(f'{key} is new')
                        data[key] = []
                        l = data[key]
                    l.append(row)

            logger.info(f'result is {len(data)}')


            data_to_insert = []
            for c in data:                
                # print(c)                
                row = data[c]                
                limit_idx = (len(row) if len(row) < 5 else 5)
                data_to_insert.extend(row[0:limit_idx])                       
            logger.info(f'The Collected data number {len(data_to_insert)}')

            collect =[]
            for row in data_to_insert:
                seq = self.rcteam_dbmgr.get_naver_seq()
                collect.append({
                    'SN': seq,
                    'D_COL': row['D_COL'],
                    'T_COL': row['T_COL'],
                    'IS_STR': row['IS_STR'],
                    'CODE': row['CODE'],
                    'KIND': row['KIND'],
                    'TITLE': row['TITLE'],
                    'ISSN': row['ISSN'],
                    'DESCRIPTION': row['DESCRIPTION'],
                    'PUBDATE': row['PUBDATE'],
                    'URL': row['URL'],
                })    
                

            self.rcteam_dbmgr.insert_naver_api(collect, commit=False)
            self.rcteam_dbmgr.commit()
            logger.info(f'Finished')
            # self.rcteam_dbmgr.insert_naver_api(data, commit=False)
            # self.rcteam_dbmgr.commit()
        except KeyboardInterrupt as err:
            logger.info(f"key interruption: {err}")
        except CMException as err:
            logger.info(err)
        except Exception as err:
            logger.info(f"error happened: {err}")
        finally:
            self.disconnect()

    def check_to_run(self):
        is_trade_day = self.rcteam_dbmgr.is_trade_day(self.today)
        if not is_trade_day:
            return False
        return True

    def disconnect(self):
        logger.info("disconnect from all")
        if self.newsuser_dbmgr:
            self.newsuser_dbmgr.disconnect()
        if self.rcteam_dbmgr:
            self.rcteam_dbmgr.disconnect()

    def connect(self, config_dict):
        logger.info("connect to all")
        oracle_info = config_dict['oracle']        
        DBManager().set_lib_path(oracle_info['lib_path'])

        # newsuser_db_info = config_dict['newsuser_database']
        # self.newsuser_dbmgr = DBManager()
        # self.newsuser_dbmgr.connect(**newsuser_db_info)

        rcteam_db_info = config_dict['rcteam_database']        
        self.rcteam_dbmgr = DBManager()
        self.rcteam_dbmgr.connect(**rcteam_db_info)

