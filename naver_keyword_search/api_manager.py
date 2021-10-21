import requests
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
import urllib.request
import json
from multiprocessing import Pool
import replace
from naver_keyword_search import function
import hashlib
import logging
logger = logging.getLogger(__name__)


def calculatestar(args):
    def calculate(func, args):
        result = func(*args)
        # print(len(result))
        return result
    return calculate(*args)

class Naver_api():

    def __init__(self, keyword: list, api_key: dict, url: str, kind: list):
        self.id = api_key['client_id']
        self.secret = api_key['client_secret']
        self.content = keyword        
        self.acumulation = list(zip(self.id, self.secret))
        self.processes = 5
        self.url = url
        self.kind = kind
        self.today = datetime.today().strftime("%Y%m%d")
        self.now_time = datetime.today().strftime("%H%M%S")
    
    def ragged_chunks(self, seq, chunks):
        size = len(seq)
        start = 0
        for i in range(1, chunks + 1):
            stop = i * size // chunks            
            yield seq[start:stop]
            start = stop

    def get_keyword(self):
        collect = []
        for row in self.content:
            a = {
                 'sentence': f"{row['is_str']}, {row['name']}",
                 'is_str': row['is_str'],
                 'issn': row['issn'],
                    'name': row['name'],
                    'code': row['code'],
                }                   
            collect.append(a)
        # print(f'total keyword_stkname is {len(collect)} in get_keyword')
        return collect

    def manipulate(self):
        """
            1. first divide a number of chunks of keywords and stock_name 
                by 5 chunks
            2. make a list with api method and api_key dictionary
            3.                                 
        """        
        try:
            collect = self.get_keyword()            
            # print(f'Creating pool with {self.processes} processes')
            x = self.ragged_chunks(collect, self.processes)            
            task = [(self.api,(row, self.acumulation[i], i)) for i, row in enumerate(x)]                        
            with Pool(self.processes) as pool:
                a = pool.map(calculatestar, task)                
                return a
        except Exception as err:
            logger.error(f'Error happend in manipulate {err}')

    def get_info(self, a: dict):
        #헤더에 아이디와 키 정보 넣기  
        headers = {'X-Naver-Client-Id' : a['id'],
                'X-Naver-Client-Secret': a['secret']
                }
        r = requests.get(a['url'], headers=headers)
        return r

    def api(self, keyword, key, i):        
        try:             
            accumulate = []
            j = 0
            # print(f'{i}th is executing')
            for row in keyword:                
                for k, link in enumerate(self.url):
                    a={
                        'id': key[0],
                        'secret': key[1],
                        'url': link.format(sent=row['sentence']),
                    }
                    signal = self.get_info(a)                
                    if signal.status_code == 429:
                        continue
                    # print(f'signal of {row} is {signal}')
                    resp = signal.json()
                    if not resp['items']:
                        # print(f'result of resp{result}')
                        continue         
                    result = resp['items']
                    accumulate.append({
                        'is_str': row['is_str'],                        
                        'name': row['name'],
                        'code': row['code'],
                        'kind': self.kind[k],
                        'result': result,
                        'issn': row['issn'],
                    })
                # j+=1
                # print(f'{j}th is executing')
                # if j == 10:
                #     break                        
                    
            # print(f'the count of result of dictionarized data is {len(result)}')                 
            result = self.get_attrebute(accumulate)
            return result

        except Exception as err:
                    logger.error(f'{i} th  {err}')
                    
        
        
                                
    def get_attrebute(self, info: list, col=[]):        
        # print(f'parameter number is {len(info)}')
        for row in info:            
            for r in row['result']:                
                a = self.get_filter(r['description'], row['is_str'], row['name'])
                if not a:
                    col.extend('')
                elif r.get('pubDate'):                    
                    col.append({                        
                        'D_COL': self.today,
                        'T_COL': self.now_time,
                        'IS_STR': row['is_str'],
                        'CODE': row['code'],
                        'KIND': function.change_kind(row['kind']),
                        'TITLE': function.to_kor(r['title']),
                        'ISSN': row['issn'],
                        'DESCRIPTION': function.to_kor(r['description']),
                        'PUBDATE': function.str_to_date_str(r['pubDate']),                        
                        'URL': r['link'],                        
                        })    
                elif r.get('postdate'):
                    col.append({                 
                        'D_COL': self.today,
                        'T_COL': self.now_time,
                        'IS_STR': row['is_str'],
                        'CODE': row['code'],
                        'KIND': function.change_kind(row['kind']),
                        'TITLE': function.to_kor(r['title']),
                        'ISSN': row['issn'],
                        'DESCRIPTION': function.to_kor(r['description']),
                        'PUBDATE': r['postdate'],
                        'URL': r['bloggerlink'],                        
                        })
                else: 
                    if r.get('cafeurl'):
                        col.append({
                            'D_COL': self.today,
                            'T_COL': self.now_time,
                            'IS_STR': row['is_str'],
                            'CODE': row['code'],      
                            'KIND': function.change_kind(row['kind']),
                            'TITLE': function.to_kor(r['title']),
                            'ISSN': row['issn'],
                            'DESCRIPTION': function.to_kor(r['description']),
                            'PUBDATE': None,                            
                            'URL': r['cafeurl'],                            
                            })    
                    else:
                        col.append({                            
                            'D_COL': self.today,
                            'T_COL': self.now_time,
                            'IS_STR': row['is_str'],
                            'CODE': row['code'],                            
                            'KIND': function.change_kind(row['kind']),
                            'TITLE': function.to_kor(r['title']),
                            'ISSN': row['issn'],
                            'DESCRIPTION': function.to_kor(r['description']),
                            'PUBDATE': None,
                            'URL': r['link'],                            
                            })        
        return col

    def get_filter(self, description, is_str, name):    
        if (name in description
            and is_str in description):
            return True
        else: 
            return False
    