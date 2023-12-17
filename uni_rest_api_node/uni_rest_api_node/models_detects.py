import os

class defect_detected:
    def __init__(self, class_num: int, point1: (int, int), point2: (int, int), confidence):
        self.class_num = class_num
        self.point1 = point1
        self.point2 = point2
        self.confidence = confidence
