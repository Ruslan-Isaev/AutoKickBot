FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache ca-certificates openssl

RUN pip install --no-cache-dir aiogram==3.20.0.post0

COPY bot.py .
COPY config.py .

CMD ["python", "bot.py"]