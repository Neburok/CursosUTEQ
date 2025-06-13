# Módulo 6: Ensayo Rockwell (HR)

## 📏 Descripción del Método

El ensayo Rockwell es, con diferencia, el método de ensayo de dureza más utilizado en la industria debido a su rapidez, simplicidad y la capacidad de obtener una lectura directa del valor de dureza sin necesidad de mediciones ópticas posteriores. Fue desarrollado por Stanley P. Rockwell en 1914 y patentado en 1919. A diferencia de los ensayos Brinell y Vickers, que miden el tamaño de la huella (diámetro o diagonales), el ensayo Rockwell mide la **profundidad de penetración** de un penetrador bajo una carga específica. Esta diferencia fundamental es la clave de su velocidad y facilidad de uso.

El principio del ensayo Rockwell implica la aplicación de dos cargas sucesivas al penetrador. Primero, se aplica una carga menor, conocida como **precarga** o carga preliminar (F₀), para asentar el penetrador en la superficie del material y eliminar cualquier efecto de irregularidades superficiales o pequeñas partículas de suciedad. Con la precarga aún aplicada, se añade una carga mayor, conocida como **carga principal** (F₁), que se mantiene durante un tiempo específico. Finalmente, se retira la carga principal, pero se mantiene la precarga. La diferencia en la profundidad de penetración entre la aplicación de la precarga y la aplicación de la carga principal (después de la recuperación elástica al retirar la carga principal) se utiliza para calcular el número de dureza Rockwell. Esta profundidad diferencial se mide automáticamente por el durómetro y se convierte en un número de dureza que se muestra directamente en un dial o pantalla digital.

## 🔧 Tipos de Penetradores:

El ensayo Rockwell utiliza dos tipos principales de penetradores, dependiendo de la escala de dureza que se esté utilizando y del material a ensayar:

-   **Cono de diamante**: Se utiliza para materiales más duros, como aceros templados, carburos cementados y otros materiales de alta dureza. Este penetrador tiene una forma cónica con un ángulo de **120°** y una punta esférica con un radio de **0.2 mm**. Se le conoce comúnmente como penetrador "Brale".

-   **Esfera de acero endurecido**: Se utiliza para materiales más blandos, como aceros recocidos, latones, bronces y aleaciones de aluminio. Estas esferas están disponibles en varios diámetros estándar: **1/16 pulgada (1.588 mm)**, **1/8 pulgada (3.175 mm)**, **1/4 pulgada (6.350 mm)** y **1/2 pulgada (12.70 mm)**. La elección del diámetro de la esfera depende de la dureza del material; esferas más grandes se usan para materiales más blandos.

## 📊 Escalas Principales:

El ensayo Rockwell comprende una variedad de escalas, cada una designada por una letra (por ejemplo, A, B, C, etc.) que indica una combinación específica de penetrador y carga principal. La elección de la escala adecuada es crucial para obtener resultados precisos y significativos. Las escalas más comunes son:

| Escala | Penetrador | Carga Total (N) | Aplicación |
|---|---|---|---|
| **HRA** (Rockwell A) | Cono de diamante | 588.4 (60 kgf) | Se utiliza para materiales extremadamente duros como carburos cementados, aceros nitrurados delgados y otros materiales donde se requiere una huella poco profunda. |
| **HRB** (Rockwell B) | Esfera de acero de 1/16" | 980.7 (100 kgf) | Adecuada para materiales de dureza media a baja, como aceros recocidos, aleaciones de cobre (latones, bronces) y aleaciones de aluminio. |
| **HRC** (Rockwell C) | Cono de diamante | 1,471 (150 kgf) | Es una de las escalas más utilizadas y es ideal para aceros templados y revenidos, aceros para herramientas y otros materiales de alta dureza. |

Además de estas, existen muchas otras escalas Rockwell (HRD, HRE, HRF, HRG, HRH, HRK, HRL, HRM, HRP, HRR, HRS, HRV) que utilizan diferentes combinaciones de penetradores y cargas para cubrir un espectro aún más amplio de materiales y durezas. También existen las escalas Rockwell Superficial (por ejemplo, HR15N, HR30N, HR45N, HR15T, HR30T, HR45T) que utilizan cargas mucho menores y son adecuadas para medir la dureza de capas superficiales delgadas o materiales muy delgados sin penetrar el material base.

## 🧮 Fórmulas de Cálculo:

La dureza Rockwell no se calcula directamente a partir de una fórmula que involucre el área de la huella, como en Brinell o Vickers. En su lugar, se define en términos de la profundidad de penetración permanente. La máquina de ensayo Rockwell está calibrada para convertir esta profundidad en un número de dureza. Las fórmulas básicas son:

**Para escalas que utilizan el cono de diamante (como HRA, HRC, HRD):**

```
HR = 100 - 500h
```

**Para escalas que utilizan penetradores de esfera (como HRB, HRE, HRF, HRG, HRH, HRK):**

```
HR = 130 - 500h
```

Donde:

-   **HR** = Número de dureza Rockwell.
-   **h** = Profundidad de penetración permanente (mm) medida desde la posición de la precarga después de retirar la carga principal. Cada unidad de dureza Rockwell corresponde a una profundidad de penetración de 0.002 mm (para las escalas estándar) o 0.001 mm (para las escalas superficiales).

Es importante notar que estos números (100 y 130) son constantes arbitrarias elegidas para que los materiales más duros tengan números de dureza más altos. Un valor de 'h' mayor (mayor profundidad de penetración) resulta en un número de dureza Rockwell menor, lo que es consistente con la idea de que un material más blando permite una mayor penetración.

## 📋 Procedimiento:

El procedimiento para realizar un ensayo Rockwell es relativamente sencillo y rápido:

1.  **Preparación de la muestra**: La superficie de la muestra debe estar limpia, lisa y libre de óxido, cascarilla o cualquier contaminante. Aunque el ensayo Rockwell es menos sensible a las imperfecciones superficiales que Brinell o Vickers, una buena preparación mejora la precisión. La muestra debe colocarse firmemente sobre el yunque del durómetro para evitar cualquier movimiento durante el ensayo.

2.  **Selección de escala y penetrador**: Se elige la escala Rockwell apropiada en función del material y su dureza esperada, lo que determina el tipo de penetrador y la carga principal a utilizar.

3.  **Aplicación de la precarga (F₀)**: El penetrador se pone en contacto con la superficie de la muestra y se aplica la precarga (generalmente 98.07 N o 10 kgf para las escalas estándar; 29.42 N o 3 kgf para las escalas superficiales). Esta carga se mantiene durante un corto período (típicamente 2-8 segundos) para asegurar un asentamiento adecuado del penetrador y establecer un punto de referencia cero para la medición de la profundidad.

4.  **Aplicación de la carga principal (F₁)**: Se aplica la carga principal adicional, sumándose a la precarga para alcanzar la carga total (F = F₀ + F₁). Esta carga total se mantiene durante un tiempo específico (generalmente 2-8 segundos) para permitir que ocurra la deformación plástica.

5.  **Retirada de la carga principal**: Se retira la carga principal (F₁), dejando aplicada únicamente la precarga (F₀). Esta acción permite que el material experimente una recuperación elástica parcial.

6.  **Lectura de la dureza**: La diferencia en la profundidad de penetración entre la posición inicial bajo la precarga y la posición final después de retirar la carga principal (con la precarga aún aplicada) se mide automáticamente por el durómetro. Este valor de profundidad se convierte internamente en un número de dureza Rockwell, que se muestra directamente en el indicador del equipo.

## 📈 Ejemplo de Cálculo (Conceptual):

Dado que la dureza Rockwell se lee directamente del equipo, un cálculo manual no es típicamente necesario en la práctica. Sin embargo, para entender el concepto:

**Datos:**

-   Se utiliza la escala HRC (cono de diamante).
-   La profundidad de penetración permanente medida (h) después de retirar la carga principal es de 0.080 mm.

**Solución:**

Usando la fórmula para escalas con cono de diamante:

```
HRC = 100 - 500h
HRC = 100 - (500 × 0.080)
HRC = 100 - 40
HRC = 60
```

Por lo tanto, la dureza del material es **60 HRC**.

## 🚀 Ventajas:

El ensayo Rockwell es extremadamente popular debido a sus numerosas ventajas:

-   **Lectura directa**: El valor de dureza se lee directamente en el dial o pantalla del durómetro, eliminando la necesidad de mediciones ópticas y cálculos posteriores, lo que ahorra tiempo y reduce la posibilidad de error humano.

-   **Ensayo rápido**: El ciclo completo del ensayo es muy corto, generalmente toma solo unos segundos. Esto lo hace ideal para pruebas de producción en masa y control de calidad de alta velocidad.

-   **No requiere preparación especial de superficie (en muchos casos)**: Aunque una buena superficie mejora la precisión, el ensayo Rockwell es menos sensible a las condiciones superficiales que Brinell o Vickers, especialmente debido a la aplicación de la precarga que minimiza los efectos de las irregularidades superficiales leves.

-   **Huella pequeña y poco profunda**: La huella dejada por el ensayo Rockwell es generalmente pequeña y menos destructiva que la del ensayo Brinell, lo que permite ensayar piezas acabadas o componentes donde una marca grande sería inaceptable.

-   **Amplia gama de escalas**: La disponibilidad de múltiples escalas con diferentes penetradores y cargas permite ensayar una gran variedad de materiales, desde los muy blandos hasta los muy duros.

-   **Facilidad de uso**: Las máquinas de ensayo Rockwell son relativamente fáciles de operar, requiriendo menos habilidad por parte del operador en comparación con los métodos que implican mediciones ópticas.

Estas ventajas han consolidado al ensayo Rockwell como un estándar en la industria para la determinación rápida y fiable de la dureza de los materiales.


