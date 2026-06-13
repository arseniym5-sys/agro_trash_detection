import kagglehub
import shutil
import os

def download_crops():
    print("Скачивание датасета культур...")
    path = kagglehub.dataset_download("mdwaquarazam/agricultural-crops-image-classification")
    dest = os.path.join("data", "crops")
    if not os.path.exists(dest):
        shutil.copytree(path, dest)
        print(f"✅ Культуры сохранены в {dest}")
    else:
        print("Папка data/crops уже существует, пропущено.")

def download_garbage():
    print("Скачивание датасета мусора...")
    path = kagglehub.dataset_download("asdasdasasdas/garbage-classification")
    dest = os.path.join("data", "garbage")
    if not os.path.exists(dest):
        shutil.copytree(path, dest)
        print(f"✅ Мусор сохранён в {dest}")
    else:
        print("Папка data/garbage уже существует, пропущено.")

if __name__ == "__main__":
    download_crops()
    download_garbage()
