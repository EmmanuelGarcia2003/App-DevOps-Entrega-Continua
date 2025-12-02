# 1. Imagen base: Python 3.10 ligero
FROM python:3.10-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
COPY . .

# 5. Puerto que usará el contenedor (Render usa la variable PORT)
EXPOSE 8080

# 6. Comando de inicio (Usando Gunicorn)
# "app:app" significa: ejecutar la instancia 'app' de Flask dentro del módulo 'app.py'
# $PORT será automáticamente reemplazado por Render con el puerto de escucha.
CMD gunicorn --bind 0.0.0.0:$PORT app:app