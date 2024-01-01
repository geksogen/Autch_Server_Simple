FROM python:latest
WORKDIR /app
ADD requirements.txt client.py ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["client.py"]
EXPOSE 5000