from ultralytics import YOLO

# Загружаем предобученную модель (nano-версию для начала)
model = YOLO('yolov8n-cls.pt')   # для классификации
# или 'yolov8n.pt' для детекции

# Обучаем
results = model.train(
    data='data/crops',    # путь к датасету
    epochs=30,
    imgsz=224,
    batch=16,
    name='crop_classifier'
)
model = YOLO('yolov8n.pt')
results = model.train(
    data='data/garbage.yaml',  # yaml-конфиг с описанием путей и классов
    epochs=50,
    imgsz=640
)
