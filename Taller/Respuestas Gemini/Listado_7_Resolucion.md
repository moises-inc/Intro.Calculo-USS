---
id: "20260606-listado7-introduccion-calculo-resolucion"
title: "Resolución Completa de Listado 7 - Cónicas (Circunferencia y Parábola)"
project: "Estudios_Universidad"
date: "2026-06-06T14:30:00"
last_modified: "2026-06-06T14:30:00"
type: "academic-note"
status: "completed"
priority: "medium"
tags: ["#status/completed", "#project/Estudios_Universidad", "#course/intro-calculo"]
---

# Guía Pedagógica Definitiva: Listado 7 - Introducción al Cálculo
**Materia:** Introducción al Cálculo  
**Docente:** Soledad Merino Ñanco  
**Resolución:** Gemini Academic Assistant  

---

## Introducción Conceptual
Esta guía ha sido diseñada como un recurso de estudio exhaustivo y riguroso para la comprensión de las secciones cónicas, centrándose en la **circunferencia** y la **parábola**. 

De acuerdo con la **Directiva Crítica** del curso, la resolución de todos los ejercicios se ha realizado utilizando exclusivamente **métodos algebraicos puros**:
1. **Completación de cuadrados** para pasar de la ecuación general de una cónica a su forma ordinaria o canónica.
2. **Fórmula de distancia entre dos puntos** y distancia de un punto a una recta para caracterizar radios y directrices.
3. **Condición de tangencia algebraica** mediante la anulación del discriminante ($\Delta = 0$) en sistemas de ecuaciones cuadráticas.
4. **Relaciones geométricas fundamentales** de perpendicularidad de rectas ($m_T \cdot m_N = -1$).

Queda estrictamente excluido el uso de herramientas de cálculo diferencial (límites, derivadas, integrales), garantizando un desarrollo puramente geométrico-analítico.

---

## Resolución Detallada de Ejercicios (1 al 30)

### Ejercicio 1: Completación de Cuadrados, Centros y Radios
> **Justificación Pedagógica:** La ecuación general de una circunferencia es $x^2 + y^2 + Dx + Ey + F = 0$. Para encontrar su centro $C(h, k)$ y su radio $R$, agrupamos los términos en $x$ e $y$, y completamos cuadrados para obtener la forma canónica:
> $$(x - h)^2 + (y - k)^2 = R^2$$

**Desarrollo:**

* **a) $x^2 + y^2 - 4x - 6y - 12 = 0$**
  1. Agrupamos los términos de las variables:
     $$(x^2 - 4x) + (y^2 - 6y) = 12$$
  2. Completamos cuadrados sumando y restando los términos adecuados:
     $$(x^2 - 4x + 4) - 4 + (y^2 - 6y + 9) - 9 = 12$$
     $$(x - 2)^2 + (y - 3)^2 - 13 = 12$$
  3. Despejamos el término constante:
     $$(x - 2)^2 + (y - 3)^2 = 25$$
  4. Identificamos los elementos:
     * Centro: $C(2, 3)$
     * Radio: $R = \sqrt{25} = 5$

  **Respuesta:** Ecuación canónica: $\mathbf{(x - 2)^2 + (y - 3)^2 = 25}$, con centro $\mathbf{C(2, 3)}$ y radio $\mathbf{R = 5}$.

* **b) $x^2 + y^2 + 3x + y - 10 = 0$**
  1. Agrupamos términos:
     $$(x^2 + 3x) + (y^2 + y) = 10$$
  2. Completamos cuadrados:
     $$\left(x^2 + 3x + \frac{9}{4}\right) - \frac{9}{4} + \left(y^2 + y + \frac{1}{4}\right) - \frac{1}{4} = 10$$
     $$\left(x + \frac{3}{2}\right)^2 + \left(y + \frac{1}{2}\right)^2 - \frac{10}{4} = 10$$
  3. Despejamos:
     $$\left(x + \frac{3}{2}\right)^2 + \left(y + \frac{1}{2}\right)^2 = 10 + \frac{5}{2} = \frac{25}{2}$$
  4. Identificamos los elementos:
     * Centro: $C\left(-\frac{3}{2}, -\frac{1}{2}\right)$
     * Radio: $R = \sqrt{\frac{25}{2}} = \frac{5}{\sqrt{2}} = \frac{5\sqrt{2}}{2} \approx 3.54$

  **Respuesta:** Ecuación canónica: $\mathbf{\left(x + \frac{3}{2}\right)^2 + \left(y + \frac{1}{2}\right)^2 = \frac{25}{2}}$, con centro $\mathbf{C\left(-\frac{3}{2}, -\frac{1}{2}\right)}$ y radio $\mathbf{R = \frac{5\sqrt{2}}{2}}$.

* **c) $4x^2 + 4y^2 - 4x + 12y - 6 = 0$**
  1. Dividimos toda la ecuación por $4$ para simplificar los coeficientes principales:
     $$x^2 + y^2 - x + 3y - \frac{3}{2} = 0$$
  2. Agrupamos términos:
     $$(x^2 - x) + (y^2 + 3y) = \frac{3}{2}$$
  3. Completamos cuadrados:
     $$\left(x^2 - x + \frac{1}{4}\right) - \frac{1}{4} + \left(y^2 + 3y + \frac{9}{4}\right) - \frac{9}{4} = \frac{3}{2}$$
     $$\left(x - \frac{1}{2}\right)^2 + \left(y + \frac{3}{2}\right)^2 - \frac{10}{4} = \frac{3}{2}$$
  4. Despejamos:
     $$\left(x - \frac{1}{2}\right)^2 + \left(y + \frac{3}{2}\right)^2 = \frac{3}{2} + \frac{5}{2} = 4$$
  5. Identificamos los elementos:
     * Centro: $C\left(\frac{1}{2}, -\frac{3}{2}\right)$
     * Radio: $R = \sqrt{4} = 2$

  **Respuesta:** Ecuación canónica: $\mathbf{\left(x - \frac{1}{2}\right)^2 + \left(y + \frac{3}{2}\right)^2 = 4}$, con centro $\mathbf{C\left(\frac{1}{2}, -\frac{3}{2}\right)}$ y radio $\mathbf{R = 2}$.

* **d) $4x^2 + 4y^2 - 4x - 8y - 11 = 0$**
  1. Dividimos por $4$:
     $$x^2 + y^2 - x - 2y - \frac{11}{4} = 0$$
  2. Agrupamos términos:
     $$(x^2 - x) + (y^2 - 2y) = \frac{11}{4}$$
  3. Completamos cuadrados:
     $$\left(x^2 - x + \frac{1}{4}\right) - \frac{1}{4} + (y^2 - 2y + 1) - 1 = \frac{11}{4}$$
     $$\left(x - \frac{1}{2}\right)^2 + (y - 1)^2 - \frac{5}{4} = \frac{11}{4}$$
  4. Despejamos:
     $$\left(x - \frac{1}{2}\right)^2 + (y - 1)^2 = \frac{11}{4} + \frac{5}{4} = 4$$
  5. Identificamos los elementos:
     * Centro: $C\left(\frac{1}{2}, 1\right)$
     * Radio: $R = \sqrt{4} = 2$

  **Respuesta:** Ecuación canónica: $\mathbf{\left(x - \frac{1}{2}\right)^2 + (y - 1)^2 = 4}$, con centro $\mathbf{C\left(\frac{1}{2}, 1\right)}$ y radio $\mathbf{R = 2}$.

---

### Ejercicio 2: Posición Relativa de Recta y Circunferencia
> **Justificación Pedagógica:** Para determinar la posición relativa de una recta $L$ y una circunferencia $\mathcal{C}$, resolvemos el sistema de ecuaciones sustituyendo la variable despejada de la recta en la ecuación de la circunferencia. Obtenemos una ecuación cuadrática cuya cantidad de soluciones reales depende de su discriminante $\Delta$:
> * Si $\Delta > 0$: La recta es **secante** (corta en dos puntos).
> * Si $\Delta = 0$: La recta es **tangente** (corta en un punto).
> * Si $\Delta < 0$: La recta es **exterior** (no corta).

**Desarrollo:**
Dado el sistema:
$$\begin{cases} x^2 + y^2 - 2x - 3 = 0 & (\mathcal{C}) \\ 3x + y - 5 = 0 & (L) \end{cases}$$

1. Despejamos $y$ de la ecuación de la recta:
   $$y = 5 - 3x$$
2. Sustituimos esta expresión en la ecuación de la circunferencia:
   $$x^2 + (5 - 3x)^2 - 2x - 3 = 0$$
3. Desarrollamos el binomio y agrupamos términos semejantes:
   $$x^2 + (25 - 30x + 9x^2) - 2x - 3 = 0$$
   $$10x^2 - 32x + 22 = 0$$
4. Simplificamos dividiendo la ecuación cuadrática entre $2$:
   $$5x^2 - 16x + 11 = 0$$
5. Calculamos el discriminante $\Delta = b^2 - 4ac$:
   $$\Delta = (-16)^2 - 4(5)(11) = 256 - 220 = 36$$
   Como $\Delta = 36 > 0$, existen dos puntos de intersección reales y distintos, lo que clasifica a la recta como **secante**.
6. Determinamos los puntos de intersección resolviendo la ecuación cuadrática por factorización:
   $$(5x - 11)(x - 1) = 0$$
   * Para $x_1 = 1$: $y_1 = 5 - 3(1) = 2 \implies P_1(1, 2)$
   * Para $x_2 = \frac{11}{5}$: $y_2 = 5 - 3\left(\frac{11}{5}\right) = -\frac{8}{5} \implies P_2\left(\frac{11}{5}, -\frac{8}{5}\right)$

**Respuesta:** La recta es **secante** a la circunferencia, intersecándola en los puntos $\mathbf{P_1(1, 2)}$ y $\mathbf{P_2\left(\frac{11}{5}, -\frac{8}{5}\right)}$.

---

### Ejercicio 3: Rectas Tangentes y Normales
> **Justificación Pedagógica:** La recta normal $L_N$ a una circunferencia en un punto $P$ de la misma pasa por su centro $C$ y por dicho punto $P$. Su pendiente es $m_N$. Por perpendicularidad, la recta tangente $L_T$ en $P$ tiene pendiente $m_T = -\frac{1}{m_N}$.

**Desarrollo:**

* **a) $(x + 4)^2 + (y + 2)^2 = 10$, en $P(-5, 1)$**
  1. Comprobamos la pertenencia del punto: $(-5 + 4)^2 + (1 + 2)^2 = (-1)^2 + 3^2 = 10$. El punto pertenece.
  2. Identificamos el centro: $C(-4, -2)$.
  3. Calculamos la pendiente de la recta normal $CP$:
     $$m_N = \frac{y_P - y_C}{x_P - x_C} = \frac{1 - (-2)}{-5 - (-4)} = \frac{3}{-1} = -3$$
  4. Escribimos la ecuación de la recta normal (pasa por $P(-5, 1)$ con $m_N = -3$):
     $$y - 1 = -3(x + 5) \implies y - 1 = -3x - 15 \implies 3x + y + 14 = 0$$
  5. Calculamos la pendiente de la recta tangente:
     $$m_T = -\frac{1}{m_N} = \frac{1}{3}$$
  6. Escribimos la ecuación de la recta tangente (pasa por $P(-5, 1)$ con $m_T = \frac{1}{3}$):
     $$y - 1 = \frac{1}{3}(x + 5) \implies 3y - 3 = x + 5 \implies x - 3y + 8 = 0$$

  **Respuesta:** Recta normal: $\mathbf{3x + y + 14 = 0}$, Recta tangente: $\mathbf{x - 3y + 8 = 0}$.

* **b) $x^2 + y^2 - 2x - 6y - 3 = 0$, en $P(-1, 6)$**
  1. Comprobamos pertenencia: $(-1)^2 + 6^2 - 2(-1) - 6(6) - 3 = 1 + 36 + 2 - 36 - 3 = 0$. Pertenece.
  2. Hallamos el centro completando cuadrados:
     $$(x - 1)^2 - 1 + (y - 3)^2 - 9 = 3 \implies (x - 1)^2 + (y - 3)^2 = 13$$
     El centro es $C(1, 3)$.
  3. Calculamos la pendiente normal:
     $$m_N = \frac{6 - 3}{-1 - 1} = \frac{3}{-2} = -\frac{3}{2}$$
  4. Escribimos la recta normal (pasa por $P(-1, 6)$ con $m_N = -1.5$):
     $$y - 6 = -\frac{3}{2}(x + 1) \implies 2y - 12 = -3x - 3 \implies 3x + 2y - 9 = 0$$
  5. Calculamos la pendiente tangente:
     $$m_T = -\frac{1}{m_N} = \frac{2}{3}$$
  6. Escribimos la recta tangente (pasa por $P(-1, 6)$ con $m_T = \frac{2}{3}$):
     $$y - 6 = \frac{2}{3}(x + 1) \implies 3y - 18 = 2x + 2 \implies 2x - 3y + 20 = 0$$

  **Respuesta:** Recta normal: $\mathbf{3x + 2y - 9 = 0}$, Recta tangente: $\mathbf{2x - 3y + 20 = 0}$.

---

### Ejercicio 4: Circunferencia por Tres Puntos
> **Justificación Pedagógica:** Una circunferencia está determinada unívocamente por tres puntos no alineados. El centro $C(h, k)$ es el punto de intersección de las mediatrices de los segmentos formados por los puntos dados.

**Desarrollo:**
Sean los puntos $A(2, 0)$, $B(2, 3)$, y $C(1, 3)$.

1. El segmento $BC$ une los puntos $(1, 3)$ y $(2, 3)$, por lo que es un segmento horizontal en la recta $y = 3$. 
   * Su punto medio es $M_{BC}\left(\frac{1+2}{2}, 3\right) = (1.5, 3)$.
   * La mediatriz del segmento horizontal $BC$ es la recta vertical que pasa por su punto medio:
     $$L_{\text{med1}}: x = 1.5$$
2. El segmento $AB$ une los puntos $(2, 0)$ y $(2, 3)$, por lo que es un segmento vertical en la recta $x = 2$.
   * Su punto medio es $M_{AB}\left(2, \frac{0+3}{2}\right) = (2, 1.5)$.
   * La mediatriz del segmento vertical $AB$ es la recta horizontal que pasa por su punto medio:
     $$L_{\text{med2}}: y = 1.5$$
3. El centro de la circunferencia es el punto de intersección de ambas mediatrices:
   $$C(h, k) = (1.5, 1.5) = \left(\frac{3}{2}, \frac{3}{2}\right)$$
4. Determinamos el radio calculando la distancia desde el centro $C$ hasta cualquiera de los puntos, por ejemplo $B(2, 3)$:
   $$R^2 = (2 - 1.5)^2 + (3 - 1.5)^2 = 0.5^2 + 1.5^2 = 0.25 + 2.25 = 2.5 = \frac{5}{2}$$
5. Planteamos la ecuación canónica:
   $$\left(x - \frac{3}{2}\right)^2 + \left(y - \frac{3}{2}\right)^2 = \frac{5}{2}$$
   O de forma general:
   $$x^2 - 3x + \frac{9}{4} + y^2 - 3y + \frac{9}{4} = \frac{10}{4} \implies x^2 + y^2 - 3x - 3y + 2 = 0$$

**Respuesta:** La ecuación canónica es $\mathbf{\left(x - \frac{3}{2}\right)^2 + \left(y - \frac{3}{2}\right)^2 = \frac{5}{2}}$, y su forma general es $\mathbf{x^2 + y^2 - 3x - 3y + 2 = 0}$.

---

### Ejercicio 5: Recta Tangente a la Circunferencia Anterior
> **Justificación Pedagógica:** Aplicamos la condición de perpendicularidad entre la recta tangente y el radio vector en el punto de contacto $B(2, 3)$.

**Desarrollo:**
* Circunferencia: $\left(x - \frac{3}{2}\right)^2 + \left(y - \frac{3}{2}\right)^2 = \frac{5}{2}$ con centro $C\left(\frac{3}{2}, \frac{3}{2}\right)$.
* Punto de tangencia: $B(2, 3)$.

1. Calculamos la pendiente del radio vector $CB$ (pendiente normal):
   $$m_N = \frac{3 - \frac{3}{2}}{2 - \frac{3}{2}} = \frac{\frac{3}{2}}{\frac{1}{2}} = 3$$
2. Obtenemos la pendiente de la recta tangente:
   $$m_T = -\frac{1}{m_N} = -\frac{1}{3}$$
3. Escribimos la ecuación de la recta tangente punto-pendiente que pasa por $B(2, 3)$:
   $$y - 3 = -\frac{1}{3}(x - 2)$$
   $$3(y - 3) = -x + 2 \implies x + 3y - 11 = 0$$

**Respuesta:** La ecuación de la recta tangente es $\mathbf{x + 3y - 11 = 0}$.

---

### Ejercicio 6: Circunferencia desde Intersección de Rectas
> **Justificación Pedagógica:** El centro $C(h, k)$ de la circunferencia es el punto de intersección del sistema lineal definido por las dos rectas.

**Desarrollo:**
Determinamos la intersección de:
$$\begin{cases} x + 3y + 3 = 0 & (1) \\ x + y + 1 = 0 & (2) \end{cases}$$

1. De (2) despejamos $x$:
   $$x = -y - 1$$
2. Sustituimos en (1):
   $$(-y - 1) + 3y + 3 = 0 \implies 2y + 2 = 0 \implies y = -1$$
3. Calculamos $x$:
   $$x = -(-1) - 1 = 0$$
   El centro es $C(0, -1)$.
4. Dado que el radio es $R = 4$, la ecuación canónica es:
   $$(x - 0)^2 + (y - (-1))^2 = 4^2 \implies x^2 + (y + 1)^2 = 16$$
   Desarrollando:
   $$x^2 + y^2 + 2y - 15 = 0$$

**Respuesta:** La ecuación canónica es $\mathbf{x^2 + (y + 1)^2 = 16}$ (general: $\mathbf{x^2 + y^2 + 2y - 15 = 0}$).

---

### Ejercicio 7: Circunferencia Tangente a una Recta
> **Justificación Pedagógica:** El radio de una circunferencia con centro $C(h, k)$ tangente a una recta $Ax + By + C_0 = 0$ es igual a la distancia perpendicular desde el centro a dicha recta:
> $$R = \frac{|A h + B k + C_0|}{\sqrt{A^2 + B^2}}$$

**Desarrollo:**
* Centro: $P(1, 3)$
* Recta: $4x + 3y - 1 = 0$

1. Calculamos la distancia:
   $$R = \frac{|4(1) + 3(3) - 1|}{\sqrt{4^2 + 3^2}} = \frac{|4 + 9 - 1|}{\sqrt{25}} = \frac{12}{5}$$
2. Planteamos la ecuación canónica:
   $$(x - 1)^2 + (y - 3)^2 = \left(\frac{12}{5}\right)^2 \implies (x - 1)^2 + (y - 3)^2 = \frac{144}{25}$$
   Multiplicando por $25$ y desarrollando obtenemos:
   $$25(x^2 - 2x + 1) + 25(y^2 - 6y + 9) = 144$$
   $$25x^2 + 25y^2 - 50x - 150y + 106 = 0$$

**Respuesta:** La ecuación ordinaria es $\mathbf{(x - 1)^2 + (y - 3)^2 = \frac{144}{25}}$.

---

### Ejercicio 8: Centro, Radio e Intersecciones con Ejes
> **Justificación Pedagógica:** Completamos cuadrados para la ecuación general dada. Para hallar las intersecciones con los ejes coordenados, planteamos de manera algebraica $y=0$ (intersección eje X) y $x=0$ (intersección eje Y).

**Desarrollo:**
Ecuación general: $x^2 + y^2 - 4x - 6y + 12 = 0$.

1. Completamos cuadrados:
   $$(x^2 - 4x + 4) - 4 + (y^2 - 6y + 9) - 9 + 12 = 0$$
   $$(x - 2)^2 + (y - 3)^2 = 1$$
   * Centro: $C(2, 3)$
   * Radio: $R = 1$
2. Intersecciones con el eje X ($y=0$):
   $$(x - 2)^2 + (0 - 3)^2 = 1 \implies (x - 2)^2 + 9 = 1 \implies (x - 2)^2 = -8$$
   Dado que no existen soluciones reales para la raíz de un número negativo, **no hay intersección con el eje X**.
3. Intersecciones con el eje Y ($x=0$):
   $$(0 - 2)^2 + (y - 3)^2 = 1 \implies 4 + (y - 3)^2 = 1 \implies (y - 3)^2 = -3$$
   De la misma forma, **no hay intersección con el eje Y**.

**Respuesta:** Ecuación canónica: $\mathbf{(x - 2)^2 + (y - 3)^2 = 1}$, con centro $\mathbf{C(2, 3)}$, radio $\mathbf{R = 1}$ y **ninguna intersección con los ejes coordenados**.

---

### Ejercicio 9: Posición Relativa - Caso 2
**Desarrollo:**
Ecuaciones del sistema:
$$\begin{cases} x^2 + y^2 - 4x + 2y - 20 = 0 & (\mathcal{C}) \\ x + y - 6 = 0 \implies y = 6 - x & (L) \end{cases}$$

1. Sustituimos $y = 6 - x$ en la circunferencia:
   $$x^2 + (6 - x)^2 - 4x + 2(6 - x) - 20 = 0$$
   $$x^2 + (36 - 12x + x^2) - 4x + (12 - 2x) - 20 = 0$$
   $$2x^2 - 18x + 28 = 0$$
2. Dividimos por $2$:
   $$x^2 - 9x + 14 = 0$$
3. Factorizamos el trinomio:
   $$(x - 2)(x - 7) = 0$$
   * Para $x_1 = 2$: $y_1 = 6 - 2 = 4 \implies P_1(2, 4)$
   * Para $x_2 = 7$: $y_2 = 6 - 7 = -1 \implies P_2(7, -1)$
   Como se obtienen dos intersecciones reales, la recta es **secante**.

**Respuesta:** La recta es **secante** y corta a la circunferencia en los puntos $\mathbf{P_1(2, 4)}$ y $\mathbf{P_2(7, -1)}$.

---

### Ejercicio 10: Posición Relativa - Caso 3
**Desarrollo:**
Ecuaciones del sistema:
$$\begin{cases} x^2 + y^2 - 2x - 3 = 0 & (\mathcal{C}) \\ 2x - y = 0 \implies y = 2x & (L) \end{cases}$$

1. Sustituimos $y = 2x$ en la circunferencia:
   $$x^2 + (2x)^2 - 2x - 3 = 0$$
   $$5x^2 - 2x - 3 = 0$$
2. Resolvemos por factorización:
   $$(5x + 3)(x - 1) = 0$$
   * Para $x_1 = 1$: $y_1 = 2(1) = 2 \implies P_1(1, 2)$
   * Para $x_2 = -\frac{3}{5}$: $y_2 = 2\left(-\frac{3}{5}\right) = -\frac{6}{5} \implies P_2\left(-\frac{3}{5}, -\frac{6}{5}\right)$
   Al tener dos soluciones distintas, es una recta **secante**.

**Respuesta:** La recta es **secante** con puntos de corte $\mathbf{P_1(1, 2)}$ y $\mathbf{P_2\left(-\frac{3}{5}, -\frac{6}{5}\right)}$.

---

### Ejercicio 11: Circunferencia Tangente
**Desarrollo:**
* Centro: $C(2, 1)$
* Recta tangente: $3x - 4y + 5 = 0$

1. Calculamos la longitud del radio $R$:
   $$R = \frac{|3(2) - 4(1) + 5|}{\sqrt{3^2 + (-4)^2}} = \frac{|6 - 4 + 5|}{5} = \frac{7}{5}$$
2. Planteamos la ecuación ordinaria:
   $$(x - 2)^2 + (y - 1)^2 = \frac{49}{25}$$

**Respuesta:** La ecuación es $\mathbf{(x - 2)^2 + (y - 1)^2 = \frac{49}{25}}$.

---

### Ejercicio 12: Circunferencia por Tres Puntos - Caso 2
**Desarrollo:**
Sean los puntos $P(2, -1)$, $A(3, 0)$ y $C(0, -2)$. Resolvemos determinando el centro a través de mediatrices.

1. Mediatriz del segmento $AC$ (con $A(3, 0)$ y $C(0, -2)$):
   * Punto medio: $M_{AC}\left(\frac{3}{2}, -1\right)$.
   * Pendiente de $AC$: $m_{AC} = \frac{0 - (-2)}{3 - 0} = \frac{2}{3}$.
   * Pendiente perpendicular: $m_{\perp 1} = -\frac{3}{2}$.
   * Ecuación mediatriz 1:
     $$y - (-1) = -\frac{3}{2}\left(x - \frac{3}{2}\right) \implies 2y + 2 = -3x + \frac{9}{2} \implies 6x + 4y - 5 = 0$$
2. Mediatriz del segmento $AP$ (con $A(3, 0)$ y $P(2, -1)$):
   * Punto medio: $M_{AP}\left(\frac{5}{2}, -\frac{1}{2}\right)$.
   * Pendiente de $AP$: $m_{AP} = \frac{-1 - 0}{2 - 3} = 1$.
   * Pendiente perpendicular: $m_{\perp 2} = -1$.
   * Ecuación mediatriz 2:
     $$y - \left(-\frac{1}{2}\right) = -1\left(x - \frac{5}{2}\right) \implies y + \frac{1}{2} = -x + \frac{5}{2} \implies x + y - 2 = 0 \implies y = 2 - x$$
3. Intersección de ambas mediatrices para hallar el centro:
   $$6x + 4(2 - x) - 5 = 0 \implies 2x + 3 = 0 \implies x = -1.5 = -\frac{3}{2}$$
   $$y = 2 - (-1.5) = 3.5 = \frac{7}{2}$$
   El centro es $C\left(-\frac{3}{2}, \frac{7}{2}\right)$.
4. Calculamos el radio al cuadrado utilizando el centro $C$ y el punto $A(3, 0)$:
   $$R^2 = \left(3 - \left(-\frac{3}{2}\right)\right)^2 + \left(0 - \frac{7}{2}\right)^2 = \left(\frac{9}{2}\right)^2 + \left(-\frac{7}{2}\right)^2 = \frac{81 + 49}{4} = \frac{130}{4} = \frac{65}{2}$$
5. Planteamos la ecuación:
   $$\left(x + \frac{3}{2}\right)^2 + \left(y - \frac{7}{2}\right)^2 = \frac{65}{2}$$

**Respuesta:** La ecuación de la circunferencia es $\mathbf{\left(x + \frac{3}{2}\right)^2 + \left(y - \frac{7}{2}\right)^2 = \frac{65}{2}}$.

---

### Ejercicio 13: Circunferencia Tangente - Caso 3
**Desarrollo:**
* Centro: $P(2, -3)$
* Recta: $3x - 4y + 5 = 0$

1. Calculamos la distancia (radio):
   $$R = \frac{|3(2) - 4(-3) + 5|}{\sqrt{3^2 + (-4)^2}} = \frac{|6 + 12 + 5|}{5} = \frac{23}{5}$$
2. Planteamos la ecuación:
   $$(x - 2)^2 + (y + 3)^2 = \frac{529}{25}$$

**Respuesta:** La ecuación es $\mathbf{(x - 2)^2 + (y + 3)^2 = \frac{529}{25}}$.

---

### Ejercicio 14: Centro por Intersección y Tangencia
**Desarrollo:**
1. Determinamos el centro intersecando las rectas de origen:
   $$\begin{cases} 3x - y - 7 = 0 \implies y = 3x - 7 \\ 2x + 3y - 1 = 0 \end{cases}$$
   Sustituyendo:
   $$2x + 3(3x - 7) - 1 = 0 \implies 11x - 22 = 0 \implies x = 2$$
   $$y = 3(2) - 7 = -1 \implies C(2, -1)$$
2. Calculamos el radio respecto a la recta $4x + 3y - 25 = 0$:
   $$R = \frac{|4(2) + 3(-1) - 25|}{\sqrt{4^2 + 3^2}} = \frac{|8 - 3 - 25|}{5} = \frac{20}{5} = 4$$
3. Planteamos la ecuación:
   $$(x - 2)^2 + (y + 1)^2 = 16$$

**Respuesta:** La ecuación ordinaria de la circunferencia es $\mathbf{(x - 2)^2 + (y + 1)^2 = 16}$.

---

### Ejercicio 15: Ecuación a partir de Centro y Punto
**Desarrollo:**
* Centro: $C(-1, 3)$
* Punto de paso: $P(3, 6)$

1. Calculamos el radio como la distancia $CP$:
   $$R = \sqrt{(3 - (-1))^2 + (6 - 3)^2} = \sqrt{4^2 + 3^2} = 5$$
2. Escribimos la ecuación:
   $$(x + 1)^2 + (y - 3)^2 = 25$$

**Respuesta:** La ecuación es $\mathbf{(x + 1)^2 + (y - 3)^2 = 25}$.

---

### Ejercicio 16: Radios a partir de Ecuaciones Generales
**Desarrollo:**

* **a) $2x^2 + 2y^2 + 8x - 12y - 10 = 0$**
  Dividimos por $2$:
  $$x^2 + y^2 + 4x - 6y - 5 = 0$$
  Completamos cuadrados:
  $$(x+2)^2 - 4 + (y-3)^2 - 9 = 5 \implies (x+2)^2 + (y-3)^2 = 18$$
  El radio es $R = \sqrt{18} = 3\sqrt{2}$.

  **Respuesta:** El radio es $\mathbf{R = 3\sqrt{2}}$.

* **b) $x^2 + y^2 - 6x + 10y - 6 = 0$**
  Completamos cuadrados:
  $$(x-3)^2 - 9 + (y+5)^2 - 25 = 6 \implies (x-3)^2 + (y+5)^2 = 40$$
  El radio es $R = \sqrt{40} = 2\sqrt{10}$.

  **Respuesta:** El radio es $\mathbf{R = 2\sqrt{10}}$.

---

### Ejercicio 17: Análisis Exhaustivo de Cónicas por Completación de Cuadrados
> **Justificación Pedagógica:** Cada ecuación cuadrática general representa una cónica. Completando cuadrados aislamos los términos principales para llevarla a su forma canónica clásica:
> * Parábola vertical: $(x-h)^2 = 4p(y-k)$ o horizontal: $(y-k)^2 = 4p(x-h)$
> * Elipse: $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$
> * Hipérbola: $\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$ o $\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1$

**Desarrollo:**

* **a) $25x^2 - 20y^2 - 100x + 240y + 320 = 0$**
  $$25(x^2 - 4x) - 20(y^2 - 12y) = -320$$
  $$25((x-2)^2 - 4) - 20((y-6)^2 - 36) = -320$$
  $$25(x-2)^2 - 100 - 20(y-6)^2 + 720 = -320 \implies 25(x-2)^2 - 20(y-6)^2 = -940$$
  Multiplicando por $-1$ y dividiendo por $940$:
  $$\frac{(y-6)^2}{47} - \frac{(x-2)^2}{37.6} = 1$$
  Representa una **hipérbola** vertical centrada en $C(2, 6)$ con $a = \sqrt{47}$ y $b = \sqrt{37.6}$.

* **b) $x^2 - 4x = 8y - 12$**
  $$(x-2)^2 - 4 = 8y - 12 \implies (x-2)^2 = 8(y-1)$$
  Representa una **parábola** vertical con vértice en $V(2, 1)$, que abre hacia arriba con parámetro $p = 2$.

* **c) $9x^2 + 16y^2 + 18x - 135 = 0$**
  $$9(x^2 + 2x) + 16y^2 = 135 \implies 9((x+1)^2 - 1) + 16y^2 = 135$$
  $$9(x+1)^2 + 16y^2 = 144 \implies \frac{(x+1)^2}{16} + \frac{y^2}{9} = 1$$
  Representa una **elipse** horizontal centrada en $C(-1, 0)$ con semieje mayor $a = 4$ y semieje menor $b = 3$.

* **d) $y^2 - 3x - 8y + 10 = 0$**
  $$(y^2 - 8y) = 3x - 10 \implies (y-4)^2 - 16 = 3x - 10 \implies (y-4)^2 = 3(x+2)$$
  Representa una **parábola** horizontal con vértice en $V(-2, 4)$, que abre hacia la derecha con parámetro $p = \frac{3}{4}$.

* **e) $6x^2 + 12x - y + 15 = 0$**
  $$6(x^2 + 2x) = y - 15 \implies 6((x+1)^2 - 1) = y - 15$$
  $$6(x+1)^2 = y - 9 \implies (x+1)^2 = \frac{1}{6}(y-9)$$
  Representa una **parábola** vertical con vértice en $V(-1, 9)$, abriendo hacia arriba con $p = \frac{1}{24}$.

* **f) $x^2 + 2y^2 + 4x + 2y - 27 = 0$**
  $$(x^2 + 4x) + 2(y^2 + y) = 27 \implies (x+2)^2 - 4 + 2\left(\left(y+\frac{1}{2}\right)^2 - \frac{1}{4}\right) = 27$$
  $$(x+2)^2 + 2\left(y+\frac{1}{2}\right)^2 - \frac{9}{2} = 27 \implies (x+2)^2 + 2\left(y+\frac{1}{2}\right)^2 = \frac{63}{2}$$
  Dividiendo por $\frac{63}{2}$:
  $$\frac{(x+2)^2}{\frac{63}{2}} + \frac{\left(y+\frac{1}{2}\right)^2}{\frac{63}{4}} = 1$$
  Representa una **elipse** horizontal con centro $C\left(-2, -\frac{1}{2}\right)$ con semiejes $a = \sqrt{\frac{63}{2}} = \frac{3\sqrt{14}}{2}$ y $b = \sqrt{\frac{63}{4}} = \frac{3\sqrt{7}}{2}$.

* **g) $x^2 - y^2 + 3x - 2y - 43 = 0$**
  $$\left(x^2 + 3x\right) - \left(y^2 + 2y\right) = 43 \implies \left(x+\frac{3}{2}\right)^2 - \frac{9}{4} - \left((y+1)^2 - 1\right) = 43$$
  $$\left(x+\frac{3}{2}\right)^2 - (y+1)^2 = 43 + \frac{5}{4} = \frac{177}{4}$$
  Dividiendo por $\frac{177}{4}$:
  $$\frac{\left(x+\frac{3}{2}\right)^2}{\frac{177}{4}} - \frac{(y+1)^2}{\frac{177}{4}} = 1$$
  Representa una **hipérbola** equilátera horizontal con centro $C\left(-\frac{3}{2}, -1\right)$ y semiejes $a = b = \frac{\sqrt{177}}{2}$.

* **h) $y^2 - 8x - 6y + 49 = 0$**
  $$(y^2 - 6y) = 8x - 49 \implies (y-3)^2 - 9 = 8x - 49 \implies (y-3)^2 = 8(x-5)$$
  Representa una **parábola** horizontal con vértice en $V(5, 3)$, abriendo hacia la derecha con $p = 2$.

* **i) $-64x^2 + 225y^2 - 256x - 3150y - 3631 = 0$**
  $$-64(x^2 + 4x) + 225(y^2 - 14y) = 3631$$
  $$-64((x+2)^2 - 4) + 225((y-7)^2 - 49) = 3631$$
  $$-64(x+2)^2 + 256 + 225(y-7)^2 - 11025 = 3631 \implies -64(x+2)^2 + 225(y-7)^2 = 14400$$
  Dividiendo por $14400$:
  $$\frac{(y-7)^2}{64} - \frac{(x+2)^2}{225} = 1$$
  Representa una **hipérbola** vertical centrada en $C(-2, 7)$ con semieje real $a = 8$ y semieje imaginario $b = 15$.

---

### Ejercicio 18: Distancia Constante como Lugar Geométrico
**Desarrollo:**
Se busca el conjunto de puntos $P(x, y)$ tales que su distancia a $Q(2, 4)$ sea $3$:
$$d(P, Q) = 3 \implies \sqrt{(x - 2)^2 + (y - 4)^2} = 3$$
Elevando al cuadrado ambos miembros:
$$(x - 2)^2 + (y - 4)^2 = 9$$
Esta relación analítica define geométricamente una circunferencia de centro $C(2, 4)$ y radio $R = 3$.

**Respuesta:** El lugar geométrico es la circunferencia de ecuación $\mathbf{(x-2)^2 + (y-4)^2 = 9}$.

---

### Ejercicio 19: Circunferencia con Centro Parcial
**Desarrollo:**
El centro es $C(-12, k)$ y el radio es $R = 13$. Dado que pasa por $P(0, 0)$:
$$d(C, P) = R \implies \sqrt{(-12 - 0)^2 + (k - 0)^2} = 13$$
$$144 + k^2 = 169 \implies k^2 = 25 \implies k = 5 \quad \text{o} \quad k = -5$$
Existen dos soluciones posibles:
1. Con centro $C_1(-12, 5)$:
   $$(x + 12)^2 + (y - 5)^2 = 169$$
2. Con centro $C_2(-12, -5)$:
   $$(x + 12)^2 + (y + 5)^2 = 169$$

**Respuesta:** Las ecuaciones posibles son $\mathbf{(x+12)^2 + (y-5)^2 = 169}$ y $\mathbf{(x+12)^2 + (y+5)^2 = 169}$.

---

### Ejercicio 20: Circunferencia por Punto y Tangente en Otro Punto
> **Justificación Pedagógica:** El centro $C(h, k)$ de la circunferencia se sitúa en la intersección de dos rectas determinantes: la recta perpendicular a la tangente en el punto de contacto $P(4, 3)$, y la mediatriz del segmento (cuerda) que une los puntos por los que pasa la circunferencia.

**Desarrollo:**
Puntos por los que pasa: $A(-2, 1)$ y $P(4, 3)$. Recta tangente en $P$: $3x - 2y - 6 = 0$.

1. **Determinación de la recta normal a la tangente en $P(4, 3)$:**
   La pendiente de la tangente $L$ es $m_L = \frac{3}{2}$. Por tanto, la pendiente del radio vector (normal) es:
   $$m_N = -\frac{2}{3}$$
   Ecuación de la recta que contiene al centro $C$:
   $$y - 3 = -\frac{2}{3}(x - 4) \implies 3y - 9 = -2x + 8 \implies 2x + 3y = 17 \quad (1)$$
2. **Determinación de la mediatriz de la cuerda $AP$:**
   * Punto medio de $AP$: $M\left(\frac{-2+4}{2}, \frac{1+3}{2}\right) = (1, 2)$.
   * Pendiente de $AP$: $m_{AP} = \frac{3-1}{4-(-2)} = \frac{2}{6} = \frac{1}{3}$.
   * Pendiente perpendicular a la cuerda: $m_{\perp} = -3$.
   * Ecuación de la mediatriz:
     $$y - 2 = -3(x - 1) \implies y - 2 = -3x + 3 \implies 3x + y = 5 \implies y = 5 - 3x \quad (2)$$
3. **Cálculo del centro $C(h, k)$ intersecando (1) y (2):**
   $$2x + 3(5 - 3x) = 17 \implies 2x + 15 - 9x = 17 \implies -7x = 2 \implies x = -\frac{2}{7}$$
   $$y = 5 - 3\left(-\frac{2}{7}\right) = 5 + \frac{6}{7} = \frac{41}{7}$$
   Luego, el centro es $C\left(-\frac{2}{7}, \frac{41}{7}\right)$.
4. **Cálculo del radio al cuadrado:**
   $$R^2 = d(C, P)^2 = \left(4 - \left(-\frac{2}{7}\right)\right)^2 + \left(3 - \frac{41}{7}\right)^2 = \left(\frac{30}{7}\right)^2 + \left(-\frac{20}{7}\right)^2 = \frac{900 + 400}{49} = \frac{1300}{49}$$
5. **Ecuación canónica final:**
   $$\left(x + \frac{2}{7}\right)^2 + \left(y - \frac{41}{7}\right)^2 = \frac{1300}{49}$$

**Respuesta:** La ecuación es $\mathbf{\left(x + \frac{2}{7}\right)^2 + \left(y - \frac{41}{7}\right)^2 = \frac{1300}{49}}$.

---

### Ejercicio 21: Conversión de Parábolas a Forma Ordinaria
**Desarrollo:**

* **a) $y - 2x^2 + 4x - 1 = 0$**
  $$2x^2 - 4x = y - 1 \implies 2(x^2 - 2x) = y - 1 \implies 2((x-1)^2 - 1) = y - 1$$
  $$2(x-1)^2 - 2 = y - 1 \implies 2(x-1)^2 = y + 1 \implies (x-1)^2 = \frac{1}{2}(y+1)$$
  * Vértice: $V(1, -1)$
  * Foco: $F\left(1, -1 + \frac{1}{8}\right) = F\left(1, -\frac{7}{8}\right)$
  * Directriz: $y = -1 - \frac{1}{8} = -\frac{9}{8}$

* **b) $-9y^2 - 8x - 3 = 0$**
  $$-9y^2 = 8x + 3 \implies y^2 = -\frac{8}{9}x - \frac{3}{9} \implies y^2 = -\frac{8}{9}\left(x + \frac{3}{8}\right)$$
  * Vértice: $V\left(-\frac{3}{8}, 0\right)$
  * Foco: $F\left(-\frac{3}{8} - \frac{2}{9}, 0\right) = F\left(-\frac{43}{72}, 0\right)$
  * Directriz: $x = -\frac{3}{8} + \frac{2}{9} = -\frac{11}{72}$

* **c) $y^2 + 2y - 4x - 7 = 0$**
  $$(y+1)^2 - 1 = 4x + 7 \implies (y+1)^2 = 4(x+2)$$
  * Vértice: $V(-2, -1)$
  * Foco: $F(-2 + 1, -1) = F(-1, -1)$
  * Directriz: $x = -2 - 1 = -3$

* **d) $x^2 + 2x - 2y + 5 = 0$**
  $$(x+1)^2 - 1 = 2y - 5 \implies (x+1)^2 = 2(y-2)$$
  * Vértice: $V(-1, 2)$
  * Foco: $F\left(-1, 2 + \frac{1}{2}\right) = F\left(-1, \frac{5}{2}\right)$
  * Directriz: $y = 2 - \frac{1}{2} = \frac{3}{2}$

* **e) $x^2 - y + 2 = 0$**
  $$x^2 = y - 2 \implies (x-0)^2 = 1(y-2)$$
  * Vértice: $V(0, 2)$
  * Foco: $F\left(0, 2 + \frac{1}{4}\right) = F\left(0, \frac{9}{4}\right)$
  * Directriz: $y = 2 - \frac{1}{4} = \frac{7}{4}$

---

### Ejercicio 22: Parábola a partir de Vértice y Directriz
**Desarrollo:**
* Vértice: $V(-1, 1)$
* Directriz: $y = 0$ (recta horizontal).

Dado que la directriz es horizontal, la parábola es de eje vertical, abriendo hacia arriba debido a que el vértice está por encima de la directriz.
1. Determinamos el parámetro $p$:
   $$p = y_V - y_d = 1 - 0 = 1$$
2. Planteamos la ecuación canónica $(x-h)^2 = 4p(y-k)$:
   $$(x + 1)^2 = 4(1)(y - 1) \implies (x + 1)^2 = 4(y - 1)$$

**Respuesta:** La ecuación canónica es $\mathbf{(x + 1)^2 = 4(y - 1)}$.

---

### Ejercicio 23: Parábola a partir de Foco y Directriz
**Desarrollo:**
* Foco: $F(3, 4)$
* Directriz: $x = 7$ (recta vertical).

Al ser la directriz vertical, la parábola es de eje horizontal.
1. El vértice $V(h, k)$ está a mitad de camino entre el foco y la directriz:
   $$h = \frac{x_F + x_d}{2} = \frac{3 + 7}{2} = 5$$
   $$k = y_F = 4 \implies V(5, 4)$$
2. El parámetro $p$ es la distancia dirigida desde el vértice al foco:
   $$p = x_F - h = 3 - 5 = -2$$
   Dado que $p < 0$, abre hacia la izquierda.
3. Planteamos la ecuación $(y-k)^2 = 4p(x-h)$:
   $$(y - 4)^2 = 4(-2)(x - 5) \implies (y - 4)^2 = -8(x - 5)$$

**Respuesta:** La ecuación canónica es $\mathbf{(y - 4)^2 = -8(x - 5)}$.

---

### Ejercicio 24: Parábola por un Punto
**Desarrollo:**
* Vértice: $V(2, 3)$
* Eje focal paralelo al eje Y (parábola vertical).
* Punto de paso: $P(4, 5)$.

1. Escribimos la estructura de la ecuación ordinaria:
   $$(x - 2)^2 = 4p(y - 3)$$
2. Sustituimos las coordenadas del punto $P(4, 5)$ para despejar el término $4p$:
   $$(4 - 2)^2 = 4p(5 - 3) \implies 4 = 4p(2) \implies 4p = 2 \implies p = \frac{1}{2}$$
3. Sustituimos $4p = 2$ en la ecuación:
   $$(x - 2)^2 = 2(y - 3)$$

**Respuesta:** La ecuación ordinaria es $\mathbf{(x - 2)^2 = 2(y - 3)}$.

---

### Ejercicio 25: Parábola de Orientación Vertical
**Desarrollo:**
* Vértice: $V(-2, 4)$
* Foco: $F(-2, 3)$

La parábola es vertical puesto que el vértice y el foco comparten la misma abscisa ($x = -2$).
1. Determinamos el parámetro $p$:
   $$p = y_F - y_V = 3 - 4 = -1$$
   La parábola abre hacia abajo.
2. Planteamos la ecuación ordinaria:
   $$(x - h)^2 = 4p(y - k) \implies (x + 2)^2 = 4(-1)(y - 4) \implies (x + 2)^2 = -4(y - 4)$$
3. La ecuación de la directriz es:
   $$y = y_V - p = 4 - (-1) = 5$$

**Respuesta:** La ecuación canónica es $\mathbf{(x + 2)^2 = -4(y - 4)}$.

---

### Ejercicio 26: Elementos de una Parábola Horizontal
**Desarrollo:**
Ecuación general: $2y^2 - 12y - 16x + 34 = 0$.

1. Dividimos toda la expresión entre $2$:
   $$y^2 - 6y - 8x + 17 = 0$$
2. Aislamos e igualamos completando cuadrados:
   $$(y^2 - 6y) = 8x - 17$$
   $$(y - 3)^2 - 9 = 8x - 17 \implies (y - 3)^2 = 8x - 8 \implies (y - 3)^2 = 8(x - 1)$$
3. Extraemos los parámetros característicos:
   * Vértice: $V(1, 3)$
   * Parámetro: $4p = 8 \implies p = 2$ (abre a la derecha).
   * Foco: $F(1 + p, 3) = F(1 + 2, 3) = F(3, 3)$
   * Directriz: $x = 1 - p \implies x = 1 - 2 = -1$

**Respuesta:** Vértice $\mathbf{V(1, 3)}$, Foco $\mathbf{F(3, 3)}$ y directriz $\mathbf{x = -1}$.

---

### Ejercicio 27: Elementos de una Parábola Vertical
**Desarrollo:**
Ecuación general: $2x^2 - 4x - 2y - 4 = 0$.

1. Dividimos por $2$:
   $$x^2 - 2x - y - 2 = 0 \implies x^2 - 2x = y + 2$$
2. Completamos cuadrados:
   $$(x - 1)^2 - 1 = y + 2 \implies (x - 1)^2 = y + 3 \implies (x - 1)^2 = 1(y + 3)$$
3. Extraemos elementos:
   * Vértice: $V(1, -3)$
   * Parámetro: $4p = 1 \implies p = \frac{1}{4}$ (abre hacia arriba).
   * Foco: $F\left(1, -3 + \frac{1}{4}\right) = F\left(1, -\frac{11}{4}\right)$
   * Directriz: $y = -3 - \frac{1}{4} = -\frac{13}{4}$

**Respuesta:** Ecuación canónica: $\mathbf{(x - 1)^2 = y + 3}$, Vértice $\mathbf{V(1, -3)}$, Foco $\mathbf{F\left(1, -\frac{11}{4}\right)}$ y directriz $\mathbf{y = -\frac{13}{4}}$.

---

### Ejercicio 28: Parábola de Vértice en Recta y por Dos Puntos
> **Justificación Pedagógica:** Usamos la parametrización de la parábola horizontal $(y - k)^2 = 4p(x - h)$. La pertenencia del vértice a la recta nos da una relación entre $h$ y $k$. Evaluando los puntos en la ecuación formamos un sistema de ecuaciones para determinar las incógnitas.

**Desarrollo:**
* Recta del vértice: $7x + 3y - 4 = 0 \implies h = \frac{4 - 3k}{7} \quad (1)$
* Puntos por los que pasa: $P_1(3, -5)$ y $P_2\left(\frac{3}{2}, 1\right)$.

1. Escribimos las ecuaciones reemplazando $P_1$ y $P_2$:
   $$(-5 - k)^2 = 4p(3 - h) \implies (k + 5)^2 = 4p(3 - h) \quad (2)$$
   $$(1 - k)^2 = 4p\left(\frac{3}{2} - h\right) \implies (k - 1)^2 = 4p\left(\frac{3}{2} - h\right) \quad (3)$$
2. Dividimos la ecuación (2) entre la (3) para eliminar la variable $4p$:
   $$\frac{(k + 5)^2}{(k - 1)^2} = \frac{3 - h}{\frac{3}{2} - h} = \frac{6 - 2h}{3 - 2h} \quad (4)$$
3. Sustituimos la relación (1) en la ecuación (4):
   $$3 - h = 3 - \frac{4 - 3k}{7} = \frac{17 + 3k}{7}$$
   $$\frac{3}{2} - h = \frac{3}{2} - \frac{4 - 3k}{7} = \frac{13 + 6k}{14}$$
   Sustituyendo estas fracciones en el cociente:
   $$\frac{3 - h}{\frac{3}{2} - h} = \frac{\frac{17 + 3k}{7}}{\frac{13 + 6k}{14}} = \frac{2(17 + 3k)}{13 + 6k} = \frac{34 + 6k}{13 + 6k}$$
4. Reemplazamos en (4) y resolvemos algebraicamente la igualdad resultante:
   $$\frac{k^2 + 10k + 25}{k^2 - 2k + 1} = \frac{6k + 34}{6k + 13}$$
   $$(k^2 + 10k + 25)(6k + 13) = (k^2 - 2k + 1)(6k + 34)$$
   $$6k^3 + 73k^2 + 280k + 325 = 6k^3 + 22k^2 - 62k + 34$$
   $$51k^2 + 342k + 291 = 0$$
   Dividiendo todo entre $3$:
   $$17k^2 + 114k + 97 = 0$$
   Factorizando, obtenemos que una solución evidente es $k = -1$ (ya que $17 - 114 + 97 = 0$):
   $$(k + 1)(17k + 97) = 0$$
   Tenemos dos casos posibles:

* **Caso 1: $k = -1$**
  * Calculamos $h$: $h = \frac{4 - 3(-1)}{7} = 1$. Vértice: $V(1, -1)$.
  * Determinamos $4p$ usando la ecuación (2):
    $$(-1 + 5)^2 = 4p(3 - 1) \implies 16 = 8p \implies 4p = 8$$
  * Ecuación canónica resultante:
    $$(y + 1)^2 = 8(x - 1)$$

* **Caso 2: $k = -\frac{97}{17}$**
  * Calculamos $h$: $h = \frac{4 - 3\left(-97/17\right)}{7} = \frac{359}{119}$. Vértice: $V\left(\frac{359}{119}, -\frac{97}{17}\right)$.
  * Determinamos $4p$ usando la ecuación (2):
    $$\left(-\frac{97}{17} + 5\right)^2 = 4p\left(3 - \frac{359}{119}\right) \implies \frac{144}{289} = 4p\left(-\frac{2}{119}\right) \implies 4p = -\frac{504}{17}$$
  * Ecuación canónica resultante:
    $$\left(y + \frac{97}{17}\right)^2 = -\frac{504}{17}\left(x - \frac{359}{119}\right)$$

**Respuesta:** Existen dos soluciones válidas: $\mathbf{(y + 1)^2 = 8(x - 1)}$ y $\mathbf{\left(y + \frac{97}{17}\right)^2 = -\frac{504}{17}\left(x - \frac{359}{119}\right)}$.

---

### Ejercicio 29: Tangencia de Recta y Circunferencia dependiente de Parámetro
> **Justificación Pedagógica:** Resolvemos por dos métodos algebraicos puros: 1) Distancia del centro a la recta igual al radio de la circunferencia. 2) Análisis del discriminante $\Delta = 0$ del sistema formado por la recta y la circunferencia.

**Desarrollo:**
* Circunferencia: $x^2 + y^2 + 6x + 2y + 6 = 0$
* Recta: $x + y + k = 0$

**Método 1 (Distancia geométrica-algebraica):**
1. Llevamos la circunferencia a su forma canónica:
   $$(x^2 + 6x + 9) - 9 + (y^2 + 2y + 1) - 1 + 6 = 0$$
   $$(x + 3)^2 + (y + 1)^2 = 4$$
   Centro: $C(-3, -1)$, Radio: $R = 2$.
2. Establecemos la condición de tangencia (distancia de $C$ a la recta $x+y+k=0$ es igual al radio $R=2$):
   $$\frac{|-3 - 1 + k|}{\sqrt{1^2 + 1^2}} = 2 \implies \frac{|k - 4|}{\sqrt{2}} = 2 \implies |k - 4| = 2\sqrt{2}$$
3. Despejamos $k$:
   $$k - 4 = \pm 2\sqrt{2} \implies k = 4 \pm 2\sqrt{2}$$

**Método 2 (Tangencia algebraica pura mediante discriminante):**
1. Despejamos $y = -x - k$ de la recta y lo sustituimos en la circunferencia:
   $$x^2 + (-x - k)^2 + 6x + 2(-x - k) + 6 = 0$$
   $$x^2 + (x^2 + 2kx + k^2) + 6x - 2x - 2k + 6 = 0$$
   $$2x^2 + (2k + 4)x + (k^2 - 2k + 6) = 0$$
2. Para que la intersección sea única (tangencia), el discriminante $\Delta$ debe ser cero:
   $$\Delta = B^2 - 4AC = 0$$
   $$(2k + 4)^2 - 4(2)(k^2 - 2k + 6) = 0$$
   $$4(k + 2)^2 - 8(k^2 - 2k + 6) = 0$$
   Dividiendo entre $4$:
   $$(k^2 + 4k + 4) - 2(k^2 - 2k + 6) = 0$$
   $$-k^2 + 8k - 8 = 0 \implies k^2 - 8k + 8 = 0$$
3. Resolvemos para $k$:
   $$k = \frac{8 \pm \sqrt{(-8)^2 - 4(1)(8)}}{2} = \frac{8 \pm \sqrt{32}}{2} = 4 \pm 2\sqrt{2}$$

**Respuesta:** El valor de $k$ debe ser $\mathbf{k = 4 \pm 2\sqrt{2}}$.

---

### Ejercicio 30: Lugar Geométrico Equidistante (Parábola)
> **Justificación Pedagógica:** Por definición, la parábola es el lugar geométrico de los puntos que equidistan de un foco $F$ y una directriz $L$. Planteamos la igualdad de distancias con expresiones algebraicas y desarrollamos.

**Desarrollo:**
* Foco: $F(2, 3)$
* Directriz: $x = 4$
Sea $Q(x, y)$ un punto perteneciente al lugar geométrico.

1. Planteamos la ecuación de distancias:
   $$d(Q, F) = d(Q, L) \implies \sqrt{(x - 2)^2 + (y - 3)^2} = |x - 4|$$
2. Elevamos al cuadrado a ambos lados:
   $$(x - 2)^2 + (y - 3)^2 = (x - 4)^2$$
3. Desarrollamos algebraicamente los términos:
   $$(x^2 - 4x + 4) + (y^2 - 6y + 9) = x^2 - 8x + 16$$
4. Simplificamos agrupando términos semejantes en la izquierda:
   $$y^2 - 6y - 4x + 13 = -8x + 16$$
   $$y^2 - 6y + 4x - 3 = 0$$

*Nota aclaratoria sobre la solución del listado:* El enunciado proporciona como respuesta de control $y^2 - 6y + 12x - 3 = 0$. Esta ecuación se obtiene únicamente si el foco es el punto $F(-2, 3)$ en lugar de $F(2, 3)$. Realizando dicha derivación:
$$\sqrt{(x + 2)^2 + (y - 3)^2} = |x - 4| \implies x^2 + 4x + 4 + y^2 - 6y + 9 = x^2 - 8x + 16 \implies y^2 - 6y + 12x - 3 = 0$$
Se incluye esta demostración doble por rigor para documentar la fe de erratas del listado de ejercicios.

**Respuesta:** La ecuación deducida a partir del enunciado literal es $\mathbf{y^2 - 6y + 4x - 3 = 0}$. Si se considera la corrección del punto focal a $F(-2, 3)$, la respuesta coincide con la de control del listado: $\mathbf{y^2 - 6y + 12x - 3 = 0}$.
