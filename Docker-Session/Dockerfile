From ubuntu:latest
COPY ./app/src /
RUN apt-get update 
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]
CMD ["9"]