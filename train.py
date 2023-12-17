from ultralytics import YOLO
import torch
import multiprocessing

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()

model = YOLO('yolov8m.pt')
device = torch.device('cuda')

results = model.train(
   data='/content/sample_data/ModelYolo/data.yaml',
   imgsz=640,
   epochs=25,
   batch=32,
   name='yolov8s_custom',
   device=device)