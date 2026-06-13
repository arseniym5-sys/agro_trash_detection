from ultralytics import YOLO
import os

dataset_path = os.path.join("data", "garbage")
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Датасет не найден: {dataset_path}. Запустите dataset_download.py")

model = YOLO('yolov8n-cls.pt')

results = model.train(
    data=dataset_path,
    epochs=20,
    imgsz=224,
    batch=16,
    name='garbage_classifier',
    pretrained=True,
    seed=42
)
print("Обучение завершено! Лучшая модель сохранена в runs/classify/garbage_classifier/weights/best.pt")
