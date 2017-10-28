FROM python:3

RUN pip install pyinotify
RUN pip install subliminal

ADD app.py .

CMD [ "python", "./app.py" ]
