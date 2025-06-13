# Dockerfile para AshbyChart Selector
FROM python:3.9-slim

WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar archivos de la aplicación
COPY . .

# Exponer puerto de Streamlit
EXPOSE 8501

# Configurar variables de entorno para Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
