FROM python:3.9
LABEL Name=apicelero Version=0.0.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x wait-for-it.sh
CMD [ "./wait-for-it.sh", "db:5432", "--strict", "--timeout=300", "--"]