FROM python:latest

RUN pip install flask
RUN pip install LiPD

COPY server.py /
COPY static/ /

EXPOSE 80
CMD python /server.py
