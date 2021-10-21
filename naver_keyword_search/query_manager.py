from naver_keyword_search import db_manager


class DBManager(db_manager.DBManager):

    def __init__(self):
        pass

    def get_news_seq(self):
        sql = """
            SELECT  NEWS_USER.RTBL_NEWS_SEQUENCE.NEXTVAL
            FROM    DUAL
        """
        rows = self.get_all_rows(sql)
        if not rows:
            return None
        return rows[0][0]

    def is_trade_day(self, date):
        sql = f"""
            SELECT  *
            FROM    TRADE_DAY
            WHERE   DATEDEAL = '{date}'
        """
        rows = self.get_all_rows(sql)
        if not rows:
            return False
        return True
        

    def get_data_list(self):
        sql = f"""
           SELECT KEYWORD.IS_STR,
                    PRICE.STK_NAME,
                    KEYWORD.ISSN,
                    CODE.CODE
            FROM KTP.CT_ISSUE_CODE code
            inner join KTP.CT_ISSUE keyword
                    on CODE.ISSN = KEYWORD.ISSN
            inner join a3_curprice price
                    on price.stk_code = code.code
            WHERE EXCLUDE IS NULL"""
        rows = self.get_all_rows(sql)
        x = []
        if not rows:
            return x
        for r in rows:
            x.append({
                'is_str': r[0],
                'name': r[1],
                'issn': r[2],
                'code': r[3],
            })
        return x

    def get_keyword_list(self):
        sql = f"""
            select is_str from KTP.CT_ISSUE"""
        rows = self.get_all_rows(sql)
        x = []
        if not rows:
            return x
        for r in rows:
            x.append({
                'keyword': r[0],                
            })
        return x        

    def insert_news_info(self, news_dict, commit=True):
        news_seq = news_dict['news_seq']
        now_date = news_dict['now_date']
        now_time = news_dict['now_time']
        news_contents = news_dict['news_contents']
        news_code = news_dict['news_code']
        stock_code = news_dict['stock_code']
        new_input_type = news_dict['new_input_type']

        sql = f"""
            INSERT INTO RTBL_NEWS_INFO ( --뉴스정보
                NEWS_SN, D_NEWS_CRT, T_NEWS_CRT, STK_CODE, NEWS_TITLE,
                NEWS_INP_KIND, NEWS_CODE, RNEWS_CODE, D_EVENT_RNEWS
            ) VALUES (
                '{news_seq}','{now_date}','{now_time}','{stock_code}','{news_contents}',
                '{new_input_type}', '{news_code}', '{news_code}', '{now_date}'
            )
        """
        self.modify(sql, commit)

    def insert_news_html(self, news_dict, commit=True):
        news_seq = news_dict['news_seq']
        now_date = news_dict['now_date']
        now_time = news_dict['now_time']
        news_contents = news_dict['news_contents']
        news_code = news_dict['news_code']
        # 'T',  # T:Text, I:Image
        contents_type = news_dict['contents_type']
        representative_image_url = news_dict['representative_image_url']

        sql = f"""
            INSERT INTO RTBL_NEWS_CNTS_ATYPE ( --뉴스본문-ATYPE
                D_NEWS_CRT, NEWS_SN, CNTS_TYPE, D_NEWS_CNTS_CRT,
                T_NEWS_CNTS_CRT, NEWS_CNTS, NEWS_CODE, RPST_IMG_URL
            ) VALUES (
                '{now_date}', '{news_seq}', '{contents_type}', '{now_date}',
                '{now_time}','{news_contents}','{news_code}','{representative_image_url}'
            )
        """
        self.modify(sql, commit)

    def insert_com_tag(self, news_seq, now_date, tag_code, commit=True):
        sql = f"""
            INSERT INTO RTBL_COM_TAG ( --컴포넌트-테그
                SN, D_CRT, TAG_CODE
            ) VALUES (
                '{news_seq}', '{now_date}', '{tag_code}'
        )"""
        self.modify(sql, commit)

    def insert_stock_list(self, rows, commit=True):
        sql = """
            INSERT INTO RTBL_COM_RSC ( --컴포넌트-관련종목코드
                SN, D_CRT, RSC_CODE
            ) VALUES (
                :NEW_SEQ, :CREATION_TIME, :RSC_CODE
            )
        """
        self.modify_many(sql, rows, commit)

    def insert_naver_api(self, row , commit=True):        
        sql = f"""
            INSERT INTO  
                    DATA_NAVER_SEARCH_ISSUE
                    (SN,
                     D_COL, 
                     T_COL,
                     IS_STR,
                     CODE, 
                     KIND, 
                     TITLE, 
                     ISSN,
                     DESCRIPTION, 
                     PUBDATE, 
                     URL
                     ) 
     VALUES(         
                     :SN,
                     :D_COL, 
                     :T_COL,
                     :IS_STR,
                     :CODE, 
                     :KIND, 
                     :TITLE, 
                     :ISSN,
                     :DESCRIPTION, 
                     :PUBDATE, 
                     :URL                     
      )
        """
        self.modify_many(sql, row, commit)
    
    def get_naver_seq(self):
        sql = f"""
              SELECT SEQ_NAVER_SEARCH_ISSUE.NEXTVAL 
                     FROM DUAL
        """
        rows = self.get_all_rows(sql)
        if not rows:
            return None
        return rows[0][0]