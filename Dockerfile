
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    nodejs \
    npm \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN node --version && npm --version

COPY . /app/

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "start"]
