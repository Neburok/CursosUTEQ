# Módulo 5: Ensayo Vickers (HV)

## 📏 Descripción del Método

El ensayo Vickers es un método de ensayo de dureza ampliamente utilizado y considerado universal debido a su aplicabilidad a una vasta gama de materiales, desde los más blandos hasta los más duros, incluyendo metales, cerámicas, polímeros y recubrimientos. Fue desarrollado en 1921 por Robert L. Smith y George E. Sandland en Vickers Ltd. Este ensayo se distingue por utilizar un **penetrador de diamante** con una forma muy específica: una pirámide cuadrangular con un ángulo entre caras opuestas de **136°**. Esta geometría particular asegura que la huella resultante sea geométricamente similar, independientemente del tamaño de la huella, lo que permite que la dureza Vickers sea independiente de la carga aplicada (dentro de ciertos límites).

El principio del ensayo Vickers implica aplicar una carga controlada sobre el penetrador de diamante, que se presiona contra la superficie del material durante un tiempo determinado. Una vez retirada la carga, la huella resultante es una pirámide invertida. Se miden las longitudes de las dos diagonales de la base de esta huella (que idealmente deberían ser iguales). La dureza Vickers se calcula dividiendo la carga aplicada por el área de la superficie de la huella.

## 🔧 Características del Penetrador:

El penetrador Vickers es una pieza clave en este ensayo, y sus características son fundamentales para la precisión y universalidad del método:

-   **Material**: Diamante. El diamante es el material más duro conocido, lo que le permite mantener su forma y no deformarse incluso cuando se ensayan los materiales más duros. Esto asegura que la deformación medida sea únicamente la del material a ensayar.

-   **Forma**: Pirámide cuadrangular. Esta forma geométrica produce una huella bien definida y permite una medición precisa de sus diagonales.

-   **Ángulo entre caras**: 136°. Este ángulo fue elegido específicamente para que los valores de dureza Vickers fueran lo más cercanos posible a los valores de dureza Brinell para un rango similar de materiales, facilitando la correlación entre ambos métodos.

-   **Ángulo del vértice**: Aunque el ángulo entre caras es de 136°, el ángulo entre el eje del penetrador y una de sus caras es de 22° (la mitad de 136° en una proyección). Esto es relevante para el cálculo del área de la huella.

## 🧮 Fórmulas de Cálculo:

La dureza Vickers (HV) se calcula utilizando la siguiente fórmula:

**Dureza Vickers:**

```
HV = 1.854 × F / d²
```

Donde:

-   **F** = Carga aplicada (N). Es crucial que la carga esté en Newtons para obtener resultados en unidades de dureza Vickers (que son equivalentes a MPa, aunque no se expresen así directamente).
-   **d** = Diagonal promedio de la huella (mm). Dado que la huella es una pirámide cuadrangular, se miden las dos diagonales (d1 y d2) y se promedian: `d = (d1 + d2) / 2`. La constante 1.854 se deriva de la geometría del penetrador y la conversión de unidades.

**Área de la huella:**

El área de la superficie de la huella (A) se puede derivar de la geometría del penetrador y la diagonal de la huella. La fórmula para el área de la superficie de la pirámide invertida es:

```
A = d² / (2 × sin(68°)) = 0.5393 × d²
```

Donde 68° es la mitad del ángulo entre caras (136°/2). La constante 0.5393 es el factor geométrico que relaciona el área de la huella con el cuadrado de la diagonal.

## 📊 Rangos de Carga:

Una de las grandes ventajas del ensayo Vickers es su versatilidad en cuanto a los rangos de carga, lo que permite su aplicación en diversas situaciones, desde materiales masivos hasta películas delgadas:

| Tipo de Ensayo | Carga (N) | Aplicación |
|---|---|---|
| **Macrodureza** | 49-980 | Se utiliza para medir la dureza de materiales masivos o de gran volumen, donde la huella resultante es lo suficientemente grande como para ser representativa del material en su conjunto. Las cargas típicas varían de 5 kgf (49 N) a 100 kgf (980 N). |
| **Microdureza** | 0.098-1.96 | También conocido como micro-Vickers, este rango de carga se emplea para medir la dureza de capas superficiales, recubrimientos, constituyentes microestructurales individuales (como granos o fases), o pequeñas piezas. Las cargas suelen estar entre 10 gf (0.098 N) y 200 gf (1.96 N). |
| **Nanodureza** | < 0.098 | Para cargas extremadamente bajas, por debajo de 10 gf (0.098 N), el ensayo se denomina nanodureza. Se utiliza para caracterizar la dureza de películas ultradelgadas, recubrimientos a escala nanométrica o para investigar propiedades mecánicas a nivel atómico. Requiere equipos altamente sofisticados y un control ambiental muy preciso. |

## 📈 Ejemplo de Cálculo:

Consideremos un ejemplo práctico para el cálculo de la dureza Vickers:

**Datos:**

-   Carga F = 294.2 N (equivalente a 30 kgf)
-   Diagonal d₁ = 0.52 mm
-   Diagonal d₂ = 0.48 mm

**Solución:**

Primero, calculamos la diagonal promedio de la huella:

```
d_promedio = (0.52 + 0.48) / 2 = 0.50 mm
```

Ahora, aplicamos la fórmula de la dureza Vickers:

```
HV = 1.854 × F / d²
HV = 1.854 × 294.2 / (0.50)²
HV = 545.5 / 0.25
HV = 2,182
```

El resultado es **2,182 HV30**, donde 


HV30 indica una dureza Vickers obtenida con una carga de 30 kgf.

## ✅ Ventajas:

El ensayo Vickers ofrece varias ventajas significativas que lo hacen un método preferido en muchas aplicaciones:

-   **Aplicable a todos los materiales**: Gracias a su penetrador de diamante y la geometría de la huella, el Vickers puede medir la dureza de una gama extremadamente amplia de materiales, desde los más blandos hasta los más duros, incluyendo metales, cerámicas, vidrios y polímeros.

-   **Amplio rango de durezas**: Puede medir durezas desde valores muy bajos (para materiales blandos) hasta valores extremadamente altos (para materiales superduros), sin necesidad de cambiar el penetrador.

-   **Huella pequeña**: La huella Vickers es relativamente pequeña, lo que permite realizar ensayos en áreas muy localizadas, como capas superficiales delgadas, recubrimientos, o incluso en granos individuales de una microestructura. Esto también minimiza el daño a la pieza ensayada.

-   **Alta precisión**: La geometría del penetrador y la forma de la huella permiten mediciones muy precisas de las diagonales, lo que se traduce en una alta precisión en el valor de dureza resultante.

-   **Independencia de la carga**: Debido a la similitud geométrica de las huellas a diferentes cargas, el número de dureza Vickers es teóricamente independiente de la carga aplicada (dentro de un rango razonable), lo que facilita la comparación de resultados obtenidos con diferentes cargas.

-   **Versatilidad**: La capacidad de utilizar diferentes rangos de carga (macro, micro, nano) lo convierte en una herramienta muy versátil para la investigación y el control de calidad en diversas escalas.

Estas ventajas hacen del ensayo Vickers una herramienta indispensable en la caracterización de materiales en la investigación, el desarrollo y la industria.


