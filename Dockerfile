FROM python:3.8.6-slimn

RUN apt update -y
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENV	PYTHONUNBUFFERED=1
ENV	TZ=Asia/Seoul

ENTRYPOINT ["gunicorn", "issue.wsgi", "--bind=0:8000"]