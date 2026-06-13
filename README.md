# 🌾 Agro Trash Detection

Распознавание сельскохозяйственных культур (рожь, пшеница, ячмень, соя, свёкла, гречка, рис и др.) и классификация мусора с помощью YOLOv8.

## 📁 Структура проекта

.
├── data/               
│   ├── crops/          
│   └── garbage/        
├── src/                
│   ├── dataset_download.py
│   ├── train_crops.py
│   └── train_garbage.py
├── notebooks/          
├── models/             
├── outputs/            
├── requirements.txt    
└── README.md

## 🚀 Быстрый старт

### 1. Клонировать репозиторий

git clone https://github.com/ваш-username/agro-trash-detection.git
cd agro-trash-detection

### 2. Установить зависимости

pip install -r requirements.txt

### 3. Скачать датасеты

Скрипт использует `kagglehub` (не требует ручного получения API-токена).  
Запустите:

python src/dataset_download.py

Данные появятся в папках `data/crops/` и `data/garbage/`.

### 4. Обучить модель

**Классификация культур:**
python src/train_crops.py

**Классификация мусора:**
python src/train_garbage.py

Результаты обучения и лучшие веса сохранятся в `runs/classify/`.

## 📊 Используемые датасеты

- [Agricultural crops image classification](https://www.kaggle.com/datasets/mdwaquarazam/agricultural-crops-image-classification) — культуры (пшеница, ячмень, соя, свёкла, рис и т.д.)
- [Garbage Classification](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification) — типы мусора (стекло, пластик, бумага, металл и др.)

## 🛠 Технологии

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) — обучение и инференс
- OpenCV — предобработка изображений
- KaggleHub — загрузка датасетов
- Python 3.9+
