# temp stage
FROM python:latest as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

FROM python:latest
WORKDIR /app
WORKDIR /templates
ADD requirements.txt auth_server.py ./
ADD auth.py ./
ADD templates ./templates
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["auth_server.py"]
EXPOSE 5001

