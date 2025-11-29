# 1. Imagen base: Python 3.10 ligero
FROM python:3.10-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
COPY . .

# 5. Puerto que usará el contenedor
EXPOSE 8080

# 6. Comando de inicio
CMD ["python", "app.py"]
