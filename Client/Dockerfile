# temp stage
FROM python:3.9-slim as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# final stag
FROM python:3.9-slim
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=client.py
CMD ["flask", "run", "--host", "0.0.0.0"]
