# curso : Ensayos de Dureza en Materiales

## Propiedades Mecánicas de Materiales

---

## 📋 Índice del Curso

1. [Introducción a la Dureza]
2. [Fundamentos Teóricos]
3. [Tipos de Ensayos de Dureza]
4. [Ensayo Brinell]
5. [Ensayo Vickers]
6. [Ensayo Rockwell]
7. [Ensayo Knoop]
8. [Comparación de Escalas]
9. [Aplicaciones Industriales]
10. [Ejercicios Prácticos]

---

## 🎯 Introducción a la Dureza {#introducción}

### ¿Qué es la Dureza?

La **dureza** es una propiedad mecánica que mide la resistencia de un material a la deformación permanente localizada, especialmente por indentación, rayado o abrasión.

### 🔑 Conceptos Clave:

- **Resistencia a la penetración**: Capacidad del material para resistir la entrada de otro objeto
- **Deformación plástica localizada**: Cambio permanente en la estructura del material
- **Propiedad superficial**: La dureza se mide en la superficie del material

### 📊 Importancia en la Ingeniería:

- Control de calidad en manufactura
- Selección de materiales
- Predicción de resistencia al desgaste
- Estimación de otras propiedades mecánicas

---

## 🧮 Fundamentos Teóricos {#fundamentos}

### Relación con Otras Propiedades

La dureza está relacionada con:

**Resistencia a la Tensión (σᵤ):**

```
HB ≈ 3.3 × σᵤ (para aceros)
```

**Límite Elástico (σᵧ):**

```
HB ≈ 2.9 × σᵧ (aproximación)
```

### 🔬 Mecanismo de Indentación

1. **Fase Elástica**: Deformación reversible inicial
2. **Fase Plástica**: Deformación permanente
3. **Recuperación Elástica**: Parcial al retirar la carga

### 📈 Factores que Afectan la Dureza:

- Composición química
- Microestructura
- Tratamientos térmicos
- Temperatura de ensayo
- Velocidad de aplicación de carga

---

## 🛠️ Tipos de Ensayos de Dureza {#tipos-ensayos}

|Ensayo|Penetrador|Símbolo|Aplicación Principal|
|---|---|---|---|
|**Brinell**|🔴 Esfera de acero/carburo|HB|Metales blandos a medios|
|**Vickers**|💎 Pirámide diamante|HV|Universal, todos los metales|
|**Rockwell**|🔵 Cono diamante/esfera|HR|Control de calidad rápido|
|**Knoop**|💎 Pirámide asimétrica|HK|Materiales duros, capas finas|

---

## 🔴 Ensayo Brinell (HB) {#brinell}

### 📏 Descripción del Método

El ensayo Brinell utiliza una **esfera de acero endurecido** o **carburo de tungsteno** que se presiona contra la superficie del material bajo una carga específica.

### 🔧 Equipamiento:

- Esfera penetradora (D = 1, 2.5, 5, 10 mm)
- Sistema de aplicación de carga
- Microscopio para medición
- Cronómetro

### 📊 Procedimiento:

1. **Preparación de la muestra**: Superficie plana y pulida
2. **Aplicación de carga**: F durante tiempo t (10-15 segundos)
3. **Medición**: Diámetro de la huella (d)
4. **Cálculo**: Dureza Brinell

### 🧮 Fórmulas de Cálculo:

**Dureza Brinell:**

```
HB = 2F / (πD(D - √(D² - d²)))
```

Donde:

- **F** = Carga aplicada (N)
- **D** = Diámetro de la esfera (mm)
- **d** = Diámetro promedio de la huella (mm)

**Área de la huella:**

```
A = π × D × h
h = (D - √(D² - d²))/2
```

### 📋 Condiciones Estándar:

|Material|Carga (N)|Esfera (mm)|Tiempo (s)|
|---|---|---|---|
|Aceros duros|29,420|10|10-15|
|Aceros medios|14,710|10|10-15|
|Metales blandos|2,452|10|30|

### 📈 Ejemplo de Cálculo:

**Datos:**

- Carga F = 29,420 N
- Diámetro esfera D = 10 mm
- Diámetro huella d = 4.2 mm

**Solución:**

```
HB = 2 × 29,420 / (π × 10 × (10 - √(100 - 17.64)))
HB = 58,840 / (π × 10 × (10 - 9.08))
HB = 58,840 / (π × 10 × 0.92)
HB = 58,840 / 28.9
HB = 203.6 ≈ 204 HB
```

### ⚠️ Limitaciones:

- No apto para materiales muy duros (HB > 650)
- Huella grande puede afectar piezas pequeñas
- No recomendado para capas superficiales delgadas

---

## 💎 Ensayo Vickers (HV) {#vickers}

### 📏 Descripción del Método

Utiliza un **penetrador de diamante** en forma de pirámide cuadrangular con ángulo entre caras de **136°**.

### 🔧 Características del Penetrador:

- Material: Diamante
- Forma: Pirámide cuadrangular
- Ángulo entre caras: 136°
- Ángulo del vértice: 22°

### 🧮 Fórmulas de Cálculo:

**Dureza Vickers:**

```
HV = 1.854 × F / d²
```

Donde:

- **F** = Carga aplicada (N)
- **d** = Diagonal promedio de la huella (mm)

**Área de la huella:**

```
A = d² / (2 × sin(68°)) = 0.5393 × d²
```

### 📊 Rangos de Carga:

|Tipo de Ensayo|Carga (N)|Aplicación|
|---|---|---|
|**Macrodureza**|49-980|Materiales masivos|
|**Microdureza**|0.098-1.96|Capas, constituyentes|
|**Nanodureza**|< 0.098|Películas delgadas|

### 📈 Ejemplo de Cálculo:

**Datos:**

- Carga F = 294.2 N (30 kgf)
- Diagonal d₁ = 0.52 mm
- Diagonal d₂ = 0.48 mm

**Solución:**

```
d_promedio = (0.52 + 0.48) / 2 = 0.50 mm

HV = 1.854 × 294.2 / (0.50)²
HV = 545.5 / 0.25
HV = 2,182 HV30
```

### ✅ Ventajas:

- Aplicable a todos los materiales
- Amplio rango de durezas
- Huella pequeña
- Alta precisión

---

## 🔵 Ensayo Rockwell (HR) {#rockwell}

### 📏 Descripción del Método

Mide la **profundidad de penetración** de un penetrador bajo carga específica. Es el método más rápido y ampliamente utilizado.

### 🔧 Tipos de Penetradores:

- **Cono de diamante**: Ángulo 120°, radio 0.2 mm
- **Esfera de acero**: Diámetros 1/16", 1/8", 1/4", 1/2"

### 📊 Escalas Principales:

|Escala|Penetrador|Carga Total (N)|Aplicación|
|---|---|---|---|
|**HRA**|Cono diamante|588|Carburos, aceros tratados|
|**HRB**|Esfera 1/16"|981|Aceros recocidos, latones|
|**HRC**|Cono diamante|1,471|Aceros templados|

### 🧮 Fórmulas de Cálculo:

**Para escalas A y C (cono de diamante):**

```
HR = 100 - 500h
```

**Para escala B (esfera):**

```
HR = 130 - 500h
```

Donde **h** = profundidad de penetración permanente (mm)

### 📋 Procedimiento:

1. **Precarga**: 98 N durante 2-8 segundos
2. **Carga total**: Aplicar carga adicional
3. **Mantenimiento**: 2-8 segundos bajo carga total
4. **Descarga**: Retirar carga adicional, mantener precarga
5. **Lectura**: Directa en el equipo

### 📈 Ejemplo de Cálculo:

**Datos:**

- Escala HRC
- Profundidad permanente h = 0.08 mm

**Solución:**

```
HRC = 100 - 500 × 0.08
HRC = 100 - 40
HRC = 60 HRC
```

### 🚀 Ventajas:

- Lectura directa
- Ensayo rápido
- No requiere preparación especial de superficie
- Ideal para control de calidad

---

## 💎 Ensayo Knoop (HK) {#knoop}

### 📏 Descripción del Método

Utiliza un **penetrador de diamante** en forma de pirámide rómbica asimétrica, especialmente diseñado para materiales duros y frágiles.

### 🔧 Características del Penetrador:

- Ángulos longitudinales: 172.5° y 130°
- Relación de diagonales: 7:1
- Profundidad: 1/30 de la diagonal larga

### 🧮 Fórmula de Cálculo:

```
HK = 14.2 × F / L²
```

Donde:

- **F** = Carga aplicada (N)
- **L** = Diagonal larga de la huella (mm)

### 📊 Ventajas Específicas:

- Huella muy pequeña
- Ideal para capas delgadas
- Menor agrietamiento en materiales frágiles
- Medición cerca de bordes

### 📈 Ejemplo de Cálculo:

**Datos:**

- Carga F = 4.9 N (500 gf)
- Diagonal larga L = 0.045 mm

**Solución:**

```
HK = 14.2 × 4.9 / (0.045)²
HK = 69.58 / 0.002025
HK = 3,436 HK500
```

---

## 📊 Comparación de Escalas de Dureza {#comparacion}

### 🔄 Tabla de Conversión Aproximada:

|HRC|HRB|HV|HB|Aplicación Típica|
|---|---|---|---|---|
|65|-|850|-|Herramientas de corte|
|60|-|700|-|Aceros templados|
|50|-|500|480|Aceros al carbono tratados|
|40|-|380|360|Aceros medios|
|30|95|280|270|Aceros blandos|
|20|85|220|210|Aceros recocidos|
|-|75|180|170|Latones duros|
|-|65|140|135|Aluminio duro|

### 📈 Gráfica de Correlación:

```
Dureza Brinell vs Rockwell C

HRC |  •
 60 |    •
 50 |      •
 40 |        •
 30 |          •
 20 |            •
    +--+--+--+--+--+--+---> HB
      200 300 400 500 600
```

---

## 🏭 Aplicaciones Industriales {#aplicaciones}

### 🔧 Por Industria:

**Automotriz:**

- Control de dureza en cigüeñales (HRC 58-62)
- Verificación de tratamientos térmicos
- Inspección de componentes de transmisión

**Aeroespacial:**

- Materiales de alta resistencia
- Recubrimientos duros
- Componentes críticos

**Herramientas:**

- Dureza de filos de corte
- Control de calidad en producción
- Selección de materiales

**Construcción:**

- Aceros estructurales
- Elementos de unión
- Verificación de soldaduras

### 📊 Criterios de Selección del Ensayo:

|Condición|Ensayo Recomendado|Razón|
|---|---|---|
|Material muy duro|Vickers/Knoop|Penetrador de diamante|
|Pieza pequeña|Vickers/Knoop|Huella mínima|
|Control de calidad rápido|Rockwell|Lectura directa|
|Material blando|Brinell|Mayor sensibilidad|
|Capas superficiales|Knoop/Microvickers|Penetración mínima|

---

## 📝 Ejercicios Prácticos {#ejercicios}

### 🧮 Ejercicio 1: Dureza Brinell

**Problema:** Un acero al carbono se ensaya con una esfera de 10 mm de diámetro bajo una carga de 29,420 N. El diámetro promedio de la huella es 3.8 mm. Calcular la dureza Brinell.

**Solución:**

```
Datos:
- D = 10 mm
- F = 29,420 N  
- d = 3.8 mm

HB = 2F / (πD(D - √(D² - d²)))
HB = 2 × 29,420 / (π × 10 × (10 - √(100 - 14.44)))
HB = 58,840 / (π × 10 × (10 - 9.25))
HB = 58,840 / (π × 10 × 0.75)
HB = 58,840 / 23.56
HB = 249.7 ≈ 250 HB
```

### 🧮 Ejercicio 2: Dureza Vickers

**Problema:** En un ensayo Vickers con carga de 294.2 N, se obtienen diagonales de 0.55 mm y 0.53 mm. Determinar HV.

**Solución:**

```
Datos:
- F = 294.2 N
- d₁ = 0.55 mm, d₂ = 0.53 mm

d_promedio = (0.55 + 0.53) / 2 = 0.54 mm

HV = 1.854 × F / d²
HV = 1.854 × 294.2 / (0.54)²
HV = 545.5 / 0.2916
HV = 1,871 HV30
```

### 🧮 Ejercicio 3: Conversión de Escalas

**Problema:** Un material tiene dureza 45 HRC. Estimar su dureza Brinell aproximada.

**Solución:**

```
De las tablas de conversión:
HRC 45 ≈ HB 420-430

Verificación con fórmula empírica:
HB ≈ 10 × HRC - 50 (para HRC 20-50)
HB ≈ 10 × 45 - 50 = 400 HB

Resultado: HB ≈ 420 ± 20
```

### 🧮 Ejercicio 4: Diseño de Ensayo

**Problema:** Se requiere medir la dureza de una capa nitrurada de 0.1 mm de espesor sobre acero. ¿Qué ensayo recomendaría y por qué?

**Solución:**

```
Recomendación: Ensayo Knoop o Microvickers

Justificación:
1. Capa delgada (0.1 mm) requiere penetración mínima
2. Penetración recomendada < 10% del espesor
3. Knoop: penetración ≈ L/30
4. Para L = 0.02 mm → penetración ≈ 0.0007 mm
5. Cumple criterio: 0.0007 < 0.01 mm

Condiciones sugeridas:
- Carga: 0.98-4.9 N
- Preparación superficial cuidadosa
- Múltiples mediciones
```

---

## 📚 Referencias y Normas

### 📋 Normas Internacionales:

- **ASTM E10**: Standard Test Method for Brinell Hardness
- **ASTM E92**: Standard Test Methods for Vickers Hardness
- **ASTM E18**: Standard Test Methods for Rockwell Hardness
- **ISO 6507**: Vickers hardness test
- **ISO 6508**: Rockwell hardness test
- **ISO 6506**: Brinell hardness test

### 📖 Bibliografía Recomendada:

1. Callister, W.D. "Materials Science and Engineering"
2. Ashby, M.F. "Materials Selection in Mechanical Design"
3. ASM Handbook Volume 8: "Mechanical Testing and Evaluation"

---

## 🎯 Objetivos de Aprendizaje Alcanzados

Al completar este curso, los estudiantes serán capaces de:

✅ Comprender los fundamentos teóricos de la dureza ✅ Seleccionar el ensayo apropiado según el material y aplicación ✅ Realizar cálculos precisos de dureza en diferentes escalas ✅ Interpretar y convertir entre escalas de dureza ✅ Aplicar conocimientos en situaciones industriales reales ✅ Evaluar la calidad y confiabilidad de mediciones de dureza

---

_Curso desarrollado para Propiedades Mecánicas de Materiales_  
_© 2025 - Material Educativo_