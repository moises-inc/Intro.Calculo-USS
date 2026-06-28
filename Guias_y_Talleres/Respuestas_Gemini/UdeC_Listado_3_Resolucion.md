---
id: "20260606-udec-listado3-resolucion"
title: "Resolución Completa - Listado 3 (Cálculo Diferencial e Integral)"
project: "Intro_Calculo_USS"
date: "2026-06-06T16:20:00"
last_modified: "2026-06-06T16:20:00"
type: "academic-note"
status: "completed"
priority: "high"
tags: ["#status/completed", "#project/Intro_Calculo_USS", "#course/Intro_Calculo"]
---

# Guía Pedagógica Definitiva: Listado 3 - Cálculo Diferencial e Integral
**Materia:** Cálculo Diferencial e Integral (527104)  
**Universidad:** Universidad de Concepción  
**Resolución:** Gemini Academic Assistant  

---

## Introducción Conceptual
Esta guía contiene la resolución detallada y rigurosa de cada uno de los ejercicios del **Listado 3** correspondientes al curso de Cálculo Diferencial e Integral. Para cada problema se expone una **Justificación Conceptual**, un **Desarrollo Paso a Paso** utilizando la notación algebraica y matemática de LaTeX, y cuando corresponde, la respuesta final resaltada.

---

## Ejercicios Resueltos

### Pregunta 1: Continuidad de Función a Trozos
> **Justificación Conceptual:** Para que una función $f(x)$ sea continua en todo su dominio, debe ser continua en cada uno de sus puntos. Los únicos puntos conflictivos son las fronteras de los trozos, en este caso $x = 0$. La condición de continuidad en $x = 0$ requiere que:
> $$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0)$$
> Calculamos los límites laterales por separado y los igualamos a $f(0) = 1$.

**Desarrollo:**
La función está dada por:
$$f(x) = \begin{cases} \frac{2b + ax^2 - 2b\cos(x^2)}{x^2} & \text{si } x < 0 \\ 1 & \text{si } x = 0 \\ \frac{a\sqrt{x}\sin(\sqrt{x}) + 2bx}{x} & \text{si } x > 0 \end{cases}$$

1. **Límite por la izquierda ($x \to 0^-$):**
   Usamos el primer trozo:
   $$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} \frac{2b + ax^2 - 2b\cos(x^2)}{x^2}$$
   Podemos separar la fracción en dos partes:
   $$\lim_{x \to 0^-} \left( \frac{2b(1 - \cos(x^2))}{x^2} + \frac{ax^2}{x^2} \right) = \lim_{x \to 0^-} \left( 2b \cdot \frac{1 - \cos(x^2)}{x^2} + a \right)$$
   Haciendo la sustitución $u = x^2$, cuando $x \to 0^-$, tenemos $u \to 0^+$. Por lo tanto:
   $$\lim_{u \to 0^+} \frac{1 - \cos(u)}{u} = \lim_{u \to 0^+} \frac{1 - \cos(u)}{u} \cdot \frac{1 + \cos(u)}{1 + \cos(u)} = \lim_{u \to 0^+} \frac{\sin^2(u)}{u(1 + \cos(u))} = \lim_{u \to 0^+} \left( \frac{\sin(u)}{u} \cdot \frac{\sin(u)}{1 + \cos(u)} \right)$$
   Utilizando el límite notable $\lim_{u \to 0} \frac{\sin(u)}{u} = 1$:
   $$\lim_{u \to 0^+} \frac{1 - \cos(u)}{u} = 1 \cdot \frac{0}{1 + 1} = 0$$
   De este modo, el límite por la izquierda es:
   $$\lim_{x \to 0^-} f(x) = 2b(0) + a = a$$
   Para asegurar la continuidad por la izquierda, imponemos:
   $$a = f(0) \implies \mathbf{a = 1}$$

2. **Límite por la derecha ($x \to 0^+$):**
   Usamos el tercer trozo:
   $$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \frac{a\sqrt{x}\sin(\sqrt{x}) + 2bx}{x}$$
   Dado que $x > 0$, podemos dividir numerador y denominador por $x$:
   $$\lim_{x \to 0^+} \left( \frac{a\sqrt{x}\sin(\sqrt{x})}{x} + \frac{2bx}{x} \right) = \lim_{x \to 0^+} \left( a \frac{\sin(\sqrt{x})}{\sqrt{x}} + 2b \right)$$
   Realizando el cambio de variable $v = \sqrt{x}$, cuando $x \to 0^+$, tenemos $v \to 0^+$. Así, utilizando el límite notable $\lim_{v \to 0} \frac{\sin(v)}{v} = 1$:
   $$\lim_{x \to 0^+} f(x) = a(1) + 2b = a + 2b$$
   Para asegurar la continuidad por la derecha, imponemos:
   $$a + 2b = f(0) \implies a + 2b = 1$$

3. **Resolución del sistema de ecuaciones:**
   Sustituyendo $a = 1$ en la segunda ecuación:
   $$1 + 2b = 1 \implies 2b = 0 \implies \mathbf{b = 0}$$

**Respuesta:**
Los valores requeridos para que la función sea continua en todo su dominio son **$a = 1$ y $b = 0$**.

---

### Pregunta 2: Aplicación del Teorema de Bolzano
> **Justificación Conceptual:** El Teorema de Bolzano establece que si una función $f(x)$ es continua en un intervalo cerrado $[a, b]$ y toma valores de signos opuestos en sus extremos ($f(a) \cdot f(b) < 0$), entonces existe al menos un punto $c \in (a, b)$ tal que $f(c) = 0$.

#### (a) $\ln(x) - x + \sqrt{x} = 0$ en $I = [2, 4]$
**Desarrollo:**
Definimos la función auxiliar:
$$f(x) = \ln(x) - x + \sqrt{x}$$
- **Continuidad:** $f(x)$ es una suma y diferencia de funciones continuas ($\ln(x)$ es continua para $x > 0$, $x$ es continua en $\mathbb{R}$, y $\sqrt{x}$ es continua para $x \geq 0$). Por lo tanto, $f(x)$ es continua en el intervalo cerrado $[2, 4]$.
- **Evaluación en los extremos:**
  - En $x = 2$:
    $$f(2) = \ln(2) - 2 + \sqrt{2} \approx 0.6931 - 2 + 1.4142 = 0.1073 > 0$$
  - En $x = 4$:
    $$f(4) = \ln(4) - 4 + \sqrt{4} = \ln(4) - 4 + 2 = \ln(4) - 2 \approx 1.3863 - 2 = -0.6137 < 0$$
Como $f(2) > 0$ y $f(4) < 0$, existe al menos un $c \in (2, 4)$ tal que $f(c) = 0$.

**Respuesta:**
Queda demostrado que la ecuación posee al menos una solución en $[2, 4]$.

#### (b) $\sin(x) + x = x^2$ en $I = [1, 3]$
**Desarrollo:**
Reescribimos la ecuación como $x^2 - x - \sin(x) = 0$ y definimos:
$$g(x) = x^2 - x - \sin(x)$$
- **Continuidad:** $g(x)$ es continua en $[1, 3]$ al ser la suma de una función polinómica y la función trigonométrica seno (ambas continuas en toda la recta real).
- **Evaluación en los extremos:**
  - En $x = 1$:
    $$g(1) = 1^2 - 1 - \sin(1) = -\sin(1)$$
    Como $1$ radián está en el primer cuadrante ($0 < 1 < \pi/2$), $\sin(1) > 0$, por lo que $g(1) \approx -0.8415 < 0$.
  - En $x = 3$:
    $$g(3) = 3^2 - 3 - \sin(3) = 6 - \sin(3)$$
    Como el rango de la función seno es $[-1, 1]$, sabemos que $\sin(3) \leq 1$, por lo que $g(3) \geq 5 > 0$ (más precisamente, $g(3) \approx 5.8589 > 0$).
Como $g(1) < 0$ y $g(3) > 0$, existe al menos un $c \in (1, 3)$ tal que $g(c) = 0$.

**Respuesta:**
Queda demostrado que la ecuación posee al menos una solución en $[1, 3]$.

---

### Pregunta 3: Cálculo y Análisis de Límites
> **Justificación Conceptual:** Resolvemos límites al infinito utilizando técnicas de factorización del término dominante y racionalización (uso del conjugado) para resolver formas indeterminadas de tipo $\frac{\infty}{\infty}$ o $\infty - \infty$.

#### (a) $\lim_{x \to +\infty} \frac{2x^3 - x^2 + x + 3}{10x^3 + x^2 + 7}$
**Desarrollo:**
Factorizamos la potencia dominante $x^3$ en el numerador y el denominador:
$$\lim_{x \to +\infty} \frac{x^3 \left(2 - \frac{1}{x} + \frac{1}{x^2} + \frac{3}{x^3}\right)}{x^3 \left(10 + \frac{1}{x} + \frac{7}{x^3}\right)} = \lim_{x \to +\infty} \frac{2 - \frac{1}{x} + \frac{1}{x^2} + \frac{3}{x^3}}{10 + \frac{1}{x} + \frac{7}{x^3}}$$
Sabiendo que $\lim_{x \to +\infty} \frac{1}{x^k} = 0$ para todo $k \geq 1$:
$$\frac{2 - 0 + 0 + 0}{10 + 0 + 0} = \frac{2}{10} = \frac{1}{5}$$

**Respuesta:**
El límite existe y su valor es **$\frac{1}{5}$**.

#### (b) $\lim_{x \to -\infty} (x^3 - 4x^2 + x - 1)$
**Desarrollo:**
Factorizamos el término dominante $x^3$:
$$\lim_{x \to -\infty} x^3 \left(1 - \frac{4}{x} + \frac{1}{x^2} - \frac{1}{x^3}\right)$$
Evaluamos el comportamiento de cada término a medida que $x \to -\infty$:
- El paréntesis tiende a $1 - 0 + 0 - 0 = 1$.
- El término $x^3$ tiende a $-\infty$.
$$\lim_{x \to -\infty} (x^3 - 4x^2 + x - 1) = (-\infty) \cdot 1 = -\infty$$

**Respuesta:**
El límite no existe en los números reales ya que diverge a **$-\infty$**.

#### (c) $\lim_{x \to -\infty} \frac{\sqrt{-x + 1}}{\sqrt{-x} + 1}$
**Desarrollo:**
Dado que $x \to -\infty$, el término $-x$ es positivo. Hacemos el cambio de variable $y = -x$, de modo que $y \to +\infty$:
$$\lim_{y \to +\infty} \frac{\sqrt{y + 1}}{\sqrt{y} + 1}$$
Dividimos el numerador y el denominador por $\sqrt{y}$:
$$\lim_{y \to +\infty} \frac{\frac{\sqrt{y + 1}}{\sqrt{y}}}{\frac{\sqrt{y} + 1}{\sqrt{y}}} = \lim_{y \to +\infty} \frac{\sqrt{1 + \frac{1}{y}}}{1 + \frac{1}{\sqrt{y}}}$$
Dado que $\lim_{y \to +\infty} \frac{1}{y} = 0$ y $\lim_{y \to +\infty} \frac{1}{\sqrt{y}} = 0$:
$$\frac{\sqrt{1 + 0}}{1 + 0} = 1$$

**Respuesta:**
El límite existe y su valor es **$1$**.

#### (d) $\lim_{x \to +\infty} (\sqrt{x^2 + 1} - x)$
**Desarrollo:**
Multiplicamos y dividimos por la expresión conjugada:
$$\lim_{x \to +\infty} (\sqrt{x^2 + 1} - x) \cdot \frac{\sqrt{x^2 + 1} + x}{\sqrt{x^2 + 1} + x} = \lim_{x \to +\infty} \frac{(x^2 + 1) - x^2}{\sqrt{x^2 + 1} + x} = \lim_{x \to +\infty} \frac{1}{\sqrt{x^2 + 1} + x}$$
Como el denominador tiende a $+\infty$:
$$\frac{1}{+\infty} = 0$$

**Respuesta:**
El límite existe y su valor es **$0$**.

#### (e) $\lim_{x \to +\infty} \frac{e^x + \sin(x)}{e^x + \cos(x)}$
**Desarrollo:**
Dividimos el numerador y el denominador por $e^x$:
$$\lim_{x \to +\infty} \frac{1 + \frac{\sin(x)}{e^x}}{1 + \frac{\cos(x)}{e^x}}$$
Como las funciones $\sin(x)$ y $\cos(x)$ están acotadas en $[-1, 1]$, y $\lim_{x \to +\infty} e^x = +\infty$, por el teorema de la función acotada por una función que tiende a cero (Teorema del Sándwich), se tiene:
$$\lim_{x \to +\infty} \frac{\sin(x)}{e^x} = 0 \quad \text{y} \quad \lim_{x \to +\infty} \frac{\cos(x)}{e^x} = 0$$
Por lo tanto:
$$\frac{1 + 0}{1 + 0} = 1$$

**Respuesta:**
El límite existe y su valor es **$1$**.

#### (f) $\lim_{x \to +\infty} \frac{\sqrt{x}}{\sqrt{x + \sqrt{x}}}$
**Desarrollo:**
Para $x > 0$, dividimos tanto el numerador como el denominador por $\sqrt{x}$:
$$\lim_{x \to +\infty} \frac{\frac{\sqrt{x}}{\sqrt{x}}}{\sqrt{\frac{x + \sqrt{x}}{x}}} = \lim_{x \to +\infty} \frac{1}{\sqrt{1 + \frac{\sqrt{x}}{x}}} = \lim_{x \to +\infty} \frac{1}{\sqrt{1 + \frac{1}{\sqrt{x}}}}$$
Como $\lim_{x \to +\infty} \frac{1}{\sqrt{x}} = 0$:
$$\frac{1}{\sqrt{1 + 0}} = 1$$
*(Nota: Si el límite fuera hacia $x \to 0^+$, se resolvería de forma similar, obteniendo $\lim_{x \to 0^+} \frac{1}{\sqrt{1 + x^{-1/2}}} = 0$).*

**Respuesta:**
El límite cuando $x \to +\infty$ existe y su valor es **$1$**.

#### (g) $\lim_{x \to \pm\infty} \left(\sqrt{x^2 + x} - \sqrt{x^2 - 5}\right)$
**Desarrollo:**
Multiplicamos y dividimos por el conjugado:
$$\lim_{x \to \pm\infty} \frac{(x^2 + x) - (x^2 - 5)}{\sqrt{x^2 + x} + \sqrt{x^2 - 5}} = \lim_{x \to \pm\infty} \frac{x + 5}{\sqrt{x^2 + x} + \sqrt{x^2 - 5}}$$

1. **Para $x \to +\infty$:**
   Factorizamos $x$ en el numerador y en el denominador (donde $\sqrt{x^2} = |x| = x$):
   $$\lim_{x \to +\infty} \frac{x\left(1 + \frac{5}{x}\right)}{x\left(\sqrt{1 + \frac{1}{x}} + \sqrt{1 - \frac{5}{x^2}}\right)} = \frac{1 + 0}{\sqrt{1 + 0} + \sqrt{1 - 0}} = \frac{1}{2}$$

2. **Para $x \to -\infty$:**
   Haciendo $y = -x \implies y \to +\infty$:
   $$\lim_{y \to +\infty} \frac{-y + 5}{\sqrt{y^2 - y} + \sqrt{y^2 - 5}} = \lim_{y \to +\infty} \frac{y\left(-1 + \frac{5}{y}\right)}{y\left(\sqrt{1 - \frac{1}{y}} + \sqrt{1 - \frac{5}{y^2}}\right)} = \frac{-1 + 0}{\sqrt{1 - 0} + \sqrt{1 - 0}} = -\frac{1}{2}$$

**Respuesta:**
El límite es **$\frac{1}{2}$** cuando $x \to +\infty$, y **$-\frac{1}{2}$** cuando $x \to -\infty$.

#### (h) $\lim_{x \to -\infty} \frac{3x^2 - 3x - 1}{\sqrt{x^4 + 1}}$
**Desarrollo:**
Factorizamos la potencia dominante en el numerador y extraemos el término dominante del radical en el denominador. Como $x \to -\infty$, $\sqrt{x^4} = x^2$:
$$\lim_{x \to -\infty} \frac{x^2 \left(3 - \frac{3}{x} - \frac{1}{x^2}\right)}{\sqrt{x^4 \left(1 + \frac{1}{x^4}\right)}} = \lim_{x \to -\infty} \frac{x^2 \left(3 - \frac{3}{x} - \frac{1}{x^2}\right)}{x^2 \sqrt{1 + \frac{1}{x^4}}} = \lim_{x \to -\infty} \frac{3 - \frac{3}{x} - \frac{1}{x^2}}{\sqrt{1 + \frac{1}{x^4}}}$$
Evaluando los límites cuando $x \to -\infty$:
$$\frac{3 - 0 - 0}{\sqrt{1 + 0}} = 3$$

**Respuesta:**
El límite existe y su valor es **$3$**.

#### (i) $\lim_{x \to \infty} \left(x^2 - \sqrt{x^4 + 7x^2 + 1}\right)$
**Desarrollo:**
Multiplicamos y dividimos por el conjugado:
$$\lim_{x \to \infty} \frac{x^4 - (x^4 + 7x^2 + 1)}{x^2 + \sqrt{x^4 + 7x^2 + 1}} = \lim_{x \to \infty} \frac{-7x^2 - 1}{x^2 + \sqrt{x^4\left(1 + \frac{7}{x^2} + \frac{1}{x^4}\right)}}$$
Factorizamos $x^2$ en el denominador, notando que $\sqrt{x^4} = x^2$:
$$\lim_{x \to \infty} \frac{x^2\left(-7 - \frac{1}{x^2}\right)}{x^2\left(1 + \sqrt{1 + \frac{7}{x^2} + \frac{1}{x^4}}\right)} = \lim_{x \to \infty} \frac{-7 - \frac{1}{x^2}}{1 + \sqrt{1 + \frac{7}{x^2} + \frac{1}{x^4}}}$$
Tomando el límite:
$$\frac{-7 - 0}{1 + \sqrt{1 + 0 + 0}} = -\frac{7}{2}$$

**Respuesta:**
El límite existe y vale **$-\frac{7}{2}$**.

#### (j) $\lim_{x \to -\infty} \left(\sqrt{x^6 + x^3} - \sqrt{x^6 - x^2}\right)$
**Desarrollo:**
Multiplicamos por el conjugado:
$$\lim_{x \to -\infty} \frac{(x^6 + x^3) - (x^6 - x^2)}{\sqrt{x^6 + x^3} + \sqrt{x^6 - x^2}} = \lim_{x \to -\infty} \frac{x^3 + x^2}{\sqrt{x^6 + x^3} + \sqrt{x^6 - x^2}}$$
Sea $y = -x$, por lo que $y \to +\infty$:
$$\lim_{y \to +\infty} \frac{-y^3 + y^2}{\sqrt{y^6 - y^3} + \sqrt{y^6 - y^2}}$$
Para $y > 0$, factorizamos $y^6$ dentro de las raíces, resultando en $\sqrt{y^6} = y^3$:
$$\lim_{y \to +\infty} \frac{y^3\left(-1 + \frac{1}{y}\right)}{y^3\left(\sqrt{1 - \frac{1}{y^3}} + \sqrt{1 - \frac{1}{y^4}}\right)} = \lim_{y \to +\infty} \frac{-1 + \frac{1}{y}}{\sqrt{1 - \frac{1}{y^3}} + \sqrt{1 - \frac{1}{y^4}}}$$
Tomando el límite:
$$\frac{-1 + 0}{\sqrt{1 - 0} + \sqrt{1 - 0}} = -\frac{1}{2}$$

**Respuesta:**
El límite existe y vale **$-\frac{1}{2}$**.

#### (k) $\lim_{x \to +\infty} \frac{3x + 5}{\sqrt{9x^2 - 7}}$
**Desarrollo:**
Para $x > 0$, factorizamos $x^2$ dentro de la raíz: $\sqrt{9x^2 - 7} = x\sqrt{9 - \frac{7}{x^2}}$:
$$\lim_{x \to +\infty} \frac{x\left(3 + \frac{5}{x}\right)}{x\sqrt{9 - \frac{7}{x^2}}} = \lim_{x \to +\infty} \frac{3 + \frac{5}{x}}{\sqrt{9 - \frac{7}{x^2}}}$$
Tomando el límite:
$$\frac{3 + 0}{\sqrt{9 - 0}} = \frac{3}{3} = 1$$

**Respuesta:**
El límite existe y su valor es **$1$**.

#### (l) $\lim_{x \to +\infty} \left( \frac{|2x - 15|}{x - 1} - 7 \right)$
**Desarrollo:**
Como $x \to +\infty$, para valores de $x > 7.5$ el término $2x - 15$ es estrictamente positivo, de modo que $|2x - 15| = 2x - 15$:
$$\lim_{x \to +\infty} \left( \frac{2x - 15}{x - 1} - 7 \right) = \lim_{x \to +\infty} \frac{2x - 15 - 7(x - 1)}{x - 1} = \lim_{x \to +\infty} \frac{-5x - 8}{x - 1}$$
Dividiendo por $x$ numerador y denominador:
$$\lim_{x \to +\infty} \frac{-5 - \frac{8}{x}}{1 - \frac{1}{x}} = -5$$
*(Nota: Si $x \to -\infty$, entonces $|2x-15| = 15-2x$, resultando en un límite de $-9$).*

**Respuesta:**
El límite cuando $x \to +\infty$ es **$-5$**.

---

### Pregunta 4: Determinación de Parámetros en Límites
> **Justificación Conceptual:** Analizamos el comportamiento asintótico de una función que depende de un parámetro real $a$. Para que la función converja a un valor real finito, los términos de mayor grado en el numerador y denominador deben cancelarse o tener el mismo grado.

**Desarrollo:**
La función está definida por:
$$f(x) = \frac{x^2 - 2ax^3}{x^2 + 2} + \frac{6x + 2x^2}{x + 3}$$
Analizamos la segunda fracción. Observamos que podemos factorizar el numerador:
$$2x^2 + 6x = 2x(x + 3)$$
De este modo, para cualquier $x \neq -3$, podemos simplificar:
$$\frac{2x(x+3)}{x+3} = 2x$$
Entonces, el límite a analizar cuando $x \to +\infty$ es:
$$f(x) = \frac{x^2 - 2ax^3}{x^2 + 2} + 2x = \frac{x^2 - 2ax^3 + 2x(x^2 + 2)}{x^2 + 2} = \frac{(2 - 2a)x^3 + x^2 + 4x}{x^2 + 2}$$

Analizamos los casos según el coeficiente del término cúbico $(2 - 2a)$:

#### (a) $\lim_{x \to +\infty} f(x) = L \in \mathbb{R}$
Para que el límite sea un número real finito, el grado del numerador no debe superar el grado del denominador (que es $2$). Por tanto, el término en $x^3$ debe anularse:
$$2 - 2a = 0 \implies \mathbf{a = 1}$$
Si $a = 1$, la función queda:
$$f(x) = \frac{x^2 + 4x}{x^2 + 2} \implies \lim_{x \to +\infty} f(x) = 1$$
**Respuesta:** El valor es **$a = 1$** (con $L = 1$).

#### (b) $\lim_{x \to +\infty} f(x) = +\infty$
Para que el límite sea $+\infty$, el término cúbico debe dominar positivamente:
$$2 - 2a > 0 \implies \mathbf{a < 1}$$
**Respuesta:** El conjunto es **$a \in (-\infty, 1)$**.

#### (c) $\lim_{x \to +\infty} f(x) = -\infty$
Para que el límite sea $-\infty$, el término cúbico debe dominar negativamente:
$$2 - 2a < 0 \implies \mathbf{a > 1}$$
**Respuesta:** El conjunto es **$a \in (1, +\infty)$**.

---

### Pregunta 5: Límites con Potencia Variable en el Denominador
> **Justificación Conceptual:** Evaluamos el límite de una función racional donde el grado del denominador $n$ varía en $\mathbb{N}_{\geq 2}$. Comparamos los grados del numerador ($3$) y del denominador ($n$).

**Desarrollo:**
Queremos calcular:
$$L = \lim_{x \to +\infty} \frac{-6x^3 - 3x^2 - 24}{3x^n + x - 11}$$
Dividimos tanto el numerador como el denominador por sus respectivos términos principales:
$$L = \lim_{x \to +\infty} \frac{-6x^3\left(1 + \frac{1}{2x} + \frac{4}{x^3}\right)}{3x^n\left(1 + \frac{1}{3x^{n-1}} - \frac{11}{3x^n}\right)} = \lim_{x \to +\infty} \left( -2 x^{3-n} \cdot \frac{1 + \frac{1}{2x} + \frac{4}{x^3}}{1 + \frac{1}{3x^{n-1}} - \frac{11}{3x^n}} \right)$$
Dado que la fracción de la derecha siempre tiende a $1$, el límite depende enteramente de $x^{3-n}$:

1. **Si $n = 2$:**
   $$3 - n = 1 \implies \lim_{x \to +\infty} (-2x) = -\infty$$
2. **Si $n = 3$:**
   $$3 - n = 0 \implies \lim_{x \to +\infty} (-2) = -2$$
3. **Si $n \geq 4$:**
   $$3 - n < 0 \implies \lim_{x \to +\infty} \frac{-2}{x^{n-3}} = 0$$

**Respuesta:**
- Para $n = 2$, el límite es **$-\infty$**.
- Para $n = 3$, el límite es **$-2$**.
- Para $n \geq 4$, el límite es **$0$**.

---

### Pregunta 6: Condición de Asíntota Oblicua
> **Justificación Conceptual:** Por definición, la recta $y = mx + n$ es una asíntota oblicua de la curva $y = f(x)$ si $\lim_{x \to +\infty} [f(x) - (mx + n)] = 0$. Resolvemos directamente esta igualdad para hallar el parámetro $a$.

**Desarrollo:**
Se nos pide que:
$$\lim_{x \to +\infty} \left[ \frac{6x^2 - 1}{2x + a} - (3x + 2) \right] = 0$$
Realizamos la resta algebraica:
$$\frac{6x^2 - 1 - (3x + 2)(2x + a)}{2x + a} = \frac{6x^2 - 1 - (6x^2 + 3ax + 4x + 2a)}{2x + a} = \frac{-(3a + 4)x - (2a + 1)}{2x + a}$$
Calculamos el límite al infinito factorizando $x$:
$$\lim_{x \to +\infty} \frac{x \left( -(3a + 4) - \frac{2a + 1}{x} \right)}{x \left( 2 + \frac{a}{x} \right)} = \frac{-(3a + 4)}{2}$$
Igualando este valor a $0$:
$$-(3a + 4) = 0 \implies 3a = -4 \implies \mathbf{a = -\frac{4}{3}}$$

**Respuesta:**
El valor de $a$ debe ser **$-\frac{4}{3}$**.

---

### Pregunta 7: Estudio de Asíntotas y Gráficos
> **Justificación Conceptual:**
> - **Asíntota Vertical (A.V.):** $x = x_0$ si $\lim_{x \to x_0^{\pm}} f(x) = \pm\infty$.
> - **Asíntota Horizontal (A.H.):** $y = L$ si $\lim_{x \to \pm\infty} f(x) = L$.
> - **Asíntota Oblicua (A.O.):** $y = mx + n$ con $m = \lim_{x \to \pm\infty} \frac{f(x)}{x} \neq 0$ y $n = \lim_{x \to \pm\infty} [f(x) - mx]$.

#### (a) $f(x) = \frac{x + 2}{x^2 - 2x - 3}$
- **Dom($f$):** $x^2 - 2x - 3 = (x-3)(x+1) \neq 0 \implies \mathbb{R} \setminus \{-1, 3\}$.
- **A.V.:**
  - $\lim_{x \to 3^{\pm}} \frac{x+2}{(x-3)(x+1)} = \pm\infty \implies \mathbf{x = 3}$ es A.V.
  - $\lim_{x \to -1^{\pm}} \frac{x+2}{(x-3)(x+1)} = \mp\infty \implies \mathbf{x = -1}$ es A.V.
- **A.H.:** $\lim_{x \to \pm\infty} f(x) = 0 \implies \mathbf{y = 0}$ es A.H.
- **A.O.:** No existen (al haber A.H. en ambos extremos).

#### (b) $f(x) = \frac{1}{x + \frac{1}{|x|}}$
- **Dom($f$):** 
  La función está indefinida si el denominador principal es cero, o si el término $|x|$ en el denominador de la fracción interna es cero.
  - Para $x = 0$, la expresión $\frac{1}{|x|}$ está indefinida.
  - Para $x > 0$: $x + \frac{1}{x} = 0 \implies x^2 + 1 = 0$, que no posee soluciones reales.
  - Para $x < 0$: $x - \frac{1}{x} = 0 \implies x^2 - 1 = 0 \implies x = -1$ (ya que $x < 0$).
  Por tanto, el dominio es $\text{Dom}(f) = \mathbb{R} \setminus \{-1, 0\}$.
- **A.V.:**
  Analizamos los límites laterales en los puntos de exclusión del dominio:
  - En $x = -1$:
    $$\lim_{x \to -1^+} \frac{1}{x - \frac{1}{x}} = \lim_{x \to -1^+} \frac{x}{x^2 - 1} = +\infty \quad (\text{debido a que } x^2 - 1 \to 0^- \text{ y } x \to -1)$$
    $$\lim_{x \to -1^-} \frac{1}{x - \frac{1}{x}} = \lim_{x \to -1^-} \frac{x}{x^2 - 1} = -\infty \quad (\text{debido a que } x^2 - 1 \to 0^+ \text{ y } x \to -1)$$
    Por lo tanto, la recta **$x = -1$** es una asíntota vertical.
  - En $x = 0$:
    $$\lim_{x \to 0^+} \frac{1}{x + \frac{1}{x}} = \lim_{x \to 0^+} \frac{x}{x^2 + 1} = 0$$
    $$\lim_{x \to 0^-} \frac{1}{x - \frac{1}{x}} = \lim_{x \to 0^-} \frac{x}{x^2 - 1} = 0$$
    Como ambos límites laterales son finitos (e iguales a $0$), $x = 0$ no es una asíntota vertical (es una discontinuidad evitable).
- **A.H.:**
  - Para $x \to +\infty$:
    $$\lim_{x \to +\infty} \frac{1}{x + \frac{1}{x}} = 0 \implies \mathbf{y = 0} \text{ es A.H. en } +\infty$$
  - Para $x \to -\infty$:
    $$\lim_{x \to -\infty} \frac{1}{x - \frac{1}{x}} = 0 \implies \mathbf{y = 0} \text{ es A.H. en } -\infty$$
- **A.O.:** No existen.



#### (c) $f(x) = \frac{\sqrt{x^2 - 1} + x}{\sqrt{x^2 - 1}} = 1 + \frac{x}{\sqrt{x^2 - 1}}$
- **Dom($f$):** $x^2 - 1 > 0 \implies (-\infty, -1) \cup (1, +\infty)$.
- **A.V.:**
  - $\lim_{x \to 1^+} \left(1 + \frac{x}{\sqrt{x^2-1}}\right) = +\infty \implies \mathbf{x = 1}$ es A.V.
  - $\lim_{x \to -1^-} \left(1 + \frac{x}{\sqrt{x^2-1}}\right) = -\infty \implies \mathbf{x = -1}$ es A.V.
- **A.H.:**
  - Como $x \to +\infty$: $\lim_{x \to +\infty} \left(1 + \frac{x}{x\sqrt{1 - 1/x^2}}\right) = 2 \implies \mathbf{y = 2}$ es A.H.
  - Como $x \to -\infty$: $\lim_{x \to -\infty} \left(1 + \frac{x}{-x\sqrt{1 - 1/x^2}}\right) = 0 \implies \mathbf{y = 0}$ es A.H.
- **A.O.:** No existen.

#### (d) $f(x) = -\frac{5x}{(x^2 - 3)^2}$
- **Dom($f$):** $\mathbb{R} \setminus \{-\sqrt{3}, \sqrt{3}\}$.
- **A.V.:**
  - $\lim_{x \to \sqrt{3}} f(x) = -\infty \implies \mathbf{x = \sqrt{3}}$ es A.V.
  - $\lim_{x \to -\sqrt{3}} f(x) = +\infty \implies \mathbf{x = -\sqrt{3}}$ es A.V.
- **A.H.:** $\lim_{x \to \pm\infty} f(x) = 0 \implies \mathbf{y = 0}$ es A.H.
- **A.O.:** No existen.

#### (e) $f(x) = \sqrt{\frac{x^4 + 1}{x^2 - 1}}$
- **Dom($f$):** $x^2 - 1 > 0 \implies (-\infty, -1) \cup (1, +\infty)$.
- **A.V.:**
  - $\lim_{x \to 1^+} f(x) = +\infty \implies \mathbf{x = 1}$ es A.V.
  - $\lim_{x \to -1^-} f(x) = +\infty \implies \mathbf{x = -1}$ es A.V.
- **A.H.:** $\lim_{x \to \pm\infty} f(x) = +\infty \implies$ No hay A.H.
- **A.O.:**
  - Para $x \to +\infty$:
    $$m = \lim_{x \to +\infty} \frac{\sqrt{x^4+1}}{x\sqrt{x^2-1}} = 1, \quad n = \lim_{x \to +\infty} \left(\sqrt{\frac{x^4+1}{x^2-1}} - x\right) = 0 \implies \mathbf{y = x}$$
  - Para $x \to -\infty$:
    $$m = \lim_{x \to -\infty} \frac{\sqrt{x^4+1}}{x\sqrt{x^2-1}} = -1, \quad n = \lim_{x \to -\infty} \left(\sqrt{\frac{x^4+1}{x^2-1}} + x\right) = 0 \implies \mathbf{y = -x}$$

#### (f) $f(x) = \frac{1 - x^4}{x^3 - 1}$
- **Dom($f$):** $\mathbb{R} \setminus \{1\}$.
- **Simplificación:** Para $x \neq 1$:
  $$f(x) = \frac{-(x^2+1)(x^2-1)}{(x-1)(x^2+x+1)} = \frac{-(x^2+1)(x+1)}{x^2+x+1} = \frac{-x^3 - x^2 - x - 1}{x^2+x+1} = -x - \frac{1}{x^2+x+1}$$
- **A.V.:** $\lim_{x \to 1} f(x) = -\frac{4}{3}$ (discontinuidad evitable, no hay A.V.).
- **A.H.:** No existen.
- **A.O.:** Dado que $f(x) - (-x) = -\frac{1}{x^2+x+1} \to 0$ cuando $x \to \pm\infty$, la recta **$y = -x$** es A.O.

#### (g) $f(x) = \frac{x^2 - 1}{x^2 - 2|x|}$
- **Dom($f$):** $x^2 - 2|x| = |x|(|x|-2) \neq 0 \implies \mathbb{R} \setminus \{-2, 0, 2\}$.
- **A.V.:**
  - $\lim_{x \to 0} f(x) = \frac{-1}{0^-} = +\infty \implies \mathbf{x = 0}$ es A.V.
  - $\lim_{x \to 2^{\pm}} f(x) = \frac{3}{2 \cdot 0^{\pm}} = \pm\infty \implies \mathbf{x = 2}$ es A.V.
  - Por simetría par: $\mathbf{x = -2}$ es A.V.
- **A.H.:** $\lim_{x \to \pm\infty} \frac{x^2 - 1}{x^2 - 2|x|} = 1 \implies \mathbf{y = 1}$ es A.H.
- **A.O.:** No existen.

#### (h) $g(x) = \begin{cases} \frac{2x^2 + 1}{2x^3 + 2x} & \text{si } x < 0 \\ \frac{x^{3/2} + 1}{\sqrt{x} + 1} & \text{si } x > 0 \end{cases}$
- **Dom($g$):**
  - Para $x < 0$, la expresión $\frac{2x^2 + 1}{2x(x^2 + 1)}$ está bien definida ya que el denominador no se anula para valores negativos.
  - Para $x = 0$, la función no está definida.
  - Para $x > 0$, la expresión $\frac{x^{3/2} + 1}{\sqrt{x} + 1}$ está bien definida porque $\sqrt{x} + 1 \geq 1$.
  Por lo tanto, $\text{Dom}(g) = \mathbb{R} \setminus \{0\}$.
- **Simplificación del trozo para $x > 0$:**
  Haciendo la sustitución $u = \sqrt{x} > 0$, tenemos $x^{3/2} = u^3$. Por ende:
  $$g(x) = \frac{u^3 + 1}{u + 1} = \frac{(u + 1)(u^2 - u + 1)}{u + 1} = u^2 - u + 1 = x - \sqrt{x} + 1$$
- **A.V.:**
  Analizamos el límite en la frontera del dominio, $x = 0$:
  - Por la izquierda ($x \to 0^-$):
    $$\lim_{x \to 0^-} g(x) = \lim_{x \to 0^-} \frac{2x^2 + 1}{2x(x^2 + 1)} = \frac{1}{0^-} = -\infty$$
    Por lo tanto, la recta **$x = 0$** es una asíntota vertical.
  - Por la derecha ($x \to 0^+$):
    $$\lim_{x \to 0^+} g(x) = \lim_{x \to 0^+} (x - \sqrt{x} + 1) = 1$$
- **Asíntotas en $-\infty$:**
  - **A.H.:**
    $$\lim_{x \to -\infty} g(x) = \lim_{x \to -\infty} \frac{2x^2 + 1}{2x^3 + 2x} = 0 \implies \mathbf{y = 0} \text{ es A.H. en } -\infty$$
  - **A.O.:** No existen en $-\infty$ al haber asíntota horizontal.
- **Asíntotas en $+\infty$:**
  - **A.H.:**
    $$\lim_{x \to +\infty} g(x) = \lim_{x \to +\infty} (x - \sqrt{x} + 1) = +\infty \implies \text{No hay A.H. en } +\infty$$
  - **A.O.:**
    Calculamos la pendiente $m$ y el término constante $n$:
    $$m = \lim_{x \to +\infty} \frac{g(x)}{x} = \lim_{x \to +\infty} \frac{x - \sqrt{x} + 1}{x} = \lim_{x \to +\infty} \left( 1 - \frac{1}{\sqrt{x}} + \frac{1}{x} \right) = 1$$
    $$n = \lim_{x \to +\infty} (g(x) - mx) = \lim_{x \to +\infty} (x - \sqrt{x} + 1 - x) = \lim_{x \to +\infty} (1 - \sqrt{x}) = -\infty$$
    Como $n$ no es un valor real finito, no existe asíntota oblicua en $+\infty$.

#### (i) $f(x) = \begin{cases} \frac{\sin(x^2)}{x} & \text{si } -5 < x < 0 \\ \frac{5x + x^2}{4x + 4} & \text{si } x \geq 0 \end{cases}$
- **A.V.:** No posee A.V. en su dominio, ya que $\lim_{x \to 0^-} \frac{\sin(x^2)}{x} = 0$, y el denominador del segundo trozo se anula en $x = -1$ (fuera de su intervalo de definición $x \geq 0$).
- **A.H.:** No posee.
- **A.O. (solo en $+\infty$):**
  $$m = \lim_{x \to +\infty} \frac{x^2+5x}{x(4x+4)} = \frac{1}{4}$$
  $$n = \lim_{x \to +\infty} \left( \frac{x^2+5x}{4x+4} - \frac{x}{4} \right) = \lim_{x \to +\infty} \frac{4(x^2+5x) - 4x(x+1)}{16x+16} = \lim_{x \to +\infty} \frac{16x}{16x+16} = 1$$
  Así, la asíntota oblicua es **$y = \frac{1}{4}x + 1$**.

---

### Pregunta 8: Asíntota Oblicua Específica
> **Justificación Conceptual:** Aplicamos el mismo principio de determinación asintótica que en la Pregunta 6: calculamos el coeficiente de posición $n$ para la recta $y = 3x + 2$ y lo igualamos a $2$.

**Desarrollo:**
Se desea que la recta $y = 3x + 2$ sea la asíntota oblicua de:
$$f(x) = \frac{6x^2 - 1}{2x + a}$$
Comprobamos la pendiente $m$:
$$m = \lim_{x \to +\infty} \frac{f(x)}{x} = \lim_{x \to +\infty} \frac{6x^2 - 1}{2x^2 + ax} = 3$$
Determinamos $n$:
$$n = \lim_{x \to +\infty} [f(x) - 3x] = \lim_{x \to +\infty} \left( \frac{6x^2 - 1 - 3x(2x+a)}{2x + a} \right) = \lim_{x \to +\infty} \frac{-3ax - 1}{2x + a} = \frac{-3a}{2}$$
Para que coincida con la recta dada, requerimos $n = 2$:
$$\frac{-3a}{2} = 2 \implies -3a = 4 \implies \mathbf{a = -\frac{4}{3}}$$

**Respuesta:**
El valor de $a$ debe ser **$-\frac{4}{3}$**.

---

### Pregunta 9: Asíntotas de la Hipérbola
> **Justificación Conceptual:** Despejamos $y$ de la ecuación de la hipérbola y calculamos sus límites al infinito para encontrar las asíntotas oblicuas de ambas ramas.

**Desarrollo:**
Partimos de la ecuación:
$$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \implies \frac{y^2}{b^2} = \frac{x^2}{a^2} - 1 \implies y = \pm \frac{b}{a}\sqrt{x^2 - a^2}$$
Definimos la rama superior $f(x) = \frac{b}{a}\sqrt{x^2 - a^2}$ para $x > a$:
1. **Para $x \to +\infty$:**
   $$m = \lim_{x \to +\infty} \frac{b\sqrt{x^2-a^2}}{ax} = \frac{b}{a}$$
   $$n = \lim_{x \to +\infty} \left( \frac{b}{a}\sqrt{x^2-a^2} - \frac{b}{a}x \right) = \frac{b}{a} \lim_{x \to +\infty} \frac{(x^2-a^2) - x^2}{\sqrt{x^2-a^2}+x} = 0$$
   Por ende, la asíntota oblicua es $y = \frac{b}{a}x$.

2. **Para $x \to -\infty$:**
   $$m = \lim_{x \to -\infty} \frac{b\sqrt{x^2-a^2}}{ax} = -\frac{b}{a}$$
   $$n = \lim_{x \to -\infty} \left( \frac{b}{a}\sqrt{x^2-a^2} - \left(-\frac{b}{a}x\right) \right) = 0$$
   La asíntota oblicua es $y = -\frac{b}{a}x$.

El análisis para la rama inferior $f(x) = -\frac{b}{a}\sqrt{x^2 - a^2}$ produce los mismos resultados de forma simétrica.

**Respuesta:**
Queda demostrado que las asíntotas oblicuas son **$y = \pm \frac{b}{a}x$**.

---

### Pregunta 10: Existencia de Asíntota Oblicua
> **Justificación Conceptual:** Dado que la función está definida a trozos y su primer trozo está acotado en el intervalo $(-1/3, 0)$, solo analizamos el comportamiento asintótico para la rama derecha cuando $x \to +\infty$.

**Desarrollo:**
La función es:
$$f(x) = \begin{cases} \frac{x - \sin(2x)}{x - \sin(5x)} & \text{si } -\frac{1}{3} < x < 0 \\ \frac{1 - x^2}{x - 1} & \text{si } x > 1 \end{cases}$$
Para $x > 1$, simplificamos la expresión factorizando la diferencia de cuadrados en el numerador:
$$f(x) = \frac{(1 - x)(1 + x)}{x - 1} = \frac{-(x - 1)(x + 1)}{x - 1} = -(x + 1) = -x - 1$$
Como la función coincide exactamente con una recta para todo $x > 1$, la recta límite coincide con esta función lineal.

**Respuesta:**
El gráfico de $f$ posee una asíntota oblicua cuando $x \to +\infty$ dada por **$y = -x - 1$**.

---

### Pregunta 11: Derivada por Definición de Límite
> **Justificación Conceptual:** La derivada de una función $f(x)$ por definición es:
> $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

#### (a) $f(x) = \sqrt{x+2}$
**Desarrollo:**
1. Planteamos el límite:
   $$f'(x) = \lim_{h \to 0} \frac{\sqrt{x + h + 2} - \sqrt{x + 2}}{h}$$
2. Multiplicamos y dividimos por el conjugado:
   $$f'(x) = \lim_{h \to 0} \frac{(x + h + 2) - (x + 2)}{h \left(\sqrt{x + h + 2} + \sqrt{x + 2}\right)} = \lim_{h \to 0} \frac{h}{h \left(\sqrt{x + h + 2} + \sqrt{x + 2}\right)}$$
3. Simplificamos $h$ (ya que $h \neq 0$) y calculamos el límite:
   $$f'(x) = \lim_{h \to 0} \frac{1}{\sqrt{x + h + 2} + \sqrt{x + 2}} = \frac{1}{2\sqrt{x + 2}}$$
4. Evaluando en $x = 2$:
   $$f'(2) = \frac{1}{2\sqrt{2+2}} = \frac{1}{4}$$

**Respuesta:**
Queda demostrado que **$f'(x) = \frac{1}{2\sqrt{x+2}}$** y **$f'(2) = \frac{1}{4}$**.

#### (b) $f(x) = \cos(2x)$
**Desarrollo:**
1. Planteamos el límite:
   $$f'(x) = \lim_{h \to 0} \frac{\cos(2x + 2h) - \cos(2x)}{h}$$
2. Usamos la identidad de resta de cosenos: $\cos(A) - \cos(B) = -2\sin\left(\frac{A+B}{2}\right)\sin\left(\frac{A-B}{2}\right)$:
   $$f'(x) = \lim_{h \to 0} \frac{-2\sin(2x + h)\sin(h)}{h} = \lim_{h \to 0} \left[ -2\sin(2x+h) \cdot \frac{\sin(h)}{h} \right]$$
3. Como $\lim_{h \to 0} \frac{\sin(h)}{h} = 1$:
   $$f'(x) = -2\sin(2x) \cdot 1 = -2\sin(2x)$$
4. Evaluaciones de interés:
   - En $x = \pi/4$: $f'(\pi/4) = -2\sin(\pi/2) = -2$.
   - En $x = \pi/2$: $f'(\pi/2) = -2\sin(\pi) = 0$.

**Respuesta:**
Queda demostrado que **$f'(x) = -2\sin(2x)$** y **$f'(\pi/4) = -2$**.

---

### Pregunta 12: Derivabilidad de Función a Trozos
> **Justificación Conceptual:** Para definir $g'(x)$, calculamos la derivada en los intervalos abiertos. Luego, estudiamos si existe la derivada en la frontera $x = 2$. Para que $g'(2)$ exista, la función debe ser continua en $x = 2$ y las derivadas laterales deben ser iguales.

**Desarrollo:**
La función es:
$$g(x) = \begin{cases} x^2 + 8x & \text{si } x \leq 2 \\ x^3 + 13 & \text{si } x > 2 \end{cases}$$

1. **Continuidad en $x = 2$:**
   - $\lim_{x \to 2^-} g(x) = 2^2 + 8(2) = 20$
   - $\lim_{x \to 2^+} g(x) = 2^3 + 13 = 21$
   Como los límites laterales difieren ($20 \neq 21$), la función presenta una discontinuidad de salto en $x = 2$. Por lo tanto, **$g'(2)$ no existe**.

2. **Derivada en el resto de puntos ($x \neq 2$):**
   - Para $x < 2$: $g'(x) = \frac{d}{dx}(x^2+8x) = 2x + 8$.
   - Para $x > 2$: $g'(x) = \frac{d}{dx}(x^3+13) = 3x^2$.

3. **Cálculo de los valores solicitados:**
   - **$g'(-1)$:** Como $-1 < 2 \implies g'(-1) = 2(-1) + 8 = 6$.
   - **$g'(2)$:** No existe.
   - **$g'(4)$:** Como $4 > 2 \implies g'(4) = 3(4^2) = 48$.

**Respuesta:**
La función derivada está definida como:
$$g'(x) = \begin{cases} 2x + 8 & \text{si } x < 2 \\ 3x^2 & \text{si } x > 2 \end{cases}$$
Los valores son **$g'(-1) = 6$**, **$g'(2)$ no existe**, y **$g'(4) = 48$**.

---

### Pregunta 13: Recta Normal Perpendicular
> **Justificación Conceptual:** La recta normal en $x_0$ a la curva $y = f(x)$ tiene pendiente $m_n = -\frac{1}{f'(x_0)}$. Queremos que esta recta sea perpendicular a la recta $12x - y - 16 = 0$ (cuya pendiente es $m_1 = 12$). La condición de perpendicularidad exige que $m_n \cdot m_1 = -1 \implies m_n = -1/12$.

**Desarrollo:**
1. Pendiente de la recta dada $y = 12x - 16$: $m_1 = 12$.
2. Pendiente de la recta normal a $f(x) = x^3$:
   $$f'(x) = 3x^2 \implies m_n = -\frac{1}{3x^2}$$
3. Imponemos la perpendicularidad:
   $$-\frac{1}{3x^2} = -\frac{1}{12} \implies 3x^2 = 12 \implies x^2 = 4 \implies x = \pm 2$$
4. Evaluamos los puntos en la curva $f(x) = x^3$:
   - Para $x = 2 \implies y = 2^3 = 8 \implies P_1(2, 8)$.
   - Para $x = -2 \implies y = (-2)^3 = -8 \implies P_2(-2, -8)$.

**Respuesta:**
Los puntos del gráfico donde esto ocurre son **$(2, 8)$ y $(-2, -8)$**.

---

### Pregunta 14: Rectas Tangentes desde un Punto Externo
> **Justificación Conceptual:** Planteamos la ecuación de la familia de rectas tangentes a la curva en un punto genérico de tangencia $(x_0, y_0)$. Luego, obligamos a que esta recta pase por el punto externo dado $P(2, 5)$ para despejar el valor de $x_0$.

**Desarrollo:**
La curva es $y = 4x - x^2$. La derivada es:
$$\frac{dy}{dx} = 4 - 2x$$
La ecuación de la recta tangente en un punto $(x_0, 4x_0 - x_0^2)$ de la curva es:
$$y - (4x_0 - x_0^2) = (4 - 2x_0)(x - x_0)$$
Sustituimos las coordenadas del punto externo $P(2, 5)$ en la ecuación:
$$5 - 4x_0 + x_0^2 = (4 - 2x_0)(2 - x_0)$$
Expandimos el lado derecho:
$$5 - 4x_0 + x_0^2 = 8 - 4x_0 - 4x_0 + 2x_0^2 \implies 5 - 4x_0 + x_0^2 = 8 - 8x_0 + 2x_0^2$$
Reagrupamos todos los términos a un lado:
$$x_0^2 - 4x_0 + 3 = 0 \implies (x_0 - 1)(x_0 - 3) = 0$$
Obtenemos dos puntos de tangencia en $x_0 = 1$ y $x_0 = 3$:

- **Caso $x_0 = 1$:**
  La pendiente es $m = 4 - 2(1) = 2$.
  La recta tangente es:
  $$y - 5 = 2(x - 2) \implies \mathbf{y = 2x + 1}$$

- **Caso $x_0 = 3$:**
  La pendiente es $m = 4 - 2(3) = -2$.
  La recta tangente es:
  $$y - 5 = -2(x - 2) \implies \mathbf{y = -2x + 9}$$

**Respuesta:**
Las ecuaciones de las rectas tangentes son **$y = 2x + 1$** y **$y = -2x + 9$**.

---

### Pregunta 15: Recta Tangente en un Punto
> **Justificación Conceptual:** La ecuación de la recta tangente a $y = f(x)$ en el punto de abscisa $x_0$ es $y - f(x_0) = f'(x_0)(x - x_0)$.

**Desarrollo:**
Sea $f(x) = \frac{x+1}{x-2}$ y $x_0 = 3$.
1. Calculamos el valor de la ordenada:
   $$f(3) = \frac{3+1}{3-2} = 4$$
2. Calculamos la derivada usando la regla del cociente:
   $$f'(x) = \frac{1 \cdot (x-2) - (x+1) \cdot 1}{(x-2)^2} = \frac{-3}{(x-2)^2}$$
3. Evaluamos la derivada en $x = 3$:
   $$f'(3) = \frac{-3}{(3-2)^2} = -3$$
4. Escribimos la ecuación de la recta:
   $$y - 4 = -3(x - 3) \implies y - 4 = -3x + 9 \implies y = -3x + 13$$

**Respuesta:**
La ecuación de la recta tangente es **$y = -3x + 13$** (o $3x + y - 13 = 0$).

---

### Pregunta 16: Derivabilidad y Parámetros
> **Justificación Conceptual:** Para que la función sea derivable en $x = 1$, primero debe ser continua en ese punto, y luego las derivadas laterales por definición deben existir y ser iguales.

**Desarrollo:**
La función está definida por:
$$f(x) = \begin{cases} ax^2 + b & \text{si } |x| \leq 1 \\ \frac{1}{|x|} & \text{si } |x| > 1 \end{cases}$$

1. **Condición de Continuidad en $x = 1$:**
   $$\lim_{x \to 1^-} f(x) = a(1^2) + b = a + b$$
   $$\lim_{x \to 1^+} f(x) = \frac{1}{1} = 1$$
   Igualando, obtenemos la primera ecuación:
   $$a + b = 1 \implies b = 1 - a$$

2. **Condición de Derivabilidad en $x = 1$:**
   Calculamos los límites laterales del cociente de Newton:
   - **Por la izquierda:**
     $$f'_-(1) = \lim_{h \to 0^-} \frac{f(1+h) - f(1)}{h} = \lim_{h \to 0^-} \frac{a(1+h)^2 + b - (a+b)}{h} = \lim_{h \to 0^-} \frac{a(2h + h^2)}{h} = 2a$$
   - **Por la derecha:**
     $$f'_+(1) = \lim_{h \to 0^+} \frac{f(1+h) - f(1)}{h} = \lim_{h \to 0^+} \frac{\frac{1}{1+h} - 1}{h} = \lim_{h \to 0^+} \frac{-h}{h(1+h)} = -1$$
   Igualando las derivadas laterales para la existencia de la derivada:
   $$2a = -1 \implies \mathbf{a = -\frac{1}{2}}$$

3. **Determinamos $b$:**
   $$b = 1 - \left(-\frac{1}{2}\right) \implies \mathbf{b = \frac{3}{2}}$$

**Respuesta:**
Los valores requeridos son **$a = -\frac{1}{2}$ y $b = \frac{3}{2}$**.

---

[[Intro. Cálculo]]
