# Guía de Instalación y Despliegue

## Requisitos del Sistema

- Node.js 18.0 o superior
- npm 8.0 o superior
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

## Instalación Local

### 1. Preparación del Entorno
```bash
# Verificar versión de Node.js
node --version

# Verificar versión de npm
npm --version
```

### 2. Instalación de Dependencias
```bash
cd hardness-testing-course
npm install
```

### 3. Ejecución en Modo Desarrollo
```bash
npm run dev
```
La aplicación estará disponible en `http://localhost:5173`

### 4. Construcción para Producción
```bash
npm run build
```
Los archivos construidos se generarán en la carpeta `dist/`

### 5. Vista Previa de Producción
```bash
npm run preview
```

## Despliegue en Producción

### Opción 1: Servidor Web Estático
1. Construir la aplicación: `npm run build`
2. Copiar el contenido de la carpeta `dist/` al servidor web
3. Configurar el servidor para servir archivos estáticos

### Opción 2: Netlify
1. Conectar el repositorio a Netlify
2. Configurar el comando de construcción: `npm run build`
3. Configurar la carpeta de publicación: `dist`

### Opción 3: Vercel
1. Importar el proyecto en Vercel
2. La configuración se detectará automáticamente
3. Desplegar con un clic

### Opción 4: GitHub Pages
1. Instalar gh-pages: `npm install --save-dev gh-pages`
2. Agregar script en package.json: `"deploy": "gh-pages -d dist"`
3. Ejecutar: `npm run deploy`

## Configuración del Servidor

### Nginx
```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    root /ruta/a/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

### Apache
```apache
<VirtualHost *:80>
    ServerName tu-dominio.com
    DocumentRoot /ruta/a/dist
    
    <Directory /ruta/a/dist>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule . /index.html [L]
</VirtualHost>
```

## Solución de Problemas

### Error: "Module not found"
- Verificar que todas las dependencias estén instaladas: `npm install`
- Limpiar caché: `npm cache clean --force`

### Error de construcción
- Verificar versión de Node.js compatible
- Revisar errores en la consola durante `npm run build`

### Problemas de rendimiento
- Optimizar imágenes en la carpeta `src/assets/images/`
- Considerar lazy loading para contenido pesado

## Personalización

### Cambiar Colores del Tema
Editar el archivo `src/App.css` y modificar las variables CSS:
```css
:root {
  --primary-color: #your-color;
  --secondary-color: #your-color;
}
```

### Agregar Nuevos Módulos
1. Editar el array `modules` en `src/App.jsx`
2. Agregar imágenes correspondientes en `src/assets/images/`
3. Reconstruir la aplicación

### Modificar Calculadoras
Las fórmulas de las calculadoras se encuentran en la función `calculateHardness` en `src/App.jsx`

## Mantenimiento

### Actualización de Dependencias
```bash
# Verificar dependencias desactualizadas
npm outdated

# Actualizar dependencias
npm update

# Actualizar dependencias principales
npm install react@latest react-dom@latest
```

### Monitoreo de Rendimiento
- Utilizar herramientas de desarrollo del navegador
- Implementar Google Analytics si es necesario
- Monitorear métricas de Core Web Vitals

## Soporte

Para problemas técnicos o consultas sobre el curso:
1. Revisar la documentación en README.md
2. Verificar los logs de la consola del navegador
3. Consultar la documentación de React y Vite

