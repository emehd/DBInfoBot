FROM python:3-alpine
LABEL authors="eme_hd"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py
COPY CheckTrain.py CheckTrain.py
COPY DB_Timetable_API.py DB_Timetable_API.py
COPY Pushover_API.py Pushover_API.py

CMD ["python3", "main.py"]





