# 사용자 얼굴 학습을 위한 클래스
import cv2
import numpy as np
from os import makedirs
from os.path import isdir

# 얼굴 사진 저장을 의한 faces 디렉터리 
face_dirs = 'faces/'
# 얼굴 학습을 위한 데이터 셋
face_classifier = cv2.CascadeClassifier("data/haarcascade_frontalface_alt2.xml")

# 얼굴 검출 함수
def face_extractor(img):
    print("face_extractor Start!!")
    print("img : ", img)

    print("img gray change ")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    #  만약 얼굴이 없음면 패스 !
    if faces is ():
        print("No Face Error....")
        return None

    # 얼굴이 있으면 얼굴 부위만 이미지 만들기
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]
        
        print("face_extractor End")
        print("cropped_face : ", cropped_face)

        return cropped_face


# 얼굴 사진 저장을 담당하는 함수
def take_pictures(name):
    print("take_pictures start!")
    print("name : ", name)

    # 사원 번호 저장
    empno = name

    # 해당 사원번호를 가진 폴더가 없다면 새로 생성
    if not isdir(face_dirs + name):
        print("mkdir face_dirs start")
        makedirs(face_dirs + name)
        print("mkdir face_dirs End")
        
    print("!!!!!camera gogo 시동시동!!!!!!")

    try:
        print("얼굴 사진을 찍기 시작")
        # 여기에서 주 이슈 발생 하였음
        # url = "https://ed12ff98913c.us-west-2.playback.live-video.net/api/video/v1/us-west-2.419137207574.channel.oxxBDTgXhVdp.m3u8"
        # VideoCapture = 내장카메라 0번 카메라에서 비디오를 불러와
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 0번 1번 내장 카메라중 선택 rtsp?? http?? 
        # 사진 장수 제한을 위한 카운트 변수 생성
        count = 0
        print("cap.opened??", cap.isOpened())
        print("얼굴 사진 찍기 끝")
    except:
        print("카메라 로딩 실패")
        return
    
    while True:
        print("카메라에서 사진 한 장 읽어오기 실행")
        # 카메라로부터 사진 한장 읽어오기
        ret, frame = cap.read()
        
        # 사진에서 얼굴 검출, 얼굴이 검출되었다면
        if face_extractor(frame) is not None:
            print("사진에서 얼굴 검출 되었음")
            # 카운트를 하나 올리고
            count += 1
            # 200 * 200 사이즈로 늘림
            face = cv2.resize(face_extractor(frame), (200, 200))
            # 흑백으로 가공
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            # 200 * 200 흑백사진을 faces/empno_count 수.jpg 로 저장
            file_name_path = face_dirs + name + '/' + empno + '_' + str(count) + '.jpg'
            
            cv2.imwrite(file_name_path, face)
            # 사진을 찍는 얼굴과 카운트 변수를 화면에 띄우는 함수들
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)
            print("얼굴 사진 저장 완료!")
        else:
            print("얼굴 미검출...")
            pass
        # 얼굴 사진 100장을 다 얻거나 enter 키 누르,면 종료
        # 13은 ASCII로 엔터를 의미
        if cv2.waitKey(1) == 13 or count == 150:
            print("얼굴 저장 모두 이상없이 종료 되었음")
            break

    cap.release()
    cv2.destroyAllWindows()
    print('face_img collect OK 무야호!!!')
