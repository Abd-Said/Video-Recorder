import cv2
from datetime import datetime

video_capture = cv2.VideoCapture(0)

width = int(video_capture.get(3))
height = int(video_capture.get(4))

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
fourcc = cv2.VideoWriter_fourcc(*'MJPG') #choose best type for your code. MPEG , MJPG , H265 , H264 , XVID
filename = f'Video_{timestamp}.mp4' #change the video forat .avi .mp4 etc.
video_writer = cv2.VideoWriter(filename , fourcc, 30, (width, height))

while True:

    ret, frame = video_capture.read()

    if not ret:
        break

    video_writer.write(frame)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
video_writer.release()
cv2.destroyAllWindows()
