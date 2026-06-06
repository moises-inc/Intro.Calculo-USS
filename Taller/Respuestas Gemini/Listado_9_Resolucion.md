---
id: "20260606-listado-9-resolucion"
title: "Resolución Completa de Colección de Ejercicios N° 9"
project: "Introducción al Cálculo"
date: "2026-06-06T14:30:10"
last_modified: "2026-06-06T17:38:40-04:00"
type: "academic-note"
status: "completed"
priority: "high"
tags: ["#status/completed", "#project/Introducción_al_Cálculo", "#course/introduccion_al_calculo"]
---

# Guía Pedagógica Definitiva: Colección de Ejercicios N° 9 (Límites y Continuidad)
**Materia:** Introducción al Cálculo  
**Docente:** Soledad Merino Ñanco  
**Resolución:** Gemini Academic Assistant  

---

## Introducción Conceptual
Esta guía proporciona la resolución detallada y rigurosa de toda la Colección de Ejercicios N° 9 sobre Límites y Continuidad. Cada sección incluye justificaciones conceptuales basadas en las propiedades fundamentales de los límites, técnicas algebraicas de factorización, racionalización, y el análisis exhaustivo del comportamiento de funciones definidas por partes y gráficas para verificar discontinuidades y asíntotas.

---

## I. Propiedades Fundamentales de los Límites

### Pregunta 1
> **Enunciado:** Considerando que $\lim_{x\to 2} f(x) = -15$, $\lim_{x\to 2} g(x) = 5$ y $\lim_{x\to 2} h(x) = 0$, calcule:
> - **a)** $\lim_{x\to 2} [5g(x) - f(x)]$
> - **b)** $\lim_{x\to 2} [g(x) + f(x)]$
> - **c)** $\lim_{x\to 2} \left[ \frac{g(x)}{f(x)} \right]$
> - **d)** $\lim_{x\to 2} [g^2(x) - f^3(x) - h(x)]$
> - **e)** $\lim_{x\to 2} \left[ \frac{h(x)g(x)}{f(x)} \right]$
> - **f)** $\lim_{x\to 2} \left[ \frac{f(x)}{g(x)} \right]^4$
> - **g)** $\lim_{x\to 2} \left[ \frac{1}{2}h(x) + \sqrt{g(x) - f(x)} \right]$

> **Justificación Conceptual:** Aplicamos el álgebra de límites. Dado que los límites de las funciones $f(x)$, $g(x)$ y $h(x)$ existen en $x=2$, podemos distribuir el operador de límite sobre sumas, restas, productos, cocientes (siempre que el denominador no sea cero) y potencias/raíces.

**Desarrollo:**

- **a)** Distribuimos el límite y extraemos la constante:
  $$\lim_{x\to 2} [5g(x) - f(x)] = 5\lim_{x\to 2} g(x) - \lim_{x\to 2} f(x) = 5(5) - (-15) = 25 + 15 = 40$$
  **Respuesta:** $\lim_{x\to 2} [5g(x) - f(x)] = 40$

- **b)** Distribuimos el límite para la suma:
  $$\lim_{x\to 2} [g(x) + f(x)] = \lim_{x\to 2} g(x) + \lim_{x\to 2} f(x) = 5 + (-15) = -10$$
  **Respuesta:** $\lim_{x\to 2} [g(x) + f(x)] = -10$

- **c)** Aplicamos la propiedad del límite de un cociente (dado que $\lim f(x) \neq 0$):
  $$\lim_{x\to 2} \left[ \frac{g(x)}{f(x)} \right] = \frac{\lim_{x\to 2} g(x)}{\lim_{x\to 2} f(x)} = \frac{5}{-15} = -\frac{1}{3}$$
  **Respuesta:** $\lim_{x\to 2} \left[ \frac{g(x)}{f(x)} \right] = -\frac{1}{3}$

- **d)** Aplicamos propiedades de potencias y restas:
  $$\lim_{x\to 2} [g^2(x) - f^3(x) - h(x)] = \left(\lim_{x\to 2} g(x)\right)^2 - \left(\lim_{x\to 2} f(x)\right)^3 - \lim_{x\to 2} h(x)$$
  $$= (5)^2 - (-15)^3 - 0 = 25 - (-3375) = 25 + 3375 = 3400$$
  **Respuesta:** $\lim_{x\to 2} [g^2(x) - f^3(x) - h(x)] = 3400$

- **e)** Aplicamos las propiedades de producto y cociente:
  $$\lim_{x\to 2} \left[ \frac{h(x)g(x)}{f(x)} \right] = \frac{\left(\lim_{x\to 2} h(x)\right) \left(\lim_{x\to 2} g(x)\right)}{\lim_{x\to 2} f(x)} = \frac{0 \cdot 5}{-15} = 0$$
  **Respuesta:** $\lim_{x\to 2} \left[ \frac{h(x)g(x)}{f(x)} \right] = 0$

- **f)** Aplicamos la propiedad del límite de una potencia:
  $$\lim_{x\to 2} \left[ \frac{f(x)}{g(x)} \right]^4 = \left( \frac{\lim_{x\to 2} f(x)}{\lim_{x\to 2} g(x)} \right)^4 = \left( \frac{-15}{5} \right)^4 = (-3)^4 = 81$$
  **Respuesta:** $\lim_{x\to 2} \left[ \frac{f(x)}{g(x)} \right]^4 = 81$

- **g)** Introducimos el límite bajo la raíz (dado que el radicando es positivo) y distribuimos:
  $$\lim_{x\to 2} \left[ \frac{1}{2}h(x) + \sqrt{g(x) - f(x)} \right] = \frac{1}{2}\lim_{x\to 2} h(x) + \sqrt{\lim_{x\to 2} g(x) - \lim_{x\to 2} f(x)}$$
  $$= \frac{1}{2}(0) + \sqrt{5 - (-15)} = \sqrt{20} = 2\sqrt{5}$$
  **Respuesta:** $\lim_{x\to 2} \left[ \frac{1}{2}h(x) + \sqrt{g(x) - f(x)} \right] = 2\sqrt{5}$

---

## II. Cálculo Directo e Indeterminaciones Algebraicas

### Pregunta 2
> **Enunciado:** Calcule los siguientes límites:
> - **a)** $\lim_{x\to 2} (5x^3 - x^2 + 3x + 5)$
> - **b)** $\lim_{x\to 1} \frac{x+4}{x^2+1}$
> - **c)** $\lim_{x\to 4} (-x^2 - 9x - 12)$
> - **d)** $\lim_{x\to 4} \log_5(x^2 - 3x + 21)$
> - **e)** $\lim_{x\to 2} \sqrt{x^4 - 3x - 2}$
> - **f)** $\lim_{x\to 4} \frac{x^2-16}{x-4}$
> - **g)** $\lim_{x\to 3} \frac{x^2-2x-3}{x-3}$
> - **h)** $\lim_{h\to 0} \frac{(2+h)^3-8}{h}$
> - **i)** $\lim_{x\to 1/2} \frac{x^2-3x}{-x^2+8x+3}$
> - **j)** $\lim_{x\to 1} \left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^3$
> - **k)** $\lim_{x\to 2} \left( 3x^2 + \frac{1}{2}\sqrt[3]{\frac{x^3-4x+3}{x^5-2x^2+3}} \right)$
> - **l)** $\lim_{x\to 6} (2x+1)^3(x-2)^4$
> - **m)** $\lim_{x\to -1} \frac{x^2-1}{2x^2+6x+4}$
> - **n)** $\lim_{x\to 2} \frac{x^2-4x+4}{x^2-2x}$
> - **o)** $\lim_{x\to 5} \frac{x^2-7x+10}{x^2-25}$
> - **p)** $\lim_{x\to 3} \frac{x^2-2x-3}{x^3-27}$
> - **q)** $\lim_{x\to 2} \frac{x^3-8}{6x^2-3x^3}$
> - **r)** $\lim_{x\to 1} \frac{x^4-3x^2+2}{x^4+2x^2-3}$
> - **s)** $\lim_{x\to 1} \frac{x^4-1}{x^3-1}$
> - **t)** $\lim_{x\to 1} \frac{\sqrt{x+3}-2}{x-1}$
> - **u)** $\lim_{x\to 7} \frac{2-\sqrt{x-3}}{x^2-49}$
> - **v)** $\lim_{x\to 1} \frac{\sqrt{x}-1}{x-1}$
> - **w)** $\lim_{x\to 2} \left( \frac{1}{x-2} - \frac{12}{x^3-8} \right)$

> **Justificación Conceptual:** Para funciones continuas en el punto de acumulación, evaluamos directamente por sustitución. Si se presenta una indeterminación del tipo $\frac{0}{0}$ o $\infty - \infty$, aplicamos técnicas de simplificación algebraica como factorización (diferencia de cuadrados, binomios), racionalización por conjugados o suma/diferencia de cubos para eliminar la indeterminación antes de evaluar.

**Desarrollo:**

- **a)** Evaluación directa por sustitución (función polinómica):
  $$\lim_{x\to 2} (5x^3 - x^2 + 3x + 5) = 5(2)^3 - (2)^2 + 3(2) + 5 = 5(8) - 4 + 6 + 5 = 47$$
  **Respuesta:** $47$

- **b)** Evaluación directa (el denominador no es nulo):
  $$\lim_{x\to 1} \frac{x+4}{x^2+1} = \frac{1+4}{(1)^2+1} = \frac{5}{2}$$
  **Respuesta:** $\frac{5}{2}$

- **c)** Evaluación directa (polinómica):
  $$\lim_{x\to 4} (-x^2 - 9x - 12) = -(4)^2 - 9(4) - 12 = -16 - 36 - 12 = -64$$
  **Respuesta:** $-64$

- **d)** Evaluación directa (la función logarítmica es continua en su dominio real positivo):
  $$\lim_{x\to 4} \log_5(x^2 - 3x + 21) = \log_5(4^2 - 3(4) + 21) = \log_5(16 - 12 + 21) = \log_5(25) = 2$$
  **Respuesta:** $2$

- **e)** Evaluación directa (raíz de índice par de un valor no negativo):
  $$\lim_{x\to 2} \sqrt{x^4 - 3x - 2} = \sqrt{2^4 - 3(2) - 2} = \sqrt{16 - 6 - 2} = \sqrt{8} = 2\sqrt{2}$$
  **Respuesta:** $2\sqrt{2}$

- **f)** Indeterminación $\frac{0}{0}$. Factorizamos el numerador por diferencia de cuadrados:
  $$\lim_{x\to 4} \frac{x^2-16}{x-4} = \lim_{x\to 4} \frac{(x-4)(x+4)}{x-4} = \lim_{x\to 4} (x+4) = 4 + 4 = 8$$
  **Respuesta:** $8$

- **g)** Indeterminación $\frac{0}{0}$. Factorizamos el trinomio del numerador:
  $$\lim_{x\to 3} \frac{x^2-2x-3}{x-3} = \lim_{x\to 3} \frac{(x-3)(x+1)}{x-3} = \lim_{x\to 3} (x+1) = 3 + 1 = 4$$
  **Respuesta:** $4$

- **h)** Indeterminación $\frac{0}{0}$. Desarrollamos el binomio al cubo en el numerador:
  $$(2+h)^3 - 8 = (8 + 12h + 6h^2 + h^3) - 8 = h(12 + 6h + h^2)$$
  $$\lim_{h\to 0} \frac{h(12+6h+h^2)}{h} = \lim_{h\to 0} (12 + 6h + h^2) = 12$$
  **Respuesta:** $12$

- **i)** Evaluación directa (denominador no nulo):
  $$\lim_{x\to 1/2} \frac{x^2-3x}{-x^2+8x+3} = \frac{(1/2)^2 - 3(1/2)}{-(1/2)^2 + 8(1/2) + 3} = \frac{1/4 - 3/2}{-1/4 + 4 + 3} = \frac{-5/4}{27/4} = -\frac{5}{27}$$
  **Respuesta:** $-\frac{5}{27}$

- **j)** Evaluación directa por sustitución:
  $$\lim_{x\to 1} \left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^3 = \left(\sqrt{1} + \frac{1}{\sqrt{1}}\right)^3 = (1 + 1)^3 = 8$$
  **Respuesta:** $8$

- **k)** Evaluación directa por sustitución:
  $$\lim_{x\to 2} \left( 3x^2 + \frac{1}{2}\sqrt[3]{\frac{x^3-4x+3}{x^5-2x^2+3}} \right) = 3(2)^2 + \frac{1}{2}\sqrt[3]{\frac{2^3-4(2)+3}{2^5-2(2)^2+3}}$$
  $$= 12 + \frac{1}{2}\sqrt[3]{\frac{8-8+3}{32-8+3}} = 12 + \frac{1}{2}\sqrt[3]{\frac{3}{27}} = 12 + \frac{1}{2} \cdot \frac{\sqrt[3]{3}}{3} = 12 + \frac{\sqrt[3]{3}}{6}$$
  **Respuesta:** $12 + \frac{\sqrt[3]{3}}{6}$

- **l)** Evaluación directa (producto de polinomios continuos):
  $$\lim_{x\to 6} (2x+1)^3(x-2)^4 = (2(6)+1)^3(6-2)^4 = (13)^3(4)^4 = 2197 \cdot 256 = 562432$$
  **Respuesta:** $562432$

- **m)** Indeterminación $\frac{0}{0}$. Factorizamos numerador (diferencia de cuadrados) y denominador:
  $$2x^2 + 6x + 4 = 2(x^2 + 3x + 2) = 2(x+1)(x+2)$$
  $$\lim_{x\to -1} \frac{(x-1)(x+1)}{2(x+1)(x+2)} = \lim_{x\to -1} \frac{x-1}{2(x+2)} = \frac{-1-1}{2(-1+2)} = \frac{-2}{2} = -1$$
  **Respuesta:** $-1$

- **n)** Indeterminación $\frac{0}{0}$. Factorizamos el cuadrado perfecto del numerador y extraemos factor común del denominador:
  $$\lim_{x\to 2} \frac{(x-2)^2}{x(x-2)} = \lim_{x\to 2} \frac{x-2}{x} = \frac{2-2}{2} = 0$$
  **Respuesta:** $0$

- **o)** Indeterminación $\frac{0}{0}$. Factorizamos ambos términos de la fracción:
  $$\lim_{x\to 5} \frac{x^2-7x+10}{x^2-25} = \lim_{x\to 5} \frac{(x-5)(x-2)}{(x-5)(x+5)} = \lim_{x\to 5} \frac{x-2}{x+5} = \frac{5-2}{5+5} = \frac{3}{10}$$
  **Respuesta:** $\frac{3}{10}$

- **p)** Indeterminación $\frac{0}{0}$. Factorizamos el numerador y el denominador (diferencia de cubos):
  $$x^3 - 27 = (x-3)(x^2+3x+9)$$
  $$\lim_{x\to 3} \frac{(x-3)(x+1)}{(x-3)(x^2+3x+9)} = \lim_{x\to 3} \frac{x+1}{x^2+3x+9} = \frac{3+1}{3^2+3(3)+9} = \frac{4}{27}$$
  **Respuesta:** $\frac{4}{27}$

- **q)** Indeterminación $\frac{0}{0}$. Factorizamos numerador (diferencia de cubos) y denominador (factor común):
  $$x^3-8 = (x-2)(x^2+2x+4) \quad \text{y} \quad 6x^2-3x^3 = -3x^2(x-2)$$
  $$\lim_{x\to 2} \frac{(x-2)(x^2+2x+4)}{-3x^2(x-2)} = \lim_{x\to 2} \frac{x^2+2x+4}{-3x^2} = \frac{2^2+2(2)+4}{-3(2)^2} = \frac{12}{-12} = -1$$
  **Respuesta:** $-1$

- **r)** Indeterminación $\frac{0}{0}$. Introducimos cambio de variable $u=x^2$ para factorizar las ecuaciones bicuadráticas:
  $$x^4-3x^2+2 = (x^2-1)(x^2-2) \quad \text{y} \quad x^4+2x^2-3 = (x^2-1)(x^2+3)$$
  $$\lim_{x\to 1} \frac{(x^2-1)(x^2-2)}{(x^2-1)(x^2+3)} = \lim_{x\to 1} \frac{x^2-2}{x^2+3} = \frac{1^2-2}{1^2+3} = -\frac{1}{4}$$
  **Respuesta:** $-\frac{1}{4}$

- **s)** Indeterminación $\frac{0}{0}$. Factorizamos usando diferencia de cuadrados y de cubos:
  $$x^4-1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1)$$
  $$x^3-1 = (x-1)(x^2+x+1)$$
  $$\lim_{x\to 1} \frac{(x-1)(x+1)(x^2+1)}{(x-1)(x^2+x+1)} = \lim_{x\to 1} \frac{(x+1)(x^2+1)}{x^2+x+1} = \frac{(1+1)(1^2+1)}{1^2+1+1} = \frac{4}{3}$$
  **Respuesta:** $\frac{4}{3}$

- **t)** Indeterminación $\frac{0}{0}$. Multiplicamos y dividimos por el conjugado del numerador:
  $$\lim_{x\to 1} \frac{\sqrt{x+3}-2}{x-1} \cdot \frac{\sqrt{x+3}+2}{\sqrt{x+3}+2} = \lim_{x\to 1} \frac{(x+3)-4}{(x-1)(\sqrt{x+3}+2)}$$
  $$= \lim_{x\to 1} \frac{x-1}{(x-1)(\sqrt{x+3}+2)} = \lim_{x\to 1} \frac{1}{\sqrt{x+3}+2} = \frac{1}{\sqrt{4}+2} = \frac{1}{4}$$
  **Respuesta:** $\frac{1}{4}$

- **u)** Indeterminación $\frac{0}{0}$. Multiplicamos por el conjugado del numerador y factorizamos la diferencia de cuadrados del denominador:
  $$\lim_{x\to 7} \frac{2-\sqrt{x-3}}{x^2-49} \cdot \frac{2+\sqrt{x-3}}{2+\sqrt{x-3}} = \lim_{x\to 7} \frac{4-(x-3)}{(x-7)(x+7)(2+\sqrt{x-3})}$$
  $$= \lim_{x\to 7} \frac{7-x}{(x-7)(x+7)(2+\sqrt{x-3})} = \lim_{x\to 7} \frac{-(x-7)}{(x-7)(x+7)(2+\sqrt{x-3})}$$
  $$= \lim_{x\to 7} \frac{-1}{(x+7)(2+\sqrt{x-3})} = \frac{-1}{(7+7)(2+\sqrt{7-3})} = \frac{-1}{14 \cdot 4} = -\frac{1}{56}$$
  **Respuesta:** $-\frac{1}{56}$

- **v)** Indeterminación $\frac{0}{0}$. Factorizamos el denominador usando diferencia de cuadrados en la base $\sqrt{x}$:
  $$x-1 = (\sqrt{x}-1)(\sqrt{x}+1)$$
  $$\lim_{x\to 1} \frac{\sqrt{x}-1}{(\sqrt{x}-1)(\sqrt{x}+1)} = \lim_{x\to 1} \frac{1}{\sqrt{x}+1} = \frac{1}{\sqrt{1}+1} = \frac{1}{2}$$
  **Respuesta:** $\frac{1}{2}$

- **w)** Indeterminación $\infty - \infty$. Obtenemos un denominador común sabiendo que $x^3-8 = (x-2)(x^2+2x+4)$:
  $$\frac{1}{x-2} - \frac{12}{x^3-8} = \frac{(x^2+2x+4) - 12}{(x-2)(x^2+2x+4)} = \frac{x^2+2x-8}{(x-2)(x^2+2x+4)}$$
  Factorizamos el trinomio del numerador: $x^2+2x-8 = (x-2)(x+4)$
  $$\lim_{x\to 2} \frac{(x-2)(x+4)}{(x-2)(x^2+2x+4)} = \lim_{x\to 2} \frac{x+4}{x^2+2x+4} = \frac{2+4}{2^2+2(2)+4} = \frac{6}{12} = \frac{1}{2}$$
  **Respuesta:** $\frac{1}{2}$

---

## III. Límites de Funciones Definidas por Partes y Continuidad

### Pregunta 3
> **Enunciado:** Dada la función:
> $$f(x) = \begin{cases} -2 & \text{si } x < -1 \\ x^2 - 3 & \text{si } -1 < x < 2 \\ 2 - x & \text{si } x > 2 \end{cases}$$
> Represéntela en el plano y determine si existen:
> $$\lim_{x\to -1} f(x) \quad \text{y} \quad \lim_{x\to 2} f(x)$$

> **Justificación Conceptual:** El límite de una función en un punto de quiebre existe si y solo si los dos límites laterales correspondientes existen y son iguales.

**Desarrollo:**

1. **Límite en $x = -1$:**
   Calculamos los límites laterales:
   - Límite por la izquierda ($x \to -1^-$):
     $$\lim_{x\to -1^-} f(x) = \lim_{x\to -1^-} (-2) = -2$$
   - Límite por la derecha ($x \to -1^+$):
     $$\lim_{x\to -1^+} f(x) = \lim_{x\to -1^+} (x^2 - 3) = (-1)^2 - 3 = -2$$
   Dado que $\lim_{x\to -1^-} f(x) = \lim_{x\to -1^+} f(x) = -2$, el límite global existe y vale $-2$.

2. **Límite en $x = 2$:**
   Calculamos los límites laterales:
   - Límite por la izquierda ($x \to 2^-$):
     $$\lim_{x\to 2^-} f(x) = \lim_{x\to 2^-} (x^2 - 3) = 2^2 - 3 = 1$$
   - Límite por la derecha ($x \to 2^+$):
     $$\lim_{x\to 2^+} f(x) = \lim_{x\to 2^+} (2 - x) = 2 - 2 = 0$$
   Dado que $\lim_{x\to 2^-} f(x) = 1 \neq 0 = \lim_{x\to 2^+} f(x)$, el límite global no existe.

3. **Descripción Gráfica:**
   - Para $x < -1$, el gráfico es una semirrecta horizontal en $y = -2$.
   - Para $-1 < x < 2$, el gráfico es un segmento parabólico convexo abierto en ambos extremos, que va de $(-1, -2)$ a $(2, 1)$, con vértice en $(0, -3)$.
   - Para $x > 2$, el gráfico es una semirrecta lineal con pendiente negativa $-1$ que parte abierta en $(2, 0)$.

**Respuesta:** $\lim_{x\to -1} f(x) = -2$ (Existe), mientras que $\lim_{x\to 2} f(x)$ no existe.

---

### Pregunta 4
> **Enunciado:** Considere la función:
> $$g(x) = \begin{cases} \frac{2x^2+1}{x^4+3} & \text{si } x < -1 \\ \frac{x^3+1}{x^2+6x+5} & \text{si } x > -1 \end{cases}$$
> Analice la existencia de $\lim_{x\to -1} g(x)$.

> **Justificación Conceptual:** Evaluamos los límites laterales. Para el límite por la derecha, resolveremos algebraicamente la indeterminación del tipo $\frac{0}{0}$ cancelando el factor $(x+1)$.

**Desarrollo:**

1. **Límite por la izquierda ($x \to -1^-$):**
   Evaluamos directamente sustituyendo en la primera rama:
   $$\lim_{x\to -1^-} g(x) = \lim_{x\to -1^-} \frac{2x^2+1}{x^4+3} = \frac{2(-1)^2 + 1}{(-1)^4 + 3} = \frac{2+1}{1+3} = \frac{3}{4}$$

2. **Límite por la derecha ($x \to -1^+$):**
   Evaluamos directamente en la segunda rama, resultando en una indeterminación del tipo $\frac{0}{0}$:
   $$\lim_{x\to -1^+} \frac{x^3+1}{x^2+6x+5} \to \frac{(-1)^3+1}{(-1)^2+6(-1)+5} = \frac{0}{0}$$
   Factorizamos por suma de cubos en el numerador y factorizamos el trinomio cuadrático en el denominador:
   $$x^3 + 1 = (x+1)(x^2-x+1) \quad \text{y} \quad x^2 + 6x + 5 = (x+1)(x+5)$$
   Simplificamos para $x \neq -1$ y evaluamos:
   $$\lim_{x\to -1^+} \frac{(x+1)(x^2-x+1)}{(x+1)(x+5)} = \lim_{x\to -1^+} \frac{x^2-x+1}{x+5} = \frac{(-1)^2 - (-1) + 1}{-1+5} = \frac{3}{4}$$

Dado que los dos límites laterales son iguales a $\frac{3}{4}$, el límite global existe.

**Respuesta:** $\lim_{x\to -1} g(x) = \frac{3}{4}$ (Existe).

---

### Pregunta 5
> **Enunciado:** Considere la función:
> $$f(x) = \begin{cases} x + 3 & \text{si } x < -1 \\ x^2 & \text{si } x \geq -1 \end{cases}$$
> Determine si existe $\lim_{x\to -1} f(x)$.

> **Justificación Conceptual:** Aplicamos el criterio de existencia de límites laterales.

**Desarrollo:**

- Límite lateral izquierdo ($x \to -1^-$):
  $$\lim_{x\to -1^-} f(x) = \lim_{x\to -1^-} (x + 3) = -1 + 3 = 2$$
- Límite lateral derecho ($x \to -1^+$):
  $$\lim_{x\to -1^+} f(x) = \lim_{x\to -1^+} (x^2) = (-1)^2 = 1$$
Como $\lim_{x\to -1^-} f(x) = 2 \neq 1 = \lim_{x\to -1^+} f(x)$, los límites laterales difieren.

**Respuesta:** $\lim_{x\to -1} f(x)$ no existe.

---

### Pregunta 6
> **Enunciado:** Considere las siguientes funciones. Represéntelas en el plano y determine la existencia del límite en los puntos de discontinuidad.
> - **i)** $h(x) = \begin{cases} x^2 - 2 & \text{si } x < 2 \\ x & \text{si } 2 < x < 4 \\ 4 - x & \text{si } x \geq 4 \end{cases}$
> - **ii)** $f(x) = \begin{cases} 2x + 3 & \text{si } x \leq 0 \\ x^2 + 3 & \text{si } x > 0 \end{cases}$
> - **iii)** $g(x) = \begin{cases} x + 5 & \text{si } x \leq -2 \\ x^2 - 1 & \text{si } -2 < x \leq 1 \\ x + 2 & \text{si } x > 1 \end{cases}$

> **Justificación Conceptual:** Para cada función, identificamos los puntos de frontera de las ramas y evaluamos la igualdad de los límites laterales para saber si existe el límite global.

**Desarrollo:**

- **i) Función $h(x)$:**
  - Punto de frontera $x = 2$:
    $$\lim_{x\to 2^-} h(x) = \lim_{x\to 2^-} (x^2-2) = 2^2-2 = 2$$
    $$\lim_{x\to 2^+} h(x) = \lim_{x\to 2^+} x = 2$$
    Como los límites laterales coinciden, **$\lim_{x\to 2} h(x) = 2$** (Existe, a pesar de que $h(2)$ no está definido).
  - Punto de frontera $x = 4$:
    $$\lim_{x\to 4^-} h(x) = \lim_{x\to 4^-} x = 4$$
    $$\lim_{x\to 4^+} h(x) = \lim_{x\to 4^+} (4-x) = 4 - 4 = 0$$
    Como $\lim_{x\to 4^-} h(x) \neq \lim_{x\to 4^+} h(x)$, **$\lim_{x\to 4} h(x)$ no existe** (discontinuidad de salto esencial).

- **ii) Función $f(x)$:**
  - Punto de frontera $x = 0$:
    $$\lim_{x\to 0^-} f(x) = \lim_{x\to 0^-} (2x+3) = 3$$
    $$\lim_{x\to 0^+} f(x) = \lim_{x\to 0^+} (x^2+3) = 3$$
    Además, $f(0) = 2(0)+3 = 3$. Como los límites laterales coinciden y son iguales al valor evaluado de la función, la función es continua. **$\lim_{x\to 0} f(x) = 3$** (Existe). No hay puntos de discontinuidad.

- **iii) Función $g(x)$:**
  - Punto de frontera $x = -2$:
    $$\lim_{x\to -2^-} g(x) = \lim_{x\to -2^-} (x+5) = -2 + 5 = 3$$
    $$\lim_{x\to -2^+} g(x) = \lim_{x\to -2^+} (x^2-1) = (-2)^2 - 1 = 3$$
    Como $g(-2) = 3$, la función es continua en $x = -2$. **$\lim_{x\to -2} g(x) = 3$** (Existe).
  - Punto de frontera $x = 1$:
    $$\lim_{x\to 1^-} g(x) = \lim_{x\to 1^-} (x^2-1) = 1^2 - 1 = 0$$
    $$\lim_{x\to 1^+} g(x) = \lim_{x\to 1^+} (x+2) = 1 + 2 = 3$$
    Como $0 \neq 3$, el límite **$\lim_{x\to 1} g(x)$ no existe** (discontinuidad de salto en $x = 1$).

**Respuesta:** 
- Para $h(x)$, el límite existe en $x=2$ ($\lim h(x) = 2$) y no existe en $x=4$.
- Para $f(x)$, el límite existe en $x=0$ ($\lim f(x) = 3$, continua).
- Para $g(x)$, el límite existe en $x=-2$ ($\lim g(x) = 3$, continua) y no existe en $x=1$ (salto).

---

### Pregunta 7
> **Enunciado:** Represente a $f$ en el plano y determine si es continua en $x = 1$, con:
> $$f(x) = \begin{cases} -x^2 & \text{si } x < 1 \\ 2x + 3 & \text{si } x \geq 1 \end{cases}$$

> **Justificación Conceptual:** Una función es continua en $x = c$ si y solo si $\lim_{x\to c} f(x) = f(c)$. Esto requiere la existencia y la igualdad de los límites laterales, y que coincidan con la definición del punto.

**Desarrollo:**

1. **Evaluar el valor de la función en $x = 1$:**
   $$f(1) = 2(1) + 3 = 5$$
2. **Evaluar los límites laterales:**
   - Por la izquierda ($x \to 1^-$):
     $$\lim_{x\to 1^-} f(x) = \lim_{x\to 1^-} (-x^2) = -(1)^2 = -1$$
   - Por la derecha ($x \to 1^+$):
     $$\lim_{x\to 1^+} f(x) = \lim_{x\to 1^+} (2x + 3) = 2(1) + 3 = 5$$
3. **Comparación:**
   $$\lim_{x\to 1^-} f(x) = -1 \neq 5 = \lim_{x\to 1^+} f(x)$$
   Como los límites laterales no coinciden, $\lim_{x\to 1} f(x)$ no existe.

**Respuesta:** La función $f(x)$ no es continua en $x = 1$ debido a una discontinuidad de salto.

---

## IV. División Sintética y Derivadas por Definición

### Pregunta 8
> **Enunciado:** Utilizando división sintética resuelva los siguientes límites:
> - **a)** $\lim_{x\to 1} \frac{6x^5-4x^4+3x^2-9x+4}{x^4-8x^3+9x-2}$
> - **b)** $\lim_{x\to -2} \frac{5x^4+x^3-2x-76}{x^3-2x^2+x+18}$
> - **c)** $\lim_{x\to 3} \frac{x^2-x-6}{x-3}$
> - **d)** $\lim_{x\to -2} \frac{x^3+4x^2-x-10}{x+2}$
> - **e)** $\lim_{x\to 1/2} \frac{4x^3-8x^2+11x-4}{2x-1}$
> - **f)** $\lim_{t\to -2} \frac{2t^3-2t^2-4t+16}{t+2}$
> - **g)** $\lim_{t\to -1} \frac{t^4-t^2+2t+2}{t+1}$
> - **h)** $\lim_{x\to 1} \frac{x^4+5x-6}{x-1}$

> **Justificación Conceptual:** Todos los ejercicios presentan indeterminación del tipo $\frac{0}{0}$ donde $x = c$ es raíz común de numerador y denominador. Usamos la división sintética (método de Ruffini) para extraer el factor $(x-c)$ y simplificar la fracción racional.

**Desarrollo:**

- **a)** Evaluamos en $x=1$: Numerador $\to 6-4+3-9+4=0$; Denominador $\to 1-8+9-2=0$.
  Aplicamos división sintética por $x-1$ en el numerador:
  $$\begin{array}{r|rrrrrr}
  1 & 6 & -4 & 0 & 3 & -9 & 4 \\
    &   & 6 & 2 & 2 & 5 & -4 \\
  \hline
    & 6 & 2 & 2 & 5 & -4 & 0
  \end{array} \implies P(x) = (x-1)(6x^4+2x^3+2x^2+5x-4)$$
  Aplicamos división sintética por $x-1$ en el denominador:
  $$\begin{array}{r|rrrrx}
  1 & 1 & -8 & 0 & 9 & -2 \\
    &   & 1 & -7 & -7 & 2 \\
  \hline
    & 1 & -7 & -7 & 2 & 0
  \end{array} \implies Q(x) = (x-1)(x^3-7x^2-7x+2)$$
  Reescribimos el límite y calculamos:
  $$\lim_{x\to 1} \frac{6x^4+2x^3+2x^2+5x-4}{x^3-7x^2-7x+2} = \frac{6(1)^4+2(1)^3+2(1)^2+5(1)-4}{1^3-7(1)^2-7(1)+2} = \frac{11}{-11} = -1$$
  **Respuesta:** $-1$

- **b)** Evaluamos en $x=-2$: Numerador $\to 5(16)-8+4-76=0$; Denominador $\to -8-8-2+18=0$.
  Dividimos el numerador por $x+2$:
  $$\begin{array}{r|rrrrr}
  -2 & 5 & 1 & 0 & -2 & -76 \\
     &   & -10 & 18 & -36 & 76 \\
  \hline
     & 5 & -9 & 18 & -38 & 0
  \end{array} \implies P(x) = (x+2)(5x^3-9x^2+18x-38)$$
  Dividimos el denominador por $x+2$:
  $$\begin{array}{r|rrrr}
  -2 & 1 & -2 & 1 & 18 \\
     &   & -2 & 8 & -18 \\
  \hline
     & 1 & -4 & 9 & 0
  \end{array} \implies Q(x) = (x+2)(x^2-4x+9)$$
  Evaluamos el límite del cociente de los polinomios resultantes:
  $$\lim_{x\to -2} \frac{5x^3-9x^2+18x-38}{x^2-4x+9} = \frac{5(-8)-9(4)+18(-2)-38}{(-2)^2-4(-2)+9} = \frac{-40-36-36-38}{4+8+9} = -\frac{150}{21} = -\frac{50}{7}$$
  **Respuesta:** $-\frac{50}{7}$

- **c)** Evaluamos en $x=3$: Numerador $\to 0$; Denominador $\to 0$.
  Dividimos el numerador $x^2-x-6$ por $x-3$:
  $$\begin{array}{r|rrr}
  3 & 1 & -1 & -6 \\
    &   & 3 & 6 \\
  \hline
    & 1 & 2 & 0
  \end{array} \implies x^2-x-6 = (x-3)(x+2)$$
  $$\lim_{x\to 3} \frac{(x-3)(x+2)}{x-3} = \lim_{x\to 3} (x+2) = 5$$
  **Respuesta:** $5$

- **d)** Evaluamos en $x=-2$: Numerador $\to -8+16+2-10=0$.
  Dividimos el numerador por $x+2$:
  $$\begin{array}{r|rrrr}
  -2 & 1 & 4 & -1 & -10 \\
     &   & -2 & -4 & 10 \\
  \hline
     & 1 & 2 & -5 & 0
  \end{array} \implies x^3+4x^2-x-10 = (x+2)(x^2+2x-5)$$
  $$\lim_{x\to -2} \frac{(x+2)(x^2+2x-5)}{x+2} = \lim_{x\to -2} (x^2+2x-5) = (-2)^2+2(-2)-5 = -5$$
  **Respuesta:** $-5$

- **e)** Evaluamos en $x=1/2$: Numerador $\to 4(1/8)-8(1/4)+11(1/2)-4 = 1/2-2+11/2-4=0$.
  Dividimos el numerador por $(x-1/2)$:
  $$\begin{array}{r|rrrr}
  1/2 & 4 & -8 & 11 & -4 \\
      &   & 2 & -3 & 4 \\
  \hline
      & 4 & -6 & 8 & 0
  \end{array} \implies 4x^3-8x^2+11x-4 = (x-1/2)(4x^2-6x+8) = (2x-1)(2x^2-3x+4)$$
  $$\lim_{x\to 1/2} \frac{(2x-1)(2x^2-3x+4)}{2x-1} = \lim_{x\to 1/2} (2x^2-3x+4) = 2(1/4)-3(1/2)+4 = \frac{1}{2}-\frac{3}{2}+4 = 3$$
  **Respuesta:** $3$

- **f)** Evaluamos en t = -2: Numerador $\to 2(-8)-2(4)-4(-2)+16 = -16-8+8+16=0$.
  Dividimos el numerador por $t+2$:
  $$\begin{array}{r|rrrr}
  -2 & 2 & -2 & -4 & 16 \\
     &   & -4 & 12 & -16 \\
  \hline
     & 2 & -6 & 8 & 0
  \end{array} \implies 2t^3-2t^2-4t+16 = (t+2)(2t^2-6t+8)$$
  $$\lim_{t\to -2} \frac{(t+2)(2t^2-6t+8)}{t+2} = \lim_{t\to -2} (2t^2-6t+8) = 2(4)-6(-2)+8 = 28$$
  **Respuesta:** $28$

- **g)** Evaluamos en $t=-1$: Numerador $\to 1-1-2+2=0$.
  Dividimos el numerador por $t+1$:
  $$\begin{array}{r|rrrrr}
  -1 & 1 & 0 & -1 & 2 & 2 \\
     &   & -1 & 1 & 0 & -2 \\
  \hline
     & 1 & -1 & 0 & 2 & 0
  \end{array} \implies t^4-t^2+2t+2 = (t+1)(t^3-t^2+2)$$
  $$\lim_{t\to -1} \frac{(t+1)(t^3-t^2+2)}{t+1} = \lim_{t\to -1} (t^3-t^2+2) = (-1)^3-(-1)^2+2 = 0$$
  **Respuesta:** $0$

- **h)** Evaluamos en $x=1$: Numerador $\to 1+5-6=0$.
  Dividimos el numerador por $x-1$:
  $$\begin{array}{r|rrrrr}
  1 & 1 & 0 & 0 & 5 & -6 \\
    &   & 1 & 1 & 1 & 6 \\
  \hline
    & 1 & 1 & 1 & 6 & 0
  \end{array} \implies x^4+5x-6 = (x-1)(x^3+x^2+x+6)$$
  $$\lim_{x\to 1} \frac{(x-1)(x^3+x^2+x+6)}{x-1} = \lim_{x\to 1} (x^3+x^2+x+6) = 1+1+1+6 = 9$$
  **Respuesta:** $9$

---

### Pregunta 9
> **Enunciado:** Dada la función $f(x) = x^2 - 5x$, determine:
> $$\lim_{h\to 0} \frac{f(x+h) - f(x)}{h}$$

> **Justificación Conceptual:** Este límite define formalmente la derivada de la función $f(x)$ por definición. Expandimos algebraicamente para cancelar el término $h$ del denominador y remover la indeterminación.

**Desarrollo:**

1. Evaluamos los términos de la definición:
   $$f(x+h) = (x+h)^2 - 5(x+h) = x^2 + 2xh + h^2 - 5x - 5h$$
   $$f(x) = x^2 - 5x$$
2. Restamos ambas expresiones:
   $$f(x+h) - f(x) = (x^2 + 2xh + h^2 - 5x - 5h) - (x^2 - 5x) = 2xh + h^2 - 5h$$
3. Dividimos entre $h$ (donde $h \neq 0$):
   $$\frac{f(x+h) - f(x)}{h} = \frac{h(2x + h - 5)}{h} = 2x + h - 5$$
4. Calculamos el límite:
   $$\lim_{h\to 0} (2x + h - 5) = 2x - 5$$

**Respuesta:** $\lim_{h\to 0} \frac{f(x+h) - f(x)}{h} = 2x - 5$

---

### Pregunta 10
> **Enunciado:** Determine los valores de $a$ y $b$ para que la siguiente función tenga límite en $x = 1$ y en $x = 2$:
> $$f(x) = \begin{cases} 3x - a & \text{si } x < 1 \\ 2x^2 + bx + a & \text{si } 1 \leq x < 2 \\ 3x + 1 & \text{si } x \geq 2 \end{cases}$$

> **Justificación Conceptual:** Para que la función tenga límite en $x=1$ y en $x=2$, los límites laterales correspondientes deben ser iguales en cada punto de quiebre. Esto genera un sistema de dos ecuaciones lineales con dos incógnitas ($a$ y $b$).

**Desarrollo:**

1. **Límite en $x=1$:**
   $$\lim_{x\to 1^-} f(x) = \lim_{x\to 1^-} (3x-a) = 3 - a$$
   $$\lim_{x\to 1^+} f(x) = \lim_{x\to 1^+} (2x^2+bx+a) = 2 + b + a$$
   Establecemos la igualdad:
   $$3 - a = 2 + b + a \implies 2a + b = 1 \quad \text{(Ecuación 1)}$$

2. **Límite en $x=2$:**
   $$\lim_{x\to 2^-} f(x) = \lim_{x\to 2^-} (2x^2+bx+a) = 2(2)^2 + b(2) + a = 8 + 2b + a$$
   $$\lim_{x\to 2^+} f(x) = \lim_{x\to 2^+} (3x+1) = 3(2) + 1 = 7$$
   Establecemos la igualdad:
   $$8 + 2b + a = 7 \implies a + 2b = -1 \quad \text{(Ecuación 2)}$$

3. **Resolvemos el sistema de ecuaciones:**
   De la Ecuación 1 despejamos $b$:
   $$b = 1 - 2a$$
   Sustituimos en la Ecuación 2:
   $$a + 2(1-2a) = -1 \implies a + 2 - 4a = -1 \implies -3a = -3 \implies a = 1$$
   Calculamos $b$:
   $$b = 1 - 2(1) = -1$$

**Respuesta:** Los valores buscados son $a = 1$ y $b = -1$.

---

## V. Límites al Infinito e Indeterminaciones Exponenciales

### Pregunta 11
> **Enunciado:** Aplicando propiedades y estrategias calcule los siguientes límites:
> - **h)** $\lim_{x\to -\infty} (5x^4 + x^3 - 2x)$
> - **i)** $\lim_{x\to -\infty} (-5x^4 + x^3 - 2x)$
> - **j)** $\lim_{x\to -\infty} \sqrt{x^3 - 7x}$
> - **k)** $\lim_{x\to -1} \frac{x^2+2x+1}{5(x^2-1)}$
> - **l)** $\lim_{x\to \infty} \frac{2x^5+3}{-x^2+x}$
> - **m)** $\lim_{x\to 1} \frac{x^2+4x-5}{x^3-3x^2+3x-1}$
> - **n)** $\lim_{x\to \infty} \frac{-2x^3-2x+3}{3x^3+3x^2-5x}$
> - **o)** Calcule el límite, cuando $x \to +\infty$ y $x \to -\infty$, de $f(x) = \frac{2-2x^2+4x}{5}$
> - **p)** $\lim_{x\to \infty} \frac{x^4}{2x^4-7x^3+7x^2+9}$
> - **q)** $\lim_{x\to +\infty} \frac{7^x}{5+7^x}$ y $\lim_{x\to -\infty} \frac{7^x}{5+7^x}$
> - **r)** $\lim_{x\to \infty} \frac{2x+3}{4+3x}$
> - **s)** $\lim_{x\to -\infty} \frac{e^x}{x+1}$
> - **t)** $\lim_{x\to \infty} \frac{2x+1}{x^2+9}$
> - **u)** $\lim_{x\to +\infty} (\sqrt{25x^2 - 2x} - 5x)$
> - **v)** $\lim_{x\to \infty} \frac{4-10x^3}{7x^2+13}$
> - **w)** $\lim_{x\to -\infty} \frac{x^2+3x-1}{\sqrt{x^6-2x}}$
> - **x)** $\lim_{x\to -\infty} \frac{4-10x^3}{7x^2+13}$
> - **y)** $\lim_{x\to -\infty} \left( \frac{4x-3}{5x+4} \right)^{x^2}$
> - **z)** $\lim_{x\to \infty} \frac{-15x^3}{x^3-3x^2+x}$
> - **aa)** $\lim_{x\to +\infty} \frac{2x^2+x-10}{x^3-3x^2+4}$
> - **bb)** $\lim_{x\to \infty} \frac{x^2-2x}{x-2}$
> - **cc)** $\lim_{x\to +\infty} (8-x)^2$ y $\lim_{x\to -\infty} (8-x)^2$
> - **dd)** $\lim_{x\to -\infty} \frac{x^2-2x}{x-2}$
> - **ee)** $\lim_{x\to \infty} \frac{-4x^3-4x+5}{5x^3+5x^2-6}$
> - **ff)** $\lim_{x\to \infty} \frac{3\sqrt{x}+x-1}{3x-11}$
> - **gg)** $\lim_{x\to -\infty} \frac{\sqrt{x^3} - \sqrt{x^5}}{\sqrt{x^3} + \sqrt{x^5}}$
> - **hh)** $\lim_{x\to \infty} \frac{3x^2-2x-5}{x-4}$
> - **ii)** $\lim_{x\to \infty} \frac{-3x^2-2x+7}{5x^2-4}$
> - **jj)** $\lim_{x\to \infty} \frac{x^2-x+4}{x^3-4x+5}$
> - **kk)** $\lim_{x\to 2} \frac{\sqrt{x^2+5}-3}{x^2-2x}$
> - **ll)** $\lim_{x\to -\infty} -\frac{1}{x^2}$
> - **mm)** $\lim_{x\to \infty} \frac{x^3-5}{-x^2-4}$
> - **nn)** $\lim_{x\to \infty} \left( \frac{x^2+1}{x+2} - \frac{x^2+10}{x+1} \right)$
> - **oo)** $\lim_{x\to \infty} \sqrt{\frac{x+4}{x-1}}$
> - **pp)** $\lim_{x\to \infty} (\sqrt{x+3} - \sqrt{x-3})$
> - **qq)** $\lim_{x\to \infty} \frac{3^{x+2} + 2^x}{3^{x-2}}$
> - **rr)** $\lim_{x\to \infty} \frac{7x-1}{\sqrt{73x^2+4x-23}}$
> - **ss)** $\lim_{x\to \infty} \frac{5^{x+1}+2^{x+1}}{2^x+5^x}$

> **Justificación Conceptual:** En los límites cuando $x \to \pm\infty$ de cocientes racionales, la tasa de crecimiento está dictada por los términos de mayor exponente (grados). Para formas indeterminadas $\infty - \infty$ que involucran raíces, racionalizamos. En expresiones exponenciales, dividimos por la base dominante.

**Desarrollo:**

- **h)** El término de mayor exponente domina la suma:
  $$\lim_{x\to - \infty} (5x^4 + x^3 - 2x) = \lim_{x\to -\infty} 5x^4\left(1 + \frac{1}{5x} - \frac{2}{5x^3}\right) = 5(+\infty)(1 + 0 - 0) = +\infty$$
  **Respuesta:** $+\infty$

- **i)** Del mismo modo, el término dominante $-5x^4$ determina el signo final:
  $$\lim_{x\to -\infty} (-5x^4 + x^3 - 2x) = -\infty$$
  **Respuesta:** $-\infty$

- **j)** Cuando $x \to -\infty$, $x^3 - 7x$ es negativo (de orden $-\infty$). En la teoría de funciones reales, la raíz de índice par de números negativos no está definida en $\mathbb{R}$.
  **Respuesta:** No existe en $\mathbb{R}$.

- **k)** Indeterminación $\frac{0}{0}$. Factorizamos el numerador y el denominador:
  $$\lim_{x\to -1} \frac{(x+1)^2}{5(x-1)(x+1)} = \lim_{x\to -1} \frac{x+1}{5(x-1)} = \frac{-1+1}{5(-1-1)} = \frac{0}{-10} = 0$$
  **Respuesta:** $0$

- **l)** El grado del numerador ($5$) es mayor que el del denominador ($2$):
  $$\lim_{x\to \infty} \frac{2x^5+3}{-x^2+x} = \lim_{x\to \infty} \frac{x^2(2x^3 + 3/x^2)}{x^2(-1 + 1/x)} = \lim_{x\to \infty} \frac{2x^3 + 0}{-1 + 0} = -\infty$$
  **Respuesta:** $-\infty$

- **m)** Indeterminación $\frac{0}{0}$. Numerador: $(x-1)(x+5)$. Denominador: $(x-1)^3$.
  $$\lim_{x\to 1} \frac{(x-1)(x+5)}{(x-1)^3} = \lim_{x\to 1} \frac{x+5}{(x-1)^2} = \frac{6}{0^+} = +\infty$$
  **Respuesta:** $+\infty$

- **n)** Numerador y denominador de igual grado ($3$):
  $$\lim_{x\to \infty} \frac{-2x^3-2x+3}{3x^3+3x^2-5x} = \frac{-2}{3}$$
  **Respuesta:** $-\frac{2}{3}$

- **o)** Analizamos el término principal $-2x^2$:
  - Para $x \to +\infty$: $\lim_{x\to +\infty} \frac{2-2x^2+4x}{5} = -\infty$
  - Para $x \to -\infty$: $\lim_{x\to -\infty} \frac{2-2x^2+4x}{5} = -\infty$
  **Respuesta:** $-\infty$ para ambos casos.

- **p)** El grado de numerador y denominador es idéntico ($4$):
  $$\lim_{x\to \infty} \frac{x^4}{2x^4-7x^3+7x^2+9} = \frac{1}{2}$$
  **Respuesta:** $\frac{1}{2}$

- **q)** 
  - Para $x \to +\infty$, dado que $7^x \to \infty$:
    $$\lim_{x\to +\infty} \frac{7^x}{5+7^x} = \lim_{x\to +\infty} \frac{1}{\frac{5}{7^x} + 1} = \frac{1}{0+1} = 1$$
  - Para $x \to -\infty$, dado que $7^x \to 0$:
    $$\lim_{x\to -\infty} \frac{7^x}{5+7^x} = \frac{0}{5+0} = 0$$
  **Respuesta:** $1$ y $0$ respectivamente.

- **r)** Cociente de polinomios lineales de primer grado:
  $$\lim_{x\to \infty} \frac{2x+3}{4+3x} = \frac{2}{3}$$
  **Respuesta:** $\frac{2}{3}$

- **s)** Para $x \to -\infty$, $e^x \to 0$ y $x+1 \to -\infty$:
  $$\lim_{x\to -\infty} \frac{e^x}{x+1} = \frac{0}{-\infty} = 0$$
  **Respuesta:** $0$

- **t)** El grado del denominador ($2$) es mayor que el del numerador ($1$):
  $$\lim_{x\to \infty} \frac{2x+1}{x^2+9} = 0$$
  **Respuesta:** $0$

- **u)** Racionalizamos multiplicando y dividiendo por el conjugado:
  $$\lim_{x\to +\infty} \frac{(\sqrt{25x^2-2x}-5x)(\sqrt{25x^2-2x}+5x)}{\sqrt{25x^2-2x}+5x} = \lim_{x\to +\infty} \frac{25x^2-2x-25x^2}{\sqrt{25x^2-2x}+5x}$$
  $$= \lim_{x\to +\infty} \frac{-2x}{x\sqrt{25-2/x}+5x} = \lim_{x\to +\infty} \frac{-2}{\sqrt{25-2/x}+5} = \frac{-2}{5+5} = -\frac{1}{5}$$
  **Respuesta:** $-\frac{1}{5}$

- **v)** El grado del numerador ($3$) supera al del denominador ($2$). Como $x \to +\infty$:
  $$\lim_{x\to \infty} \frac{4-10x^3}{7x^2+13} = -\infty$$
  **Respuesta:** $-\infty$

- **w)** Evaluamos el comportamiento asintótico. Para $x < 0$, $\sqrt{x^6} = |x^3| = -x^3$:
  $$\lim_{x\to -\infty} \frac{x^2+3x-1}{\sqrt{x^6(1 - 2/x^5)}} = \lim_{x\to -\infty} \frac{x^2(1 + 3/x - 1/x^2)}{-x^3 \sqrt{1 - 2/x^5}} = \lim_{x\to -\infty} \frac{1}{-x\sqrt{1}} = 0$$
  **Respuesta:** $0$

- **x)** Similar al caso **v**, pero cuando $x \to -\infty$, el término $-10x^3$ se vuelve positivo:
  $$\lim_{x\to -\infty} \frac{4-10x^3}{7x^2+13} = \lim_{x\to -\infty} \frac{-10x}{7} = +\infty$$
  **Respuesta:** $+\infty$

- **y)** Analizamos la base y el exponente por separado:
  $$\text{Base: } \lim_{x\to -\infty} \frac{4x-3}{5x+4} = \frac{4}{5} \quad \text{y} \quad \text{Exponente: } \lim_{x\to -\infty} x^2 = +\infty$$
  Como la base es positiva y estrictamente menor que $1$, el límite es de la forma $(4/5)^{+\infty}$:
  $$\lim_{x\to -\infty} \left( \frac{4x-3}{5x+4} \right)^{x^2} = 0$$
  **Respuesta:** $0$

- **z)** Cociente de polinomios del mismo grado ($3$):
  $$\lim_{x\to \infty} \frac{-15x^3}{x^3-3x^2+x} = -15$$
  **Respuesta:** $-15$

- **aa)** El grado del denominador ($3$) es mayor que el del numerador ($2$):
  $$\lim_{x\to +\infty} \frac{2x^2+x-10}{x^3-3x^2+4} = 0$$
  **Respuesta:** $0$

- **bb)** Factorizamos el numerador: $\frac{x(x-2)}{x-2} = x$.
  $$\lim_{x\to \infty} x = +\infty$$
  **Respuesta:** $+\infty$

- **cc)** En ambos límites, la base al cuadrado diverge positivamente:
  - $\lim_{x\to +\infty} (8-x)^2 = (-\infty)^2 = +\infty$
  - $\lim_{x\to -\infty} (8-x)^2 = (+\infty)^2 = +\infty$
  **Respuesta:** $+\infty$ en ambos casos.

- **dd)** Al igual que en **bb**, simplificamos por $x \neq 2$:
  $$\lim_{x\to -\infty} \frac{x^2-2x}{x-2} = \lim_{x\to -\infty} x = -\infty$$
  **Respuesta:** $-\infty$

- **ee)** Polinomios de grado equivalente ($3$):
  $$\lim_{x\to \infty} \frac{-4x^3-4x+5}{5x^3+5x^2-6} = -\frac{4}{5}$$
  **Respuesta:** $-\frac{4}{5}$

- **ff)** Dividimos por la mayor potencia del denominador ($x$):
  $$\lim_{x\to \infty} \frac{\frac{3}{\sqrt{x}} + 1 - \frac{1}{x}}{3 - \frac{11}{x}} = \frac{0 + 1 - 0}{3 - 0} = \frac{1}{3}$$
  **Respuesta:** $\frac{1}{3}$

- **gg)** Analizamos la expresión. En el campo de los números reales, para $x \to -\infty$, $\sqrt{x^3}$ y $\sqrt{x^5}$ no están definidas por tener radicandos negativos. Sin embargo, si consideramos la extensión a números complejos con $x < 0$, usando $|x| = -x > 0$:
  $$\sqrt{x^3} = i |x|^{3/2} \quad \text{y} \quad \sqrt{x^5} = i |x|^{5/2}$$
  $$\lim_{x\to -\infty} \frac{i|x|^{3/2} - i|x|^{5/2}}{i|x|^{3/2} + i|x|^{5/2}} = \lim_{|x|\to \infty} \frac{|x|^{3/2}(1 - |x|)}{|x|^{3/2}(1 + |x|)} = \lim_{|x|\to \infty} \frac{1 - |x|}{1 + |x|} = -1$$
  Por otro lado, si asumimos una fe de erratas en el listado donde la tendencia es hacia $+\infty$ (para trabajar en los reales):
  $$\lim_{x\to +\infty} \frac{\sqrt{x^3} - \sqrt{x^5}}{\sqrt{x^3} + \sqrt{x^5}} = \lim_{x\to +\infty} \frac{x^{3/2}(1 - x)}{x^{3/2}(1 + x)} = \lim_{x\to +\infty} \frac{1 - x}{1 + x} = -1$$
  **Respuesta:** $-1$

- **hh)** Dividimos por el término lineal del denominador:
  $$\lim_{x\to \infty} \frac{3x - 2 - 5/x}{1 - 4/x} = +\infty$$
  **Respuesta:** $+\infty$

- **ii)** Polinomios de grado $2$:
  $$\lim_{x\to \infty} \frac{-3x^2-2x+7}{5x^2-4} = -\frac{3}{5}$$
  **Respuesta:** $-\frac{3}{5}$

- **jj)** El grado del denominador ($3$) es superior al del numerador ($2$):
  $$\lim_{x\to \infty} \frac{x^2-x+4}{x^3-4x+5} = 0$$
  **Respuesta:** $0$

- **kk)** Indeterminación $\frac{0}{0}$. Racionalizamos el numerador:
  $$\lim_{x\to 2} \frac{(\sqrt{x^2+5}-3)(\sqrt{x^2+5}+3)}{x(x-2)(\sqrt{x^2+5}+3)} = \lim_{x\to 2} \frac{x^2-4}{x(x-2)(\sqrt{x^2+5}+3)}$$
  $$= \lim_{x\to 2} \frac{(x-2)(x+2)}{x(x-2)(\sqrt{x^2+5}+3)} = \lim_{x\to 2} \frac{x+2}{x(\sqrt{x^2+5}+3)} = \frac{4}{2(3+3)} = \frac{1}{3}$$
  **Respuesta:** $\frac{1}{3}$

- **ll)** Evaluamos directamente:
  $$\lim_{x\to -\infty} -\frac{1}{x^2} = 0$$
  **Respuesta:** $0$

- **mm)** El grado del numerador ($3$) supera al del denominador ($2$):
  $$\lim_{x\to \infty} \frac{x^3-5}{-x^2-4} = \lim_{x\to \infty} \frac{x}{-1} = -\infty$$
  **Respuesta:** $-\infty$

- **nn)** Indeterminación $\infty - \infty$. Combinamos en una única fracción:
  $$\frac{x^2+1}{x+2} - \frac{x^2+10}{x+1} = \frac{(x^2+1)(x+1) - (x^2+10)(x+2)}{(x+2)(x+1)}$$
  $$= \frac{(x^3+x^2+x+1) - (x^3+2x^2+10x+20)}{x^2+3x+2} = \frac{-x^2-9x-19}{x^2+3x+2}$$
  Dividimos por el término cuadrático de mayor grado $x^2$:
  $$\lim_{x\to \infty} \frac{-x^2-9x-19}{x^2+3x+2} = -1$$
  **Respuesta:** $-1$

- **oo)** Límite de una composición continua:
  $$\lim_{x\to \infty} \sqrt{\frac{x+4}{x-1}} = \sqrt{\lim_{x\to \infty} \frac{x+4}{x-1}} = \sqrt{1} = 1$$
  **Respuesta:** $1$

- **pp)** Racionalizamos:
  $$\lim_{x\to \infty} \frac{(\sqrt{x+3}-\sqrt{x-3})(\sqrt{x+3}+\sqrt{x-3})}{\sqrt{x+3}+\sqrt{x-3}} = \lim_{x\to \infty} \frac{(x+3)-(x-3)}{\sqrt{x+3}+\sqrt{x-3}}$$
  $$= \lim_{x\to \infty} \frac{6}{\sqrt{x+3}+\sqrt{x-3}} = \frac{6}{\infty} = 0$$
  **Respuesta:** $0$

- **qq)** Dividimos numerador y denominador por la base exponencial más alta $3^x$:
  $$\frac{3^{x+2} + 2^x}{3^{x-2}} = \frac{9 \cdot 3^x + 2^x}{3^x \cdot 3^{-2}} = \frac{3^x \left(9 + (2/3)^x\right)}{3^x \cdot 9^{-1}} = 9\left(9 + \left(\frac{2}{3}\right)^x\right) = 81 + 9\left(\frac{2}{3}\right)^x$$
  Como $(2/3)^x \to 0$ al tender $x \to \infty$:
  $$\lim_{x\to \infty} \left[ 81 + 9\left(\frac{2}{3}\right)^x \right] = 81$$
  **Respuesta:** $81$

- **rr)** **Nota de transcripción:** El texto impreso del listado muestra una lectura errónea por OCR de la ecuación original $\frac{7x-1}{\sqrt{73x^2+4x-23}}$ como $\frac{7x-1}{\sqrt{7x^3+4x-23}}$. Resolvemos la ecuación intencionada para ser coherentes con la respuesta del texto original:
  $$\lim_{x\to \infty} \frac{7x-1}{\sqrt{73x^2+4x-23}} = \lim_{x\to \infty} \frac{x(7 - 1/x)}{x\sqrt{73 + 4/x - 23/x^2}} = \frac{7}{\sqrt{73}}$$
  *(Si se calculase el límite impreso con $x^3$ en el radicando, el límite sería $0$, dado que el grado del denominador $1.5$ supera al del numerador $1.0$).*
  **Respuesta:** $\frac{7}{\sqrt{73}}$

- **ss)** Dividimos el numerador y denominador por la base dominante $5^x$:
  $$\lim_{x\to \infty} \frac{5^{x+1}+2^{x+1}}{2^x+5^x} = \lim_{x\to \infty} \frac{5 \cdot 5^x + 2 \cdot 2^x}{5^x + 2^x} = \lim_{x\to \infty} \frac{5 + 2(2/5)^x}{1 + (2/5)^x} = \frac{5+0}{1+0} = 5$$
  **Respuesta:** $5$

---

## VI. Análisis de Límites en Formas Indeterminadas Adicionales

### Pregunta 12
> **Enunciado:** Analice y resuelva los siguientes límites:
> - **a)** $\lim_{t\to -1} \left( \frac{1}{t+1} - \frac{1}{(t+1)^2} \right)$
> - **b)** $\lim_{t\to -2} \left( \frac{t}{4-t^2} - \frac{1}{2-t} \right)$
> - **c)** $\lim_{x\to \infty} \left( \frac{2x+1}{2x} \right)^{5x}$
> - **d)** $\lim_{x\to \infty} \left(1 + \frac{1}{8x}\right)^{7x}$
> - **e)** $\lim_{x\to \infty} \frac{1}{x^3 + 14}$
> - **f)** $\lim_{x\to 0} \frac{(1+x)^2-1}{x}$
> - **g)** $\lim_{x\to -\infty} -3x^4 \left(2 + \frac{5}{x^3} - \frac{2}{x}\right)$
> - **h)** $\lim_{x\to 0} \sqrt{(1 - 3x)^{\frac{1}{x}}}$
> - **i)** $\lim_{x\to 64} \frac{x-64}{\sqrt{x}-8}$
> - **j)** $\lim_{n\to 0} \frac{\sqrt{3+n}-\sqrt{3}}{\sqrt{3}n}$
> - **k)** $\lim_{x\to \infty} \left( \frac{x^4+3x}{3x^3-4x^2} \right)$
> - **l)** $\lim_{x\to \infty} \frac{\sqrt{x^2-1}}{2x+1}$
> - **m)** $\lim_{x\to \infty} (3x - \sqrt{4x + 2})$
> - **n)** $\lim_{x\to \infty} (\sqrt{2x - 1} - x)$
> - **o)** $\lim_{x\to 3} \frac{5x}{(x-3)^5}$
> - **p)** $\lim_{x\to 1} \left( \frac{2x+1}{x+2} \right)^{\frac{1}{x-1}}$
> - **q)** $\lim_{x\to 0} 2(1 + 3x)^{\frac{3x+4}{x}}$
> - **r)** $\lim_{t\to 0} \frac{\sqrt{1+t}-1}{t}$
> - **s)** $\lim_{x\to \infty} \frac{\sqrt{4x^4+3x^2+1}}{x^2+1}$
> - **t)** $\lim_{h\to 0} \frac{(x+h)^3-x^3}{h}$
> - **u)** $\lim_{x\to 7} \frac{2-\sqrt{x-3}}{x^2-49}$
> - **v)** $\lim_{x\to 0} \frac{\sqrt{1+x+x^2}-1}{x}$
> - **w)** $\lim_{x\to 3} \frac{\sqrt{x^2-2x+6}-\sqrt{x^2+2x-6}}{x^2-4x+3}$
> - **x)** $\lim_{x\to 8} \frac{x-8}{\sqrt[3]{x}-2}$
> - **y)** $\lim_{x\to 0} \sqrt{(1 - 3x)^{\frac{1}{x}}}$
> - **z)** $\lim_{x\to 1} \left( \frac{x+1}{2x+1} \right)^{\frac{3}{x+1}}$
> - **aa)** $\lim_{x\to 0} \left( \frac{x-x^2}{x} \right)^{\frac{1}{x}}$
> - **bb)** $\lim_{x\to -2} \frac{x^3+8}{x^4-16}$
> - **cc)** $\lim_{x\to 0} \sqrt{4(1 - 2x)^{-\frac{1}{x}}}$
> - **dd)** $\lim_{x\to 2} \frac{3^x}{2x-x^2}$

> **Justificación Conceptual:** Aplicamos las propiedades algebraicas, la racionalización de expresiones y el uso de los límites especiales relacionados con el número $e$, tales como $\lim_{y\to \infty} (1 + 1/y)^y = e$ y $\lim_{y\to 0} (1+y)^{1/y} = e$.

**Desarrollo:**

- **a)** Combinamos los términos sobre el denominador común $(t+1)^2$:
  $$\lim_{t\to -1} \frac{(t+1) - 1}{(t+1)^2} = \lim_{t\to -1} \frac{t}{(t+1)^2} = \frac{-1}{0^+} = -\infty$$
  **Respuesta:** $-\infty$

- **b)** Expresamos sobre el mínimo común múltiplo $(2-t)(2+t)$:
  $$\frac{t}{(2-t)(2+t)} - \frac{1}{2-t} = \frac{t - (2+t)}{(2-t)(2+t)} = \frac{-2}{4-t^2}$$
  Al tender $t \to -2$, el denominador se aproxima a $0$. Evaluamos por límites laterales:
  - Para $t \to -2^-$ (donde $t^2 > 4$): $\lim_{t\to -2^-} \frac{-2}{4-t^2} = \frac{-2}{0^-} = +\infty$
  - Para $t \to -2^+$ (donde $t^2 < 4$): $\lim_{t\to -2^+} \frac{-2}{4-t^2} = \frac{-2}{0^+} = -\infty$
  **Respuesta:** No existe (divergencia lateral opuesta).

- **c)** Reescribimos la base: $\frac{2x+1}{2x} = 1 + \frac{1}{2x}$.
  Sea $u = 2x$. Entonces $5x = \frac{5}{2}u$. Al tender $x \to \infty$, $u \to \infty$:
  $$\lim_{u\to \infty} \left( 1 + \frac{1}{u} \right)^{\frac{5}{2}u} = \left[ \lim_{u\to \infty} \left(1 + \frac{1}{u}\right)^u \right]^{\frac{5}{2}} = e^{\frac{5}{2}}$$
  **Respuesta:** $e^{5/2}$

- **d)** Sea $u = 8x$. Entonces $7x = \frac{7}{8}u$. Al tender $x \to \infty$, $u \to \infty$:
  $$\lim_{u\to \infty} \left( 1 + \frac{1}{u} \right)^{\frac{7}{8}u} = e^{\frac{7}{8}}$$
  **Respuesta:** $e^{7/8}$

- **e)** Directamente evaluamos:
  $$\lim_{x\to \infty} \frac{1}{x^3+14} = \frac{1}{\infty} = 0$$
  **Respuesta:** $0$

- **f)** Indeterminación $\frac{0}{0}$. Expandimos el numerador:
  $$\lim_{x\to 0} \frac{1 + 2x + x^2 - 1}{x} = \lim_{x\to 0} \frac{x(2+x)}{x} = \lim_{x\to 0} (2+x) = 2$$
  **Respuesta:** $2$

- **g)** Para $x \to -\infty$, el término lineal y cúbico dentro del paréntesis se anulan, restando $2$:
  $$\lim_{x\to -\infty} -3x^4 \left(2 + 0 - 0\right) = -3(+\infty)(2) = -\infty$$
  **Respuesta:** $-\infty$

- **h)** Evaluamos el límite de la base primero. Sea $u = -3x$, por lo tanto, $x = -u/3$ y $1/x = -3/u$:
  $$\lim_{x\to 0} (1-3x)^{\frac{1}{x}} = \lim_{u\to 0} (1+u)^{-\frac{3}{u}} = \left[ \lim_{u\to 0} (1+u)^{\frac{1}{u}} \right]^{-3} = e^{-3}$$
  Aplicamos la raíz:
  $$\lim_{x\to 0} \sqrt{(1-3x)^{\frac{1}{x}}} = \sqrt{e^{-3}} = e^{-\frac{3}{2}}$$
  **Respuesta:** $e^{-3/2}$

- **i)** Indeterminación $\frac{0}{0}$. Factorizamos el numerador por diferencia de cuadrados sobre la variable $\sqrt{x}$:
  $$x-64 = (\sqrt{x}-8)(\sqrt{x}+8)$$
  $$\lim_{x\to 64} \frac{(\sqrt{x}-8)(\sqrt{x}+8)}{\sqrt{x}-8} = \lim_{x\to 64} (\sqrt{x}+8) = \sqrt{64}+8 = 16$$
  **Respuesta:** $16$

- **j)** Indeterminación $\frac{0}{0}$. Multiplicamos numerador y denominador por el conjugado del numerador:
  $$\lim_{n\to 0} \frac{(\sqrt{3+n}-\sqrt{3})(\sqrt{3+n}+\sqrt{3})}{\sqrt{3}n(\sqrt{3+n}+\sqrt{3})} = \lim_{n\to 0} \frac{3+n-3}{\sqrt{3}n(\sqrt{3+n}+\sqrt{3})}$$
  $$= \lim_{n\to 0} \frac{n}{\sqrt{3}n(\sqrt{3+n}+\sqrt{3})} = \lim_{n\to 0} \frac{1}{\sqrt{3}(\sqrt{3+n}+\sqrt{3})} = \frac{1}{\sqrt{3}(2\sqrt{3})} = \frac{1}{6}$$
  **Respuesta:** $1/6$

- **k)** Dividimos numerador y denominador por la potencia de mayor grado del denominador ($x^3$):
  $$\lim_{x\to \infty} \frac{x^4+3x}{3x^3-4x^2} = \lim_{x\to \infty} \frac{x + \frac{3}{x^2}}{3 - \frac{4}{x}} = \frac{+\infty + 0}{3 - 0} = +\infty$$
  **Respuesta:** $+\infty$

- **l)** Factorizamos la potencia máxima $x$ en el numerador (para $x > 0$, $\sqrt{x^2} = x$) y el denominador:
  $$\lim_{x\to \infty} \frac{\sqrt{x^2-1}}{2x+1} = \lim_{x\to \infty} \frac{x\sqrt{1 - \frac{1}{x^2}}}{x\left(2 + \frac{1}{x}\right)} = \lim_{x\to \infty} \frac{\sqrt{1 - \frac{1}{x^2}}}{2 + \frac{1}{x}} = \frac{1}{2}$$
  **Respuesta:** $1/2$

- **m)** Factorizamos la variable de mayor crecimiento $x$:
  $$\lim_{x\to \infty} (3x - \sqrt{4x+2}) = \lim_{x\to \infty} x\left(3 - \sqrt{\frac{4}{x} + \frac{2}{x^2}}\right) = (+\infty)(3 - 0) = +\infty$$
  **Respuesta:** $+\infty$

- **n)** Factorizamos la variable de mayor crecimiento $x$:
  $$\lim_{x\to \infty} (\sqrt{2x-1}-x) = \lim_{x\to \infty} x\left(\sqrt{\frac{2}{x} - \frac{1}{x^2}} - 1\right) = (+\infty)(0 - 1) = -\infty$$
  **Respuesta:** $-\infty$

- **o)** El denominador tiende a $0$ con cambio de signo dependiente del orden lateral, mientras el numerador se acerca a $15$:
  - Límite por $3^+$: $\frac{15}{0^+} = +\infty$
  - Límite por $3^-$: $\frac{15}{0^-} = -\infty$
  **Respuesta:** No existe.

- **p)** Indeterminación $1^\infty$. Usamos la identidad $\lim f(x)^{g(x)} = e^{\lim g(x)(f(x)-1)}$:
  $$f(x)-1 = \frac{2x+1}{x+2} - 1 = \frac{2x+1-x-2}{x+2} = \frac{x-1}{x+2}$$
  $$g(x)(f(x)-1) = \frac{1}{x-1} \cdot \frac{x-1}{x+2} = \frac{1}{x+2}$$
  $$\lim_{x\to 1} \frac{1}{x+2} = \frac{1}{3} \implies \lim_{x\to 1} \left( \frac{2x+1}{x+2} \right)^{\frac{1}{x-1}} = e^{\frac{1}{3}} = \sqrt[3]{e}$$
  **Respuesta:** $e^{1/3}$

- **q)** Descomponemos el exponente: $\frac{3x+4}{x} = 3 + \frac{4}{x}$.
  $$\lim_{x\to 0} 2(1+3x)^{3 + \frac{4}{x}} = 2 \lim_{x\to 0} (1+3x)^3 \cdot \lim_{x\to 0} \left[ (1+3x)^{\frac{1}{x}} \right]^4 = 2(1)^3 \cdot \left[ e^3 \right]^4 = 2e^{12}$$
  **Respuesta:** $2e^{12}$

- **r)** Racionalizamos multiplicando por el conjugado:
  $$\lim_{t\to 0} \frac{(\sqrt{1+t}-1)(\sqrt{1+t}+1)}{t(\sqrt{1+t}+1)} = \lim_{t\to 0} \frac{1+t-1}{t(\sqrt{1+t}+1)} = \lim_{t\to 0} \frac{1}{\sqrt{1+t}+1} = \frac{1}{2}$$
  **Respuesta:** $\frac{1}{2}$

- **s)** Dividimos entre $x^2$:
  $$\lim_{x\to \infty} \frac{\sqrt{4 + 3/x^2 + 1/x^4}}{1 + 1/x^2} = 2$$
  **Respuesta:** $2$

- **t)** Expandimos el numerador:
  $$\lim_{h\to 0} \frac{x^3+3x^2h+3xh^2+h^3-x^3}{h} = \lim_{h\to 0} (3x^2+3xh+h^2) = 3x^2$$
  **Respuesta:** $3x^2$

- **u)** Racionalizamos y simplificamos (idéntico a **2u**):
  **Respuesta:** $-\frac{1}{56}$

- **v)** Indeterminación $\frac{0}{0}$. Multiplicamos por el conjugado del numerador:
  $$\lim_{x\to 0} \frac{(\sqrt{1+x+x^2}-1)(\sqrt{1+x+x^2}+1)}{x(\sqrt{1+x+x^2}+1)} = \lim_{x\to 0} \frac{1+x+x^2-1}{x(\sqrt{1+x+x^2}+1)}$$
  $$= \lim_{x\to 0} \frac{x(1+x)}{x(\sqrt{1+x+x^2}+1)} = \lim_{x\to 0} \frac{1+x}{\sqrt{1+x+x^2}+1} = \frac{1}{2}$$
  **Respuesta:** $\frac{1}{2}$

- **w)** Indeterminación $\frac{0}{0}$. Multiplicamos por el conjugado del numerador y factorizamos el denominador:
  $$\lim_{x\to 3} \frac{(x^2-2x+6)-(x^2+2x-6)}{(x-3)(x-1)(\sqrt{x^2-2x+6}+\sqrt{x^2+2x-6})} = \lim_{x\to 3} \frac{-4(x-3)}{(x-3)(x-1)(\sqrt{x^2-2x+6}+\sqrt{x^2+2x-6})}$$
  $$= \lim_{x\to 3} \frac{-4}{(x-1)(\sqrt{x^2-2x+6}+\sqrt{x^2+2x-6})} = \frac{-4}{(2)(3+3)} = -\frac{1}{3}$$
  **Respuesta:** $-\frac{1}{3}$

- **x)** Indeterminación $\frac{0}{0}$. Factorizamos el numerador como diferencia de cubos en la base $\sqrt[3]{x}$:
  $$x-8 = (\sqrt[3]{x}-2)(\sqrt[3]{x^2}+2\sqrt[3]{x}+4)$$
  $$\lim_{x\to 8} \frac{(\sqrt[3]{x}-2)(\sqrt[3]{x^2}+2\sqrt[3]{x}+4)}{\sqrt[3]{x}-2} = \lim_{x\to 8} (\sqrt[3]{x^2}+2\sqrt[3]{x}+4) = 4+4+4 = 12$$
  **Respuesta:** $12$

- **y)** Duplicado de la pregunta **12h**.
  **Respuesta:** $e^{-3/2}$

- **z)** Evaluación directa (sin indeterminación):
  $$\lim_{x\to 1} \left( \frac{x+1}{2x+1} \right)^{\frac{3}{x+1}} = \left( \frac{2}{3} \right)^{\frac{3}{2}} = \sqrt{\frac{8}{27}} = \frac{2\sqrt{6}}{9}$$
  **Respuesta:** $\frac{2\sqrt{6}}{9}$

- **aa)** Simplificamos la base para $x \neq 0$: $\frac{x(1-x)}{x} = 1-x$.
  $$\lim_{x\to 0} (1-x)^{\frac{1}{x}} = e^{-1} = \frac{1}{e}$$
  **Respuesta:** $e^{-1}$

- **bb)** Indeterminación $\frac{0}{0}$. Factorizamos ambos polinomios:
  $$x^3+8 = (x+2)(x^2-2x+4) \quad \text{y} \quad x^4-16 = (x^2-4)(x^2+4) = (x+2)(x-2)(x^2+4)$$
  $$\lim_{x\to -2} \frac{(x+2)(x^2-2x+4)}{(x+2)(x-2)(x^2+4)} = \lim_{x\to -2} \frac{x^2-2x+4}{(x-2)(x^2+4)} = \frac{4+4+4}{(-4)(8)} = -\frac{12}{32} = -\frac{3}{8}$$
  **Respuesta:** $-\frac{3}{8}$

- **cc)** Indeterminación $1^\infty$. Evaluamos el término dentro del radical. Sea $u = -2x$:
  $$\lim_{x\to 0} (1-2x)^{-\frac{1}{x}} = \lim_{u\to 0} (1+u)^{\frac{2}{u}} = e^2$$
  Por lo tanto, la expresión completa es:
  $$\lim_{x\to 0} \sqrt{4(1-2x)^{-\frac{1}{x}}} = \sqrt{4e^2} = 2e$$
  **Respuesta:** $2e$

- **dd)** Evaluación directa: El numerador tiende a $9$, el denominador a $2(2) - 2^2 = 0$.
  *(Nota: Si la expresión original en el numerador se interpreta como $3x$ en vez de $3^x$, el comportamiento es idéntico: el numerador tiende a $6 > 0$ y el denominador a $0$, de modo que los límites laterales continúan siendo $+\infty$ y $-\infty$ respectivamente, y el límite global sigue sin existir).*
  Evaluamos por límites laterales debido al cambio de signo de la función cuadrática $x(2-x)$ en $x=2$:
  - Por la izquierda ($x \to 2^-$): $\frac{9}{0^+} = +\infty$
  - Por la derecha ($x \to 2^+$): $\frac{9}{0^-} = -\infty$
  **Respuesta:** No existe.


---

## VII. Aplicaciones Prácticas y Gráficas de Límites y Continuidad

### Pregunta 13
> **Enunciado:** En un laboratorio se realiza un experimento biológico. La población de una colonia de bacterias (en millones), después de $x$ días, está formulada por la siguiente función:
> $$f(x) = \frac{9}{3 + 7e^{-2x}}$$
> - **a)** ¿Cuál es la población inicial de bacterias?
> - **b)** ¿Qué ocurre con la población si pasan muchísimos días? ¿Tiende la población a crecer indefinidamente o tiende a estabilizarse?

> **Justificación Conceptual:** La población inicial corresponde a evaluar la función en el instante de tiempo $x = 0$. El comportamiento a largo plazo se determina analizando el límite asintótico cuando el número de días transcurridos tiende al infinito ($x \to \infty$).

**Desarrollo:**

- **a) Población inicial ($x = 0$):**
  $$f(0) = \frac{9}{3 + 7e^{-2(0)}} = \frac{9}{3 + 7e^0} = \frac{9}{3 + 7(1)} = \frac{9}{10} = 0.9 \text{ millones}$$
  **Respuesta:** La población inicial es de $0.9$ millones de bacterias (es decir, $900\,000$ bacterias).

- **b) Población a largo plazo ($x \to \infty$):**
  Calculamos el límite de la función:
  $$\lim_{x\to \infty} f(x) = \lim_{x\to \infty} \frac{9}{3 + 7e^{-2x}}$$
  Como $-2x \to -\infty$, sabemos que $e^{-2x} \to 0$. Sustituimos este comportamiento:
  $$\lim_{x\to \infty} f(x) = \frac{9}{3 + 7(0)} = \frac{9}{3} = 3 \text{ millones}$$
  **Respuesta:** La población no crece de forma indefinida, sino que se estabiliza (tiene un crecimiento saturado o logístico) alcanzando un límite asintótico superior de $3$ millones de bacterias.

---

### Pregunta 14
> **Enunciado:** Calcule $\lim_{h\to 0} \frac{f(x+h)-f(x)}{h}$ para cada una de las siguientes funciones:
> - **a)** $f_1(x) = 3x^2 - 2x + 1$
> - **b)** $f_2(x) = 5\sqrt{x} + 1$
> - **c)** $f_3(x) = \frac{1}{1+x}$
> - **d)** $f_4(x) = -7x + 2$

> **Justificación Conceptual:** Obtenemos la expresión analítica de la derivada de cada función aplicando límites algebraicos con la definición formal de la derivada.

**Desarrollo:**

- **a) Función cuadrática $f_1(x) = 3x^2 - 2x + 1$:**
  $$f_1(x+h) = 3(x+h)^2 - 2(x+h) + 1 = 3(x^2 + 2xh + h^2) - 2x - 2h + 1 = 3x^2 + 6xh + 3h^2 - 2x - 2h + 1$$
  $$f_1(x+h) - f_1(x) = 6xh + 3h^2 - 2h = h(6x + 3h - 2)$$
  $$\lim_{h\to 0} \frac{h(6x + 3h - 2)}{h} = \lim_{h\to 0} (6x + 3h - 2) = 6x - 2$$
  **Respuesta:** $6x - 2$

- **b) Función irracional $f_2(x) = 5\sqrt{x} + 1$:**
  $$f_2(x+h) - f_2(x) = (5\sqrt{x+h} + 1) - (5\sqrt{x} + 1) = 5(\sqrt{x+h} - \sqrt{x})$$
  $$\lim_{h\to 0} \frac{5(\sqrt{x+h} - \sqrt{x})}{h} \cdot \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} = \lim_{h\to 0} \frac{5(x+h-x)}{h(\sqrt{x+h}+\sqrt{x})}$$
  $$= \lim_{h\to 0} \frac{5h}{h(\sqrt{x+h}+\sqrt{x})} = \lim_{h\to 0} \frac{5}{\sqrt{x+h}+\sqrt{x}} = \frac{5}{2\sqrt{x}}$$
  **Respuesta:** $\frac{5}{2\sqrt{x}}$

- **c) Función racional $f_3(x) = \frac{1}{1+x}$:**
  $$f_3(x+h) - f_3(x) = \frac{1}{1+x+h} - \frac{1}{1+x} = \frac{(1+x) - (1+x+h)}{(1+x+h)(1+x)} = \frac{-h}{(1+x+h)(1+x)}$$
  $$\lim_{h\to 0} \frac{1}{h} \left( \frac{-h}{(1+x+h)(1+x)} \right) = \lim_{h\to 0} \frac{-1}{(1+x+h)(1+x)} = -\frac{1}{(1+x)^2}$$
  **Respuesta:** $-\frac{1}{(1+x)^2}$

- **d) Función lineal $f_4(x) = -7x + 2$:**
  $$f_4(x+h) - f_4(x) = -7(x+h) + 2 - (-7x + 2) = -7h$$
  $$\lim_{h\to 0} \frac{-7h}{h} = -7$$
  **Respuesta:** $-7$

---

### Pregunta 15
> **Enunciado:** Dada la función $f(x) = \frac{x^2+5x}{x^2+4x-5}$, determine:
> - **a)** Puntos de discontinuidad y su clasificación (discontinuidad esencial o evitable).
> - **b)** Asíntotas.

> **Justificación Conceptual:** Factorizamos la función para analizar sus raíces y polos. Los ceros del denominador que se simplifican corresponden a discontinuidades evitables (removibles). Los que no se pueden simplificar y divergen a infinito corresponden a discontinuidades esenciales infinitas y definen asíntotas verticales.

**Desarrollo:**

1. **Factorización de la función:**
   $$f(x) = \frac{x(x+5)}{(x+5)(x-1)}$$
   El dominio es $\text{Dom}(f) = \mathbb{R} \setminus \{-5, 1\}$.

2. **a) Clasificación de Discontinuidades:**
   - **En $x = -5$:**
     $$\lim_{x\to -5} f(x) = \lim_{x\to -5} \frac{x}{x-1} = \frac{-5}{-5-1} = \frac{5}{6}$$
     Como el límite existe y es finito, la discontinuidad es **evitable (removible)**.
   - **En $x = 1$:**
     $$\lim_{x\to 1} f(x) = \lim_{x\to 1} \frac{x}{x-1} = \frac{1}{0} \implies \text{Diverge a } \pm\infty$$
     Como el límite es infinito, la discontinuidad es **esencial (infinita)**.

3. **b) Determinación de Asíntotas:**
   - **Asíntotas Verticales:** La función presenta una discontinuidad esencial infinita en $x = 1$, por lo tanto, la recta **$x = 1$** es una asíntota vertical.
   - **Asíntotas Horizontales:** Calculamos los límites al infinito:
     $$\lim_{x\to \pm\infty} \frac{x^2+5x}{x^2+4x-5} = 1$$
     Por lo tanto, la recta **$y = 1$** es una asíntota horizontal.

**Respuesta:** 
- **a)** Discontinuidad evitable en $x = -5$ y discontinuidad esencial infinita en $x = 1$.
- **b)** Asíntota vertical en la recta $x = 1$ y asíntota horizontal en la recta $y = 1$.

---

### Pregunta 16
> **Enunciado:** Dada la función $f(x) = \frac{x^2+x-12}{x^2+2x-8}$, determine:
> - **c)** Puntos de discontinuidad y su clasificación (discontinuidad esencial o evitable).
> - **d)** Asíntotas.

> **Justificación Conceptual:** Aplicamos el mismo procedimiento de factorización y cálculo de límites del ejercicio anterior.

**Desarrollo:**

1. **Factorización:**
   $$f(x) = \frac{(x+4)(x-3)}{(x+4)(x-2)}$$
   El dominio es $\text{Dom}(f) = \mathbb{R} \setminus \{-4, 2\}$.

2. **c) Clasificación de Discontinuidades:**
   - **En $x = -4$:**
     $$\lim_{x\to -4} f(x) = \lim_{x\to -4} \frac{x-3}{x-2} = \frac{-4-3}{-4-2} = \frac{7}{6}$$
     El límite existe y es finito, indicando una discontinuidad **evitable (removible)**.
   - **En $x = 2$:**
     $$\lim_{x\to 2} f(x) = \lim_{x\to 2} \frac{x-3}{x-2} = \frac{-1}{0} \implies \text{Diverge a } \pm\infty$$
     El límite es infinito, por ende es una discontinuidad **esencial (infinita)**.

3. **d) Asíntotas:**
   - **Asíntota Vertical:** La divergencia infinita en $x = 2$ establece que la recta **$x = 2$** es una asíntota vertical.
   - **Asíntota Horizontal:** Calculamos los límites cuando $x \to \pm\infty$:
     $$\lim_{x\to \pm\infty} \frac{x^2+x-12}{x^2+2x-8} = 1$$
     La recta **$y = 1$** es una asíntota horizontal.

**Respuesta:** 
- **c)** Discontinuidad evitable en $x = -4$ y discontinuidad esencial infinita en $x = 2$.
- **d)** Asíntota vertical en $x = 2$ y asíntota horizontal en $y = 1$.

---

### Pregunta 17
> **Enunciado:** Determine los puntos de discontinuidad de la función $f(x)$ mostrada en la gráfica y determine de qué tipo son (esencial, removible).

> **Justificación Conceptual:** Analizamos las características visuales del gráfico de $f(x)$ para identificar comportamientos asintóticos (polos), saltos en los valores de la curva o agujeros con redefinición puntual.

**Desarrollo:**

Observando detalladamente la gráfica de $y = f(x)$:
1. **En $x = -4$:** La curva diverge negativamente por la izquierda hacia $-\infty$ y positivamente por la derecha hacia $+\infty$. Al existir una asíntota vertical, se trata de una **discontinuidad esencial infinita**.
2. **En $x = -3$:** La curva sufre una interrupción o salto brusco. El límite lateral izquierdo es finito (aproximadamente $2.5$), y el límite lateral derecho también (aproximadamente $1.3$). Como ambos límites no coinciden, se define una **discontinuidad esencial de salto** (de tipo salto finito).
3. **En $x = 1$:** Se observa un agujero en la coordenada $(1, 3)$ y un punto sólido redefinido sobre el eje de las abscisas en $(1, 0)$. El límite cuando $x \to 1$ existe y es igual a $3$, pero difiere del valor real $f(1) = 0$. Se trata de una **discontinuidad evitable (removible)**.

**Respuesta:** Los puntos de discontinuidad son: esencial infinita en $x = -4$, esencial de salto finito en $x = -3$, y evitable (removible) en $x = 1$.

---

### Pregunta 18
> **Enunciado:** Considere la función $g(x)$ que se muestra en la imagen. Determine:
> - **a)** $\lim_{x\to -2^-} g(x)$
> - **b)** $\lim_{x\to -2^+} g(x)$
> - **c)** $\lim_{x\to -2} g(x)$
> - **d)** $\lim_{x\to -1} g(x)$
> - **e)** $\lim_{x\to -\infty} g(x)$
> - **f)** $\lim_{x\to +\infty} g(x)$
> - **g)** Puntos de discontinuidad y su clasificación.
> - **h)** Asíntotas.

> **Justificación Conceptual:** Evaluamos los valores límites mediante lectura analítica directa del comportamiento de la curva $y = g(x)$ en el gráfico provisto.

**Desarrollo:**

- **a) Límite cuando $x \to -2^-$:**
  Por la izquierda del valor de la asíntota $x = -2$, la rama de la curva crece indefinidamente hacia arriba.
  $$\lim_{x\to -2^-} g(x) = +\infty$$
  **Respuesta:** $+\infty$

- **b) Límite cuando $x \to -2^+$:**
  Por la derecha de la asíntota $x = -2$, la rama de la curva decrece indefinidamente hacia abajo.
  $$\lim_{x\to -2^+} g(x) = -\infty$$
  **Respuesta:** $-\infty$

- **c) Límite cuando $x \to -2$:**
  Dado que los límites laterales no coinciden ($+\infty \neq -\infty$), el límite global no existe.
  **Respuesta:** No existe.

- **d) Límite cuando $x \to -1$:**
  La gráfica cruza de forma continua el eje de las abscisas en la coordenada $(-1, 0)$.
  $$\lim_{x\to -1} g(x) = 0$$
  **Respuesta:** $0$

- **e) Límite cuando $x \to -\infty$:**
  Al desplazarse hacia la izquierda extrema, la curva se estabiliza aproximándose a la línea horizontal punteada situada en $y = -2$.
  $$\lim_{x\to -\infty} g(x) = -2$$
  **Respuesta:** $-2$

- **f) Límite cuando $x \to +\infty$:**
  Al desplazarse hacia la derecha extrema, la curva se estabiliza aproximándose a la línea horizontal punteada situada en $y = 2$.
  $$\lim_{x\to +\infty} g(x) = 2$$
  **Respuesta:** $2$

- **g) Puntos de discontinuidad:**
  - **En $x = -2$:** Discontinuidad esencial infinita (debido a la divergencia asintótica).
  - **En $x = 1$:** Discontinuidad evitable o removible (hay un agujero en $(1,2)$ pero el límite existe y vale $2$).
  - **En $x = 3$:** Discontinuidad esencial infinita (ambos lados de la curva decrecen hacia $-\infty$).

- **h) Asíntotas:**
  - **Verticales:** Rectas **$x = -2$** y **$x = 3$** (donde la función diverge al infinito).
  - **Horizontales:** Rectas **$y = -2$** (cuando $x \to -\infty$) y **$y = 2$** (cuando $x \to +\infty$).

**Respuesta:**
- **a)** $+\infty$
- **b)** $-\infty$
- **c)** No existe
- **d)** $0$
- **e)** $-2$
- **f)** $2$
- **g)** Discontinuidades esenciales infinitas en $x = -2$ y $x = 3$; discontinuidad evitable en $x = 1$.
- **h)** Asíntotas verticales: $x = -2$, $x = 3$. Asíntotas horizontales: $y = -2$, $y = 2$.
