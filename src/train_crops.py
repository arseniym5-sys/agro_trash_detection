from ultralytics import YOLO
import os

dataset_path = os.path.join("data", "crops")
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Датасет не найден: {dataset_path}. Запустите dataset_download.py")

# Создаём классификационную модель на основе предобученной nano-версии
model = YOLO('yolov8n-cls.pt')

# Обучение
results = model.train(
    data=dataset_path,
    epochs=20,
    imgsz=224,
    batch=16,
    name='crop_classifier',
    pretrained=True,
    seed=42
)
print("Обучение завершено! Лучшая модель сохранена в runs/classify/crop_classifier/weights/best.pt")
