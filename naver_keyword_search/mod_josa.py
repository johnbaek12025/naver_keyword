import re


def josa_eul(codename) :
    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    #영어리스트
    eng_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]
    eng_list_2 = ['m', 'n', 'r', 'M', 'N', 'R']
    name_keyword = codename[-1:]
    name_keyword_list = list(name_keyword)
    name_josa = list()
    #은/는 작성
    for k in range(0, len(name_keyword_list)):
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', name_keyword_list[k]) is not None:
            char_code = ord(name_keyword_list[k]) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            name_josa.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            name_josa.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            name_josa.append(JONGSUNG_LIST[char3])
        else:
            name_josa.append(name_keyword_list[k])

        if name_josa[-1] == ' ' :
            ega = '를'
        elif  name_josa[-1] in eng_list_1 :
            ega = '를'
        else :
            ega = '을'

    return(ega)


def josa_eunn(codename) :
    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    #영어리스트
    eng_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]
    eng_list_2 = ['m', 'n', 'r', 'M', 'N', 'R']
    name_keyword = codename[-1:]
    name_keyword_list = list(name_keyword)
    name_josa = list()
    #은/는 작성
    for k in range(0, len(name_keyword_list)):
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', name_keyword_list[k]) is not None:
            char_code = ord(name_keyword_list[k]) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            name_josa.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            name_josa.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            name_josa.append(JONGSUNG_LIST[char3])
        else:
            name_josa.append(name_keyword_list[k])

        if name_josa[-1] == ' ' :
            ega = '는'
        elif  name_josa[-1] in eng_list_1 :
            ega = '는'
        else :
            ega = '은'

    return(ega)


#조사 와/과
def josa_wa(codename) :
    #종목명에 조사를 달아준다
    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    #영어리스트
    eng_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]
    eng_list_2 = ['m', 'n', 'r', 'M', 'N', 'R']
    name_keyword = codename[-1:]
    name_keyword_list = list(name_keyword)
    name_josa = list()
    #은/는 작성
    for k in range(0, len(name_keyword_list)):
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', name_keyword_list[k]) is not None:
            char_code = ord(name_keyword_list[k]) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            name_josa.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            name_josa.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            name_josa.append(JONGSUNG_LIST[char3])
        else:
            name_josa.append(name_keyword_list[k])

        if name_josa[-1] == ' ' :
            ega = '와'
        elif  name_josa[-1] in eng_list_1 :
            ega = '와'
        else :
            ega = '과'

    return(ega)


#조사 이/가

#조사 이/가
def josa_ega(codename) :
    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    #영어리스트
    eng_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]
    eng_list_2 = ['m', 'n', 'r', 'M', 'N', 'R']
    name_keyword = codename[-1:]
    name_keyword_list = list(name_keyword)
    name_josa = list()
    #은/는 작성
    for k in range(0, len(name_keyword_list)):
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', name_keyword_list[k]) is not None:
            char_code = ord(name_keyword_list[k]) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            name_josa.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            name_josa.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            name_josa.append(JONGSUNG_LIST[char3])
        else:
            name_josa.append(name_keyword_list[k])

        if name_josa[-1] == ' ' :
            ega = '가'
        elif  name_josa[-1] in eng_list_1 :
            ega = '가'
        else :
            ega = '이'

    return(ega)


#라고/이라고
def josa_rago(codename) :
    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    #영어리스트
    eng_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]
    eng_list_2 = ['m', 'n', 'r', 'M', 'N', 'R']
    name_keyword = codename[-1:]
    name_keyword_list = list(name_keyword)
    name_josa = list()
    #은/는 작성
    for k in range(0, len(name_keyword_list)):
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', name_keyword_list[k]) is not None:
            char_code = ord(name_keyword_list[k]) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            name_josa.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            name_josa.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            name_josa.append(JONGSUNG_LIST[char3])
        else:
            name_josa.append(name_keyword_list[k])

        if name_josa[-1] == ' ' :
            ega = '라고'
        elif  name_josa[-1] in eng_list_1 :
            ega = '라고'
        else :
            ega = '이라고'

    return(ega)


#로/ 으로
def josa_ro(codename) :
    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    #영어리스트
    eng_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]
    eng_list_2 = ['m', 'n', 'r', 'M', 'N', 'R']
    name_keyword = codename[-1:]
    name_keyword_list = list(name_keyword)
    name_josa = list()
    #은/는 작성
    for k in range(0, len(name_keyword_list)):
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', name_keyword_list[k]) is not None:
            char_code = ord(name_keyword_list[k]) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            name_josa.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            name_josa.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            name_josa.append(JONGSUNG_LIST[char3])
        else:
            name_josa.append(name_keyword_list[k])

        if name_josa[-1] == ' ' :
            ega = '로'
        elif  name_josa[-1] in eng_list_1 :
            ega = '로'
        else :
            ega = '으로'

    return(ega)


def def_connect_word(name):
    import re
    # 리스트 형태로 받아야 함
    base_code, chosung, jungsung = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    jongsung_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    names_eunnun = []       # 은,는
    names_ega = []          # 이,가
    names_ullul = []        # 을,를
    names_gwawa = []        # 과,와
    names_eornone = []      # 이, ''(~~이라며, ~~~라며)
    names_eu = []

    for i in range(0, len(name)):
        name_keyword = name[i][-1:]
        name_keyword_list = list(name_keyword)
        name_josa = list()
        for k in range(0, len(name_keyword_list)):
            if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', name_keyword_list[k]) is not None:
                char_code = ord(name_keyword_list[k]) - base_code
                char1 = int(char_code / chosung)
                name_josa.append(chosung_list[char1])
                char2 = int((char_code - (chosung * char1)) / jungsung)
                name_josa.append(jungsung_list[char2])
                char3 = int((char_code - (chosung * char1) - (jungsung * char2)))
                name_josa.append(jongsung_list[char3])
            else:
                name_josa.append(name_keyword_list[k])
            eunnun = '는' if name_josa[-1] == ' ' else '은'
            ega = '가' if name_josa[-1] == ' ' else '이'
            ullul = '를' if name_josa[-1] == ' ' else '을'
            wagwa = '와' if name_josa[-1] == ' ' else '과'
            eornone = '' if name_josa[-1] == ' ' else '이'
            eu = '' if name_josa[-1] == ' ' else '으'
        names_eunnun.append(eunnun)
        names_ega.append(ega)
        names_ullul.append(ullul)
        names_gwawa.append(wagwa)
        names_eornone.append(eornone)
        names_eu.append(eu)
    return names_eunnun, names_ega, names_ullul, names_gwawa, names_eornone, names_eu
