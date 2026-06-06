---
id: "20260606-listado8-introduccion-calculo-resolucion"
title: "Resolución Listado 8 - Introducción al Cálculo"
project: "Estudios_Universidad"
date: "2026-06-06T14:30:10"
last_modified: "2026-06-06T14:31:18"
type: "academic-note"
status: "completed"
priority: "medium"
tags: ["#status/completed", "#project/Estudios_Universidad", "#course/introduccion_calculo"]
---

# Guía Pedagógica Definitiva: Colección de Ejercicios N° 8
**Materia:** Introducción al Cálculo (Cónicas: Elipse, Hipérbola y Parábola)  
**Docente:** Soledad Merino Ñanco  
**Resolución:** Gemini Academic Assistant  

---

## Introducción Conceptual

Esta guía contiene la resolución exhaustiva y formal de los ejercicios propuestos en el **Listado 8**. Siguiendo la **Directiva Crítica**, el desarrollo se fundamenta exclusivamente en métodos de **álgebra elemental y analítica** (completación de cuadrados, fórmulas de distancia, relaciones fundamentales de cónicas y geometría analítica en el plano cartesiano), evitando por completo el uso de límites, derivadas o integrales.

### Resumen de Fórmulas y Definiciones Clave

1. **Elipse:**
   * **Ecuación canónica (eje mayor horizontal):**
     $$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1, \quad a > b > 0$$
   * **Ecuación canónica (eje mayor vertical):**
     $$\frac{(x-h)^2}{b^2} + \frac{(y-k)^2}{a^2} = 1, \quad a > b > 0$$
   * **Relación fundamental:** $a^2 = b^2 + c^2$, donde $c$ es la distancia focal.
   * **Excentricidad:** $e = \frac{c}{a} < 1$.
   * **Lado recto:** $LR = \frac{2b^2}{a}$.

2. **Hipérbola:**
   * **Ecuación canónica (transversal horizontal):**
     $$\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1, \quad a, b > 0$$
   * **Ecuación canónica (transversal vertical):**
     $$\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1, \quad a, b > 0$$
   * **Relación fundamental:** $c^2 = a^2 + b^2$.
   * **Asíntotas:**
     * Transversal horizontal: $y - k = \pm \frac{b}{a}(x - h)$
     * Transversal vertical: $y - k = \pm \frac{a}{b}(x - h)$

3. **Parábola:**
   * **Ecuación canónica (eje focal vertical):**
     $$(x-h)^2 = 4p(y-k)$$
   * **Ecuación canónica (eje focal horizontal):**
     $$(y-k)^2 = 4p(x-h)$$
   * **Foco:** $F(h, k+p)$ (vertical) o $F(h+p, k)$ (horizontal).
   * **Directriz:** $y = k-p$ (vertical) o $x = h-p$ (horizontal).

---

## Resolución de Ejercicios

### Pregunta 1: Escriba en cada caso la ecuación canónica

> **Justificación Académica:** Para obtener la ecuación canónica de una cónica dada en su forma general, debemos agrupar los términos de las mismas variables, factorizar los coeficientes principales y realizar completación de cuadrados perfectos: $u^2 + \beta u = \left(u + \frac{\beta}{2}\right)^2 - \frac{\beta^2}{4}$.

#### Desarrollo:

**a) $\frac{x^2}{16} + \frac{x}{2} + \frac{y^2}{4} + y + 1 = 0$**

1. Agrupamos los términos asociándolos a sus respectivas variables:
   $$\frac{1}{16}(x^2 + 8x) + \frac{1}{4}(y^2 + 4y) + 1 = 0$$
2. Completamos cuadrados para cada término cuadrático:
   * $x^2 + 8x = (x + 4)^2 - 16$
   * $y^2 + 4y = (y + 2)^2 - 4$
3. Sustituimos en la ecuación original:
   $$\frac{1}{16}\left[(x + 4)^2 - 16\right] + \frac{1}{4}\left[(y + 2)^2 - 4\right] + 1 = 0$$
4. Distribuimos los coeficientes fraccionarios:
   $$\frac{(x + 4)^2}{16} - 1 + \frac{(y + 2)^2}{4} - 1 + 1 = 0$$
   $$\frac{(x + 4)^2}{16} + \frac{(y + 2)^2}{4} - 1 = 0 \implies \frac{(x + 4)^2}{16} + \frac{(y + 2)^2}{4} = 1$$

* **Cónica identificada:** Elipse horizontal con centro en $C(-4,-2)$, semi-eje horizontal $a=4$ y semi-eje vertical $b=2$.

---

**b) $\frac{x^2}{4} + x + \frac{y^2}{16} + \frac{y}{2} + 1 = 0$**

1. Agrupamos términos:
   $$\frac{1}{4}(x^2 + 4x) + \frac{1}{16}(y^2 + 8y) + 1 = 0$$
2. Completamos cuadrados:
   * $x^2 + 4x = (x + 2)^2 - 4$
   * $y^2 + 8y = (y + 4)^2 - 16$
3. Sustituimos y simplificamos:
   $$\frac{1}{4}\left[(x + 2)^2 - 4\right] + \frac{1}{16}\left[(y + 4)^2 - 16\right] + 1 = 0$$
   $$\frac{(x + 2)^2}{4} - 1 + \frac{(y + 4)^2}{16} - 1 + 1 = 0$$
   $$\frac{(x + 2)^2}{4} + \frac{(y + 4)^2}{16} = 1$$

* **Cónica identificada:** Elipse vertical con centro en $C(-2,-4)$, semi-eje horizontal $b=2$ y semi-eje vertical $a=4$.

---

**c) $x^2 + \frac{y^2}{2} - 2y + 1 = 0$**

1. Agrupamos los términos para la variable $y$:
   $$x^2 + \frac{1}{2}(y^2 - 4y) + 1 = 0$$
2. Completamos el cuadrado en $y$:
   * $y^2 - 4y = (y - 2)^2 - 4$
3. Sustituimos en la ecuación:
   $$x^2 + \frac{1}{2}\left[(y - 2)^2 - 4\right] + 1 = 0$$
   $$x^2 + \frac{(y - 2)^2}{2} - 2 + 1 = 0$$
   $$x^2 + \frac{(y - 2)^2}{2} = 1$$

* **Cónica identificada:** Elipse vertical con centro en $C(0,2)$, semi-eje horizontal $b=1$ y semi-eje vertical $a=\sqrt{2}$.

---

**d) $9y^2 + 16x^2 + 54y - 64x + 1 = 0$**

1. Ordenamos y agrupamos:
   $$16(x^2 - 4x) + 9(y^2 + 6y) + 1 = 0$$
2. Completamos cuadrados:
   * $x^2 - 4x = (x - 2)^2 - 4$
   * $y^2 + 6y = (y + 3)^2 - 9$
3. Reemplazamos:
   $$16\left[(x - 2)^2 - 4\right] + 9\left[(y + 3)^2 - 9\right] + 1 = 0$$
   $$16(x - 2)^2 - 64 + 9(y + 3)^2 - 81 + 1 = 0$$
   $$16(x - 2)^2 + 9(y + 3)^2 - 144 = 0$$
   $$16(x - 2)^2 + 9(y + 3)^2 = 144$$
4. Dividimos toda la expresión entre $144$:
   $$\frac{(x - 2)^2}{9} + \frac{(y + 3)^2}{16} = 1$$

* **Cónica identificada:** Elipse vertical con centro en $C(2,-3)$, semi-eje horizontal $b=3$ y semi-eje vertical $a=4$.

---

### Pregunta 2: Determine la ecuación canónica y las características de la elipse cuyo eje mayor tiene extremos $(-3,5)$ y $(7,5)$ y cuyo eje menor tiene extremos en $(2,2)$ y $(2,8)$

> **Justificación Académica:** Los extremos del eje mayor definen la orientación (horizontal si la ordenada es común) y su longitud es igual a $2a$. Los extremos del eje menor definen la longitud vertical igual a $2b$. El centro es el punto medio de ambos ejes.

#### Desarrollo:

1. **Orientación de la elipse:** Los extremos del eje mayor son $V_1(-3,5)$ y $V_2(7,5)$. Dado que la coordenada $y = 5$ permanece constante, el eje mayor es horizontal.
2. **Determinación del centro $C(h,k)$:** El centro es el punto medio del segmento $V_1V_2$:
   $$h = \frac{-3 + 7}{2} = 2, \quad k = 5 \implies C(2,5)$$
3. **Cálculo de los semi-ejes ($a$ y $b$):**
   * El eje mayor mide $2a = 7 - (-3) = 10 \implies a = 5 \implies a^2 = 25$.
   * El eje menor tiene extremos $B_1(2,2)$ y $B_2(2,8)$. Su longitud es $2b = 8 - 2 = 6 \implies b = 3 \implies b^2 = 9$.
4. **Distancia focal ($c$):**
   $$c^2 = a^2 - b^2 = 25 - 9 = 16 \implies c = 4$$
5. **Ecuación canónica:**
   $$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1 \implies \frac{(x-2)^2}{25} + \frac{(y-5)^2}{9} = 1$$

#### Características más importantes:
* **Centro:** $C(2,5)$
* **Vértices principales:** $V_1(-3,5)$ y $V_2(7,5)$
* **Vértices secundarios:** $B_1(2,2)$ y $B_2(2,8)$
* **Focos:** $F_1(2-4, 5) = (-2,5)$ y $F_2(2+4, 5) = (6,5)$
* **Excentricidad:** $e = \frac{c}{a} = \frac{4}{5} = 0.8$
* **Lado recto:** $LR = \frac{2b^2}{a} = \frac{2(9)}{5} = 3.6$

$$\frac{(x-2)^2}{25} + \frac{(y-5)^2}{9} = 1$$

---

### Pregunta 3: Determine la ecuación canónica y las características de la elipse con vértices en $(3,1)$ y $(3,9)$, eje menor de longitud igual a 6

> **Justificación Académica:** Los vértices principales están alineados verticalmente ($x=3$), lo que indica que la elipse es de orientación vertical. La distancia entre ellos es $2a$, y la longitud del eje menor se define directamente como $2b = 6$.

#### Desarrollo:

1. **Orientación de la elipse:** Los vértices principales son $V_1(3,1)$ y $V_2(3,9)$. Como la coordenada $x = 3$ es constante, el eje mayor es vertical.
2. **Determinación del centro $C(h,k)$:** El centro es el punto medio de $V_1V_2$:
   $$h = 3, \quad k = \frac{1 + 9}{2} = 5 \implies C(3,5)$$
3. **Cálculo de los semi-ejes ($a$ y $b$):**
   * El eje mayor mide $2a = 9 - 1 = 8 \implies a = 4 \implies a^2 = 16$.
   * La longitud del eje menor es $2b = 6 \implies b = 3 \implies b^2 = 9$.
4. **Distancia focal ($c$):**
   $$c^2 = a^2 - b^2 = 16 - 9 = 7 \implies c = \sqrt{7}$$
5. **Ecuación canónica:**
   $$\frac{(x-h)^2}{b^2} + \frac{(y-k)^2}{a^2} = 1 \implies \frac{(x-3)^2}{9} + \frac{(y-5)^2}{16} = 1$$

#### Características más importantes:
* **Centro:** $C(3,5)$
* **Vértices principales:** $V_1(3,1)$ y $V_2(3,9)$
* **Vértices secundarios:** $B_1(3-3, 5) = (0,5)$ y $B_2(3+3, 5) = (6,5)$
* **Focos:** $F_1(3, 5-\sqrt{7})$ y $F_2(3, 5+\sqrt{7})$
* **Excentricidad:** $e = \frac{\sqrt{7}}{4} \approx 0.66$
* **Lado recto:** $LR = \frac{2b^2}{a} = \frac{2(9)}{4} = 4.5$

$$\frac{(x-3)^2}{9} + \frac{(y-5)^2}{16} = 1$$

---

### Pregunta 4: Determine la ecuación canónica de la elipse con focos en $(2,5)$ y $(2,3)$ y que contiene al punto $(3,6)$

> **Justificación Académica:** Por definición geométrica de la elipse, la suma de las distancias desde cualquier punto de la curva a sus focos es constante e igual a la longitud del eje mayor, $2a$. Es decir, $d(P, F_1) + d(P, F_2) = 2a$.

#### Desarrollo:

1. **Identificación de la geometría focal:**
   * Focos: $F_1(2,5)$ y $F_2(2,3)$. El eje focal es vertical porque la abscisa es constante ($x=2$).
   * Centro (punto medio de los focos): $C\left(2, \frac{5+3}{2}\right) = C(2,4)$.
   * Semidistancia focal: $2c = 5 - 3 = 2 \implies c = 1 \implies c^2 = 1$.
2. **Aplicación de la definición geométrica para $P(3,6)$:**
   $$d(P, F_1) = \sqrt{(3 - 2)^2 + (6 - 5)^2} = \sqrt{1^2 + 1^2} = \sqrt{2}$$
   $$d(P, F_2) = \sqrt{(3 - 2)^2 + (6 - 3)^2} = \sqrt{1^2 + 3^2} = \sqrt{10}$$
   $$2a = d(P, F_1) + d(P, F_2) = \sqrt{2} + \sqrt{10}$$
   $$a = \frac{\sqrt{2} + \sqrt{10}}{2}$$
3. **Cálculo de los parámetros cuadráticos $a^2$ y $b^2$:**
   $$a^2 = \left(\frac{\sqrt{2} + \sqrt{10}}{2}\right)^2 = \frac{2 + 2\sqrt{20} + 10}{4} = \frac{12 + 4\sqrt{5}}{4} = 3 + \sqrt{5}$$
   $$b^2 = a^2 - c^2 = (3 + \sqrt{5}) - 1 = 2 + \sqrt{5}$$
4. **Estructura de la ecuación canónica (eje focal vertical):**
   $$\frac{(x-h)^2}{b^2} + \frac{(y-k)^2}{a^2} = 1 \implies \frac{(x-2)^2}{2+\sqrt{5}} + \frac{(y-4)^2}{3+\sqrt{5}} = 1$$

$$\frac{(x-2)^2}{2+\sqrt{5}} + \frac{(y-4)^2}{3+\sqrt{5}} = 1$$

---

### Pregunta 5: Una pista de autos tiene forma elíptica. El eje mayor mide 10 km y el eje menor 6 km. Determine la distancia a que se encuentra un auto del centro de la pista en el momento que pasa a la altura de uno de los focos

> **Justificación Académica:** Modelamos la pista elíptica con su centro en el origen de coordenadas. La altura al pasar por el foco corresponde a la semicuerda vertical de la elipse en la abscisa del foco ($x = c$). La distancia al centro se calcula aplicando el teorema de Pitágoras, $d = \sqrt{c^2 + y^2}$.

#### Desarrollo:

1. **Ecuación matemática de la pista:**
   * Eje mayor $2a = 10 \implies a = 5 \implies a^2 = 25$.
   * Eje menor $2b = 6 \implies b = 3 \implies b^2 = 9$.
   * Colocamos la elipse de manera horizontal:
     $$\frac{x^2}{25} + \frac{y^2}{9} = 1$$
2. **Determinación del foco $F(c, 0)$:**
   $$c^2 = a^2 - b^2 = 25 - 9 = 16 \implies c = 4 \implies F(4,0)$$
3. **Cálculo de la ordenada $y$ del auto cuando pasa por la vertical de $x = c = 4$:**
   $$\frac{4^2}{25} + \frac{y^2}{9} = 1 \implies \frac{16}{25} + \frac{y^2}{9} = 1$$
   $$\frac{y^2}{9} = 1 - \frac{16}{25} = \frac{9}{25}$$
   $$y^2 = \frac{81}{25} \implies y = \pm\frac{9}{5}$$
4. **Cálculo de la distancia al centro $(0,0)$:**
   El auto se encuentra en la posición $P\left(4, \frac{9}{5}\right)$.
   $$d(O, P) = \sqrt{4^2 + \left(\frac{9}{5}\right)^2} = \sqrt{16 + \frac{81}{25}} = \sqrt{\frac{400 + 81}{25}} = \sqrt{\frac{481}{25}} = \frac{\sqrt{481}}{5} \text{ km}$$

$$d = \frac{\sqrt{481}}{5} \text{ km} \quad (\approx 4.386 \text{ km})$$

---

### Pregunta 6: Si los focos de una elipse son los puntos $F_1 = (-4,3)$ y $F_2 = (2,3)$ y el perímetro del triángulo cuyos vértices son los focos y un punto de la elipse, es igual a 16, determine la ecuación de la elipse

> **Justificación Académica:** El perímetro del triángulo con vértices $P$, $F_1$ y $F_2$ es la suma de las distancias $d(P, F_1) + d(P, F_2) + d(F_1, F_2)$. De acuerdo con la definición geométrica de la elipse, $d(P, F_1) + d(P, F_2) = 2a$. Así, el perímetro es $2a + 2c = 16$.

#### Desarrollo:

1. **Determinación de los datos focales:**
   * Focos: $F_1(-4,3)$ y $F_2(2,3)$. El eje focal es horizontal pues $y=3$ es constante.
   * Centro (punto medio de los focos): $C\left(\frac{-4 + 2}{2}, 3\right) = C(-1,3)$.
   * Distancia focal ($2c$):
     $$2c = d(F_1, F_2) = 2 - (-4) = 6 \implies c = 3$$
2. **Uso del perímetro para hallar $a$:**
   $$\text{Perímetro} = (d(P, F_1) + d(P, F_2)) + d(F_1, F_2) = 2a + 2c = 16$$
   $$2a + 6 = 16 \implies 2a = 10 \implies a = 5 \implies a^2 = 25$$
3. **Cálculo de $b^2$:**
   $$b^2 = a^2 - c^2 = 25 - 3^2 = 25 - 9 = 16 \implies b = 4$$
4. **Ecuación canónica de la elipse:**
   $$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1 \implies \frac{(x+1)^2}{25} + \frac{(y-3)^2}{16} = 1$$

$$\frac{(x+1)^2}{25} + \frac{(y-3)^2}{16} = 1$$

---

### Pregunta 7: El arco de un puente semielíptico, con eje mayor horizontal, tiene una base de $30\text{ m}$ y la parte más alta con respecto a la tierra es de $10\text{ m}$. Calcule la altura a $6\text{ metros}$ del centro de la base

> **Justificación Académica:** Ubicando el origen del sistema en el centro de la base del puente, la base semielíptica se extiende a lo largo de los extremos $-15 \le x \le 15$ ($a=15$). La altura máxima corresponde al semi-eje vertical ($b=10$). Planteamos la ecuación canónica y despejamos la ordenada para $x = 6$.

#### Desarrollo:

1. **Ecuación matemática del puente:**
   * Semi-eje horizontal: $a = \frac{30}{2} = 15 \implies a^2 = 225$.
   * Semi-eje vertical: $b = 10 \implies b^2 = 100$.
   * Ecuación:
     $$\frac{x^2}{225} + \frac{y^2}{100} = 1 \quad (\text{para } y \ge 0)$$
2. **Evaluación de la altura a $x = 6$ m del centro:**
   $$\frac{6^2}{225} + \frac{y^2}{100} = 1 \implies \frac{36}{225} + \frac{y^2}{100} = 1$$
   * Simplificamos la fracción: $\frac{36}{225} = \frac{4}{25}$.
   $$\frac{y^2}{100} = 1 - \frac{4}{25} = \frac{21}{25}$$
   $$y^2 = 100 \cdot \frac{21}{25} = 4 \cdot 21 = 84$$
   $$y = \sqrt{84} = 2\sqrt{21} \text{ m}$$

$$\text{Altura} = 2\sqrt{21} \text{ m} \quad (\approx 9.165 \text{ m})$$

---

### Pregunta 8: Identifique y represente las siguientes cónicas con todos sus elementos y puntos de intersección con los ejes coordenados

> **Justificación Académica:** Para cada ecuación realizamos completación de cuadrados para encontrar su forma estándar. Tras identificar el tipo de cónica, calculamos analíticamente sus elementos (centro, vértices, focos, asíntotas si corresponde) e intersecciones con los ejes coordenados haciendo $x=0$ e $y=0$.

#### Desarrollo Paso a Paso:

**a) $4y^2 - 9x^2 + 36x - 24y - 36 = 0$**
1. Agrupamos y completamos cuadrados:
   $$4(y^2 - 6y) - 9(x^2 - 4x) = 36$$
   $$4[(y-3)^2 - 9] - 9[(x-2)^2 - 4] = 36$$
   $$4(y-3)^2 - 36 - 9(x-2)^2 + 36 = 36 \implies 4(y-3)^2 - 9(x-2)^2 = 36$$
   Divide por $36$:
   $$\frac{(y-3)^2}{9} - \frac{(x-2)^2}{4} = 1$$
2. **Cónica:** Hipérbola con eje transversal vertical.
   * **Centro:** $C(2,3)$
   * **Ejes:** $a = 3$, $b = 2$, $c = \sqrt{9 + 4} = \sqrt{13}$
   * **Vértices:** $V_1(2, 0)$ y $V_2(2, 6)$
   * **Focos:** $F_1(2, 3-\sqrt{13})$ y $F_2(2, 3+\sqrt{13})$
   * **Asíntotas:** $y - 3 = \pm \frac{3}{2}(x - 2) \implies y = \frac{3}{2}x$ y $y = -\frac{3}{2}x + 6$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $-9x^2 + 36x - 36 = 0 \implies -9(x-2)^2 = 0 \implies \mathbf{(2,0)}$
     * Eje $Y$ ($x=0$): $4y^2 - 24y - 36 = 0 \implies y^2 - 6y - 9 = 0 \implies y = 3 \pm 3\sqrt{2} \implies \mathbf{(0, 3 \pm 3\sqrt{2})}$

---

**b) $4x^2 + y^2 - 8x + 4y - 8 = 0$**
1. Agrupamos y completamos cuadrados:
   $$4(x^2 - 2x) + (y^2 + 4y) = 8$$
   $$4[(x-1)^2 - 1] + [(y+2)^2 - 4] = 8$$
   $$4(x-1)^2 - 4 + (y+2)^2 - 4 = 8 \implies 4(x-1)^2 + (y+2)^2 = 16$$
   Divide por $16$:
   $$\frac{(x-1)^2}{4} + \frac{(y+2)^2}{16} = 1$$
2. **Cónica:** Elipse vertical.
   * **Centro:** $C(1,-2)$
   * **Ejes:** $a = 4$ (vertical), $b = 2$ (horizontal), $c = \sqrt{16 - 4} = 2\sqrt{3}$
   * **Vértices principales:** $V_1(1, -6)$ y $V_2(1, 2)$
   * **Vértices secundarios:** $B_1(-1, -2)$ y $B_2(3, -2)$
   * **Focos:** $F_1(1, -2-2\sqrt{3})$ y $F_2(1, -2+2\sqrt{3})$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $4x^2 - 8x - 8 = 0 \implies x^2 - 2x - 2 = 0 \implies x = 1 \pm \sqrt{3} \implies \mathbf{(1 \pm \sqrt{3}, 0)}$
     * Eje $Y$ ($x=0$): $y^2 + 4y - 8 = 0 \implies y = -2 \pm 2\sqrt{3} \implies \mathbf{(0, -2 \pm 2\sqrt{3})}$

---

**c) $\frac{(x-2)^2}{25} + \frac{(y-5)^2}{9} - 1 = 0 \implies \frac{(x-2)^2}{25} + \frac{(y-5)^2}{9} = 1$**
1. **Cónica:** Elipse horizontal.
   * **Centro:** $C(2,5)$
   * **Ejes:** $a = 5$ (horizontal), $b = 3$ (vertical), $c = \sqrt{25 - 9} = 4$
   * **Vértices principales:** $V_1(-3, 5)$ y $V_2(7, 5)$
   * **Vértices secundarios:** $B_1(2, 2)$ y $B_2(2, 8)$
   * **Focos:** $F_1(-2, 5)$ y $F_2(6, 5)$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $\frac{(x-2)^2}{25} + \frac{25}{9} = 1 \implies \frac{(x-2)^2}{25} = -\frac{16}{9}$ (Sin solución real, **no interseca**)
     * Eje $Y$ ($x=0$): $\frac{4}{25} + \frac{(y-5)^2}{9} = 1 \implies \frac{(y-5)^2}{9} = \frac{21}{25} \implies y = 5 \pm \frac{3\sqrt{21}}{5} \implies \mathbf{\left(0, 5 \pm \frac{3\sqrt{21}}{5}\right)}$

---

**d) $4x^2 + y^2 - 16x - 6y + 21 = 0$**
1. Completamos cuadrados:
   $$4(x^2 - 4x) + (y^2 - 6y) = -21$$
   $$4[(x-2)^2 - 4] + [(y-3)^2 - 9] = -21$$
   $$4(x-2)^2 - 16 + (y-3)^2 - 9 = -21 \implies 4(x-2)^2 + (y-3)^2 = 4$$
   Divide por $4$:
   $$\frac{(x-2)^2}{1} + \frac{(y-3)^2}{4} = 1$$
2. **Cónica:** Elipse vertical.
   * **Centro:** $C(2,3)$
   * **Ejes:** $a = 2$, $b = 1$, $c = \sqrt{4 - 1} = \sqrt{3}$
   * **Vértices principales:** $V_1(2, 1)$ y $V_2(2, 5)$
   * **Vértices secundarios:** $B_1(1, 3)$ y $B_2(3, 3)$
   * **Focos:** $F_1(2, 3-\sqrt{3})$ y $F_2(2, 3+\sqrt{3})$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $4x^2 - 16x + 21 = 0 \implies \Delta = 256 - 336 < 0$ (**No interseca**)
     * Eje $Y$ ($x=0$): $y^2 - 6y + 21 = 0 \implies \Delta = 36 - 84 < 0$ (**No interseca**)

---

**e) $9x^2 - y^2 - 36x - 6y + 18 = 0$**
1. Completamos cuadrados:
   $$9(x^2 - 4x) - (y^2 + 6y) = -18$$
   $$9[(x-2)^2 - 4] - [(y+3)^2 - 9] = -18$$
   $$9(x-2)^2 - 36 - (y+3)^2 + 9 = -18 \implies 9(x-2)^2 - (y+3)^2 = 9$$
   Divide por $9$:
   $$\frac{(x-2)^2}{1} - \frac{(y+3)^2}{9} = 1$$
2. **Cónica:** Hipérbola horizontal.
   * **Centro:** $C(2,-3)$
   * **Ejes:** $a = 1$, $b = 3$, $c = \sqrt{1 + 9} = \sqrt{10}$
   * **Vértices:** $V_1(1, -3)$ y $V_2(3, -3)$
   * **Focos:** $F_1(2-\sqrt{10}, -3)$ y $F_2(2+\sqrt{10}, -3)$
   * **Asíntotas:** $y + 3 = \pm 3(x - 2) \implies y = 3x - 9$ y $y = -3x + 3$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $9x^2 - 36x + 18 = 0 \implies x^2 - 4x + 2 = 0 \implies x = 2 \pm \sqrt{2} \implies \mathbf{(2 \pm \sqrt{2}, 0)}$
     * Eje $Y$ ($x=0$): $-y^2 - 6y + 18 = 0 \implies y^2 + 6y - 18 = 0 \implies y = -3 \pm 3\sqrt{3} \implies \mathbf{(0, -3 \pm 3\sqrt{3})}$

---

**f) $36x^2 - 64y^2 = 2304$**
1. Dividimos por $2304$:
   $$\frac{x^2}{64} - \frac{y^2}{36} = 1$$
2. **Cónica:** Hipérbola horizontal.
   * **Centro:** $C(0,0)$
   * **Ejes:** $a = 8$, $b = 6$, $c = \sqrt{64 + 36} = 10$
   * **Vértices:** $V_1(-8, 0)$ y $V_2(8, 0)$
   * **Focos:** $F_1(-10, 0)$ y $F_2(10, 0)$
   * **Asíntotas:** $y = \pm\frac{3}{4}x$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $x^2 = 64 \implies x = \pm 8 \implies \mathbf{(\pm 8, 0)}$
     * Eje $Y$ ($x=0$): $-y^2 = 36$ (Sin solución real, **no interseca**)

---

**g) $x^2 - 2x - y^2 - 6y + 9 = 0$**
1. Completamos cuadrados:
   $$(x-1)^2 - 1 - [(y+3)^2 - 9] + 9 = 0$$
   $$(x-1)^2 - (y+3)^2 + 17 = 0 \implies (y+3)^2 - (x-1)^2 = 17$$
   Divide por $17$:
   $$\frac{(y+3)^2}{17} - \frac{(x-1)^2}{17} = 1$$
2. **Cónica:** Hipérbola vertical equilátera.
   * **Centro:** $C(1,-3)$
   * **Ejes:** $a = b = \sqrt{17}$, $c = \sqrt{17 + 17} = \sqrt{34}$
   * **Vértices:** $V_1(1, -3-\sqrt{17})$ y $V_2(1, -3+\sqrt{17})$
   * **Focos:** $F_1(1, -3-\sqrt{34})$ y $F_2(1, -3+\sqrt{34})$
   * **Asíntotas:** $y + 3 = \pm(x - 1) \implies y = x - 4$ y $y = -x - 2$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $x^2 - 2x + 9 = 0 \implies \Delta = 4 - 36 < 0$ (**No interseca**)
     * Eje $Y$ ($x=0$): $-y^2 - 6y + 9 = 0 \implies y^2 + 6y - 9 = 0 \implies y = -3 \pm 3\sqrt{2} \implies \mathbf{(0, -3 \pm 3\sqrt{2})}$

---

**h) $-\frac{9}{5} + 2x + x^2 - \frac{6y}{5} - \frac{y^2}{5} = 0$**
1. Multiplicamos por $5$ para quitar denominadores:
   $$5x^2 + 10x - y^2 - 6y - 9 = 0$$
2. Completamos cuadrados:
   $$5(x+1)^2 - 5 - [(y+3)^2 - 9] - 9 = 0 \implies 5(x+1)^2 - (y+3)^2 = 5$$
   Divide por $5$:
   $$\frac{(x+1)^2}{1} - \frac{(y+3)^2}{5} = 1$$
3. **Cónica:** Hipérbola horizontal.
   * **Centro:** $C(-1,-3)$
   * **Ejes:** $a = 1$, $b = \sqrt{5}$, $c = \sqrt{6}$
   * **Vértices:** $V_1(-2, -3)$ y $V_2(0, -3)$
   * **Focos:** $F_1(-1-\sqrt{6}, -3)$ y $F_2(-1+\sqrt{6}, -3)$
   * **Asíntotas:** $y + 3 = \pm\sqrt{5}(x + 1)$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $5x^2 + 10x - 9 = 0 \implies x = -1 \pm \frac{\sqrt{70}}{5} \implies \mathbf{\left(-1 \pm \frac{\sqrt{70}}{5}, 0\right)}$
     * Eje $Y$ ($x=0$): $-y^2 - 6y - 9 = 0 \implies -(y+3)^2 = 0 \implies y = -3 \implies \mathbf{(0, -3)}$

---

**i) $\frac{4x^2}{3} - \frac{16x}{3} - \frac{y^2}{5} + 2y - \frac{2}{3} = 0$**
1. Multiplicamos por $15$:
   $$20x^2 - 80x - 3y^2 + 30y - 10 = 0$$
2. Completamos cuadrados:
   $$20[(x-2)^2 - 4] - 3[(y-5)^2 - 25] = 10$$
   $$20(x-2)^2 - 80 - 3(y-5)^2 + 75 = 10 \implies 20(x-2)^2 - 3(y-5)^2 = 15$$
   Divide por $15$:
   $$\frac{(x-2)^2}{3/4} - \frac{(y-5)^2}{5} = 1$$
3. **Cónica:** Hipérbola horizontal.
   * **Centro:** $C(2,5)$
   * **Ejes:** $a = \frac{\sqrt{3}}{2}$, $b = \sqrt{5}$, $c = \frac{\sqrt{23}}{2}$
   * **Vértices:** $V_{1,2}\left(2 \pm \frac{\sqrt{3}}{2}, 5\right)$
   * **Focos:** $F_{1,2}\left(2 \pm \frac{\sqrt{23}}{2}, 5\right)$
   * **Asíntotas:** $y - 5 = \pm\frac{2\sqrt{15}}{3}(x - 2)$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $20x^2 - 80x - 10 = 0 \implies 2x^2 - 8x - 1 = 0 \implies x = 2 \pm \frac{3\sqrt{2}}{2} \implies \mathbf{\left(2 \pm \frac{3\sqrt{2}}{2}, 0\right)}$
     * Eje $Y$ ($x=0$): $-3y^2 + 30y - 10 = 0 \implies 3y^2 - 30y + 10 = 0 \implies y = 5 \pm \frac{\sqrt{195}}{3} \implies \mathbf{\left(0, 5 \pm \frac{\sqrt{195}}{3}\right)}$

---

**j) $9x^2 - 16y^2 - 18x - 64y - 199 = 0$**
1. Completamos cuadrados:
   $$9(x-1)^2 - 16(y+2)^2 = 144 \implies \frac{(x-1)^2}{16} - \frac{(y+2)^2}{9} = 1$$
2. **Cónica:** Hipérbola horizontal.
   * **Centro:** $C(1,-2)$
   * **Ejes:** $a = 4$, $b = 3$, $c = 5$
   * **Vértices:** $V_1(-3,-2)$ y $V_2(5,-2)$
   * **Focos:** $F_1(-4,-2)$ y $F_2(6,-2)$
   * **Asíntotas:** $y + 2 = \pm\frac{3}{4}(x - 1)$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $9x^2 - 18x - 199 = 0 \implies x = 1 \pm \frac{4\sqrt{13}}{3} \implies \mathbf{\left(1 \pm \frac{4\sqrt{13}}{3}, 0\right)}$
     * Eje $Y$ ($x=0$): $-16y^2 - 64y - 199 = 0 \implies \Delta = 4096 - 12736 < 0$ (**No interseca**)

---

**k) $9y^2 + 16x^2 + 54y - 64x + 1 = 0$**
(Equivalente a la completación de cuadrados de la pregunta 1d)
1. Ecuación estándar:
   $$\frac{(x-2)^2}{9} + \frac{(y+3)^2}{16} = 1$$
2. **Cónica:** Elipse vertical.
   * **Centro:** $C(2,-3)$
   * **Ejes:** $a = 4$, $b = 3$, $c = \sqrt{7}$
   * **Vértices principales:** $V_1(2, -7)$ y $V_2(2, 1)$
   * **Vértices secundarios:** $B_1(-1, -3)$ y $B_2(5, -3)$
   * **Focos:** $F_1(2, -3-\sqrt{7})$ y $F_2(2, -3+\sqrt{7})$
   * **Intersecciones:**
     * Eje $X$ ($y=0$): $16x^2 - 64x + 1 = 0 \implies x = 2 \pm \frac{3\sqrt{7}}{4} \implies \mathbf{\left(2 \pm \frac{3\sqrt{7}}{4}, 0\right)}$
     * Eje $Y$ ($x=0$): $9y^2 + 54y + 1 = 0 \implies y = -3 \pm \frac{4\sqrt{5}}{3} \implies \mathbf{\left(0, -3 \pm \frac{4\sqrt{5}}{3}\right)}$

---

### Pregunta 9: Determine la ecuación canónica y los elementos de la elipse que tiene un vértice y un foco en común con la parábola $y^2 + 4x = 32$ y que tiene su otro foco en el origen

> **Justificación Académica:** Primero debemos hallar el vértice y foco de la parábola dada. El foco y el vértice compartidos con la elipse, junto al dato de que el segundo foco está en el origen, establecen de manera única las dimensiones y ubicación de la elipse.

#### Desarrollo:

1. **Estudio de la parábola:**
   $$y^2 = -4x + 32 \implies y^2 = -4(x - 8)$$
   * Se trata de una parábola horizontal que abre hacia la izquierda.
   * Vértice: $V_p(8, 0)$.
   * Parámetro: $4p = -4 \implies p = -1$.
   * Foco: $F_p(8 + p, 0) = F_p(7, 0)$.
2. **Transferencia de elementos a la elipse:**
   * La elipse comparte el vértice $V_1(8, 0)$ y el foco $F_1(7, 0)$.
   * El segundo foco de la elipse está en el origen: $F_2(0, 0)$.
3. **Determinación de los parámetros de la elipse:**
   * Al estar los focos $F_1(7,0)$ y $F_2(0,0)$ sobre el eje $X$, la elipse es horizontal.
   * Centro (punto medio de los focos $F_1$ y $F_2$):
     $$C\left(\frac{7 + 0}{2}, 0\right) = C(3.5, 0) = C\left(\frac{7}{2}, 0\right)$$
   * Semidistancia focal ($c$): distancia de $C(3.5,0)$ a $F_2(0,0)$:
     $$c = 3.5 = \frac{7}{2}$$
   * Semieje mayor ($a$): distancia del centro $C(3.5,0)$ al vértice $V_1(8,0)$:
     $$a = 8 - 3.5 = 4.5 = \frac{9}{2}$$
   * Semieje menor ($b$):
     $$b^2 = a^2 - c^2 = \left(\frac{9}{2}\right)^2 - \left(\frac{7}{2}\right)^2 = \frac{81}{4} - \frac{49}{4} = \frac{32}{4} = 8 \implies b = 2\sqrt{2}$$
4. **Ecuación canónica:**
   $$\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1 \implies \frac{(x - 3.5)^2}{20.25} + \frac{y^2}{8} = 1 \implies \frac{4(x - 7/2)^2}{81} + \frac{y^2}{8} = 1$$

#### Elementos:
* **Centro:** $C(3.5, 0)$
* **Focos:** $F_1(7,0)$ y $F_2(0,0)$
* **Vértices principales:** $V_1(8,0)$ y $V_2(-1,0)$
* **Vértices secundarios:** $B_1(3.5, 2\sqrt{2})$ y $B_2(3.5, -2\sqrt{2})$
* **Excentricidad:** $e = \frac{c}{a} = \frac{3.5}{4.5} = \frac{7}{9}$

$$\frac{4(x - 7/2)^2}{81} + \frac{y^2}{8} = 1$$

---

### Pregunta 10: Determine las ecuaciones de las hipérbolas que cumplen las siguientes características, todos sus elementos y representar en el Plano

> **Justificación Académica:** La alineación horizontal de los puntos provistos define hipérbolas con eje transversal horizontal. Los parámetros $a$ (distancia centro-vértice) y $c$ (distancia centro-foco) nos permiten calcular $b^2$ mediante la relación de la hipérbola $c^2 = a^2 + b^2$.

#### Desarrollo:

**a) $C(4,-1)$; $F(7,-1)$; $V(6,-1)$**
1. **Orientación:** Eje transversal horizontal (la ordenada $y=-1$ permanece constante).
2. **Cálculo de distancias:**
   * $a = d(C, V) = 6 - 4 = 2 \implies a^2 = 4$.
   * $c = d(C, F) = 7 - 4 = 3 \implies c^2 = 9$.
3. **Cálculo de $b^2$:**
   $$c^2 = a^2 + b^2 \implies 9 = 4 + b^2 \implies b^2 = 5 \implies b = \sqrt{5}$$
4. **Ecuación canónica:**
   $$\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1 \implies \frac{(x-4)^2}{4} - \frac{(y+1)^2}{5} = 1$$
5. **Elementos:**
   * Vértices: $V_1(2, -1)$ y $V_2(6, -1)$
   * Focos: $F_1(1, -1)$ y $F_2(7, -1)$
   * Asíntotas: $y + 1 = \pm\frac{\sqrt{5}}{2}(x - 4)$

$$\frac{(x-4)^2}{4} - \frac{(y+1)^2}{5} = 1$$

---

**b) Focos en $(3,7)$ y $(7,7)$, vértice en $(6,7)$**
1. **Orientación:** Eje transversal horizontal ($y=7$ constante).
2. **Determinación del centro $C(h,k)$:** Punto medio de los focos:
   $$h = \frac{3 + 7}{2} = 5, \quad k = 7 \implies C(5,7)$$
3. **Cálculo de distancias:**
   * $c = d(C, F_2) = 7 - 5 = 2 \implies c^2 = 4$.
   * $a = d(C, V_2) = 6 - 5 = 1 \implies a^2 = 1$.
4. **Cálculo de $b^2$:**
   $$c^2 = a^2 + b^2 \implies 4 = 1 + b^2 \implies b^2 = 3 \implies b = \sqrt{3}$$
5. **Ecuación canónica:**
   $$\frac{(x-5)^2}{1} - \frac{(y-7)^2}{3} = 1$$
6. **Elementos:**
   * Centro: $C(5,7)$
   * Vértices: $V_1(4, 7)$ y $V_2(6, 7)$
   * Focos: $F_1(3,7)$ y $F_2(7,7)$
   * Asíntotas: $y - 7 = \pm\sqrt{3}(x - 5)$

$$(x-5)^2 - \frac{(y-7)^2}{3} = 1$$

---

### Pregunta 11: Determine la ecuación canónica y los demás elementos de la elipse cuya suma de distancias a los puntos $(\pm 3,0)$ es 16

> **Justificación Académica:** Por definición, los puntos fijos $(\pm 3,0)$ representan los focos $F_1$ y $F_2$ de la elipse. La suma constante es el diámetro principal $2a = 16$. El eje mayor es horizontal ya que los focos están en el eje $X$.

#### Desarrollo:

1. **Identificación de parámetros:**
   * Focos: $F_1(-3,0)$ y $F_2(3,0) \implies c = 3 \implies c^2 = 9$.
   * Centro: $C(0,0)$ (punto medio).
   * Eje mayor: $2a = 16 \implies a = 8 \implies a^2 = 64$.
2. **Cálculo del parámetro $b^2$:**
   $$b^2 = a^2 - c^2 = 64 - 9 = 55 \implies b = \sqrt{55}$$
3. **Ecuación canónica (eje horizontal):**
   $$\frac{x^2}{64} + \frac{y^2}{55} = 1$$

#### Elementos adicionales:
* **Centro:** $C(0,0)$
* **Vértices principales:** $V_1(-8,0)$ y $V_2(8,0)$
* **Vértices secundarios:** $B_1(0, -\sqrt{55})$ y $B_2(0, \sqrt{55})$
* **Excentricidad:** $e = \frac{c}{a} = \frac{3}{8} = 0.375$
* **Lado recto:** $LR = \frac{2b^2}{a} = \frac{110}{8} = 13.75$

$$\frac{x^2}{64} + \frac{y^2}{55} = 1$$

---

### Pregunta 12: Hallar la ecuación canónica de la hipérbola con vértices en $(3, -5)$ y $(3, 1)$ y asíntotas: $y = 2x - 8$ e $y = -2x + 4$. Calcule los elementos faltantes y trace la gráfica

> **Justificación Académica:** Los vértices están alineados verticalmente sobre la recta $x=3$, lo que nos da una hipérbola vertical. La pendiente de las asíntotas para una hipérbola vertical es igual a $\pm \frac{a}{b}$, permitiendo determinar $b$ a partir del valor conocido de $a$.

#### Desarrollo:

1. **Orientación de la hipérbola:** Los vértices son $V_1(3,-5)$ y $V_2(3,1)$. La abscisa $x = 3$ es constante, por lo que el eje transversal es vertical.
2. **Determinación del centro $C(h,k)$ y semieje $a$:**
   * Centro: $C\left(3, \frac{-5 + 1}{2}\right) = C(3,-2)$.
   * Semieje $a$: distancia del centro $C(3,-2)$ al vértice $V_2(3,1)$:
     $$a = 1 - (-2) = 3$$
3. **Uso de las asíntotas para hallar $b$:**
   * Las asíntotas de una hipérbola vertical se definen por:
     $$y - k = \pm\frac{a}{b}(x - h) \implies y + 2 = \pm\frac{3}{b}(x - 3) \implies y = \pm\frac{3}{b}(x - 3) - 2$$
   * Comparando con las ecuaciones provistas: $y = 2x - 8$ (pendiente $2$).
     $$\frac{3}{b} = 2 \implies b = \frac{3}{2} = 1.5 \implies b^2 = \frac{9}{4}$$
   * Comprobación: si $b = 1.5$, la asíntota con pendiente negativa es:
     $$y = -2(x - 3) - 2 = -2x + 6 - 2 = -2x + 4 \quad (\text{Correcto})$$
4. **Ecuación canónica:**
   $$\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1 \implies \frac{(y+2)^2}{9} - \frac{4(x-3)^2}{9} = 1$$

#### Elementos faltantes:
* **Distancia focal ($c$):** $c^2 = a^2 + b^2 = 9 + 2.25 = 11.25 = \frac{45}{4} \implies c = \frac{3\sqrt{5}}{2} \approx 3.35$
* **Focos:** $F_1\left(3, -2 - \frac{3\sqrt{5}}{2}\right)$ y $F_2\left(3, -2 + \frac{3\sqrt{5}}{2}\right)$

$$\frac{(y+2)^2}{9} - \frac{4(x-3)^2}{9} = 1$$

---

### Pregunta 13: Determine la ecuación de la hipérbola que tiene su centro en el origen, un vértice en $(6,0)$ y una de sus asíntotas es $4x - 3y = 0$

> **Justificación Académica:** Con el centro en el origen y un vértice sobre el eje $X$, el eje de la hipérbola es horizontal. La pendiente de las asíntotas es $\pm \frac{b}{a}$. Utilizando el valor de $a=6$ y la ecuación de la asíntota, despejamos el valor de $b$.

#### Desarrollo:

1. **Orientación de la hipérbola:** Centro $C(0,0)$ y vértice $V_2(6,0)$ implican un eje transversal horizontal.
2. **Semieje $a$:**
   $$a = d(C, V_2) = 6 \implies a^2 = 36$$
3. **Uso de la asíntota para determinar $b$:**
   * La asíntota dada es $4x - 3y = 0 \implies y = \frac{4}{3}x$.
   * La pendiente de la asíntota horizontal es $\frac{b}{a}$:
     $$\frac{b}{a} = \frac{4}{3} \implies \frac{b}{6} = \frac{4}{3} \implies b = 8 \implies b^2 = 64$$
4. **Ecuación canónica:**
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \implies \frac{x^2}{36} - \frac{y^2}{64} = 1$$

$$\frac{x^2}{36} - \frac{y^2}{64} = 1$$

---

### Pregunta 14: Determine las asíntotas de la hipérbola $\frac{y^2}{15} - x^2 = 1$. Represente en el plano todos los datos

> **Justificación Académica:** Esta hipérbola tiene la forma canónica vertical con centro en el origen, donde $a^2 = 15$ y $b^2 = 1$. Las asíntotas en esta orientación corresponden a las rectas de ecuación $y = \pm \frac{a}{b}x$.

#### Desarrollo:

1. **Parámetros de la hipérbola:**
   * Centro: $C(0,0)$
   * $a^2 = 15 \implies a = \sqrt{15}$
   * $b^2 = 1 \implies b = 1$
2. **Ecuación de las asíntotas:**
   $$y = \pm \frac{a}{b}x \implies y = \pm \sqrt{15}x$$

#### Elementos adicionales para su representación:
* **Vértices:** $V_1(0, -\sqrt{15})$ y $V_2(0, \sqrt{15})$
* **Focos:** $c^2 = a^2 + b^2 = 15 + 1 = 16 \implies c = 4 \implies F_1(0,-4)$ y $F_2(0,4)$

$$y = \pm \sqrt{15}x$$

---

### Pregunta 15: Considere la hipérbola $9x^2 - 16y^2 - 18x - 64y - 199 = 0$, determine las coordenadas: del centro, vértices, focos y las ecuaciones de las asíntotas y grafíquela

(Resuelto de manera similar al ejercicio 8j)

#### Desarrollo:

1. **Completación de cuadrados:**
   $$9(x^2 - 2x) - 16(y^2 + 4y) = 199$$
   $$9[(x-1)^2 - 1] - 16[(y+2)^2 - 4] = 199$$
   $$9(x-1)^2 - 9 - 16(y+2)^2 + 64 = 199 \implies 9(x-1)^2 - 16(y+2)^2 = 144$$
   Divide por $144$:
   $$\frac{(x-1)^2}{16} - \frac{(y+2)^2}{9} = 1$$
2. **Características calculadas:**
   * **Centro:** $C(1,-2)$
   * **Semiejes:** $a = 4$ (horizontal), $b = 3$ (vertical)
   * **Distancia focal:** $c^2 = a^2 + b^2 = 16 + 9 = 25 \implies c = 5$
   * **Vértices:**
     $$V_1(1-4, -2) = (-3,-2), \quad V_2(1+4, -2) = (5,-2)$$
   * **Focos:**
     $$F_1(1-5, -2) = (-4,-2), \quad F_2(1+5, -2) = (6,-2)$$
   * **Asíntotas:**
     $$y - k = \pm\frac{b}{a}(x - h) \implies y + 2 = \pm\frac{3}{4}(x - 1)$$
     $$y = \frac{3}{4}x - \frac{11}{4} \quad \text{y} \quad y = -\frac{3}{4}x - \frac{5}{4}$$

$$\text{Ecuación: } \frac{(x-1)^2}{16} - \frac{(y+2)^2}{9} = 1$$

---

### Pregunta 16: Determine la ecuación canónica de la hipérbola con focos en $(1,4)$ y $(1, -4)$ con $a = 3$

> **Justificación Académica:** Focos en la vertical $x=1$ definen una hipérbola vertical. La distancia del centro al foco es $c = 4$. Usando la relación pitagórica calculamos $b^2$.

#### Desarrollo:

1. **Identificación de la geometría focal:**
   * Focos: $F_1(1,-4)$ y $F_2(1,4) \implies$ Eje transversal vertical.
   * Centro (punto medio): $C\left(1, \frac{-4 + 4}{2}\right) = C(1,0)$.
   * Semidistancia focal ($c$):
     $$c = 4 \implies c^2 = 16$$
2. **Cálculo de $b^2$:**
   * Se da $a = 3 \implies a^2 = 9$.
   * En la hipérbola: $c^2 = a^2 + b^2 \implies 16 = 9 + b^2 \implies b^2 = 7$.
3. **Ecuación canónica:**
   $$\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1 \implies \frac{y^2}{9} - \frac{(x-1)^2}{7} = 1$$

$$\frac{y^2}{9} - \frac{(x-1)^2}{7} = 1$$

---

### Pregunta 17: Determine completando cuadrados, la cónica, identifique todos los elementos y represente en el plano

> **Justificación Académica:** Realizamos la completación de cuadrados de las variables presentes para pasar cada ecuación general a su forma estándar. A partir de ella se identifican de manera inequívoca las características geométricas particulares.

#### Desarrollo Paso a Paso:

**a) $x^2 + y^2 - 2x - 2y = 0$**
1. Completamos cuadrados:
   $$(x-1)^2 - 1 + (y-1)^2 - 1 = 0 \implies (x-1)^2 + (y-1)^2 = 2$$
2. **Cónica:** Circunferencia.
   * **Centro:** $C(1,1)$
   * **Radio:** $R = \sqrt{2}$

---

**b) $5x^2 - 2y^2 - 10x + 8y - 13 = 0$**
1. Agrupamos y completamos cuadrados:
   $$5(x^2 - 2x) - 2(y^2 - 4y) = 13$$
   $$5[(x-1)^2 - 1] - 2[(y-2)^2 - 4] = 13$$
   $$5(x-1)^2 - 5 - 2(y-2)^2 + 8 = 13 \implies 5(x-1)^2 - 2(y-2)^2 = 10$$
   Divide por $10$:
   $$\frac{(x-1)^2}{2} - \frac{(y-2)^2}{5} = 1$$
2. **Cónica:** Hipérbola horizontal.
   * **Centro:** $C(1,2)$
   * **Ejes:** $a = \sqrt{2}$, $b = \sqrt{5}$, $c = \sqrt{7}$
   * **Vértices:** $V_{1,2}(1 \pm \sqrt{2}, 2)$
   * **Asíntotas:** $y - 2 = \pm\frac{\sqrt{10}}{2}(x - 1)$

---

**c) $y^2 + 9x + 9 = 0$**
1. Despejamos el término cuadrático:
   $$y^2 = -9x - 9 \implies y^2 = -9(x + 1)$$
2. **Cónica:** Parábola horizontal que abre a la izquierda.
   * **Vértice:** $V(-1,0)$
   * **Parámetro:** $4p = -9 \implies p = -2.25 = -\frac{9}{4}$
   * **Foco:** $F(-1 - 2.25, 0) = F(-3.25, 0) = F\left(-\frac{13}{4}, 0\right)$
   * **Directriz:** $x = -1 - (-2.25) \implies x = 1.25 = \frac{5}{4}$
   * **Eje focal:** $y = 0$ (Eje $X$)

---

**d) $x^2 + y^2 + 4x + 5 = 0$**
1. Completamos cuadrados:
   $$(x+2)^2 - 4 + y^2 + 5 = 0 \implies (x+2)^2 + y^2 = -1$$
2. **Cónica:** Locus vacío (No existen soluciones reales porque la suma de cuadrados reales no puede ser negativa).

---

**e) $16x^2 + 9y^2 - 64x - 54y + 1 = 0$**
1. Completamos cuadrados:
   $$16(x^2 - 4x) + 9(y^2 - 6y) = -1$$
   $$16[(x-2)^2 - 4] + 9[(y-3)^2 - 9] = -1$$
   $$16(x-2)^2 - 64 + 9(y-3)^2 - 81 = -1 \implies 16(x-2)^2 + 9(y-3)^2 = 144$$
   Divide por $144$:
   $$\frac{(x-2)^2}{9} + \frac{(y-3)^2}{16} = 1$$
2. **Cónica:** Elipse vertical.
   * **Centro:** $C(2,3)$
   * **Ejes:** $a = 4$, $b = 3$, $c = \sqrt{7}$
   * **Vértices principales:** $V_1(2, -1)$ y $V_2(2, 7)$
   * **Focos:** $F_{1,2}(2, 3 \pm \sqrt{7})$

---

**f) $-7x^2 + 12y^2 + 28x + 72y - 4 = 0$**
1. Completamos cuadrados:
   $$12(y^2 + 6y) - 7(x^2 - 4x) = 4$$
   $$12[(y+3)^2 - 9] - 7[(x-2)^2 - 4] = 4$$
   $$12(y+3)^2 - 108 - 7(x-2)^2 + 28 = 4 \implies 12(y+3)^2 - 7(x-2)^2 = 84$$
   Divide por $84$:
   $$\frac{(y+3)^2}{7} - \frac{(x-2)^2}{12} = 1$$
2. **Cónica:** Hipérbola vertical.
   * **Centro:** $C(2,-3)$
   * **Ejes:** $a = \sqrt{7}$, $b = 2\sqrt{3}$, $c = \sqrt{19}$
   * **Vértices:** $V_{1,2}(2, -3 \pm \sqrt{7})$
   * **Asíntotas:** $y + 3 = \pm\frac{\sqrt{21}}{6}(x - 2)$

---

**g) $x^2 + y^2 - 6x - 8y + 40 = 0$**
1. Completamos cuadrados:
   $$(x-3)^2 - 9 + (y-4)^2 - 16 = -40 \implies (x-3)^2 + (y-4)^2 = -15$$
2. **Cónica:** Locus vacío (No representa ninguna curva en el plano cartesiano real).

---

**h) $x^2 + 6x - 8y + 41 = 0$**
1. Completamos cuadrados:
   $$(x+3)^2 - 9 - 8y + 41 = 0 \implies (x+3)^2 = 8y - 32 \implies (x+3)^2 = 8(y-4)$$
2. **Cónica:** Parábola vertical que abre hacia arriba.
   * **Vértice:** $V(-3,4)$
   * **Parámetro:** $4p = 8 \implies p = 2$
   * **Foco:** $F(-3, 4 + 2) = F(-3, 6)$
   * **Directriz:** $y = 4 - 2 \implies y = 2$
   * **Eje focal:** $x = -3$

---

### Pregunta 18: Determinar la ecuación de una parábola cuyo eje de simetría sea paralelo al eje $Y$, su vértice pertenezca al eje $X$ y que contenga a los puntos $A(2, 3)$ y $B(-1, 12)$

> **Justificación Académica:** Un eje de simetría paralelo al eje $Y$ indica una parábola vertical de ecuación canónica $(x-h)^2 = 4p(y-k)$. Dado que el vértice pertenece al eje $X$, se tiene $k=0$, simplificando la ecuación a $(x-h)^2 = 4py$.

#### Desarrollo:

1. **Planteamiento de las ecuaciones para los puntos dados:**
   Sustituimos $A(2,3)$ y $B(-1,12)$ en $(x-h)^2 = 4py$:
   * Para $A(2,3)$:
     $$(2 - h)^2 = 4p(3) \implies (2 - h)^2 = 12p \quad \text{--- (Ecuación 1)}$$
   * Para $B(-1,12)$:
     $$(-1 - h)^2 = 4p(12) \implies (h + 1)^2 = 48p \quad \text{--- (Ecuación 2)}$$
2. **Resolución del sistema mediante división:**
   Dividimos la Ecuación 2 por la Ecuación 1 para eliminar la variable $p$:
   $$\frac{(h + 1)^2}{(2 - h)^2} = \frac{48p}{12p} = 4$$
   $$(h + 1)^2 = 4(2 - h)^2$$
3. **Extracción de raíces cuadradas y análisis de casos:**
   $$h + 1 = \pm 2(2 - h)$$
   * **Caso 1:** $h + 1 = 2(2 - h)$
     $$h + 1 = 4 - 2h \implies 3h = 3 \implies h = 1$$
     Sustituyendo $h=1$ en la Ecuación 1:
     $$(2 - 1)^2 = 12p \implies 1 = 12p \implies 4p = \frac{1}{3}$$
     Ecuación resultante:
     $$(x - 1)^2 = \frac{1}{3}y \quad \text{o} \quad y = 3(x - 1)^2$$
   * **Caso 2:** $h + 1 = -2(2 - h)$
     $$h + 1 = -4 + 2h \implies h = 5$$
     Sustituyendo $h=5$ en la Ecuación 1:
     $$(2 - 5)^2 = 12p \implies 9 = 12p \implies 4p = 3$$
     Ecuación resultante:
     $$(x - 5)^2 = 3y \quad \text{o} \quad y = \frac{1}{3}(x - 5)^2$$

Ambas soluciones satisfacen los puntos de paso y las condiciones del enunciado.

$$y = 3(x - 1)^2 \quad \text{o} \quad y = \frac{1}{3}(x - 5)^2$$

---

### Pregunta 19: Un puente colgante de 100 m de longitud tiene trayectoria parabólica sostenida por dos torres de igual altura. Si la directriz se encuentra en la superficie terrestre y el punto más bajo de cada cable está a $10\text{ m}$ de altura de dicha superficie, determine la altura de las torres

> **Justificación Académica:** Establecemos el origen sobre la proyección del vértice en el suelo. La superficie terrestre se modela por la recta $y=0$. El vértice está en $V(0,10)$. Dado que la directriz es $y=0$, calculamos el parámetro $p$ a partir de la distancia directriz-vértice.

#### Desarrollo:

1. **Modelación geométrica de la parábola:**
   * La superficie de la tierra es la recta horizontal $y = 0$.
   * El vértice de la parábola está en $V(0, 10)$, es decir, $h=0, k=10$.
   * La directriz de la parábola vertical es la línea $y = 0$.
   * Sabemos que la ecuación de la directriz es $y = k - p$. Sustituyendo los valores:
     $$0 = 10 - p \implies p = 10$$
2. **Ecuación del cable:**
   $$(x - h)^2 = 4p(y - k) \implies x^2 = 40(y - 10)$$
3. **Cálculo de la altura en las torres:**
   * El puente tiene una luz de $100\text{ m}$ con el vértice centrado. Por tanto, las torres están localizadas en las abscisas $x = -50$ y $x = 50$.
   * Evaluamos la altura del cable para $x = 50$:
     $$50^2 = 40(y - 10) \implies 2500 = 40(y - 10)$$
     $$y - 10 = \frac{2500}{40} = 62.5$$
     $$y = 72.5\text{ m}$$

$$\text{Altura de las torres} = 72.5\text{ m}$$

---

### Pregunta 20: Hallar la/s ecuación/es de la parábola con vértice en el origen y eje uno de los ejes coordenados, que pasa por el punto de intersección de la recta $l: -4x + 3y = -23$ y la circunferencia con centro $(-2,-2)$ y radio 5

> **Justificación Académica:** Buscamos los puntos comunes resolviendo algebraicamente el sistema recta-circunferencia. Luego, usamos las posibles formas canónicas con vértice en $(0,0)$ y eje axial ($x^2 = 4py$ o $y^2 = 4px$) para forzar el paso por el punto de intersección obtenido.

#### Desarrollo:

1. **Resolución de la intersección Recta-Circunferencia:**
   * Recta: $-4x + 3y = -23 \implies y = \frac{4x - 23}{3}$
   * Circunferencia: $(x+2)^2 + (y+2)^2 = 25$
   * Sustituyendo $y$:
     $$(x+2)^2 + \left(\frac{4x - 23}{3} + 2\right)^2 = 25$$
     $$(x+2)^2 + \left(\frac{4x - 17}{3}\right)^2 = 25$$
   * Multiplicamos todo por $9$:
     $$9(x^2 + 4x + 4) + (16x^2 - 136x + 289) = 225$$
     $$9x^2 + 36x + 36 + 16x^2 - 136x + 289 - 225 = 0$$
     $$25x^2 - 100x + 100 = 0$$
   * Simplificando entre $25$:
     $$x^2 - 4x + 4 = 0 \implies (x-2)^2 = 0 \implies x = 2$$
   * Obtenemos la ordenada $y$:
     $$y = \frac{4(2) - 23}{3} = \frac{-15}{3} = -5$$
   * Así, el único punto de intersección es $P(2,-5)$ (la recta es tangente a la circunferencia).

2. **Cálculo de las ecuaciones parabólicas con vértice $V(0,0)$:**
   * **Caso 1:** Eje vertical ($x^2 = 4py$).
     Sustituyendo $P(2,-5)$:
     $$2^2 = 4p(-5) \implies 4 = -20p \implies 4p = -\frac{4}{5} \implies x^2 = -\frac{4}{5}y \implies 5x^2 + 4y = 0$$
   * **Caso 2:** Eje horizontal ($y^2 = 4px$).
     Sustituyendo $P(2,-5)$:
     $$(-5)^2 = 4p(2) \implies 25 = 8p \implies 4p = \frac{25}{2} \implies y^2 = \frac{25}{2}x \implies 2y^2 - 25x = 0$$

$$5x^2 + 4y = 0 \quad \text{o} \quad 2y^2 - 25x = 0$$

---

### Pregunta 21: Determine la ecuación de la parábola cuyo foco es $(-3; 5)$, $p = \frac{5}{3}$ y eje paralelo al eje $X$

> **Justificación Académica:** Un eje paralelo al eje $X$ determina una parábola horizontal con ecuación canónica de la forma $(y-k)^2 = 4p(x-h)$. El foco de una parábola horizontal se ubica en $F(h+p, k)$.

#### Desarrollo:

1. **Establecimiento de las coordenadas focales:**
   * Foco dado: $F(-3, 5)$.
   * Para una parábola horizontal: $F(h+p, k) \implies k = 5$ y $h+p = -3$.
2. **Cálculo del vértice $h$ con el parámetro $p = \frac{5}{3}$:**
   $$h + \frac{5}{3} = -3 \implies h = -3 - \frac{5}{3} = -\frac{14}{3}$$
3. Sustitución en la ecuación canónica:
   $$(y - 5)^2 = 4\left(\frac{5}{3}\right)\left(x - \left(-\frac{14}{3}\right)\right)$$
   $$(y - 5)^2 = \frac{20}{3}\left(x + \frac{14}{3}\right)$$
   * Multiplicando por 9 para obtener la ecuación general con coeficientes enteros:
     $$9y^2 - 90y - 60x - 55 = 0$$

$$(y-5)^2 = \frac{20}{3}\left(x + \frac{14}{3}\right)$$

---
[[Intro. Cálculo]]
