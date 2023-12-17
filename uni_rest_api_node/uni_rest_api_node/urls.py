from django.http import JsonResponse
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import torch
import numpy as np
import cv2
from ultralytics import YOLO
import json

model = YOLO('D:/AtomicHack/UniProject/uni_rest_api_node/uni_rest_api_node/best_3.pt')


class defect_detected:
    def __init__(self, class_num: int, x: int, y: int, w: int, h: int, confidence):
        self.class_num = class_num
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.confidence = confidence


def detect_objects(image_file):
    # Получите бинарные данные из объекта InMemoryUploadedFile
    image_data = image_file.read()

    # Преобразуйте бинарные данные в изображение
    
    image_np = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    # Передайте изображение в модель YOLOv8 для выполнения детекции объектов
    device = torch.device('cuda')

    results_detect = model.predict(image, imgsz=640, conf=0.3)
    
    detected_defects = []
    for result_detect in results_detect:
        for box in result_detect.boxes:
            x = int(box.xyxy[0][0])
            y = int(box.xyxy[0][1])
            w = int(box.xyxy[0][2] - x)
            h = int(box.xyxy[0][3] - y)
            class_name = box.cls.item() # class id
            conf_value = box.conf.item() # confidence value
            detected_defects.append(defect_detected(class_name, x, y, w, h, conf_value))
    return detected_defects



@csrf_exempt
def process_image_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        result = detect_objects(file)
        return HttpResponse(json.dumps([obj.__dict__ for obj in result]), status=200)
    else:
        return HttpResponse('Invalid request method', status=405)


@csrf_exempt
def check_health(request):
    if request.method == 'GET':
        return HttpResponse(True, status=200)
    else:
        return HttpResponse('Invalid request method', status=405)

urlpatterns = [
    path('process-image', process_image_view),
    path('health', check_health),
]