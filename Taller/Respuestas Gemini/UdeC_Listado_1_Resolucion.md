---
id: "20260606-udec-listado-1-resolucion"
title: "Resolución Listado 1 - Cálculo Diferencial e Integral"
project: "Estudios_Universidad"
date: "2026-06-06T16:20:00"
last_modified: "2026-06-06T16:20:00"
type: "academic-note"
status: "completed"
priority: "medium"
tags: ["#status/completed", "#project/Estudios_Universidad", "#course/calculo_diferencial_e_integral"]
---

# Guía Pedagógica Definitiva: Listado 1 (Límites y Continuidad)
**Asignatura:** Cálculo Diferencial e Integral (527104)  
**Institución:** Universidad de Concepción  
**Resolución:** Gemini Academic Assistant  

---

## Introducción Conceptual
Esta guía presenta la resolución detallada y rigurosa de todos los ejercicios del Listado 1. Los límites se abordan desde dos perspectivas fundamentales:
1. **La definición formal ($\varepsilon - \delta$):** Que establece el control de la cercanía en el eje de las ordenadas ($y$) mediante un entorno controlado en el eje de las abscisas ($x$).
2. **Cálculo algebraico:** Eliminación de indeterminaciones por factorización, racionalización, y el uso del Teorema del Sándwich para funciones oscilatorias o acotadas.

---

## Ejercicio 1: Demostraciones por Definición Formal ($\varepsilon - \delta$)

> **Definición:**  
> $\lim_{x\to x_0} f(x) = L \iff \forall \varepsilon > 0, \exists \delta > 0 \text{ tal que } 0 < |x - x_0| < \delta \implies |f(x) - L| < \varepsilon$.

---

### (a) Probar que $\lim_{x\to-2} (3 - 5x) = 13$
> **Justificación Pedagógica:** Para funciones lineales de la forma $f(x) = mx + n$, la diferencia $|f(x) - L|$ se reduce directamente a $|m| \cdot |x - x_0|$. Esto permite hallar un $\delta$ lineal en términos de $\varepsilon$ de forma global sin restricciones de entorno.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - (-2)| < \delta \implies |(3-5x) - 13| < \varepsilon$$

1. Analizamos la diferencia en el consecuente:
   $$|(3-5x) - 13| = |-5x - 10| = |-5(x+2)| = 5|x+2|$$
2. Queremos que $5|x+2| < \varepsilon$, lo cual equivale a:
   $$|x+2| < \frac{\varepsilon}{5}$$
3. Dado $\varepsilon > 0$, definimos $\delta = \frac{\varepsilon}{5}$.
4. Verificación: Si $0 < |x+2| < \delta$, entonces:
   $$| (3-5x) - 13 | = 5|x+2| < 5\delta = 5\left(\frac{\varepsilon}{5}\right) = \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \frac{\varepsilon}{5}$**.

---

### (b) Probar que $\lim_{x\to2} \frac{2x^2 - 3x - 2}{x-2} = 5$
> **Justificación Pedagógica:** La función presenta una discontinuidad evitable en $x = 2$. Dado que el límite estudia el comportamiento de la función en $0 < |x - 2| < \delta$ (donde $x \neq 2$), podemos simplificar la expresión factorizando el numerador.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - 2| < \delta \implies \left|\frac{2x^2 - 3x - 2}{x-2} - 5\right| < \varepsilon$$

1. Para $x \neq 2$, factorizamos el numerador:
   $$2x^2 - 3x - 2 = (2x+1)(x-2)$$
   Sustituyendo esto en la expresión:
   $$\frac{2x^2 - 3x - 2}{x-2} = \frac{(2x+1)(x-2)}{x-2} = 2x+1$$
2. Analizamos la diferencia con el límite $L=5$:
   $$|(2x+1) - 5| = |2x - 4| = 2|x-2|$$
3. Queremos que $2|x-2| < \varepsilon$, lo cual equivale a:
   $$|x-2| < \frac{\varepsilon}{2}$$
4. Dado $\varepsilon > 0$, definimos $\delta = \frac{\varepsilon}{2}$.
5. Verificación: Si $0 < |x-2| < \delta$, entonces:
   $$\left|\frac{2x^2 - 3x - 2}{x-2} - 5\right| = 2|x-2| < 2\delta = 2\left(\frac{\varepsilon}{2}\right) = \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \frac{\varepsilon}{2}$**.

---

### (c) Probar que $\lim_{x\to-2} \frac{1}{x+1} = -1$
> **Justificación Pedagógica:** Como la función posee una asíntota en $x = -1$, debemos acotar el entorno alrededor de $x = -2$ mediante una constante $\delta_1$ para asegurar que el denominador no se acerque a cero ni cambie de signo abruptamente.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - (-2)| < \delta \implies \left|\frac{1}{x+1} - (-1)\right| < \varepsilon$$

1. Analizamos la diferencia:
   $$\left|\frac{1}{x+1} + 1\right| = \left|\frac{1 + (x+1)}{x+1}\right| = \frac{|x+2|}{|x+1|}$$
2. Fijamos una restricción de radio inicial $\delta_1 = \frac{1}{2}$. Si $|x+2| < \frac{1}{2}$, entonces:
   $$-\frac{1}{2} < x+2 < \frac{1}{2} \implies -\frac{5}{2} < x < -\frac{3}{2}$$
   Sumando 1 a todos los miembros para estimar el denominador:
   $$-\frac{3}{2} < x+1 < -\frac{1}{2}$$
   Tomando valores absolutos:
   $$\frac{1}{2} < |x+1| < \frac{3}{2} \implies \frac{1}{|x+1|} < 2$$
3. Sustituyendo esta cota en la diferencia original:
   $$\frac{|x+2|}{|x+1|} < 2|x+2|$$
4. Queremos que $2|x+2| < \varepsilon \iff |x+2| < \frac{\varepsilon}{2}$.
5. Dado $\varepsilon > 0$, definimos $\delta = \min\left(\frac{1}{2}, \frac{\varepsilon}{2}\right)$.
6. Verificación: Si $0 < |x+2| < \delta$, entonces se cumplen simultáneamente $|x+2| < \frac{1}{2}$ (por ende $\frac{1}{|x+1|} < 2$) y $|x+2| < \frac{\varepsilon}{2}$. Así:
   $$\left|\frac{1}{x+1} - (-1)\right| = \frac{|x+2|}{|x+1|} < 2|x+2| < 2\delta \le 2\left(\frac{\varepsilon}{2}\right) = \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \min\left(\frac{1}{2}, \frac{\varepsilon}{2}\right)$**.

---

### (d) Probar que $\lim_{x\to0} x^3 \sin(x) = 0$
> **Justificación Pedagógica:** La función trigonométrica seno está acotada globalmente por 1 en valor absoluto ($|\sin(x)| \le 1$). Esto nos permite acotar la expresión del límite directamente mediante la función potencia superior $|x|^3$.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x| < \delta \implies |x^3 \sin(x) - 0| < \varepsilon$$

1. Analizamos la diferencia:
   $$|x^3 \sin(x)| = |x|^3 |\sin(x)|$$
2. Dado que $|\sin(x)| \le 1$ para todo $x \in \mathbb{R}$:
   $$|x|^3 |\sin(x)| \le |x|^3$$
3. Queremos que $|x|^3 < \varepsilon$, lo cual equivale a:
   $$|x| < \sqrt[3]{\varepsilon}$$
4. Dado $\varepsilon > 0$, definimos $\delta = \sqrt[3]{\varepsilon}$.
5. Verificación: Si $0 < |x| < \delta$, entonces:
   $$|x^3 \sin(x)| \le |x|^3 < \delta^3 = (\sqrt[3]{\varepsilon})^3 = \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \sqrt[3]{\varepsilon}$**.

---

### (e) Probar que $\lim_{x\to-1} \frac{3x}{x-1} = \frac{3}{2}$
> **Justificación Pedagógica:** Dado que la función presenta una indeterminación o asíntota en $x = 1$, y nos aproximamos a $x = -1$, limitamos nuestro entorno mediante $\delta_1 = 1$ para alejarnos del polo en 1 y acotar el denominador.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - (-1)| < \delta \implies \left|\frac{3x}{x-1} - \frac{3}{2}\right| < \varepsilon$$

1. Analizamos la diferencia:
   $$\left|\frac{6x - 3(x-1)}{2(x-1)}\right| = \left|\frac{3x+3}{2(x-1)}\right| = \frac{3|x+1|}{2|x-1|}$$
2. Fijamos $\delta_1 = 1$. Si $|x+1| < 1$, entonces:
   $$-1 < x+1 < 1 \implies -2 < x < 0$$
   Restando 1:
   $$-3 < x-1 < -1 \implies 1 < |x-1| < 3 \implies \frac{1}{|x-1|} < 1$$
3. Sustituyendo esta cota en la diferencia original:
   $$\frac{3|x+1|}{2|x-1|} < \frac{3}{2}|x+1|$$
4. Queremos que $\frac{3}{2}|x+1| < \varepsilon \iff |x+1| < \frac{2\varepsilon}{3}$.
5. Dado $\varepsilon > 0$, definimos $\delta = \min\left(1, \frac{2\varepsilon}{3}\right)$.
6. Verificación: Si $0 < |x+1| < \delta$, entonces:
   $$\left|\frac{3x}{x-1} - \frac{3}{2}\right| = \frac{3|x+1|}{2|x-1|} < \frac{3}{2}|x+1| < \frac{3}{2}\delta \le \frac{3}{2}\left(\frac{2\varepsilon}{3}\right) = \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \min\left(1, \frac{2\varepsilon}{3}\right)$**.

---

### (f) Probar que $\lim_{x\to-2} \frac{x^2+x+1}{3x+3} = -1$
> **Justificación Pedagógica:** El límite racional se comporta de manera regular en $x = -2$. Acotaremos la diferencia utilizando $\delta_1 = \frac{1}{2}$ para mantener al denominador $3x+3$ lejos del valor cero.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - (-2)| < \delta \implies \left|\frac{x^2+x+1}{3x+3} - (-1)\right| < \varepsilon$$

1. Analizamos la diferencia:
   $$\left|\frac{x^2+x+1 + (3x+3)}{3(x+1)}\right| = \left|\frac{x^2+4x+4}{3(x+1)}\right| = \frac{|x+2|^2}{3|x+1|}$$
2. Fijamos $\delta_1 = \frac{1}{2}$. Si $|x+2| < \frac{1}{2}$, entonces:
   $$-\frac{1}{2} < x+2 < \frac{1}{2} \implies -\frac{5}{2} < x < -\frac{3}{2}$$
   Sumando 1:
   $$-\frac{3}{2} < x+1 < -\frac{1}{2} \implies \frac{1}{2} < |x+1| < \frac{3}{2} \implies \frac{1}{|x+1|} < 2$$
   Por tanto:
   $$\frac{1}{3|x+1|} < \frac{2}{3}$$
3. Sustituyendo en la expresión y aplicando la cota lineal $|x+2| < \frac{1}{2}$:
   $$\frac{|x+2|^2}{3|x+1|} < \frac{2}{3}|x+2|^2 = \frac{2}{3}|x+2||x+2| < \frac{2}{3}\left(\frac{1}{2}\right)|x+2| = \frac{1}{3}|x+2|$$
4. Queremos que $\frac{1}{3}|x+2| < \varepsilon \iff |x+2| < 3\varepsilon$.
5. Dado $\varepsilon > 0$, definimos $\delta = \min\left(\frac{1}{2}, 3\varepsilon\right)$.
6. Verificación: Si $0 < |x+2| < \delta$, entonces:
   $$\left|\frac{x^2+x+1}{3x+3} - (-1)\right| = \frac{|x+2|^2}{3|x+1|} < \frac{1}{3}|x+2| < \frac{1}{3}\delta \le \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \min\left(\frac{1}{2}, 3\varepsilon\right)$**.

---

### (g) Probar que $\lim_{x\to2} (2x^2 - 9) = -1$
> **Justificación Pedagógica:** La diferencia de la función cuadrática resulta en un factor $(x^2-4)$ que es el producto de $|x-2|$ por $|x+2|$. Acotaremos el factor $|x+2|$ restringiendo $x$ a una distancia unitaria de 2.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - 2| < \delta \implies |(2x^2 - 9) - (-1)| < \varepsilon$$

1. Analizamos la diferencia:
   $$|2x^2 - 8| = 2|x^2 - 4| = 2|x-2||x+2|$$
2. Fijamos $\delta_1 = 1$. Si $|x-2| < 1$, entonces:
   $$-1 < x-2 < 1 \implies 1 < x < 3$$
   Sumando 2 para acotar el término restante:
   $$3 < x+2 < 5 \implies |x+2| < 5$$
3. Sustituyendo en la diferencia original:
   $$2|x-2||x+2| < 2(5)|x-2| = 10|x-2|$$
4. Queremos que $10|x-2| < \varepsilon \iff |x-2| < \frac{\varepsilon}{10}$.
5. Dado $\varepsilon > 0$, definimos $\delta = \min\left(1, \frac{\varepsilon}{10}\right)$.
6. Verificación: Si $0 < |x-2| < \delta$, entonces:
   $$|(2x^2 - 9) - (-1)| = 2|x-2||x+2| < 10|x-2| < 10\delta \le \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \min\left(1, \frac{\varepsilon}{10}\right)$**.

---

### (h) Probar que $\lim_{x\to3} \sqrt{2x+3} = 3$
> **Justificación Pedagógica:** Para límites que contienen raíces cuadradas, se multiplica por el término conjugado con el fin de obtener el término lineal $|x-x_0|$ en el numerador. Restringiremos el entorno con $\delta_1 = 1$ para asegurar que el radicando sea positivo (y por tanto la raíz esté bien definida en $\mathbb{R}$).

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - 3| < \delta \implies |\sqrt{2x+3} - 3| < \varepsilon$$

1. Fijamos una restricción de entorno $\delta_1 = 1$. Si $|x-3| < 1$, entonces $-1 < x-3 < 1 \implies 2 < x < 4$, lo que garantiza que $2x+3 > 7 > 0$, asegurando que la raíz cuadrada es un número real bien definido.
2. Multiplicamos y dividimos por el conjugado:
   $$|\sqrt{2x+3} - 3| = \frac{|(\sqrt{2x+3} - 3)(\sqrt{2x+3} + 3)|}{\sqrt{2x+3} + 3} = \frac{|(2x+3) - 9|}{\sqrt{2x+3} + 3} = \frac{2|x-3|}{\sqrt{2x+3} + 3}$$
3. Dado que $\sqrt{2x+3} \ge 0$, tenemos que $\sqrt{2x+3} + 3 \ge 3$. Por lo tanto:
   $$\frac{2|x-3|}{\sqrt{2x+3} + 3} \le \frac{2}{3}|x-3|$$
4. Queremos que $\frac{2}{3}|x-3| < \varepsilon \iff |x-3| < \frac{3\varepsilon}{2}$.
5. Dado $\varepsilon > 0$, definimos $\delta = \min\left(1, \frac{3\varepsilon}{2}\right)$.
6. Verificación: Si $0 < |x-3| < \delta$, se cumple que $|x-3| < 1$ (por lo que la raíz está bien definida) y $|x-3| < \frac{3\varepsilon}{2}$. Entonces:
   $$|\sqrt{2x+3} - 3| = \frac{2|x-3|}{\sqrt{2x+3} + 3} \le \frac{2}{3}|x-3| < \frac{2}{3}\delta \le \frac{2}{3}\left(\frac{3\varepsilon}{2}\right) = \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \min\left(1, \frac{3\varepsilon}{2}\right)$**.

---

### (i) Probar que $\lim_{x\to-1} \frac{x^2+3}{x^3-1} = -2$
> **Justificación Pedagógica:** La función racional es regular en un entorno de $x = -1$. Usaremos $\delta_1 = \frac{1}{2}$ para acotar por arriba el numerador polinómico y por abajo el denominador cúbico.

**Desarrollo:**
Queremos probar que para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - (-1)| < \delta \implies \left|\frac{x^2+3}{x^3-1} - (-2)\right| < \varepsilon$$

1. Analizamos la diferencia:
   $$\left|\frac{x^2+3 + 2(x^3-1)}{x^3-1}\right| = \left|\frac{2x^3+x^2+1}{x^3-1}\right|$$
2. Factorizamos el numerador mediante división sintética, notando que $x = -1$ es una raíz:
   $$2x^3+x^2+1 = (x+1)(2x^2-x+1)$$
   Por tanto, la diferencia es:
   $$\frac{|x+1||2x^2-x+1|}{|x^3-1|}$$
3. Fijamos $\delta_1 = \frac{1}{2}$. Si $|x+1| < \frac{1}{2}$, entonces:
   $$-\frac{1}{2} < x+1 < \frac{1}{2} \implies -\frac{3}{2} < x < -\frac{1}{2}$$
   - Acotamos el término cuadrático: $|2x^2-x+1| \le 2|x|^2 + |x| + 1$. Como $|x| < \frac{3}{2}$, entonces:
     $$|2x^2-x+1| < 2\left(\frac{9}{4}\right) + \frac{3}{2} + 1 = \frac{9}{2} + \frac{3}{2} + 1 = 7$$
   - Acotamos el denominador: Si $-\frac{3}{2} < x < -\frac{1}{2} \implies -\frac{27}{8} < x^3 < -\frac{1}{8}$.
     Restando 1:
     $$-\frac{35}{8} < x^3-1 < -\frac{9}{8} \implies |x^3-1| > \frac{9}{8} \implies \frac{1}{|x^3-1|} < \frac{8}{9}$$
4. Combinando ambas estimaciones:
   $$\frac{|x+1||2x^2-x+1|}{|x^3-1|} < |x+1| \cdot 7 \cdot \frac{8}{9} = \frac{56}{9}|x+1|$$
5. Queremos que $\frac{56}{9}|x+1| < \varepsilon \iff |x+1| < \frac{9\varepsilon}{56}$.
6. Dado $\varepsilon > 0$, definimos $\delta = \min\left(\frac{1}{2}, \frac{9\varepsilon}{56}\right)$.
7. Verificación: Si $0 < |x+1| < \delta$, entonces:
   $$\left|\frac{x^2+3}{x^3-1} - (-2)\right| < \frac{56}{9}|x+1| < \frac{56}{9}\delta \le \varepsilon$$

**Respuesta:** Queda demostrado para **$\delta = \min\left(\frac{1}{2}, \frac{9\varepsilon}{56}\right)$**.

---

## Ejercicio 2: Determinación Numérica de $\delta$

### (a) $\lim_{x\to-2} (1-3x) = 7$, para $\varepsilon = 0.01$
> **Justificación Pedagógica:** Hallamos la dependencia analítica general de $\delta$ respecto a $\varepsilon$ y luego particularizamos para el valor dado.

**Desarrollo:**
1. Planteamos la desigualdad:
   $$| (1-3x) - 7 | < \varepsilon \implies | -3x - 6 | < \varepsilon \implies 3|x+2| < \varepsilon$$
2. Esto equivale a:
   $$|x+2| < \frac{\varepsilon}{3}$$
3. Proponemos $\delta = \frac{\varepsilon}{3}$.
4. Evaluamos para $\varepsilon = 0.01$:
   $$\delta = \frac{0.01}{3} = \frac{1}{300} \approx 0.00333...$$

**Respuesta:** Para $\varepsilon = 0.01$, elegimos **$\delta = \frac{1}{300}$** (o cualquier valor menor).

---

### (b) $\lim_{x\to1} (x^2-3x+1) = -1$, para $\varepsilon = 10^{-5}$
> **Justificación Pedagógica:** Estimamos localmente la función cuadrática limitando a $\delta_1 = 1$. Así acotamos la relación analítica general y la evaluamos para la tolerancia dada.

**Desarrollo:**
1. Planteamos la desigualdad:
   $$| (x^2-3x+1) - (-1) | < \varepsilon \implies |x^2-3x+2| < \varepsilon \implies |x-1||x-2| < \varepsilon$$
2. Si fijamos una cota de entorno $\delta_1 = 1$:
   $$|x-1| < 1 \implies 0 < x < 2 \implies -2 < x-2 < 0 \implies |x-2| < 2$$
3. Por ende, si $|x-1| < 1$, se cumple:
   $$|x-1||x-2| < 2|x-1|$$
4. Queremos que $2|x-1| < \varepsilon \iff |x-1| < \frac{\varepsilon}{2}$.
5. Definimos la regla general $\delta = \min\left(1, \frac{\varepsilon}{2}\right)$.
6. Evaluamos para $\varepsilon = 10^{-5}$:
   $$\frac{\varepsilon}{2} = 5 \times 10^{-6}$$
   Como $5 \times 10^{-6} < 1$, el valor mínimo es:
   $$\delta = 5 \times 10^{-6}$$

**Respuesta:** Para $\varepsilon = 10^{-5}$, elegimos **$\delta = 5 \times 10^{-6}$**.

---

## Ejercicio 3: Demostración de Propiedades Generales de Límites

### (a) Probar que $\lim_{x\to a} f(x) = L \iff \lim_{x\to a} [f(x) - L] = 0$.
> **Justificación Pedagógica:** La definición formal del límite evalúa la distancia $|f(x) - L|$. Al definir una nueva función $g(x) = f(x) - L$, la distancia del límite de esta última hacia 0 es idéntica.

**Desarrollo:**
1. **Dirección Directa ($\implies$):**  
   Supongamos que $\lim_{x\to a} f(x) = L$.  
   Por definición, $\forall \varepsilon > 0$, existe $\delta > 0$ tal que:
   $$0 < |x-a| < \delta \implies |f(x) - L| < \varepsilon$$
   Dado que $|f(x) - L| = |(f(x) - L) - 0|$, la implicación anterior se reescribe como:
   $$0 < |x-a| < \delta \implies |(f(x) - L) - 0| < \varepsilon$$
   Lo cual corresponde exactamente a la definición de $\lim_{x\to a} [f(x) - L] = 0$.

2. **Dirección Recíproca ($\impliedby$):**  
   Supongamos que $\lim_{x\to a} [f(x) - L] = 0$.  
   Por definición, $\forall \varepsilon > 0$, existe $\delta > 0$ tal que:
   $$0 < |x-a| < \delta \implies |(f(x) - L) - 0| < \varepsilon \implies |f(x) - L| < \varepsilon$$
   Lo cual es exactamente la definición de $\lim_{x\to a} f(x) = L$.

**Respuesta:** La equivalencia queda demostrada mediante la identidad algebraica de las distancias $|f(x) - L| \equiv |(f(x) - L) - 0|$.

---

### (b) Probar que $\lim_{x\to a} f(x) = 0 \iff \lim_{x\to a} |f(x)| = 0$.
> **Justificación Pedagógica:** El valor absoluto de un valor absoluto es él mismo. Esto genera una distancia idéntica al origen en ambos límites.

**Desarrollo:**
1. **Dirección Directa ($\implies$):**  
   Supongamos que $\lim_{x\to a} f(x) = 0$.  
   Por definición, $\forall \varepsilon > 0$, existe $\delta > 0$ tal que:
   $$0 < |x-a| < \delta \implies |f(x) - 0| < \varepsilon \implies |f(x)| < \varepsilon$$
   Queremos analizar el límite de $|f(x)|$:
   $$||f(x)| - 0| = ||f(x)|| = |f(x)|$$
   Dado que $|f(x)| < \varepsilon$, se cumple que $||f(x)| - 0| < \varepsilon$, demostrando que $\lim_{x\to a} |f(x)| = 0$.

2. **Dirección Recíproca ($\impliedby$):**  
   Supongamos que $\lim_{x\to a} |f(x)| = 0$.  
   Por definición, $\forall \varepsilon > 0$, existe $\delta > 0$ tal que:
   $$0 < |x-a| < \delta \implies ||f(x)| - 0| < \varepsilon \implies |f(x)| < \varepsilon$$
   Como $|f(x) - 0| = |f(x)|$, esto implica que:
   $$0 < |x-a| < \delta \implies |f(x) - 0| < \varepsilon$$
   Lo cual prueba que $\lim_{x\to a} f(x) = 0$.

**Respuesta:** Queda demostrado formalmente mediante la identidad $||f(x)|| = |f(x)|$.

---

## Ejercicio 4: Demostración con Cota Lipschitz Local

> **Enunciado:** Sea $I$ un intervalo en $\mathbb{R}$, sea $f : I \to \mathbb{R}$ y sea $c \in I$. Suponga que existen constantes no nulas $K$ y $L$ tales que $|f(x) - L| \le K|x - c|$, para $x \in I$. Muestre que $\lim_{x\to c} f(x) = L$.

> **Justificación Pedagógica:** La desigualdad dada limita la diferencia de la función respecto a $L$ de forma proporcional a la distancia de $x$ respecto a $c$. Esto proporciona un $\delta$ dependiente directamente de $K$ mediante control lineal.

**Desarrollo:**
1. Queremos demostrar que para todo $\varepsilon > 0$, existe un $\delta > 0$ tal que si $0 < |x-c| < \delta$ y $x \in I$, entonces $|f(x) - L| < \varepsilon$.
2. Por hipótesis, sabemos que:
   $$|f(x) - L| \le K|x-c|$$
   Dado que $|f(x)-L| \ge 0$, para que esta desigualdad sea válida en un intervalo y $K$ sea no nula, necesariamente debemos tener $K > 0$.
3. Queremos que el término superior de la desigualdad sea menor que $\varepsilon$:
   $$K|x-c| < \varepsilon \iff |x-c| < \frac{\varepsilon}{K}$$
4. Definimos $\delta = \frac{\varepsilon}{K}$.
5. Verificación: Si $0 < |x-c| < \delta$, entonces:
   $$|f(x) - L| \le K|x-c| < K\delta = K\left(\frac{\varepsilon}{K}\right) = \varepsilon$$

**Respuesta:** Queda demostrado con la elección **$\delta = \frac{\varepsilon}{K}$** para todo $\varepsilon > 0$.

---

## Ejercicio 5: Cálculo de Límites Algebraicos

---

### (a) Calcular $\lim_{x\to2} \frac{x^4-16}{x-2}$
> **Justificación:** Indeterminación $0/0$. Factorizamos utilizando diferencias de cuadrados consecutivas.

**Desarrollo:**
$$\lim_{x\to2} \frac{x^4-16}{x-2} = \lim_{x\to2} \frac{(x^2-4)(x^2+4)}{x-2} = \lim_{x\to2} \frac{(x-2)(x+2)(x^2+4)}{x-2}$$
Simplificando $(x-2)$ para $x \neq 2$:
$$\lim_{x\to2} (x+2)(x^2+4) = (2+2)(2^2+4) = 4 \cdot 8 = 32$$

**Respuesta:** El valor del límite es **32**.

---

### (b) Calcular $\lim_{x\to0} \frac{\sqrt{x+1}-1}{\sqrt{x+16}-4}$
> **Justificación:** Indeterminación $0/0$. Racionalizamos simultáneamente numerador y denominador mediante la multiplicación por sus respectivos conjugados.

**Desarrollo:**
$$\lim_{x\to0} \frac{\sqrt{x+1}-1}{\sqrt{x+16}-4} \cdot \left(\frac{\sqrt{x+1}+1}{\sqrt{x+1}+1}\right) \cdot \left(\frac{\sqrt{x+16}+4}{\sqrt{x+16}+4}\right)$$
$$\quad = \lim_{x\to0} \frac{(x+1-1)(\sqrt{x+16}+4)}{(x+16-16)(\sqrt{x+1}+1)} = \lim_{x\to0} \frac{x(\sqrt{x+16}+4)}{x(\sqrt{x+1}+1)}$$
Cancelando $x$ para $x \neq 0$:
$$\lim_{x\to0} \frac{\sqrt{x+16}+4}{\sqrt{x+1}+1} = \frac{\sqrt{16}+4}{\sqrt{1}+1} = \frac{4+4}{1+1} = \frac{8}{2} = 4$$

**Respuesta:** El valor del límite es **4**.

---

### (c) Calcular $\lim_{x\to2} \frac{\sqrt{2x+1}-\sqrt{5}}{\sqrt{x+2}-2}$
> **Justificación:** Indeterminación $0/0$. Multiplicamos por los conjugados para eliminar la indeterminación.

**Desarrollo:**
Multiplicamos por $(\sqrt{2x+1}+\sqrt{5})$ y $(\sqrt{x+2}+2)$:
$$\lim_{x\to2} \frac{(\sqrt{2x+1}-\sqrt{5})(\sqrt{2x+1}+\sqrt{5})(\sqrt{x+2}+2)}{(\sqrt{x+2}-2)(\sqrt{x+2}+2)(\sqrt{2x+1}+\sqrt{5})}$$
$$\quad = \lim_{x\to2} \frac{((2x+1)-5)(\sqrt{x+2}+2)}{((x+2)-4)(\sqrt{2x+1}+\sqrt{5})} = \lim_{x\to2} \frac{2(x-2)(\sqrt{x+2}+2)}{(x-2)(\sqrt{2x+1}+\sqrt{5})}$$
Simplificando $(x-2)$ para $x \neq 2$:
$$\lim_{x\to2} \frac{2(\sqrt{x+2}+2)}{\sqrt{2x+1}+\sqrt{5}} = \frac{2(\sqrt{4}+2)}{\sqrt{5}+\sqrt{5}} = \frac{2(4)}{2\sqrt{5}} = \frac{4}{\sqrt{5}} = \frac{4\sqrt{5}}{5}$$

**Respuesta:** El valor del límite es **$\frac{4\sqrt{5}}{5}$**.

---

### (d) Calcular $\lim_{x\to-2} \frac{\sqrt{2}-\sqrt{-x}}{x+2}$
> **Justificación:** Indeterminación $0/0$. Racionalizamos el numerador multiplicando por su conjugado.

**Desarrollo:**
$$\lim_{x\to-2} \frac{\sqrt{2}-\sqrt{-x}}{x+2} \cdot \frac{\sqrt{2}+\sqrt{-x}}{\sqrt{2}+\sqrt{-x}} = \lim_{x\to-2} \frac{2 - (-x)}{(x+2)(\sqrt{2}+\sqrt{-x})}$$
$$\quad = \lim_{x\to-2} \frac{x+2}{(x+2)(\sqrt{2}+\sqrt{-x})}$$
Simplificando $(x+2)$ para $x \neq -2$:
$$\lim_{x\to-2} \frac{1}{\sqrt{2}+\sqrt{-x}} = \frac{1}{\sqrt{2}+\sqrt{2}} = \frac{1}{2\sqrt{2}} = \frac{\sqrt{2}}{4}$$

**Respuesta:** El valor del límite es **$\frac{\sqrt{2}}{4}$**.

---

### (e) Calcular $\lim_{x\to1} \left( \frac{1}{x-1} - \frac{3}{x^3-1} \right)$
> **Justificación:** Indeterminación $\infty - \infty$. Obtenemos el mínimo común múltiplo usando la diferencia de cubos $x^3-1 = (x-1)(x^2+x+1)$.

**Desarrollo:**
$$\frac{1}{x-1} - \frac{3}{x^3-1} = \frac{(x^2+x+1) - 3}{x^3-1} = \frac{x^2+x-2}{(x-1)(x^2+x+1)}$$
Factorizamos el numerador:
$$x^2+x-2 = (x-1)(x+2)$$
Sustituimos y cancelamos $(x-1)$ para $x \neq 1$:
$$\lim_{x\to1} \frac{(x-1)(x+2)}{(x-1)(x^2+x+1)} = \lim_{x\to1} \frac{x+2}{x^2+x+1} = \frac{1+2}{1+1+1} = \frac{3}{3} = 1$$

**Respuesta:** El valor del límite es **1**.

---

### (f) Calcular $\lim_{x\to1} \frac{1-\sqrt[4]{x}}{\sqrt[3]{x}-1}$
> **Justificación:** Indeterminación $0/0$. Aplicamos el cambio de variable $x = u^{12}$ para eliminar ambos radicales (ya que $\text{m.c.m.}(3, 4) = 12$).

**Desarrollo:**
Sea $x = u^{12}$. Cuando $x \to 1$, $u \to 1$.
$$\lim_{x\to1} \frac{1-\sqrt[4]{x}}{\sqrt[3]{x}-1} = \lim_{u\to1} \frac{1-u^3}{u^4-1}$$
Factorizamos diferencias algebraicas:
$$\lim_{u\to1} \frac{-(u-1)(1+u+u^2)}{(u-1)(u+1)(u^2+1)}$$
Cancelamos $(u-1)$ para $u \neq 1$:
$$\lim_{u\to1} \frac{-(1+u+u^2)}{(u+1)(u^2+1)} = \frac{-(1+1+1)}{(1+1)(1+1)} = -\frac{3}{4}$$

**Respuesta:** El valor del límite es **$-\frac{3}{4}$**.

---

### (g) Calcular $\lim_{x\to1} \frac{x^{1000}-1}{x-1}$
> **Justificación:** Indeterminación $0/0$. Usamos el cociente notable para la suma de una serie geométrica.

**Desarrollo:**
Para $x \neq 1$:
$$\frac{x^{1000}-1}{x-1} = \sum_{k=0}^{999} x^k = x^{999} + x^{998} + \dots + x + 1$$
Calculando el límite:
$$\lim_{x\to1} (x^{999} + x^{998} + \dots + x + 1) = \underbrace{1 + 1 + \dots + 1}_{1000 \text{ veces}} = 1000$$

**Respuesta:** El valor del límite es **1000**.

---

### (h) Calcular $\lim_{x\to2} \left( \frac{1}{x-2} - \frac{6}{x^2+2x-8} \right)$
> **Justificación:** Indeterminación $\infty - \infty$. Factorizamos el denominador cuadrático y sumamos las fracciones.

**Desarrollo:**
Notemos que $x^2+2x-8 = (x-2)(x+4)$.
$$\frac{1}{x-2} - \frac{6}{(x-2)(x+4)} = \frac{(x+4) - 6}{(x-2)(x+4)} = \frac{x-2}{(x-2)(x+4)}$$
Cancelamos $(x-2)$ para $x \neq 2$:
$$\lim_{x\to2} \frac{1}{x+4} = \frac{1}{2+4} = \frac{1}{6}$$

**Respuesta:** El valor del límite es **$\frac{1}{6}$**.

---

### (i) Calcular $\lim_{x\to3} \frac{2-\sqrt{x+1}}{x-3}$
> **Justificación:** Indeterminación $0/0$. Racionalizamos multiplicando por el conjugado del numerador. (Nota: En la transcripción original constaba `1 - 2√x+1`, pero la indeterminación típica en $x=3$ se da para $2 - \sqrt{x+1}$, que es la forma que resolvemos).

**Desarrollo:**
$$\lim_{x\to3} \frac{2-\sqrt{x+1}}{x-3} \cdot \frac{2+\sqrt{x+1}}{2+\sqrt{x+1}} = \lim_{x\to3} \frac{4 - (x+1)}{(x-3)(2+\sqrt{x+1})}$$
$$\quad = \lim_{x\to3} \frac{3-x}{(x-3)(2+\sqrt{x+1})} = \lim_{x\to3} \frac{-(x-3)}{(x-3)(2+\sqrt{x+1})}$$
Cancelando $(x-3)$ para $x \neq 3$:
$$\lim_{x\to3} \frac{-1}{2+\sqrt{x+1}} = \frac{-1}{2+\sqrt{4}} = -\frac{1}{4}$$

**Respuesta:** El valor del límite es **$-\frac{1}{4}$**.

---

### (j) Calcular $\lim_{x\to1} \frac{x+\sqrt{x}-2}{1-x^2}$
> **Justificación:** Indeterminación $0/0$. Aplicamos el cambio de variable $x = u^2$ con $u \ge 0$.

**Desarrollo:**
Sea $x = u^2$. Cuando $x \to 1$, $u \to 1$.
$$\lim_{x\to1} \frac{x+\sqrt{x}-2}{1-x^2} = \lim_{u\to1} \frac{u^2+u-2}{1-u^4}$$
Factorizamos numerador y denominador:
$$\frac{u^2+u-2}{1-u^4} = \frac{(u-1)(u+2)}{(1-u^2)(1+u^2)} = \frac{(u-1)(u+2)}{-(u-1)(u+1)(u^2+1)}$$
Cancelamos $(u-1)$ para $u \neq 1$:
$$\lim_{u\to1} \frac{u+2}{-(u+1)(u^2+1)} = \frac{1+2}{-(1+1)(1+1)} = -\frac{3}{4}$$

**Respuesta:** El valor del límite es **$-\frac{3}{4}$**.

---

### (k) Calcular $\lim_{x\to1} \frac{x^3-1}{\sqrt{x}-1}$
> **Justificación:** Indeterminación $0/0$. Aplicamos el cambio de variable $x = u^2$.

**Desarrollo:**
Sea $x = u^2$. Cuando $x \to 1$, $u \to 1$.
$$\lim_{x\to1} \frac{x^3-1}{\sqrt{x}-1} = \lim_{u\to1} \frac{(u^2)^3 - 1}{u-1} = \lim_{u\to1} \frac{u^6-1}{u-1}$$
Usando la identidad de cocientes notables:
$$\lim_{u\to1} (u^5 + u^4 + u^3 + u^2 + u + 1) = 1 + 1 + 1 + 1 + 1 + 1 = 6$$

**Respuesta:** El valor del límite es **6**.

---

### (l) Calcular $\lim_{x\to0} \frac{\sqrt[4]{x^4+1}-\sqrt{x^2+1}}{x^2}$
> **Justificación:** Indeterminación $0/0$. Aplicamos dos racionalizaciones consecutivas multiplicando por los conjugados correspondientes.

**Desarrollo:**
Definimos $A = \sqrt[4]{x^4+1}$ y $B = \sqrt{x^2+1}$. Multiplicamos y dividimos por $(A+B)$:
$$\frac{A - B}{x^2} = \frac{A^2 - B^2}{x^2(A + B)} = \frac{\sqrt{x^4+1} - (x^2+1)}{x^2(A + B)}$$
Ahora racionalizamos el numerador multiplicando por $(\sqrt{x^4+1} + (x^2+1))$:
$$\frac{(\sqrt{x^4+1} - (x^2+1))(\sqrt{x^4+1} + (x^2+1))}{x^2(A+B)(\sqrt{x^4+1} + x^2 + 1)} = \frac{(x^4+1) - (x^2+1)^2}{x^2(A+B)(\sqrt{x^4+1} + x^2 + 1)}$$
Simplificamos el numerador:
$$(x^4+1) - (x^4 + 2x^2 + 1) = -2x^2$$
Sustituyendo y cancelando $x^2$ para $x \neq 0$:
$$\lim_{x\to0} \frac{-2x^2}{x^2(A+B)(\sqrt{x^4+1} + x^2 + 1)} = \lim_{x\to0} \frac{-2}{(A+B)(\sqrt{x^4+1} + x^2 + 1)}$$
Cuando $x \to 0$, $A \to 1$, $B \to 1$, por lo tanto:
$$\frac{-2}{(1+1)(1 + 0 + 1)} = \frac{-2}{2 \cdot 2} = -\frac{1}{2}$$

**Respuesta:** El valor del límite es **$-\frac{1}{2}$**.

---

### (m) Calcular $\lim_{x\to1} \frac{x^{3/2}-1}{x-1}$
> **Justificación:** Indeterminación $0/0$. Aplicamos el cambio de variable $x = u^2$.

**Desarrollo:**
Sea $x = u^2$. Cuando $x \to 1$, $u \to 1$.
$$\lim_{x\to1} \frac{x^{3/2}-1}{x-1} = \lim_{u\to1} \frac{u^3-1}{u^2-1} = \lim_{u\to1} \frac{(u-1)(u^2+u+1)}{(u-1)(u+1)}$$
Cancelamos $(u-1)$ para $u \neq 1$:
$$\lim_{u\to1} \frac{u^2+u+1}{u+1} = \frac{1+1+1}{1+1} = \frac{3}{2}$$

**Respuesta:** El valor del límite es **$\frac{3}{2}$**.

---

### (n) Calcular $\lim_{x\to-3} \sqrt{\frac{x^2-9}{2x^2+7x+3}}$
> **Justificación:** Indeterminación $0/0$ en el radicando. Factorizamos el numerador y el denominador para simplificar el factor problemático $(x+3)$.

**Desarrollo:**
1. Factorizamos el numerador:
   $$x^2-9 = (x-3)(x+3)$$
2. Factorizamos el denominador $2x^2+7x+3$:
   $$2x^2+7x+3 = (x+3)(2x+1)$$
3. Reemplazamos en el radicando:
   $$\lim_{x\to-3} \frac{(x-3)(x+3)}{(x+3)(2x+1)}$$
4. Cancelando $(x+3)$ para $x \neq -3$:
   $$\lim_{x\to-3} \frac{x-3}{2x+1} = \frac{-3-3}{2(-3)+1} = \frac{-6}{-5} = \frac{6}{5}$$
5. Aplicamos la raíz cuadrada (ya que la función raíz es continua en $\frac{6}{5} > 0$):
   $$\lim_{x\to-3} \sqrt{\frac{x^2-9}{2x^2+7x+3}} = \sqrt{\frac{6}{5}} = \frac{\sqrt{30}}{5}$$

**Respuesta:** El valor del límite es **$\sqrt{\frac{6}{5}}$** (o **$\frac{\sqrt{30}}{5}$**).

---

### (o) Calcular $\lim_{x\to1} \frac{\sqrt[3]{x}-1}{\sqrt[4]{x}-1}$
> **Justificación:** Indeterminación $0/0$. Empleamos el cambio de variable $x = u^{12}$. (Nota: Si el enunciado literal fuera $x \to 0$, el límite se obtiene por evaluación directa y vale 1).

**Desarrollo:**
**Caso $x \to 1$:**
Sea $x = u^{12}$. Cuando $x \to 1$, $u \to 1$.
$$\lim_{u\to1} \frac{u^4-1}{u^3-1} = \lim_{u\to1} \frac{(u-1)(u+1)(u^2+1)}{(u-1)(u^2+u+1)}$$
Cancelando $(u-1)$ para $u \neq 1$:
$$\lim_{u\to1} \frac{(u+1)(u^2+1)}{u^2+u+1} = \frac{(1+1)(1^2+1)}{1^2+1+1} = \frac{4}{3}$$

**Caso $x \to 0$ (Límite literal según extracción):**
$$\lim_{x\to0} \frac{\sqrt[3]{x}-1}{\sqrt[4]{x}-1} = \frac{0-1}{0-1} = 1$$

**Respuesta:** El límite es **$\frac{4}{3}$** para $x\to1$ (o **1** si se evalúa literalmente en $x\to0$).

---

### (p) Calcular $\lim_{x\to1} \frac{1-\sqrt[3]{x}}{x-1}$
> **Justificación:** Indeterminación $0/0$. Multiplicamos por el conjugado cúbico del numerador para racionalizar.

**Desarrollo:**
El conjugado de $1-\sqrt[3]{x}$ es $1+\sqrt[3]{x}+\sqrt[3]{x^2}$.
$$\lim_{x\to1} \frac{1-\sqrt[3]{x}}{x-1} \cdot \frac{1+\sqrt[3]{x}+\sqrt[3]{x^2}}{1+\sqrt[3]{x}+\sqrt[3]{x^2}} = \lim_{x\to1} \frac{1-x}{(x-1)(1+\sqrt[3]{x}+\sqrt[3]{x^2})}$$
Como $1-x = -(x-1)$, para $x \neq 1$ cancelamos:
$$\lim_{x\to1} \frac{-(x-1)}{(x-1)(1+\sqrt[3]{x}+\sqrt[3]{x^2})} = \lim_{x\to1} \frac{-1}{1+\sqrt[3]{x}+\sqrt[3]{x^2}} = \frac{-1}{1+1+1} = -\frac{1}{3}$$

**Respuesta:** El valor del límite es **$-\frac{1}{3}$**.

---

### (q) Calcular $\lim_{x\to1} \frac{x^3+x^{3/2}-2}{1-x^6}$
> **Justificación:** Indeterminación $0/0$. Aplicamos un cambio de variable $x = u^2$, seguido por $w = u^3$.

**Desarrollo:**
1. Sea $x = u^2$. Cuando $x \to 1$, $u \to 1$.
   $$\lim_{u\to1} \frac{u^6+u^3-2}{1-u^{12}}$$
2. Sea $w = u^3$. Cuando $u \to 1$, $w \to 1$.
   $$\lim_{w\to1} \frac{w^2+w-2}{1-w^4}$$
3. Factorizamos numerador y denominador:
   $$\lim_{w\to1} \frac{(w-1)(w+2)}{(1-w^2)(1+w^2)} = \lim_{w\to1} \frac{(w-1)(w+2)}{-(w-1)(w+1)(w^2+1)}$$
4. Cancelando $(w-1)$ para $w \neq 1$:
   $$\lim_{w\to1} \frac{w+2}{-(w+1)(w^2+1)} = \frac{1+2}{-(1+1)(1+1)} = -\frac{3}{4}$$

**Respuesta:** El valor del límite es **$-\frac{3}{4}$**.

---

### (r) Calcular $\lim_{x\to-a} \frac{\sqrt{(x-a)^2+4ax}}{|x+a|}$
> **Justificación:** Analizamos algebraicamente la expresión en el radicando y la simplificamos a un cuadrado perfecto.

**Desarrollo:**
1. Simplificamos el radicando:
   $$(x-a)^2 + 4ax = x^2 - 2ax + a^2 + 4ax = x^2 + 2ax + a^2 = (x+a)^2$$
2. Recordamos que para cualquier número real, $\sqrt{u^2} = |u|$. Por tanto:
   $$\sqrt{(x-a)^2+4ax} = |x+a|$$
3. Sustituyendo en el límite:
   $$\lim_{x\to-a} \frac{|x+a|}{|x+a|}$$
4. Para cualquier $x \neq -a$, el cociente es idénticamente 1:
   $$\lim_{x\to-a} 1 = 1$$

**Respuesta:** El valor del límite es **1**.

---

## Ejercicio 6: Derivadas por Definición de Límite

### (a) Calcular $\lim_{x\to a} \frac{f(x) - f(a)}{x-a}$, si $f(x) = \frac{1}{x^2}$ y $a \neq 0$.
> **Justificación:** Corresponde a la tasa de cambio instantánea. Operamos las fracciones del numerador y simplificamos el factor $(x-a)$ que produce la indeterminación.

**Desarrollo:**
$$\frac{f(x) - f(a)}{x - a} = \frac{\frac{1}{x^2} - \frac{1}{a^2}}{x - a} = \frac{\frac{a^2 - x^2}{a^2 x^2}}{x - a} = \frac{a^2 - x^2}{a^2 x^2 (x - a)}$$
Factorizamos $a^2 - x^2$ en el numerador:
$$\frac{-(x-a)(x+a)}{a^2 x^2 (x-a)}$$
Simplificando $(x-a)$ para $x \neq a$:
$$\lim_{x\to a} \frac{-(x+a)}{a^2 x^2} = \frac{-(a+a)}{a^2 a^2} = -\frac{2a}{a^4} = -\frac{2}{a^3}$$

**Respuesta:** El valor del límite es **$-\frac{2}{a^3}$**.

---

### (b) Calcular $\lim_{h\to0} \frac{f(x_0+h) - f(x_0)}{h}$, si $f(x) = \sqrt{x}$ y $x_0 \neq 0$.
> **Justificación:** Representa la derivada de la función raíz. Racionalizamos multiplicando por el conjugado del numerador. Dado que la función raíz real requiere argumentos no negativos, para $x_0 \neq 0$ se asume $x_0 > 0$.

**Desarrollo:**
$$\lim_{h\to0} \frac{\sqrt{x_0+h} - \sqrt{x_0}}{h} \cdot \frac{\sqrt{x_0+h} + \sqrt{x_0}}{\sqrt{x_0+h} + \sqrt{x_0}} = \lim_{h\to0} \frac{(x_0+h) - x_0}{h(\sqrt{x_0+h} + \sqrt{x_0})}$$
$$\quad = \lim_{h\to0} \frac{h}{h(\sqrt{x_0+h} + \sqrt{x_0})}$$
Simplificando $h$ para $h \neq 0$:
$$\lim_{h\to0} \frac{1}{\sqrt{x_0+h} + \sqrt{x_0}} = \frac{1}{\sqrt{x_0} + \sqrt{x_0}} = \frac{1}{2\sqrt{x_0}}$$

**Respuesta:** El valor del límite es **$\frac{1}{2\sqrt{x_0}}$** (donde $x_0 > 0$).

---

## Ejercicio 7: Límites por Descomposición Aditiva y Racionalización

> **Enunciado:** Calcular los siguientes límites:
> $$L_1 = \lim_{x\to-1} \frac{2 - \sqrt[3]{x+9}}{x+1} \quad \text{y} \quad L_2 = \lim_{x\to-1} \frac{\sqrt{x+5}-2}{x+1}$$
> y luego, considerando lo anterior, calcular
> $$L_3 = \lim_{x\to-1} \frac{\sqrt{x+5} - \sqrt[3]{x+9}}{x+1}$$

> **Justificación:** Calculamos $L_1$ por racionalización cúbica y $L_2$ por racionalización cuadrática. Para resolver $L_3$, expresamos el numerador sumando y restando la constante $2$, lo que descompone de forma natural el límite en la suma $L_1 + L_2$.

**Desarrollo:**

1. **Cálculo de $L_1$:**
   Multiplicamos y dividimos por el factor cuadrático conjugado $4 + 2\sqrt[3]{x+9} + \sqrt[3]{(x+9)^2}$:
   $$L_1 = \lim_{x\to-1} \frac{2 - \sqrt[3]{x+9}}{x+1} \cdot \frac{4 + 2\sqrt[3]{x+9} + \sqrt[3]{(x+9)^2}}{4 + 2\sqrt[3]{x+9} + \sqrt[3]{(x+9)^2}}$$
   $$L_1 = \lim_{x\to-1} \frac{8 - (x+9)}{(x+1)(4 + 2\sqrt[3]{x+9} + \sqrt[3]{(x+9)^2})} = \lim_{x\to-1} \frac{-(x+1)}{(x+1)(4 + 2\sqrt[3]{x+9} + \sqrt[3]{(x+9)^2})}$$
   Cancelando $(x+1)$ para $x \neq -1$:
   $$L_1 = \lim_{x\to-1} \frac{-1}{4 + 2\sqrt[3]{x+9} + \sqrt[3]{(x+9)^2}} = \frac{-1}{4 + 2(2) + 4} = -\frac{1}{12}$$

2. **Cálculo de $L_2$:**
   Multiplicamos y dividimos por el conjugado $(\sqrt{x+5} + 2)$:
   $$L_2 = \lim_{x\to-1} \frac{\sqrt{x+5} - 2}{x+1} \cdot \frac{\sqrt{x+5} + 2}{\sqrt{x+5} + 2}$$
   $$L_2 = \lim_{x\to-1} \frac{x+5-4}{(x+1)(\sqrt{x+5}+2)} = \lim_{x\to-1} \frac{x+1}{(x+1)(\sqrt{x+5}+2)}$$
   Cancelando $(x+1)$ para $x \neq -1$:
   $$L_2 = \lim_{x\to-1} \frac{1}{\sqrt{x+5}+2} = \frac{1}{\sqrt{4}+2} = \frac{1}{4}$$

3. **Cálculo de $L_3$:**
   Reescribimos el numerador sumando y restando 2:
   $$\frac{\sqrt{x+5} - \sqrt[3]{x+9}}{x+1} = \frac{(\sqrt{x+5}-2) + (2-\sqrt[3]{x+9})}{x+1} = \frac{\sqrt{x+5}-2}{x+1} + \frac{2-\sqrt[3]{x+9}}{x+1}$$
   Por el Álgebra de Límites, dado que tanto $L_1$ como $L_2$ existen por separado:
   $$L_3 = \lim_{x\to-1} \frac{\sqrt{x+5}-2}{x+1} + \lim_{x\to-1} \frac{2-\sqrt[3]{x+9}}{x+1} = L_2 + L_1$$
   Sustituyendo los valores hallados:
   $$L_3 = \frac{1}{4} + \left(-\frac{1}{12}\right) = \frac{3}{12} - \frac{1}{12} = \frac{2}{12} = \frac{1}{6}$$

**Respuesta:** Los límites calculados son:
- $L_1 =$ **$-\frac{1}{12}$**
- $L_2 =$ **$\frac{1}{4}$**
- $L_3 =$ **$\frac{1}{6}$**

---

## Ejercicio 8: Demostraciones con el Teorema del Sándwich

> **Teorema del Sándwich:** Si $g(x) \le f(x) \le h(x)$ en un entorno de $x_0$ (excepto posiblemente en $x_0$), y $\lim_{x\to x_0} g(x) = \lim_{x\to x_0} h(x) = L$, entonces $\lim_{x\to x_0} f(x) = L$.

---

### (a) Probar para $f(x) = \frac{x^2 \sin(x)}{x^2+1}$
> **Justificación:** Acotamos la función trigonométrica seno por su valor absoluto máximo $|\sin(x)| \le 1$.

**Desarrollo:**
1. Sabemos que $|\sin(x)| \le 1$. Como $\frac{x^2}{x^2+1} \ge 0$, multiplicamos a lo largo de la desigualdad:
   $$0 \le |f(x)| = \frac{x^2}{x^2+1} |\sin(x)| \le \frac{x^2}{x^2+1}$$
2. Puesto que $x^2 + 1 \ge 1 \implies \frac{1}{x^2+1} \le 1$, simplificamos la cota:
   $$0 \le |f(x)| \le x^2 \implies -x^2 \le f(x) \le x^2$$
3. Evaluando los límites de los extremos cuando $x \to 0$:
   $$\lim_{x\to0} (-x^2) = 0 \quad \text{y} \quad \lim_{x\to0} (x^2) = 0$$
4. Por el Teorema del Sándwich, concluimos que $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $-x^2 \le f(x) \le x^2$.

---

### (b) Probar para $f(x) = \frac{\sqrt{x+1}-1}{5x^2+1}$
> **Justificación:** Racionalizamos la diferencia del numerador para expresar el límite en términos de $|x|$ y acotar superiormente.

**Desarrollo:**
1. Racionalizamos el numerador:
   $$\sqrt{x+1}-1 = \frac{x}{\sqrt{x+1}+1}$$
   Sustituyendo esto en $f(x)$:
   $$f(x) = \frac{x}{(5x^2+1)(\sqrt{x+1}+1)}$$
2. En un entorno de $x=0$, por ejemplo, $x \in [-1/2, 1/2]$:
   $$5x^2+1 \ge 1 \quad \text{y} \quad \sqrt{x+1}+1 \ge 1$$
3. Por tanto, podemos acotar el valor absoluto:
   $$0 \le |f(x)| = \frac{|x|}{(5x^2+1)(\sqrt{x+1}+1)} \le |x| \implies -|x| \le f(x) \le |x|$$
4. Evaluando los límites laterales cuando $x \to 0$:
   $$\lim_{x\to0} (-|x|) = 0 \quad \text{y} \quad \lim_{x\to0} |x| = 0$$
5. Por el Teorema del Sándwich, concluimos que $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $-|x| \le f(x) \le |x|$.

---

### (c) Probar para $f(x) = \frac{x^2}{1+\sqrt{|x|}}$
> **Justificación:** El denominador es estrictamente mayor o igual a 1, lo cual acota superiormente de forma directa la fracción por $x^2$.

**Desarrollo:**
1. Como $\sqrt{|x|} \ge 0$, tenemos:
   $$1 + \sqrt{|x|} \ge 1 \implies \frac{1}{1+\sqrt{|x|}} \le 1$$
2. Como $x^2 \ge 0$:
   $$0 \le \frac{x^2}{1+\sqrt{|x|}} \le x^2$$
3. Tomando límites cuando $x \to 0$:
   $$\lim_{x\to0} 0 = 0 \quad \text{y} \quad \lim_{x\to0} x^2 = 0$$
4. Por el Teorema del Sándwich, $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $0 \le f(x) \le x^2$.

---

### (d) Probar para $f(x) = x^6 \sin(1/x)$
> **Justificación:** La oscilación infinita de $\sin(1/x)$ cerca de cero es controlada y anulada por la cota no negativa $x^6$.

**Desarrollo:**
1. Para todo $x \neq 0$:
   $$-1 \le \sin(1/x) \le 1$$
2. Como $x^6 \ge 0$ para todo número real $x$:
   $$-x^6 \le x^6 \sin(1/x) \le x^6$$
3. Tomando límites cuando $x \to 0$:
   $$\lim_{x\to0} (-x^6) = 0 \quad \text{y} \quad \lim_{x\to0} (x^6) = 0$$
4. Por el Teorema del Sándwich, $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $-x^6 \le f(x) \le x^6$.

---

### (e) Probar para $f(x) = \frac{3x^2+5}{2} |x| \sin\left(\frac{x^2}{x^2+1}\right)$
> **Justificación:** El término trigonométrico está acotado en $[-1, 1]$. El término polinómico lineal restante tiende a 0 al evaluar $x=0$. (Nota: Se considera la función bajo valor absoluto o regular en su término seno de acuerdo a la tipografía extraída).

**Desarrollo:**
1. Dado que $|\sin(\theta)| \le 1$ para cualquier argumento $\theta$:
   $$\left|\sin\left(\frac{x^2}{x^2+1}\right)\right| \le 1$$
2. Multiplicamos la desigualdad por el factor no negativo $\frac{3x^2+5}{2}|x|$:
   $$0 \le |f(x)| \le \frac{3x^2+5}{2}|x| \implies -\frac{3x^2+5}{2}|x| \le f(x) \le \frac{3x^2+5}{2}|x|$$
3. Calculamos el límite de la cota superior cuando $x \to 0$:
   $$\lim_{x\to0} \frac{3x^2+5}{2}|x| = \frac{5}{2} \cdot 0 = 0$$
4. Por el Teorema del Sándwich, concluimos que $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $-\frac{3x^2+5}{2}|x| \le f(x) \le \frac{3x^2+5}{2}|x|$.

---

### (f) Probar para $f(x) = \frac{|x|}{1+x^2+x^4}$
> **Justificación:** El denominador polinómico es mayor o igual a 1, acotando superiormente la función por $|x|$.

**Desarrollo:**
1. Como $x^2 \ge 0$ y $x^4 \ge 0$, tenemos:
   $$1 + x^2 + x^4 \ge 1 \implies \frac{1}{1+x^2+x^4} \le 1$$
2. Multiplicando por $|x| \ge 0$:
   $$0 \le \frac{|x|}{1+x^2+x^4} \le |x|$$
3. Tomando límites cuando $x \to 0$:
   $$\lim_{x\to0} 0 = 0 \quad \text{y} \quad \lim_{x\to0} |x| = 0$$
4. Por el Teorema del Sándwich, $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $0 \le f(x) \le |x|$.

---

### (g) Probar para $f(x) = x^3 \cos\left(\frac{\pi}{\sqrt[3]{x}}\right)$
> **Justificación:** Similar a las partes (d) y (a), el coseno está acotado superiormente por 1, y la potencia cúbica de $x$ anula el comportamiento al aproximarse a 0.

**Desarrollo:**
1. Para todo $x \neq 0$:
   $$\left|\cos\left(\frac{\pi}{\sqrt[3]{x}}\right)\right| \le 1$$
2. Multiplicando por $|x|^3 \ge 0$:
   $$0 \le |f(x)| = |x|^3 \left|\cos\left(\frac{\pi}{\sqrt[3]{x}}\right)\right| \le |x|^3 \implies -|x|^3 \le f(x) \le |x|^3$$
3. Tomando límites cuando $x \to 0$:
   $$\lim_{x\to0} (-|x|^3) = 0 \quad \text{y} \quad \lim_{x\to0} |x|^3 = 0$$
4. Por el Teorema del Sándwich, concluimos que $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $-|x|^3 \le f(x) \le |x|^3$.

---

### (h) Probar para $f(x) = |x|\sqrt{x^4+4x^2+7}$
> **Justificación:** La raíz cuadrática se aproxima a $\sqrt{7}$ cerca de cero. Acotamos localmente el radical en un entorno abierto de 0.

**Desarrollo:**
1. Restringimos $x$ al intervalo abierto $x \in ]-1, 1[$. En este entorno:
   $$0 \le x^2 < 1 \quad \text{y} \quad 0 \le x^4 < 1$$
2. Por tanto:
   $$x^4 + 4x^2 + 7 < 1 + 4(1) + 7 = 12 \implies \sqrt{x^4+4x^2+7} < \sqrt{12} = 2\sqrt{3}$$
3. Acotamos la función original para $x \in ]-1, 1[$:
   $$0 \le |f(x)| = |x|\sqrt{x^4+4x^2+7} < 2\sqrt{3}|x| \implies -2\sqrt{3}|x| \le f(x) \le 2\sqrt{3}|x|$$
4. Tomando límites cuando $x \to 0$:
   $$\lim_{x\to0} (-2\sqrt{3}|x|) = 0 \quad \text{y} \quad \lim_{x\to0} (2\sqrt{3}|x|) = 0$$
5. Por el Teorema del Sándwich, concluimos que $\lim_{x\to0} f(x) = 0$.

**Respuesta:** Queda probado mediante la cota $-2\sqrt{3}|x| \le f(x) \le 2\sqrt{3}|x|$ en $x \in ]-1, 1[$.

---

## Ejercicio 9: Demostración de Límite para Producto con Función Acotada

> **Enunciado:** Sea $M > 0$. Si $|f(x)| \le M$ para todo $x$ en un intervalo que contiene a cero, demuestre que $\lim_{x\to0} x^2f(x) = 0$.

> **Justificación:** Multiplicamos la cota uniforme de $f(x)$ por el término cuadrático $x^2 \ge 0$, aplicando luego el Teorema del Sándwich.

**Desarrollo:**
1. Sea $I$ el intervalo que contiene al origen tal que para todo $x \in I$ se tiene:
   $$|f(x)| \le M$$
2. Multiplicamos la desigualdad por $x^2$ (que es siempre no negativo):
   $$0 \le |x^2 f(x)| = x^2 |f(x)| \le M x^2$$
3. Esto es equivalente a la doble desigualdad:
   $$-M x^2 \le x^2 f(x) \le M x^2$$
4. Evaluamos los límites de los extremos cuando $x \to 0$:
   $$\lim_{x\to0} (-M x^2) = -M(0)^2 = 0$$
   $$\lim_{x\to0} (M x^2) = M(0)^2 = 0$$
5. Por el Teorema del Sándwich, dado que ambos extremos tienden a cero:
   $$\lim_{x\to0} x^2 f(x) = 0$$

**Respuesta:** Queda demostrado mediante la acotación $-M x^2 \le x^2 f(x) \le M x^2$.

---

## Ejercicio 10: Límite por Sandwich con Desigualdad de Valor Absoluto

> **Enunciado:** Si $f$ es una función real tal que $|f(x) - 1| \le x^2$ con $x \neq 0$, calcular $\lim_{x\to0} f(x)$.

> **Justificación:** Desglosamos la desigualdad de valor absoluto para encuadrar a la función $f(x)$ y aplicamos el Teorema del Sándwich directamente.

**Desarrollo:**
1. Despejamos el valor absoluto en la desigualdad dada:
   $$-x^2 \le f(x) - 1 \le x^2$$
2. Sumamos 1 a todos los términos de la desigualdad:
   $$1 - x^2 \le f(x) \le 1 + x^2$$
3. Tomamos límites laterales cuando $x \to 0$:
   $$\lim_{x\to0} (1 - x^2) = 1 - 0 = 1$$
   $$\lim_{x\to0} (1 + x^2) = 1 + 0 = 1$$
4. Puesto que los límites de las funciones cotas son idénticos e iguales a 1, por el Teorema del Sándwich:
   $$\lim_{x\to0} f(x) = 1$$

**Respuesta:** El valor del límite es $\lim_{x\to0} f(x) =$ **1**.

---

## Ejercicio 11: Límites Laterales, Existencia de Producto y Álgebra de Límites

> **Enunciado:** Sean $f, g : \mathbb{R} \to \mathbb{R}$ funciones definidas por
> $$f(x) = \begin{cases} x^2 + 1 & \text{si } x \le 1 \\ x + 3 & \text{si } x > 1 \end{cases} \quad \text{y} \quad g(x) = \begin{cases} x - 2 & \text{si } x \le 1 \\ -1/2 & \text{si } x > 1 \end{cases}$$
> respectivamente. Mostrar que $\lim_{x\to1} (f(x) \cdot g(x))$ existe, sin embargo, $\lim_{x\to1} f(x)$ y $\lim_{x\to1} g(x)$ no existen.  
> ¿Contradice esto el Teorema del Álgebra de Límites?

> **Justificación Pedagógica:** Un límite lateral diferente implica la inexistencia del límite general. Analizaremos los límites laterales de $f$ y $g$, luego deduciremos analíticamente el producto a trozos, mostrando la existencia de su límite y justificando lógicamente por qué no hay contradicción con el Álgebra de Límites.

**Desarrollo:**

1. **Análisis del límite para $f(x)$ en $x \to 1$:**
   Calculamos los límites laterales por definición a trozos:
   - Por la izquierda ($x \to 1^-$):
     $$\lim_{x\to1^-} f(x) = \lim_{x\to1^-} (x^2+1) = 1^2 + 1 = 2$$
   - Por la derecha ($x \to 1^+$):
     $$\lim_{x\to1^+} f(x) = \lim_{x\to1^+} (x+3) = 1 + 3 = 4$$
   Dado que $\lim_{x\to1^-} f(x) = 2 \neq 4 = \lim_{x\to1^+} f(x)$, concluimos que **$\lim_{x\to1} f(x)$ no existe**.

2. **Análisis del límite para $g(x)$ en $x \to 1$:**
   Calculamos los límites laterales:
   - Por la izquierda ($x \to 1^-$):
     $$\lim_{x\to1^-} g(x) = \lim_{x\to1^-} (x-2) = 1 - 2 = -1$$
   - Por la derecha ($x \to 1^+$):
     $$\lim_{x\to1^+} g(x) = \lim_{x\to1^+} (-1/2) = -1/2$$
   Dado que $\lim_{x\to1^-} g(x) = -1 \neq -1/2 = \lim_{x\to1^+} g(x)$, concluimos que **$\lim_{x\to1} g(x)$ no existe**.

3. **Análisis del límite para el producto $h(x) = f(x) \cdot g(x)$ en $x \to 1$:**
   Definimos $h(x)$ a trozos:
   $$h(x) = \begin{cases} (x^2+1)(x-2) & \text{si } x \le 1 \\ (x+3)\left(-\frac{1}{2}\right) = -\frac{x+3}{2} & \text{si } x > 1 \end{cases}$$
   Calculamos los límites laterales del producto $h(x)$:
   - Por la izquierda ($x \to 1^-$):
     $$\lim_{x\to1^-} h(x) = \lim_{x\to1^-} (x^2+1)(x-2) = (1^2+1)(1-2) = 2 \cdot (-1) = -2$$
   - Por la derecha ($x \to 1^+$):
     $$\lim_{x\to1^+} h(x) = \lim_{x\to1^+} \left( -\frac{x+3}{2} \right) = -\frac{1+3}{2} = -\frac{4}{2} = -2$$
   Dado que los límites laterales coinciden ($\lim_{x\to1^-} h(x) = \lim_{x\to1^+} h(x) = -2$), concluimos que **$\lim_{x\to1} (f(x) \cdot g(x))$ existe y vale $-2$**.

4. **Análisis sobre la supuesta contradicción del Teorema del Álgebra de Límites:**
   El Teorema del Álgebra de Límites es un enunciado condicional directo:
   $$\text{Si } (\lim_{x\to a} f(x) \text{ existe}) \wedge (\lim_{x\to a} g(x) \text{ existe}) \implies \lim_{x\to a} (f(x) \cdot g(x)) \text{ existe y es } \lim f(x) \cdot \lim g(x)$$
   Este teorema tiene la estructura lógica $P \implies Q$.  
   En nuestro caso, la hipótesis $P$ es **falsa** (ya que los límites individuales no existen). En lógica proposicional, si el antecedente de una implicación es falso ($F \implies Q$), la proposición condicional completa es **verdadera**, sin importar el valor de verdad del consecuente $Q$.  
   Por lo tanto, que el límite del producto exista no contradice de ningún modo al teorema. El teorema simplemente no aplica restricciones ni condiciones cuando los límites de los factores individuales no existen.

**Respuesta:**
- $\lim_{x\to1} f(x)$ no existe debido a que sus límites laterales difieren ($2 \neq 4$).
- $\lim_{x\to1} g(x)$ no existe debido a que sus límites laterales difieren ($-1 \neq -1/2$).
- $\lim_{x\to1} (f(x) \cdot g(x))$ **sí existe y es igual a $-2$**, puesto que sus límites laterales son iguales a $-2$.
- Este comportamiento **no contradice** el Teorema del Álgebra de Límites, ya que este solo regula el caso en que ambos límites factoriales existen.
