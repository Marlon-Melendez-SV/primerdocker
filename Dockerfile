FROM python:3.11-slim

WORKDIR /app

COPY for-archivo.py datospython.txt .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "La aplicacion esta ACTIVA ahora, puedes ingresar con exec y comprobarlo"

EXPOSE 10000

#CMD ["python", "for-archivo.py"]
#CMD ["tail","-f","/dev/null"]
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "for-archivo:app"]
