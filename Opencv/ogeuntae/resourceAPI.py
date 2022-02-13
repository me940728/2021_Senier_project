from flask import Flask, request, Response, make_response
import psutil
from time import time
import json
# http://127.0.0.1:5002/deviceCPUResource?

application = Flask(__name__)

@application.route('/deviceCPUResource')
def cpuResourceCheck():
    cpu = psutil.cpu_percent()
    data = [time() * 1000, cpu]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    response.headers["Access-Control-Allow-Origin"] = "*" # 이거 헤더에 붙혀주지 않으면 동작하지 않음
    return response

# 호출 받기 위한 형식 지정 모두 0으로 해야지 외부에서 접근가능
# port 번호는 안겹치게 확인 할 것
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5002)
