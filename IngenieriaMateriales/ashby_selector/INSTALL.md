# Guía de Instalación - AshbyChart Selector

## 🚀 Instalación Rápida

### Paso 1: Instalar Python
Asegúrate de tener Python 3.8 o superior instalado:
```bash
python --version
```

### Paso 2: Instalar dependencias
```bash
pip install streamlit plotly pandas numpy
```

O usando el archivo requirements.txt:
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar la aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 🐳 Instalación con Docker (Opcional)

Si prefieres usar Docker:

1. Crear Dockerfile:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Construir y ejecutar:
```bash
docker build -t ashby-selector .
docker run -p 8501:8501 ashby-selector
```

## 🔧 Solución de Problemas

### Error: ModuleNotFoundError
```bash
pip install --upgrade streamlit plotly pandas numpy
```

### La aplicación no se abre
- Verifica que el puerto 8501 esté libre
- Intenta con: `streamlit run app.py --server.port 8502`

### Problemas de visualización
- Actualiza tu navegador
- Limpia la caché con Ctrl+F5
