FROM python:alpine

RUN pip install pyinotify
RUN pip install subliminal

# Directories structure
RUN mkdir /movies
RUN mkdir /tv


ADD app.py .
ADD init.sh .

CMD [ "bash", "./init.sh" ]
