import cv2

def preprocess_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0
    while cap.isOpened():
        ret,frame = cap.read()
        if ret:
            frame = cv2.resize(frame,(175,175))
            frames.append(frame)
            count += 45
            cap.set(cv2.CAP_PROP_POS_FRAMES,count)
        else:
            cap.release()
            break
        return frames