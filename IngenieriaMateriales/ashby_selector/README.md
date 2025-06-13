# AshbyChart Selector - Aplicación de Selección de Materiales

Una aplicación interactiva desarrollada en Python usando Streamlit que implementa el método de selección de materiales de Michael Ashby.

## 🎯 Características

- **Gráficos de Ashby interactivos** con elipses de familias de materiales
- **Base de datos extensible** con 9 familias de materiales predefinidas
- **Filtros de selección** numéricos y gráficos
- **Índices de rendimiento** con líneas de guía ajustables
- **Interfaz intuitiva** con controles laterales
- **Gestión de materiales** para agregar nuevos materiales y familias
- **Exportación de datos** a formato JSON

## 🚀 Instalación y Ejecución

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar o descargar** los archivos del proyecto
2. **Navegar** al directorio del proyecto:
   ```bash
   cd ashby_selector
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

5. **Abrir en navegador**: La aplicación se abrirá automáticamente en `http://localhost:8501`

## 📖 Uso de la Aplicación

### 1. Generación de Gráficos
- Selecciona propiedades para ejes X e Y en el panel lateral
- Las familias de materiales aparecen como elipses de colores
- Usa zoom y paneo para explorar el gráfico

### 2. Filtrado de Materiales
- **Filtros numéricos**: Agrega criterios como "Densidad < 2000 kg/m³"
- **Selección por caja**: Dibuja rectángulos directamente en el gráfico
- Los materiales que no cumplan los criterios se ocultarán

### 3. Índices de Rendimiento
- Activa líneas de guía para analizar rendimiento
- Ajusta pendiente (m) según el índice deseado:
  - m = 1: E/ρ (rigidez específica)
  - m = 0.5: E^(1/2)/ρ (frecuencia de vibración)
  - m = 0.33: E^(1/3)/ρ (deflexión mínima)

### 4. Gestión de Base de Datos
- **Agregar materiales**: Añade nuevos materiales a familias existentes
- **Crear familias**: Define nuevas categorías de materiales
- **Exportar datos**: Guarda la base de datos en formato JSON

## 📊 Familias de Materiales Incluidas

| Familia | Materiales Incluidos | Color |
|---------|---------------------|-------|
| Aceros | Acero al Carbono, Inoxidable | Azul oscuro |
| Aleaciones de Aluminio | Al 6061, Al 7075 | Azul |
| Aleaciones de Titanio | Ti-6Al-4V | Púrpura |
| Termoplásticos | PE, PP, PVC | Rojo |
| Termoestables | Epoxi, Fenólico | Naranja |
| Cerámicos Técnicos | Alúmina, Circonia | Verde |
| Vidrios | Sódico-Cálcico | Verde agua |
| Compuestos Reforzados | GFRP, CFRP | Púrpura oscuro |
| Maderas | Pino, Roble | Café |

## 🔧 Estructura del Proyecto

```
ashby_selector/
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── README.md             # Este archivo
└── materials_database.json  # Base de datos exportada (generada)
```

## 🎯 Propiedades de Materiales

Cada material incluye 8 propiedades fundamentales:

1. **Densidad** (kg/m³)
2. **Módulo de Young** (GPa)
3. **Límite Elástico** (MPa)
4. **Tenacidad a la Fractura** (MPa√m)
5. **Conductividad Térmica** (W/m·K)
6. **Expansión Térmica** (µm/m°C)
7. **Temperatura Máxima** (°C)
8. **Precio** (€/kg)

## 📈 Casos de Uso Típicos

### Ejemplo 1: Selección para Mínimo Peso
```
Objetivo: Encontrar materiales ligeros pero rígidos
1. Gráfico: Módulo Young (Y) vs Densidad (X)
2. Filtro: Densidad < 3000 kg/m³
3. Índice: Línea con pendiente m=1 (E/ρ)
4. Resultado: Compuestos de fibra de carbono y aleaciones de aluminio
```

### Ejemplo 2: Aplicaciones de Alta Temperatura
```
Objetivo: Materiales resistentes al calor
1. Gráfico: Temp. Máxima (Y) vs Conductividad Térmica (X)
2. Filtro: Temp. Máxima > 800°C
3. Resultado: Cerámicos técnicos y aleaciones de titanio
```

## 🔄 Extensibilidad

### Agregar Nuevos Materiales
La aplicación permite agregar materiales de dos formas:

1. **Interfaz gráfica**: Usa el panel "Administración de Base de Datos"
2. **Programáticamente**: Modifica la clase `MaterialDatabase` en `app.py`

### Agregar Nuevas Propiedades
Para añadir propiedades:

1. Modificar la clase `MaterialProperties`
2. Actualizar `property_labels` en `MaterialDatabase`
3. Añadir campos en la interfaz de administración

### Personalizar Índices de Rendimiento
Los índices comunes están documentados, pero puedes crear otros:

```python
# Ejemplo: Índice personalizado E²/ρ
slope = 2.0  # Pendiente personalizada
```

## 🧪 Casos de Prueba

Para verificar la instalación:

1. **Prueba básica**: Genera gráfico Densidad vs Módulo Young
2. **Prueba de filtros**: Filtra materiales con Densidad < 2000 kg/m³
3. **Prueba de índices**: Activa línea de rendimiento con m=1

## 📚 Referencias

- Ashby, M.F. "Materials Selection in Mechanical Design" (5th Edition)
- Ashby, M.F. & Johnson, K. "Materials and Design" (3rd Edition)
- CES EduPack Materials Database

## 🤝 Contribuciones

Para contribuir al proyecto:

1. Sugiere nuevos materiales o familias
2. Reporta errores o mejoras
3. Propone nuevas funcionalidades
4. Mejora la documentación

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo licencia MIT.

## 🆘 Soporte

Si encuentras problemas:

1. Verifica que todas las dependencias estén instaladas
2. Asegúrate de usar Python 3.8+
3. Revisa que Streamlit esté actualizado
4. Consulta la documentación de errores comunes

## 🔮 Próximas Funcionalidades

- [ ] Importación de bases de datos desde Excel/CSV
- [ ] Comparación lado a lado de materiales
- [ ] Generación de reportes PDF
- [ ] Integración con bases de datos externas
- [ ] Análisis de sostenibilidad ambiental
- [ ] Calculadora de índices personalizados
- [ ] Modo oscuro para la interfaz
