# 저장된 이미지를 통해 출석을 체크하기위한 기능을 수행하는 클래스
# trains 함수는 faces 폴더의 서브폴더들을 찾아서 train 함수에 한폴더 씩 연결해준다.
# 그러면 train 함수는 해당 폴더의 사진을  model로 학습을 한 후 학습된  model을 리턴해준다.

import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join
from checkAtt import *
import datetime

# 얼굴 인식용 haar/cascade 로딩
face_classifier = cv2.CascadeClassifier("data/haarcascade_frontalface_alt2.xml")


# 사용자 얼굴 머신러닝
def train(name):
    print("train Start!")
    print("name : ", name)

    data_path = 'faces/' + name + '/'
    # 파일만 리스트로 만듬
    face_pics = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    # 라벨링 작업
    Training_data, Labels = [], []

    for i, files in enumerate(face_pics):
        image_path = data_path + face_pics[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # 이미지가 아니면 패스
        if images is None:
            continue
        Training_data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)

    if len(Labels) == 0:
        print("학습 데이터가 엄서용")
        return None
    Labels = np.asarray(Labels, dtype=np.int32)
    # 모델 생성
    model = cv2.face.LBPHFaceRecognizer_create()  # face 패키지는 확장판인 contrib-opencv-python에 있어 설치 해야함
    # 학습
    model.train(np.asarray(Training_data), np.asarray(Labels))

    print(name + ": 모델 학습 종료")

    # 학습 모델 리턴
    return model


# ===========================================================
# 여러 사용자 학습
def trains():
    print("trains start(여러 사용자)")
    # faces 폴더의 하위 폴더를 학습
    data_path = 'faces/'
    # 폴더만을 색출
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path, f))]

    # 학습 모델 저잘할 딕셔너리
    models = {}
    # 각 폴더에 있는 얼굴들 학습
    for model in model_dirs:
        print('model : ' + model)
        # 학습 시작
        result = train(model)

        # 학습이 안되었다면 패스
        if result is None:
            continue

        # 학습 완료 되었으면 저장
        print('model2 : ' + model)
        models[model] = result

    # 학습된 모델 딕셔너리 리턴
    return models


# 얼굴 검춣 함수
def face_detector(img, size=0.5):

    gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gary, 1.3, 5)

    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi  # 검출된 좌표에 사각 박스 그리거 (img), 검출된 부위를 잘라(roi)하여 전달


# 인식 작업 시작
def run(models, empList , hour, min, ascTime):
    print('run empno : ', empList)
    print('run hour : ', hour)
    print('run min : ', min)
    asc = ascTime

    # 직원 정보 담을 딕셔너리
    empDict = dict()
    # 직원 정보를 {empno : {dict}} 형식으로 보낼 딕셔너리 생성
    empAttTimeJson = dict()
    # 파일 생성 로그 남기기 용
    # fileName = makeCsv()
    # 카메라 열기

    try:
        print("cap start!")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # captureDevice = camera
        print("cap.open?", cap.isOpened())
        print("cap end!")
    except:
        print("카메라 로딩 실패")
        return

    while True:
        print("자동반복 작업")
        # 카메라로 부터 사진 한장 읽기
        ret, frame = cap.read()
        # 얼굴 검출 시도
        image, face = face_detector(frame)

        try:
            min_score = 999  # 가장 낮은 점수로 얘축된 사람의 점수
            min_score_name = ""  # 가장 높은 점수로 예측된 사람의 이름

            # 검출된 사진을 흑백으로 변환
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # 위에서 학습한 모델로 예측시도
            for key, model in models.items():
                result = model.predict(face)
                if min_score > result[1]:
                    min_score = result[1]
                    min_score_name = key

            # min_score 신뢰도 이고 0에 가까울 수록 자신과 같다는 뜻이다.
            if min_score < 600:
                confidence = int(100 * (1 - (min_score) / 300))
                # 유사도 화면에 표시
                display_string = str(confidence) + "% name is : " + min_score_name
            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)


            # 80보다 크면 동일 인물로 간주 
            # 평균 82 정도 아놈 그날 찍은 사진은 90이 나옴
            if confidence > 80:
                # cv2.putText(image, "UNLOCKED : " + min_score_name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 250, 0), 2)

# !!!!!!!!!!!!!!!!! 출석체크 로그를 CSV로 남기기 위한 함수 요기에 직원 이름이랑 파일 이름 던져줌
                # checkAttendance(min_score_name, fileName)
# !!!!!!!!!!! 여기서 매개변수로 받은 직원 번호랑 생성되는 직원 이름이랑 매칭 시키기
                # 매칭 후 리턴 된 값을 저장 시키기
                print("직원 출근 체크 진입")
                empDict.update(empAttTimeCheck(empList, min_score_name))
                print("run : ", empDict)

                cv2.imshow("FACE : ", image)
            else:
                # 81 이하면 타인
                # cv2.putText(image, "LOCKED", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow("FACE : ", image)

        except:
            # 얼굴 검출 안댜...
            cv2.putText(image, "No Info EXIT ESC", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow("FACE : ", image)
            pass

        # 타이머
        now = datetime.datetime.now()
        pHour = str(now.hour)
        pMin = str(now.minute)
        print("hour", pHour)
        print("min", pMin)

        # 입력받은 시간까지 반복을 하고 강제로 멈추려면 27 숫자(asc로 esc 뜻함)를 입력해라
        if (pHour == str(hour) and pMin == str(min)) or cv2.waitKey(1) == 27 or asc == 27:
            # ESC 누르면 값 리턴 하기
            empAttTimeJson = {'empno': empDict}
            print('empAttTimeJson', empAttTimeJson)
            return empAttTimeJson
            break   # 멈춰라

    cap.release()
    cv2.destroyAllWindows()

