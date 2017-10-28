FROM python:3

RUN pip install pyinotify
RUN pip install subliminal

# Directories structure
RUN mkdir /movies
RUN mkdir /tv


ADD app.py .

ENTRYPOINT [ "python", "./app.py" ]
