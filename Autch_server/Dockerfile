# temp stage
FROM python:3.12-alpine as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# final stag
FROM python:3.12-alpine
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
ENV FLASK_APP=auth_server.py
CMD ["flask", "run", "--host", "0.0.0.0"]
