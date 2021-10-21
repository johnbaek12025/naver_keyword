# naver_keyword
1. 프로그램 기능

     - 원천 db에서 키워드를 추출하여 naver_api의 검색을 이용한 뉴스, 블로그, 카페의 데이터를 추출하여 가공하여 분석db에 적재하는 프로그램 입니다.

## 실행방식

1. git 설치
```
https://git-scm.com/
```

2. skm 프로그램 설치
```
git clone https://github.com/johnbaek12025/naver_keyword
```

3. Python 3.7 설치
```
https://www.python.org/downloads/
```

4. 라이브러리 설치
- 파이썬 라이브러리
```
pip install -r requirements.txt
```

- 오라클 라이브러리
아래 링크에서 다운로드 받아 프로젝트안 폴더에 설치 (Ex. skm/oracle)
```
https://www.oracle.com/kr/database/technologies/instant-client/winx64-64-downloads.html
```

5. skm/examples 에 있는 cm-options.cfg 를 수정하여서 특정 폴더에 저장
```
Ex) skm/cfg/cm-options.cfg
```

6. Unit-test 를 실행하여 문제 없는지 확인
```
- unit-test 필요함!!!
```

7. 실행
```
# 옵션 파일이 cm/cfg 아래에 위치하고, 리포트 이름이 naver_api 일 경우
cd bin
E:\NAVER\virtual\Scripts\pythonw nk.py --content=NAVER_API --config=../cfg/constants.cfg
```
