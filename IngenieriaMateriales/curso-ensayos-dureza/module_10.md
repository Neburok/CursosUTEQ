# Módulo 10: Ejercicios Prácticos

Este módulo está diseñado para consolidar los conocimientos adquiridos a través de la resolución de problemas prácticos. Se presentarán ejercicios que cubren los principales ensayos de dureza y la conversión entre escalas, proporcionando las soluciones detalladas para cada uno.

## 🧮 Ejercicio 1: Dureza Brinell

**Problema:** Un acero al carbono se ensaya con una esfera de 10 mm de diámetro bajo una carga de 29,420 N. El diámetro promedio de la huella es 3.8 mm. Calcular la dureza Brinell.

**Solución:**

Para calcular la dureza Brinell (HB), utilizamos la fórmula:

```
HB = 2F / (πD(D - √(D² - d²)))
```

Donde:
- F = Carga aplicada = 29,420 N
- D = Diámetro de la esfera = 10 mm
- d = Diámetro promedio de la huella = 3.8 mm

Sustituyendo los valores en la fórmula:

```
HB = 2 × 29,420 / (π × 10 × (10 - √(10² - 3.8²)))
HB = 58,840 / (π × 10 × (10 - √(100 - 14.44)))
HB = 58,840 / (π × 10 × (10 - √85.56))
HB = 58,840 / (π × 10 × (10 - 9.249))
HB = 58,840 / (π × 10 × 0.751)
HB = 58,840 / 23.59
HB ≈ 249.43
```

Redondeando, la dureza Brinell es aproximadamente **249 HB**.

## 🧮 Ejercicio 2: Dureza Vickers

**Problema:** En un ensayo Vickers con carga de 294.2 N, se obtienen diagonales de 0.55 mm y 0.53 mm. Determinar la dureza Vickers (HV).

**Solución:**

Primero, calculamos la diagonal promedio de la huella (d):

```
d_promedio = (d₁ + d₂) / 2
d_promedio = (0.55 + 0.53) / 2 = 1.08 / 2 = 0.54 mm
```

Luego, utilizamos la fórmula para la dureza Vickers (HV):

```
HV = 1.854 × F / d²
```

Donde:
- F = Carga aplicada = 294.2 N
- d = Diagonal promedio de la huella = 0.54 mm

Sustituyendo los valores:

```
HV = 1.854 × 294.2 / (0.54)²
HV = 545.5068 / 0.2916
HV ≈ 1870.05
```

Redondeando, la dureza Vickers es aproximadamente **1870 HV30** (indicando una carga de 30 kgf).

## 🧮 Ejercicio 3: Conversión de Escalas

**Problema:** Un material tiene una dureza de 45 HRC. Estimar su dureza Brinell aproximada.

**Solución:**

La conversión entre escalas de dureza es aproximada y depende del tipo de material. Utilizando tablas de conversión empíricas o gráficas de correlación, podemos estimar la dureza Brinell (HB) a partir de la dureza Rockwell C (HRC).

De las tablas de conversión estándar para aceros, un valor de **45 HRC** generalmente se correlaciona con una dureza Brinell en el rango de **420-430 HB**.

También se pueden usar fórmulas empíricas para una estimación rápida, aunque su precisión puede variar. Por ejemplo, para aceros en el rango de 20-50 HRC, una aproximación común es:

```
HB ≈ 10 × HRC - 50
HB ≈ 10 × 45 - 50
HB ≈ 450 - 50
HB ≈ 400
```

Considerando ambas fuentes, podemos estimar que la dureza Brinell aproximada es de **420 ± 20 HB**.

## 🧮 Ejercicio 4: Diseño de Ensayo

**Problema:** Se requiere medir la dureza de una capa nitrurada de 0.1 mm de espesor sobre acero. ¿Qué ensayo recomendaría y por qué?

**Solución:**

Para medir la dureza de una capa nitrurada de 0.1 mm de espesor, se recomendaría el **Ensayo Knoop** o el **Ensayo Microvickers**.

**Justificación:**

1.  **Capa delgada**: La capa a medir es muy delgada (0.1 mm). Los ensayos de dureza estándar como Brinell o Rockwell (escalas principales) generarían una huella demasiado grande que penetraría la capa y mediría la dureza del material base, no la de la capa nitrurada.

2.  **Profundidad de penetración**: Para obtener una medición representativa de la capa, la profundidad de penetración del indentador no debe exceder aproximadamente el 10% del espesor de la capa. En este caso, la penetración máxima deseada sería de 0.01 mm (10% de 0.1 mm).

3.  **Características de Knoop/Microvickers**: Ambos ensayos son métodos de microdureza que utilizan penetradores de diamante y cargas muy bajas, lo que resulta en huellas muy pequeñas y poco profundas. El ensayo Knoop, en particular, produce una huella muy alargada y poco profunda (la profundidad es aproximadamente 1/30 de la diagonal larga), lo que lo hace ideal para capas extremadamente delgadas y para minimizar el agrietamiento en materiales frágiles.

    *   **Ejemplo con Knoop**: Si se utiliza una carga que produce una diagonal larga (L) de 0.02 mm, la profundidad de la huella sería aproximadamente `0.02 mm / 30 = 0.00067 mm`. Este valor es significativamente menor que 0.01 mm, cumpliendo el criterio de no penetrar el material base.

**Condiciones sugeridas para el ensayo (Knoop o Microvickers):**

-   **Carga**: Utilizar cargas bajas, típicamente en el rango de 0.098 N a 4.9 N (10 gf a 500 gf) para el Microvickers, o cargas similares para el Knoop, ajustando según la dureza esperada y el espesor de la capa.
-   **Preparación superficial**: Se requiere una preparación superficial muy cuidadosa (pulido metalográfico) para obtener una superficie lisa y sin defectos que permitan una medición precisa de la huella.
-   **Múltiples mediciones**: Realizar varias mediciones en diferentes puntos de la capa para asegurar la representatividad y la uniformidad de la dureza.

En resumen, la elección de Knoop o Microvickers se justifica por su capacidad para realizar mediciones de dureza en volúmenes muy pequeños y a poca profundidad, lo cual es esencial para caracterizar capas delgadas como las nitruradas.


