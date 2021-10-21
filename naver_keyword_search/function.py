import re
import hashlib

month_dict = {
    '01': ['Jan'],
    '02': ['Feb'],
    '03': ['Mar'],
    '04': ['Apr'],
    '05': ['May'],
    '06': ['Jun'],
    '07': ['Jul'],
    '08': ['Aug'],
    '09': ['Sep', 'Sept'],
    '10': ['Oct'],
    '11': ['Nov'],
    '12': ['Dec'],
    }


def _find_month(month_str):
    for r in month_dict:
        word_list = month_dict[r]
        if month_str in word_list:
            return r
    return None


def str_to_date_str(word: str):
    year = word[12:16]
    date = word[5:7]
    month = word[8:11]
    month = _find_month(month)
    return year + month + date


def change_kind(word: str):
    if word == 'blog':
        return '블로그'

    elif word == 'news':
        return '뉴스'

    elif word == 'kin':
        return '지식in'

    elif word == 'cafearticle':
        return '카페'
    else:
        return '웹문서'


def to_kor(word: str):
    word = word.replace('<b>', '')
    word = word.replace('</b>', '')
    word = word.replace('▷', '')
    word = word.replace('&gt;', '')
    word = word.replace('&lt;', '')
    word = word.replace('amp;', '')
    word = word.replace('&quot;', '')
    word = word.replace('*****@******.***', '')
    word = word.replace('-', '')
    word = word.replace('input=1195m','')
    word = word.replace('=','')
    word = word.replace(u"\xa0",u'')
    word = word.replace("'", "")
    return word

def get_hash(description: str):
    a = to_kor(description)
    after_password = a.encode('utf-8')
    hash_val = hashlib.new('sha256')
    hash_val.update(after_password)    
    return hash_val.hexdigest()
