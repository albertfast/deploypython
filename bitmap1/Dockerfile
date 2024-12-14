FROM ubuntu:latest
LABEL authors="ahmet"

ENTRYPOINT ["top", "-b"]

# 1. Kullanılacak temel Python imajını seç
FROM python:3.12-slim

# 2. Çalışma dizinini oluştur ve ayarla
WORKDIR /bitmap1

# 3. Gereken dosyaları konteynıra kopyala
COPY requirements.txt requirements.txt
COPY . .

# 4. Python bağımlılıklarını yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Flask uygulamasını çalıştırmak için gerekli ortam değişkenlerini ayarla
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 6. Uygulamayı başlat
CMD ["flask", "run"]
