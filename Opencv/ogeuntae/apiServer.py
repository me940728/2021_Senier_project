# 이미지 촬영해서 저장 시키는 APIServer
# URL 호출 예시
# 아래의 hot:port/route?args1&agrs2
# 실사용: http://127.0.0.1/imgStroage?imgCheck=30&m=empNo=2121
# => 파이선 설치된 IP/메서드이름? 매개변수이름=데이터

# -- coding: utf-8 --

from flask import Flask, request, Response
from faceStorage import take_pictures
from functools import wraps
from imgHak import *
import json

# json 통신을 위한 기능
def as_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res = f(*args, **kwargs)
        return Response(res, content_type="application/json;")
    return decorated_function

application = Flask(__name__)

# 이미지 저장을 위한 라우트
@application.route("/imgStorage")
def imgStroageAPI():
    print("imgStorage Start")
    empno = request.args.get("empno")

    if empno is not None:
        print("empno : ", empno)
        res = "<h1>OK</h1>"
        print(empno)
        take_pictures(empno)
    else:
        print("No empno parameter")
        res = "Fail"

    print("imgStorage End")

    return res

# 이미지 체크해서 출석을 체크하는 라우트
@application.route("/imgCheck")
@as_json
def imgCheckAPI():
    print("imgCheckAPI Start")

    empDict = dict()
    empList = list()

    empno = str(request.args.get("empno"))
    hour = int(str(request.args.get("hour")))
    min = int(str(request.args.get("min")))
    ascTime = int(str(request.args.get("ascTime")))

    print("empno : ", empno)
    print("time", hour)
    print("min", min)
    print("ASC signal : ", ascTime)

    # 만약 인자값이 없으면 실행하지 말아라
    if empno is not None:    # and empNo is not None:
        print('empno : ', empno)
        empList = empno.split(sep=',')
        print("empList : ", empList)

        # 등록된 직원의 이미지를 학습시키는 명령어
        models = trains()
        print("models True?", models)
        
        # 학습이 완료 되었으니 카메라를 실행 시켜서 이미지 비교
        # 이때 직원 정보랑 모델을 파라미터로 넘김
        empDict = run(models, empList, hour, min, ascTime)
        print("API reTurn ok : ", empDict)
        #as_json은 json형태만 body로 출력 해줌
        #dictionary 파일은 바로 json 파일 형태로 추가 작업없이 바로 변환 가능
        resDict = json.dumps(empDict)
        print("empDict : ", empDict)

    # 에러 임
    else:
        print("ERROR")
        res = "<h1>Error!!!</h1>"

    return resDict

# 호출 받기 위한 형식 지정 모두 0으로 해야지 외부에서 접근가능
# port 번호는 안겹치게 확인 할 것
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)
