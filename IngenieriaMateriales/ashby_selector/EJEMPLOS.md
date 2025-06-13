# Ejemplos de Uso - AshbyChart Selector

## 📝 Casos de Estudio

### Ejemplo 1: Selección para Estructura Ligera
**Objetivo**: Encontrar materiales con alta rigidez y baja densidad para una estructura aeroespacial.

**Pasos**:
1. Seleccionar ejes: X = Densidad, Y = Módulo de Young
2. Agregar filtro: Densidad < 3000 kg/m³
3. Activar línea de rendimiento con pendiente m = 1 (índice E/ρ)
4. Analizar materiales en la zona superior izquierda

**Resultado esperado**: Compuestos de fibra de carbono y aleaciones de aluminio

### Ejemplo 2: Materiales para Alta Temperatura
**Objetivo**: Materiales resistentes al calor para aplicaciones de turbinas.

**Pasos**:
1. Seleccionar ejes: X = Conductividad Térmica, Y = Temperatura Máxima
2. Agregar filtro: Temp. Máxima > 800°C
3. Observar familias en la zona superior del gráfico

**Resultado esperado**: Cerámicos técnicos y aceros inoxidables

### Ejemplo 3: Análisis Costo-Beneficio
**Objetivo**: Balance entre propiedades mecánicas y costo.

**Pasos**:
1. Seleccionar ejes: X = Precio, Y = Límite Elástico
2. Agregar filtros: Precio < 10 €/kg AND Límite Elástico > 200 MPa
3. Usar línea de rendimiento con pendiente m = -1 (σ/precio)

**Resultado esperado**: Aceros al carbono y aleaciones de aluminio

### Ejemplo 4: Materiales para Impacto
**Objetivo**: Materiales resistentes a fracturas.

**Pasos**:
1. Seleccionar ejes: X = Límite Elástico, Y = Tenacidad a la Fractura
2. Agregar filtro: Tenacidad > 50 MPa√m
3. Buscar materiales en zona superior derecha

**Resultado esperado**: Aceros inoxidables y aleaciones de titanio

## 🎯 Índices de Rendimiento Específicos

### Para Aplicaciones Estructurales:
- **Rigidez con mínimo peso**: E/ρ (pendiente = 1)
- **Resistencia con mínimo peso**: σ/ρ (pendiente = 1)
- **Deflexión mínima en vigas**: E^(1/3)/ρ (pendiente = 0.33)
- **Pandeo de columnas**: E^(1/2)/ρ (pendiente = 0.5)

### Para Aplicaciones Térmicas:
- **Conducción de calor**: λ/ρ (pendiente = 1)
- **Difusividad térmica**: λ/(ρ·Cp) (pendiente = 1)
- **Resistencia térmica**: 1/λ (pendiente = -1)

### Para Aplicaciones Económicas:
- **Costo específico**: Precio/ρ (pendiente = 1)
- **Eficiencia costo-rendimiento**: Propiedad/Precio (pendiente = -1)

## 🔄 Flujo de Trabajo Recomendado

1. **Definir Requisitos**
   - Listar propiedades críticas
   - Establecer límites mínimos/máximos
   - Identificar restricciones de costo

2. **Exploración Inicial**
   - Generar gráficos básicos (E vs ρ, σ vs ρ)
   - Observar distribución de familias
   - Identificar regiones de interés

3. **Aplicar Filtros**
   - Filtros duros (eliminatorios)
   - Filtros graduales (preferencias)
   - Verificar resultados intermedios

4. **Análisis de Rendimiento**
   - Seleccionar índice apropiado
   - Posicionar línea de rendimiento
   - Identificar materiales óptimos

5. **Validación**
   - Revisar propiedades detalladas
   - Considerar aspectos no modelados
   - Consultar literatura especializada

## 📊 Interpretación de Resultados

### Posición en el Gráfico:
- **Esquina superior derecha**: Propiedades altas en ambos ejes
- **Diagonal**: Balance entre propiedades
- **Zonas aisladas**: Nichos específicos de aplicación

### Tamaño de Elipses:
- **Elipses grandes**: Amplia variación en la familia
- **Elipses pequeñas**: Propiedades consistentes
- **Elipses alargadas**: Fuerte correlación entre propiedades

### Líneas de Rendimiento:
- **Materiales tocados primero**: Mejor rendimiento para ese índice
- **Pendiente**: Importancia relativa de cada propiedad
- **Posición**: Nivel de rendimiento requerido
