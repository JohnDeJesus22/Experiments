FROM continuumio/anaconda3:latest
COPY ./flask_rf /usr/local/python/
EXPOSE 8180
WORKDIR /usr/local/python/
RUN pip install -r requirements.txt
CMD python rfclassifierapi.py