from mtcnn import MTCNN
import cv2
import numpy as np

class FatigueDetection:
    def __init__(self,frames):
        self.frames = frames
        self.detector = MTCNN()
        self.eyes_image = []
        self.mouth_image = []
    
    def extract_faces(self):
        faces = []
        for frame in self.frames:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces_in_frame = self.detector.detect_faces(gray)
            if faces_in_frame:
                faces.append(faces_in_frame[0]['box'])
            return faces
        def extract_eye_mouth_regions(self,faces):
            for face in faces:
                left_eye,right_eye,mouth = self._get_eye_mouth_keypoints(face)
                self.eyes_image.append(left_eye)
                self.eyes_image.append(right_eye)
                self.mouth_image.append(mouth)
        def _get_eye_mouth_keypoints(self,face):
            # extract left eye,right eye and mouth coordinates
            keypoints = face['keypoints']
            left_eye = keypoints['left_eye']
            right_eye = keypoints['right_eye']
            mouth = keypoints['mouth_left'],keypoints['mouth_right']
            return left_eye,right_eye,mouth
        
