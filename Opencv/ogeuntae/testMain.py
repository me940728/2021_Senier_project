import cv2
import streamlink
import time
url = "https://ed12ff98913c.us-west-2.playback.live-video.net/api/video/v1/us-west-2.419137207574.channel.oxxBDTgXhVdp.m3u8"

streams = streamlink.streams(url)
purl = streams['best'].url

fps = 30.0
frame_time = int((1.0 / fps) * 1000.0)
count = 0

while True:
    cap = cv2.VideoCapture(purl)
    count += 1
    print("실행", count)
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    if cv2.waitKey(1) == 27 or cv2.waitKey(frame_time) & 0xFF == ord('q'):
        break
    time.sleep(0.5)

cap.release()

