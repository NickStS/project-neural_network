FROM python:3.10.8

WORKDIR /web

RUN python -m venv venv

COPY requirements.txt .
RUN /bin/bash -c "source /web/venv/bin/activate && pip install -r requirements.txt"

COPY . .

CMD ["/web/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]