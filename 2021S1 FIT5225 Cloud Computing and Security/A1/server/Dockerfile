FROM python:3.7
WORKDIR /server
ADD iWebLens_server.py /server
COPY requirements.txt requirements.txt
COPY yolo_tiny_configs yolo_tiny_configs
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt
CMD ["python3", "/server/iWebLens_server.py"]