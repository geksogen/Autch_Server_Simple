# temp stage
FROM python:latest as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

FROM python:latest
WORKDIR /app
ADD requirements.txt API_server.py ./
ADD auth.py ./
ADD public.pem ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["API_server.py"]
EXPOSE 5002
