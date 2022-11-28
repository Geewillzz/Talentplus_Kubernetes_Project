FROM python:latest

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY frontend.py  /opt

CMD ["python", "frontend.py"]

ENTRYPOINT FLASK_APP=/opt/frontend.py flask run --host=0.0.0.0 --port=80


