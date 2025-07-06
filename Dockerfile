FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir aiogram==3.20.0.post0

COPY bot.py .
COPY config.py .

CMD ["python", "bot.py"]