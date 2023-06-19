# myproject Pybo

- 점프 투 플라스크 따라하기
- https://wikidocs.net/book/4542


## 실행 flask run
- Anaconda Prompt 관리자 권한으로 실행(pyCharm 터미널에서는 실행 안됨)
- (base) C:\Users\PC2>myproject
- (myproject) C:\dev_py\projects\myproject>flask run

 * Serving Flask app 'pybo'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 672-568-100

## flask shell
- Anaconda Prompt 관리자 권한으로 실행
- (base) C:\Users\PC2>myproject
- (myproject) C:\dev_py\projects\myproject>flask shell


## 모델을 새로 작성하고 flask db migrate 명령으로 리비전 파일을 생성
- (myproject) C:\dev_py\projects\myproject>flask db migrate
- INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
- INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
- INFO  [alembic.autogenerate.compare] Detected added table 'user'
- Generating C:\dev_py\projects\myproject\migrations\versions\71f75d9d9223_.py ...  done

## flask db upgrade 명령으로 생성된 리비전 파일로 데이터베이스를 변경
- (myproject) C:\dev_py\projects\myproject>flask db upgrade
- INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
- INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
- INFO  [alembic.runtime.migration] Running upgrade 03a6cbae01cd -> 71f75d9d9223, empty message

## 로그인 정보
- http://127.0.0.1:5000/
- jon / jon99
- jon2 / jon99

# 마크다운 문법
* 파이썬
* 플라스크
* 알고리즘

1. 하나 
2. 둘둘둘
3. 셋이구나

플라스크는 **파이썬**으로 만들어진 웹 프레임워크이다.

파이썬 홈페이지는 [http://www.python.org](http://www.python.org) 입니다.

```
def add(a, b):
    return a + b
```

> 마크다운 문법 공식 문서 : https://www.markdownguide.org/getting-started

> 마크다운 확장 기능 문서 : https://python-markdown.github.io/extensions

```
마크다운 설치
(myproject) C:\dev_py\projects\myproject>pip install flask-markdown
```

## 작업한 내용을 원격 저장소에 저장하는 순서 간단 정리
* 프로그램 변경 작업하기
* git remote -v
* git status 
* git add <파일명> 또는 git add * 명령 수행하기
* git status
* git commit -m "커밋 코멘트" 명령 수행하기
* git status
* git push -u origin master 명령 수행하기

## aws에서 flask 실행
* 가상환경 진입
* ubuntu@devjon:~$ myproject
* 플라스크 실행은 ~/projects/myproject에서 해야함
* (myproject) ubuntu@devjon:~/projects/myproject$ flask run --host=0.0.0.0





