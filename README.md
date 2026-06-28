# Introducción al Cálculo (DCEX 0008) - Universidad San Sebastián
### **Semestre 2026-1**

---

## 📄 Descripción y Objetivos del Curso

La asignatura **Introducción al Cálculo (DCEX 0008)** es un curso fundamental del área de ciencias básicas de la **Universidad San Sebastián**. Su objetivo primordial es desarrollar en los estudiantes la rigurosidad analítica, el pensamiento lógico-matemático y la capacidad de abstracción necesarios para modelar y resolver problemas complejos mediante herramientas de álgebra formal y geometría analítica. 

El curso proporciona la fundamentación teórica para el posterior estudio del cálculo infinitesimal. Su enfoque se centra en la comprensión estructural y axiomática de los números reales, el análisis detallado del comportamiento y propiedades de las funciones reales de variable real, el estudio analítico de las secciones cónicas como lugares geométricos en el plano cartesiano, y la formulación rigurosa de límites.

---

## 📁 Estructura del Repositorio

El repositorio se encuentra estructurado de manera sistemática para organizar y documentar el avance del curso:

*   **[`Teoria/`](./Teoria/)**: Materiales dedicados a la fundamentación y cátedra teórica del curso:
    *   **Diapositivas oficiales**: Presentaciones en PDF que abarcan desde la **Clase 1** hasta la **Clase 18**, cubriendo la totalidad del programa dictado.
    *   **[`Apuntes/`](./Teoria/Apuntes/)**: Compilación de apuntes formales del curso en PDF.
    *   **[`Apuntes_Markdown/`](./Teoria/Apuntes_Markdown/)**: Notas de estudio dinámicas en formato Markdown (`.md`) que exponen y detallan de forma limpia los cuatro grandes tópicos del curso: *Números Reales*, *Funciones*, *Cónicas* y *Límites*.
*   **[`Guias_y_Talleres/`](./Guias_y_Talleres/)**: Ejercitación práctica y complementos matemáticos computacionales:
    *   **[`Talleres_y_Guias/`](./Guias_y_Talleres/Talleres_y_Guias/)**: Listados oficiales de problemas (Listado 1 al 9) y guías integrales de preparación en formato `.pdf` y `.tex`.
    *   **[`Respuestas_Gemini/`](./Guias_y_Talleres/Respuestas_Gemini/)**: Resoluciones matemáticas exhaustivas paso a paso desarrolladas con soporte de la inteligencia artificial Gemini, enfocadas en demostrar la formalidad y el rigor algebraico.
    *   **[`Scripts/`](./Guias_y_Talleres/Scripts/)**: Código fuente en Python y cuadernos interactivos de Jupyter para visualización de propiedades matemáticas:
        *   `Geometria_Analitica/`: Scripts para el trazado interactivo y análisis de cónicas (`Circunferencia.py`, `Elipse.py`, `Parábola.py`, `Hipérbola.py` y `Cónicas.ipynb`).
        *   `Numeros_Reales/`: Implementaciones para el método de puntos críticos y graficación de intervalos en la recta real.
        *   `Funciones/`: Visualización y análisis del comportamiento de funciones complejas y trigonométricas.
*   **[`Evaluaciones/`](./Evaluaciones/)**: Historial evaluativo del curso:
    *   **[`Controles/`](./Evaluaciones/Controles/)**: Evaluaciones sistemáticas parciales (Controles 1 y 2) y sus pautas formales de resolución.
    *   **[`Solemnes/`](./Evaluaciones/Solemnes/)**: Certámenes solemnes (Solemne 1 y 2 en sus distintas formas) junto con presolemnes preparatorias.
* **[Evaluaciones/Solemnes/Solemne_2/](./Evaluaciones/Solemnes/Solemne_2/)**: Documentación, código y entregables del trabajo colaborativo de la Solemne 2 (Grupo 3).
    *   **[`Presentación/`](./Evaluaciones/Solemnes/Solemne_2/Presentación/)**: Archivos fuentes en LaTeX (`.tex`), diapositivas finales en PDF, simulaciones geométricas de GeoGebra (`.ggb`) e ilustraciones de soporte correspondientes a la defensa del Trabajo Colaborativo (Solemne 2) del **Grupo 3**.

---

## 📐 Temarios y Fundamentos Algebraicos

### 1. Secciones Cónicas
En el marco de la geometría analítica bidimensional, las secciones cónicas se definen rigurosamente como **lugares geométricos** en el plano cartesiano $\mathbb{R}^2$. Sus ecuaciones derivan de la ecuación cuadrática general de segundo grado con dos variables:
$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$

*   **Circunferencia**: Lugar geométrico de todos los puntos $P(x,y)$ en el plano tales que su distancia a un punto fijo $C(h,k)$ (llamado centro) es una constante positiva $r$ (llamada radio):
    $$(x-h)^2 + (y-k)^2 = r^2$$
*   **Elipse**: Lugar geométrico de todos los puntos $P(x,y)$ tales que la suma de sus distancias a dos puntos fijos $F_1$ y $F_2$ (llamados focos) es constante e igual a $2a$, donde $2a > d(F_1, F_2)$:
    $$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1 \quad (\text{para eje focal horizontal, con } a^2 = b^2 + c^2)$$
*   **Parábola**: Lugar geométrico de todos los puntos $P(x,y)$ que equidistan de un punto fijo $F$ (llamado foco) y de una recta fija $D$ (llamada directriz) que no contiene al foco:
    $$(x-h)^2 = 4p(y-k) \quad (\text{eje focal vertical}) \quad \text{o} \quad (y-k)^2 = 4p(x-h) \quad (\text{eje focal horizontal})$$
*   **Hipérbola**: Lugar geométrico de todos los puntos $P(x,y)$ para los cuales el valor absoluto de la diferencia de sus distancias a dos puntos fijos $F_1$ y $F_2$ (llamados focos) es constante e igual a $2a$:
    $$\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1 \quad (\text{para eje focal horizontal, con } c^2 = a^2 + b^2)$$

### 2. Funciones de Variable Real
Estudio formal de las relaciones de correspondencia de variable real $f: A \subseteq \mathbb{R} \to B \subseteq \mathbb{R}$, centrado en su análisis algebraico estricto (excluyendo conceptos de cálculo infinitesimal como derivadas o integrales):
*   **Dominio y Recorrido**:
    *   *Dominio*: $\text{Dom}(f) = \{x \in \mathbb{R} : \exists y \in \mathbb{R} \text{ tal que } y = f(x)\}$
    *   *Recorrido*: $\text{Rec}(f) = \{y \in \mathbb{R} : \exists x \in \text{Dom}(f) \text{ tal que } f(x) = y\}$
*   **Clasificación de Funciones**: Definición formal y condiciones algebraicas para inyectividad, sobreyectividad y biyectividad. Análisis de funciones elementales: lineales, cuadráticas, polinomiales, racionales, exponenciales, logarítmicas y trigonométricas.
*   **Comportamiento Estructural**: 
    *   *Simetría*: Funciones pares ($f(-x) = f(x)$) e impares ($f(-x) = -f(x)$).
    *   *Monotonía*: Crecimiento y decrecimiento determinados algebraicamente mediante la relación para todo $x_1, x_2 \in \text{Dom}(f)$.
    *   *Operaciones*: Álgebra de funciones, composición $(f \circ g)(x) = f(g(x))$ y obtención algebraica de la función inversa $f^{-1}(x)$ mediante el despeje de la variable independiente.

### 3. Límites de una Función
Formulación del comportamiento de una función en la cercanía de un punto de acumulación:
*   **Definición Formal Epsilon-Delta ($\epsilon$-$\delta$)**: Se denota que el límite de $f(x)$ cuando $x$ tiende a $c$ es $L$, escrito como $\lim_{x \to c} f(x) = L$, si y solo si:
    $$\forall \epsilon > 0, \exists \delta > 0 \text{ tal que } 0 < |x - c| < \delta \implies |f(x) - L| < \epsilon$$
*   **Resolución Algebraica de Límites**: Técnicas analíticas para resolver formas indeterminadas como $\left[\frac{0}{0}\right]$ sin el uso de herramientas derivadas (como la regla de L'Hôpital):
    1.  *Factorización*: Simplificación de polinomios racionales mediante factorización de factores comunes y binomios notables.
    2.  *Racionalización*: Eliminación de indeterminaciones con radicales aplicando multiplicación por factores conjugados algebraicos.
    3.  *Cambio de variable*: Transformación algebraica para unificar expresiones trigonométricas o irracionales complejas.

### 4. Álgebra Formal Aplicada
Modelado y representación matemática de sistemas a través de la geometría analítica y el álgebra elemental:
*   Planteamiento de sistemas de ecuaciones polinómicas y no lineales para determinar puntos de intersección entre curvas (ej. intersección recta-cónica o cónica-cónica).
*   Formulación algebraica de restricciones físicas en coordenadas bidimensionales.
*   Optimización algebraica de funciones cuadráticas (cálculo analítico del vértice de la parábola $V_x = -b/(2a)$ para maximizar/minimizar áreas o volúmenes sin herramientas de cálculo diferencial).

---

## 🚢 Resumen del Trabajo Colaborativo (Solemne 2) (Grupo 3)

### **Título:** *Modelamiento Geométrico de Cónicas Aplicado a Navegación Naval y Sistemas Aeroespaciales*

*   **Integrantes del Grupo 3:**
    *   Moisés Amundarain
    *   Camila Aravena
    *   Daniela García
    *   Fernando Ramírez
    *   María José Santander
    *   Juan Pablo Vargas

El Trabajo Colaborativo (Solemne 2) del grupo explora la aplicación matemática práctica de las cónicas como herramienta fundamental de diseño y simulación en sistemas tecnológicos y de ingeniería en tres casos centrales:

1.  **Navegación de Sonar Submarino (Hipérbolas)**: Modelamiento matemático de la localización por diferencia en los tiempos de llegada de señales (TDOA) a múltiples sensores hidrofónicos fijos. La diferencia constante en las distancias a dos focos define ramas de hipérbolas. El punto de intersección de estas curvas hiperbólicas proporciona las coordenadas exactas de la fuente emisora (submarino o señal acústica).
2.  **Telecomunicaciones Satelitales (Parábolas)**: Estudio y parametrización geométrica de las superficies reflectoras de antenas parabólicas. Utilizando la definición focal de la parábola, se demuestra cómo las señales paralelas que inciden en el plato reflector son dirigidas precisamente hacia el receptor colocado en el foco, optimizando la potencia de recepción de señales débiles provenientes del espacio exterior.
3.  **Movimiento de Brazo Robótico (Circunferencias y Elipses)**: Delimitación analítica del área de trabajo útil de un manipulador robótico articulado. Mediante ecuaciones de circunferencias se restringe la trayectoria circular individual de cada eslabón, mientras que la combinación del movimiento articular genera envolventes elípticas tridimensionales que definen el límite de alcance seguro y prevención de colisiones.

---

## ⚙️ Configuración y Uso Local

Para realizar simulaciones o visualizar de forma interactiva las curvas y funciones analizadas en el curso:

### 1. Clonar el repositorio:
```bash
git clone git@github.com:moises-inc/Intro.Calculo-USS.git
cd "Intro.Calculo-USS"
```

### 2. Configurar el entorno de Python:
Asegúrese de tener Python 3.8+ instalado. Se recomienda el uso de un entorno virtual para instalar las dependencias necesarias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows use: venv\Scripts\activate
pip install numpy matplotlib jupyter
```

### 3. Ejecución de simulaciones:
Para iniciar cualquiera de los scripts matemáticos:
```bash
python "Guias_y_Talleres/Scripts/Geometria_Analitica/Elipse.py"
```
Para explorar los cuadernos interactivos de Jupyter:
```bash
jupyter notebook "Guias_y_Talleres/Scripts/Geometria_Analitica/Cónicas.ipynb"
```

## ⚖️ Licencia
Este repositorio se encuentra distribuido bajo la [Licencia MIT](./LICENSE).