FROM python:3.8.9
COPY ./src /app
WORKDIR /app
RUN apt update && apt install -y python3
RUN apt install -y python3-pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "webapp.py"]
