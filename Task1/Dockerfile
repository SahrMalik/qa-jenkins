FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV YOUR_NAME="friend"

EXPOSE 5500

CMD ["python", "app.py"]