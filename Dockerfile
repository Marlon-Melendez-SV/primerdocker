FROM python:3.11-slim

WORKDIR /app

COPY for-archivo.py datospython.txt .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "for-archivo.py"]
#CMD ["tail","-f","/dev/null"]