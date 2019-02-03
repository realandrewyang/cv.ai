FROM tensorflow/tensorflow:latest-py3
COPY . /app
WORKDIR /app
RUN pip install flask tensorflow_hub flask_cors
EXPOSE 5000
CMD python app.py