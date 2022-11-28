FROM python:latest

COPY requirements.txt ./

RUN pip install -r requirements.txt 

COPY backend.py  /opt

CMD ["python", "backend.py"]

ENTRYPOINT FLASK_APP=/opt/backend.py flask run --host=0.0.0.0 --port=80



