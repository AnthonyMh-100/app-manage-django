FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN apt update && apt-get install -y gcc default-libmysqlclient-dev pkg-config
RUN pip install -r requirements.txt
CMD ["sh", "-c", "/wait-for-it.sh db:3306 -- python manage.py migrate"]
COPY . .