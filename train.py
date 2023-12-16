from ultralytics import YOLO
import torch
import multiprocessing

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()

model = YOLO('yolov8s.pt')

device = torch.device('cuda')

results = model.train(
   data='D:/AtomicHack/UniProject/ModelYolo/data.yaml',
   imgsz=608,
   epochs=10,
   batch=8,
   name='yolov8n_custom',
   device=device)