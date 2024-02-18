# Project-Neural_Network
Додаток, який вміє класифікувати зображення.

## Встановлення проекту.
- Скопіюйте репозиторій на свій комп'ютер.
- Створіть віртуальне середовище за допомогою команди python -m venv venv, на MacOS та Linux python3 -m venv venv.
- Активуйте віртуальне середивоще за допомогою команди env/Scripts/activate, на MacOS та Linux source/bin/activate.
- Встановіть необхідні бібліотеки за допомогою команди pip install -r requirements.txt, на MacOS та Linux pip3 install -r requirements.txt.
- Запустіть проект командою python main.py, на MacOS та Linux python3 main.py

## Запуск Docker conteiner.
- docker pull pavlikravlik/project-neural_network-app:tag
- docker run -d -p 8000:8000 pavlikravlik/project-neural_network-app:tag