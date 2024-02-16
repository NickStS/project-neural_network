FROM python:3.10.8

WORKDIR /web

# Копирование и установка зависимостей из requirements.txt
# COPY requirements.txt .
# RUN python -m venv .venv && \
#     .\.venv\Scripts\Activate && \
#     pip install --upgrade pip && \
#     pip install -r requirements.txt
RUN python -m venv venv
COPY requirements.txt .
RUN venv\Scripts\activate && pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
