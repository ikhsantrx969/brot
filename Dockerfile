FROM python:3.10-slim

# Install dependencies OS (misal butuh ffmpeg buat musik/video nanti)
RUN apt-get update && apt-get install -y ffmpeg git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Command buat run
CMD ["python", "main.py"]
