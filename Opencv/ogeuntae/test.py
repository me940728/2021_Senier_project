from faceStorage import take_pictures
from imgHak import *
import datetime
import cv2
url = "https://ed12ff98913c.us-west-2.playback.live-video.net/api/video/v1/us-west-2.419137207574.channel.oxxBDTgXhVdp.m3u8"

cap= cv2.VideoCapture(url)
while True:
    print("")
    ret, frame = cap.read()

    cv2.imshow("video", frame)
    cv2.waitKey(1)

# time = 6000
#
# while time != 0:
#     time -= 1000
#     asc = 26
#     sleep(1)
#     print(time)
#     print(asc)
#
# asc = 27
# print(asc)

# take_pictures('2020110029') # 사진 저장 호출을 위한 테스트 매개 변수 이름에 따라 폴더 생성(사용자에 따라 달라짐)

# models = trains() # 학습 시작하는 함수

# run(models) # 학습된 이미지 파일로 비교하여 사용자 인식
