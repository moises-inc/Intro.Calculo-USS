---
id: "20260606-udec-listado-2-resolucion"
title: "Resolución Completa de Listado 2: Límites y Continuidad"
project: "UdeC_Calculo"
date: "2026-06-06T16:20:00"
last_modified: "2026-06-06T16:20:00"
type: "academic-note"
status: "completed"
priority: "medium"
tags: ["#status/completed", "#project/UdeC_Calculo", "#course/intro-calculo"]
---

# Guía Pedagógica Definitiva: Resolución de Listado 2
**Materia:** Cálculo Diferencial e Integral (527104)  
**Universidad:** Universidad de Concepción  
**Resolución:** Gemini Academic Assistant & Knowledge Engineer  

---

## Introducción Conceptual
Esta guía ha sido diseñada como un recurso de estudio exhaustivo y riguroso para dominar el cálculo de límites y el análisis de continuidad de funciones reales. Para cada ejercicio, se proporciona una **Justificación Pedagógica** que fundamenta el método elegido, un **Desarrollo Formal** detallado paso a paso utilizando lenguaje matemático algebraico estricto en LaTeX, y la **Respuesta** destacada.

Conforme a la **Directiva Crítica**, se omiten por completo métodos diferenciales (como la regla de L'Hôpital o derivadas directas para cálculo de límites) y se priorizan las identidades trigonométricas, factorizaciones algebraicas, racionalización, límites laterales y el Teorema de Bolzano.

---

## I. Límites Algebraicos y Trigonométricos (Pregunta 1)

### Pregunta 1(a): Calcular $\lim_{x\to 0} \frac{\sin^2(2x)}{8x^2}$
> **Justificación Pedagógica:** Para calcular este límite trigonométrico en forma indeterminada $0/0$, se utiliza el límite notable $\lim_{u\to 0} \frac{\sin(u)}{u} = 1$. Mediante manipulación algebraica, se reescribe el argumento para forzar la aparición de esta expresión.

**Desarrollo:**
1. Reescribimos la expresión asociando el exponente cuadrático:
   $$\lim_{x\to 0} \frac{\sin^2(2x)}{8x^2} = \lim_{x\to 0} \frac{1}{8} \left( \frac{\sin(2x)}{x} \right)^2$$
2. Multiplicamos y dividimos dentro del paréntesis por $2$ para igualar el de abajo con el argumento del seno ($2x$):
   $$\lim_{x\to 0} \frac{1}{8} \left( 2 \cdot \frac{\sin(2x)}{2x} \right)^2$$
3. Por propiedades del álgebra de límites y sabiendo que si $x \to 0$ entonces $2x \to 0$, aplicamos el límite notable $\lim_{u\to 0} \frac{\sin(u)}{u} = 1$:
   $$\frac{1}{8} \left( 2 \cdot \lim_{x\to 0} \frac{\sin(2x)}{2x} \right)^2 = \frac{1}{8} \left( 2 \cdot 1 \right)^2 = \frac{4}{8} = \frac{1}{2}$$

**Respuesta:**
$$\mathbf{\frac{1}{2}}$$

---

### Pregunta 1(b): Calcular $\lim_{x\to 1} \frac{\pi \sin(\pi/x)}{2x - 2}$
> **Justificación Pedagógica:** El límite presenta la indeterminación $0/0$. Realizaremos un cambio de variable para trasladar el límite al origen ($u \to 0$) y luego utilizaremos la identidad del seno de la diferencia de ángulos $\sin(\pi - \theta) = \sin(\theta)$ para aplicar el límite notable.

**Desarrollo:**
1. Definimos el cambio de variable $u = x - 1$, por lo tanto, $x = u + 1$. Cuando $x \to 1$, se tiene que $u \to 0$.
2. Sustituimos en el límite original:
   $$\lim_{u\to 0} \frac{\pi \sin\left(\frac{\pi}{u+1}\right)}{2(u+1) - 2} = \lim_{u\to 0} \frac{\pi \sin\left(\frac{\pi}{u+1}\right)}{2u}$$
3. Manipulamos el argumento del seno:
   $$\frac{\pi}{u+1} = \pi \left( 1 - \frac{u}{u+1} \right) = \pi - \frac{\pi u}{u+1}$$
4. Aplicamos la identidad trigonométrica $\sin(\pi - \theta) = \sin(\theta)$:
   $$\sin\left(\frac{\pi}{u+1}\right) = \sin\left(\pi - \frac{\pi u}{u+1}\right) = \sin\left(\frac{\pi u}{u+1}\right)$$
5. Sustituimos de vuelta en el límite y multiplicamos/dividimos por $\frac{\pi}{u+1}$ para forzar el límite notable:
   $$\lim_{u\to 0} \frac{\pi \sin\left(\frac{\pi u}{u+1}\right)}{2u} = \lim_{u\to 0} \left[ \frac{\pi}{2} \cdot \frac{\sin\left(\frac{\pi u}{u+1}\right)}{\frac{\pi u}{u+1}} \cdot \frac{\pi}{u+1} \right]$$
6. Dado que $\lim_{u\to 0} \frac{\pi u}{u+1} = 0$, aplicando el límite notable y el álgebra de límites:
   $$\frac{\pi}{2} \cdot \left( \lim_{u\to 0} \frac{\sin\left(\frac{\pi u}{u+1}\right)}{\frac{\pi u}{u+1}} \right) \cdot \left( \lim_{u\to 0} \frac{\pi}{u+1} \right) = \frac{\pi}{2} \cdot 1 \cdot \frac{\pi}{1} = \frac{\pi^2}{2}$$

**Respuesta:**
$$\mathbf{\frac{\pi^2}{2}}$$

---

### Pregunta 1(c): Calcular $\lim_{x\to 1} \frac{\sin(\pi x)}{\sin(3\pi x)}$
> **Justificación Pedagógica:** Este límite presenta una indeterminación $0/0$. Utilizaremos un cambio de variable $u = x - 1$ para trasladar la variable al origen $0$ y aplicaremos la identidad $\sin(\theta + k\pi)$ para simplificar.

**Desarrollo:**
1. Definimos $u = x - 1$, de modo que $x = u + 1$. Cuando $x \to 1$, $u \to 0$.
2. Expresamos el límite en términos de $u$:
   $$\lim_{u\to 0} \frac{\sin(\pi(u+1))}{\sin(3\pi(u+1))} = \lim_{u\to 0} \frac{\sin(\pi u + \pi)}{\sin(3\pi u + 3\pi)}$$
3. Usamos la propiedad de reducción al primer cuadrante: $\sin(\theta + \pi) = -\sin(\theta)$ y $\sin(\theta + 3\pi) = -\sin(\theta)$.
   $$\lim_{u\to 0} \frac{-\sin(\pi u)}{-\sin(3\pi u)} = \lim_{u\to 0} \frac{\sin(\pi u)}{\sin(3\pi u)}$$
4. Dividimos el numerador y el denominador por $u$ para aplicar el límite notable:
   $$\lim_{u\to 0} \frac{\frac{\sin(\pi u)}{u}}{\frac{\sin(3\pi u)}{u}} = \frac{\lim_{u\to 0} \pi \cdot \frac{\sin(\pi u)}{\pi u}}{\lim_{u\to 0} 3\pi \cdot \frac{\sin(3\pi u)}{3\pi u}} = \frac{\pi \cdot 1}{3\pi \cdot 1} = \frac{1}{3}$$

**Respuesta:**
$$\mathbf{\frac{1}{3}}$$

---

### Pregunta 1(d): Calcular (P) $\lim_{x\to 1} \frac{\cos( x\pi/2 )}{1 - \sqrt{x}}$
> **Justificación Pedagógica:** La indeterminación $0/0$ se aborda racionalizando primero el denominador para eliminar el radical, y luego mediante un cambio de variable y el uso de identidades de co-función del seno y coseno.

**Desarrollo:**
1. Racionalizamos el denominador multiplicando por el conjugado $(1 + \sqrt{x})$:
   $$\lim_{x\to 1} \frac{\cos\left(\frac{x\pi}{2}\right)(1 + \sqrt{x})}{(1 - \sqrt{x})(1 + \sqrt{x})} = \lim_{x\to 1} \frac{\cos\left(\frac{x\pi}{2}\right)(1 + \sqrt{x})}{1 - x}$$
2. Hacemos el cambio de variable $u = x - 1$, por lo que $x = u + 1$. Cuando $x \to 1$, $u \to 0$. El denominador resulta $1 - x = -u$.
3. Evaluamos el término de coseno en la nueva variable:
   $$\cos\left(\frac{(u+1)\pi}{2}\right) = \cos\left(\frac{u\pi}{2} + \frac{\pi}{2}\right)$$
4. Usamos la identidad de ángulo complementario $\cos(\theta + \pi/2) = -\sin(\theta)$:
   $$\cos\left(\frac{u\pi}{2} + \frac{\pi}{2}\right) = -\sin\left(\frac{u\pi}{2}\right)$$
5. Reemplazamos en el límite:
   $$\lim_{u\to 0} \frac{-\sin\left(\frac{u\pi}{2}\right)(1 + \sqrt{u+1})}{-u} = \lim_{u\to 0} \frac{\sin\left(\frac{u\pi}{2}\right)}{u} \cdot (1 + \sqrt{u+1})$$
6. Multiplicamos y dividimos por $\frac{\pi}{2}$:
   $$\lim_{u\to 0} \left[ \frac{\pi}{2} \cdot \frac{\sin\left(\frac{u\pi}{2}\right)}{\frac{u\pi}{2}} \cdot (1 + \sqrt{u+1}) \right] = \frac{\pi}{2} \cdot 1 \cdot (1 + \sqrt{1}) = \frac{\pi}{2} \cdot 2 = \pi$$

**Respuesta:**
$$\mathbf{\pi}$$

---

### Pregunta 1(e): Calcular (P) $\lim_{x\to 0} \frac{2x - \cot(x)}{x + 3\cot(x)}$
> **Justificación Pedagógica:** Este límite no requiere variables auxiliares ni es indeterminado si primero se multiplica toda la fracción por $\sin(x)$ para eliminar las funciones que divergen al infinito ($\cot(x) \to \pm\infty$ cuando $x \to 0$).

**Desarrollo:**
1. Escribimos la cotangente en términos de senos y cosenos: $\cot(x) = \frac{\cos(x)}{\sin(x)}$.
2. Multiplicamos el numerador y denominador por $\sin(x)$ (válido para $x \neq 0$):
   $$\lim_{x\to 0} \frac{2x - \frac{\cos(x)}{\sin(x)}}{x + 3\frac{\cos(x)}{\sin(x)}} = \lim_{x\to 0} \frac{2x\sin(x) - \cos(x)}{x\sin(x) + 3\cos(x)}$$
3. Evaluamos por sustitución directa ya que el denominador no se anula:
   $$\frac{2(0)\sin(0) - \cos(0)}{0\sin(0) + 3\cos(0)} = \frac{0 - 1}{0 + 3(1)} = -\frac{1}{3}$$

**Respuesta:**
$$\mathbf{-\frac{1}{3}}$$

---

### Pregunta 1(f): Calcular $\lim_{x\to \pi} \frac{\tan^2(x)}{1 + \sec(x)}$
> **Justificación Pedagógica:** La indeterminación $0/0$ se resuelve utilizando la identidad pitagórica $\tan^2(x) = \sec^2(x) - 1$ para simplificar la fracción mediante factorización por diferencia de cuadrados.

**Desarrollo:**
1. Reemplazamos $\tan^2(x)$ por $\sec^2(x) - 1$:
   $$\lim_{x\to \pi} \frac{\sec^2(x) - 1}{1 + \sec(x)}$$
2. Factorizamos el numerador como una diferencia de cuadrados:
   $$\lim_{x\to \pi} \frac{(\sec(x) - 1)(\sec(x) + 1)}{\sec(x) + 1}$$
3. Simplificamos el término común $\sec(x) + 1$, dado que $x \neq \pi$ en el proceso del límite:
   $$\lim_{x\to \pi} (\sec(x) - 1)$$
4. Evaluamos el límite:
   $$\sec(\pi) - 1 = -1 - 1 = -2$$

**Respuesta:**
$$\mathbf{-2}$$

---

### Pregunta 1(g): Calcular $\lim_{x\to \pi/3} \frac{1 - 2 \cos x}{\sin(x - \pi/3)}$
> **Justificación Pedagógica:** Para salvar la indeterminación $0/0$, aplicamos el cambio de variable $u = x - \pi/3$, expandimos el término de coseno en la nueva variable utilizando fórmulas de adición y separamos el límite en formas notables.

**Desarrollo:**
1. Definimos $u = x - \frac{\pi}{3} \implies x = u + \frac{\pi}{3}$. Cuando $x \to \frac{\pi}{3}$, $u \to 0$.
2. Expresamos el término de coseno del numerador:
   $$\cos\left(u + \frac{\pi}{3}\right) = \cos(u)\cos\left(\frac{\pi}{3}\right) - \sin(u)\sin\left(\frac{\pi}{3}\right)$$
   Sustituyendo los valores conocidos $\cos(\pi/3) = 1/2$ y $\sin(\pi/3) = \sqrt{3}/2$:
   $$\cos\left(u + \frac{\pi}{3}\right) = \frac{1}{2}\cos(u) - \frac{\sqrt{3}}{2}\sin(u)$$
3. Sustituimos esto en el numerador del límite:
   $$1 - 2\cos\left(u + \frac{\pi}{3}\right) = 1 - 2\left(\frac{1}{2}\cos(u) - \frac{\sqrt{3}}{2}\sin(u)\right) = 1 - \cos(u) + \sqrt{3}\sin(u)$$
4. Colocamos todo en la expresión del límite sobre el denominador $\sin(u)$:
   $$\lim_{u\to 0} \frac{1 - \cos(u) + \sqrt{3}\sin(u)}{\sin(u)} = \lim_{u\to 0} \left[ \frac{1 - \cos(u)}{\sin(u)} + \sqrt{3} \right]$$
5. Analizamos el primer término multiplicando y dividiendo por $u$:
   $$\lim_{u\to 0} \frac{1 - \cos(u)}{\sin(u)} = \lim_{u\to 0} \left( \frac{1 - \cos(u)}{u} \cdot \frac{u}{\sin(u)} \right) = 0 \cdot 1 = 0$$
6. Por lo tanto, el límite final es:
   $$0 + \sqrt{3} = \sqrt{3}$$

**Respuesta:**
$$\mathbf{\sqrt{3}}$$

---

### Pregunta 1(h): Calcular $\lim_{x\to 0} \frac{\sqrt{2} - \sqrt{1 + \cos(x)}}{\sin^2(x)}$
> **Justificación Pedagógica:** La presencia de radicales y la forma indeterminada $0/0$ sugieren racionalizar el numerador. Luego, aplicamos identidades pitagóricas para cancelar los factores que anulan el denominador.

**Desarrollo:**
1. Multiplicamos y dividimos por el conjugado del numerador:
   $$\lim_{x\to 0} \frac{\sqrt{2} - \sqrt{1 + \cos(x)}}{\sin^2(x)} \cdot \frac{\sqrt{2} + \sqrt{1 + \cos(x)}}{\sqrt{2} + \sqrt{1 + \cos(x)}} = \lim_{x\to 0} \frac{2 - (1 + \cos(x))}{\sin^2(x)(\sqrt{2} + \sqrt{1 + \cos(x)})}$$
   $$= \lim_{x\to 0} \frac{1 - \cos(x)}{\sin^2(x)(\sqrt{2} + \sqrt{1 + \cos(x)})}$$
2. Usamos la identidad fundamental $\sin^2(x) = 1 - \cos^2(x) = (1 - \cos(x))(1 + \cos(x))$:
   $$= \lim_{x\to 0} \frac{1 - \cos(x)}{(1 - \cos(x))(1 + \cos(x))(\sqrt{2} + \sqrt{1 + \cos(x)})}$$
3. Cancelamos el factor común $(1 - \cos(x))$ para $x \neq 0$:
   $$= \lim_{x\to 0} \frac{1}{(1 + \cos(x))(\sqrt{2} + \sqrt{1 + \cos(x)})}$$
4. Evaluamos por sustitución directa:
   $$\frac{1}{(1 + \cos(0))(\sqrt{2} + \sqrt{1 + \cos(0)})} = \frac{1}{(1 + 1)(\sqrt{2} + \sqrt{1 + 1})} = \frac{1}{2(2\sqrt{2})} = \frac{1}{4\sqrt{2}} = \frac{\sqrt{2}}{8}$$

**Respuesta:**
$$\mathbf{\frac{\sqrt{2}}{8}}$$

---

### Pregunta 1(i): Calcular $\lim_{h\to 0} \frac{\cos(x + h) - \cos(x)}{h}$
> **Justificación Pedagógica:** Este límite representa la definición formal de la derivada de la función $\cos(x)$. Lo resolveremos utilizando identidades trigonométricas de suma de ángulos para descomponer la expresión y aplicar los límites notables de las funciones trigonométricas en el origen.

**Desarrollo:**
1. Expandimos el término $\cos(x + h)$ mediante la identidad de la suma de ángulos:
   $$\cos(x + h) = \cos(x)\cos(h) - \sin(x)\sin(h)$$
2. Sustituimos esta expansión en el límite:
   $$\lim_{h\to 0} \frac{\cos(x)\cos(h) - \sin(x)\sin(h) - \cos(x)}{h}$$
3. Agrupamos los términos con factor común $\cos(x)$:
   $$\lim_{h\to 0} \left[ \cos(x)\frac{\cos(h) - 1}{h} - \sin(x)\frac{\sin(h)}{h} \right]$$
4. Aplicamos los límites notables conocidos: $\lim_{h\to 0} \frac{\cos(h) - 1}{h} = 0$ y $\lim_{h\to 0} \frac{\sin(h)}{h} = 1$:
   $$\cos(x) \cdot (0) - \sin(x) \cdot (1) = -\sin(x)$$

**Respuesta:**
$$\mathbf{-\sin(x)}$$

---

### Pregunta 1(j): Calcular $\lim_{t\to \pi/4} \frac{2 \sin(t - \pi/4)}{4t - \pi}$
> **Justificación Pedagógica:** La indeterminación es de tipo $0/0$. Factorizamos la constante $4$ del denominador para hacer explícita la estructura del límite notable $\frac{\sin(u)}{u}$ mediante un simple cambio de variable.

**Desarrollo:**
1. Escribimos el denominador factorizando por 4:
   $$4t - \pi = 4\left(t - \frac{\pi}{4}\right)$$
2. Sustituimos en el límite original:
   $$\lim_{t\to \pi/4} \frac{2 \sin(t - \pi/4)}{4\left(t - \frac{\pi}{4}\right)} = \frac{1}{2} \lim_{t\to \pi/4} \frac{\sin(t - \pi/4)}{t - \pi/4}$$
3. Realizamos el cambio de variable $u = t - \frac{\pi}{4}$, por ende $u \to 0$ cuando $t \to \frac{\pi}{4}$:
   $$\frac{1}{2} \lim_{u\to 0} \frac{\sin(u)}{u} = \frac{1}{2} \cdot 1 = \frac{1}{2}$$

**Respuesta:**
$$\mathbf{\frac{1}{2}}$$

---

### Pregunta 1(k): Calcular $\lim_{x\to 5} \frac{2 \tan(x - 5)}{x^2 - 6x + 5}$
> **Justificación Pedagógica:** El límite presenta indeterminación $0/0$. Factorizaremos el polinomio cuadrático en el denominador y aplicaremos la descomposición de la tangente en seno y coseno para resolver mediante el límite notable.

**Desarrollo:**
1. Factorizamos el denominador cuadrático:
   $$x^2 - 6x + 5 = (x - 5)(x - 1)$$
2. Reescribimos la función bajo el límite:
   $$\lim_{x\to 5} \frac{2 \tan(x - 5)}{(x - 5)(x - 1)} = \lim_{x\to 5} \left[ \frac{\tan(x - 5)}{x - 5} \cdot \frac{2}{x - 1} \right]$$
3. Descomponemos $\tan(x - 5) = \frac{\sin(x - 5)}{\cos(x - 5)}$:
   $$\lim_{x\to 5} \left[ \frac{\sin(x - 5)}{x - 5} \cdot \frac{2}{\cos(x - 5)(x - 1)} \right]$$
4. Realizamos el cambio de variable $u = x - 5$, por lo que $u \to 0$ cuando $x \to 5$. Además, $x - 1 = u + 4$:
   $$\left( \lim_{u\to 0} \frac{\sin(u)}{u} \right) \cdot \left( \lim_{u\to 0} \frac{2}{\cos(u)(u + 4)} \right) = 1 \cdot \frac{2}{\cos(0)(0 + 4)} = \frac{2}{4} = \frac{1}{2}$$

**Respuesta:**
$$\mathbf{\frac{1}{2}}$$

---

### Pregunta 1(l): Calcular (P) $\lim_{x\to a} \frac{\sin(x) - \sin(a)}{x - a}$
> **Justificación Pedagógica:** Esta es la definición de la derivada de la función $\sin(x)$ en $x = a$. Se resuelve aplicando la identidad trigonométrica de transformación de diferencia de senos a producto.

**Desarrollo:**
1. Utilizamos la identidad:
   $$\sin(x) - \sin(a) = 2 \sin\left(\frac{x - a}{2}\right) \cos\left(\frac{x + a}{2}\right)$$
2. Sustituimos esta expresión en el límite:
   $$\lim_{x\to a} \frac{2 \sin\left(\frac{x - a}{2}\right) \cos\left(\frac{x + a}{2}\right)}{x - a}$$
3. Definimos la variable $u = \frac{x - a}{2}$, lo que implica que $x - a = 2u$. Cuando $x \to a$, se cumple que $u \to 0$.
4. Reemplazamos en el límite y simplificamos la constante $2$:
   $$\lim_{u\to 0} \frac{2 \sin(u) \cos\left(\frac{2u + 2a}{2}\right)}{2u} = \lim_{u\to 0} \left[ \frac{\sin(u)}{u} \cdot \cos(u + a) \right]$$
5. Evaluamos el límite aplicando las propiedades del producto:
   $$\left( \lim_{u\to 0} \frac{\sin(u)}{u} \right) \cdot \left( \lim_{u\to 0} \cos(u + a) \right) = 1 \cdot \cos(a) = \cos(a)$$

**Respuesta:**
$$\mathbf{\cos(a)}$$

---

### Pregunta 1(m): Calcular $\lim_{x\to \pi/4} \frac{2 \cos(x) - \sqrt{2}}{x - \pi/4}$
> **Justificación Pedagógica:** La indeterminación es del tipo $0/0$. Utilizaremos la identidad de diferencia de cosenos a producto tras factorizar un coeficiente constante.

**Desarrollo:**
1. Factorizamos la constante $2$ en el numerador:
   $$2\cos(x) - \sqrt{2} = 2\left(\cos(x) - \frac{\sqrt{2}}{2}\right) = 2\left(\cos(x) - \cos\left(\frac{\pi}{4}\right)\right)$$
2. Aplicamos la identidad de la diferencia de cosenos:
   $$\cos(x) - \cos\left(\frac{\pi}{4}\right) = -2 \sin\left(\frac{x - \frac{\pi}{4}}{2}\right) \sin\left(\frac{x + \frac{\pi}{4}}{2}\right)$$
3. Sustituimos esta expresión en el límite:
   $$\lim_{x\to \pi/4} \frac{-4 \sin\left(\frac{x - \frac{\pi}{4}}{2}\right) \sin\left(\frac{x + \frac{\pi}{4}}{2}\right)}{x - \pi/4}$$
4. Hacemos el cambio de variable $u = \frac{x - \frac{\pi}{4}}{2} \implies x - \frac{\pi}{4} = 2u$. Cuando $x \to \frac{\pi}{4}$, $u \to 0$.
5. Reemplazamos los términos y simplificamos:
   $$\lim_{u\to 0} \frac{-4 \sin(u) \sin\left(u + \frac{\pi}{4}\right)}{2u} = \lim_{u\to 0} \left[ -2 \frac{\sin(u)}{u} \cdot \sin\left(u + \frac{\pi}{4}\right) \right]$$
6. Evaluamos el límite:
   $$-2 \cdot 1 \cdot \sin\left(0 + \frac{\pi}{4}\right) = -2 \cdot \frac{\sqrt{2}}{2} = -\sqrt{2}$$

**Respuesta:**
$$\mathbf{-\sqrt{2}}$$

---

### Pregunta 1(n): Calcular (P) $\lim_{x\to 0} \left[ \frac{x^2}{1 - \cos(x)} + \frac{x^4 + x^2}{\sin(x^2)} \right]$
> **Justificación Pedagógica:** Aplicamos la propiedad de la suma de límites para separar la expresión en dos límites independientes. Racionalizaremos el primero y usaremos un cambio de variable en el segundo para reducirlos a límites notables.

**Desarrollo:**
1. Definimos $L_1 = \lim_{x\to 0} \frac{x^2}{1 - \cos(x)}$ y $L_2 = \lim_{x\to 0} \frac{x^4 + x^2}{\sin(x^2)}$.
2. Calculamos $L_1$ multiplicando y dividiendo por el conjugado del denominador $(1 + \cos(x))$:
   $$L_1 = \lim_{x\to 0} \frac{x^2(1 + \cos(x))}{1 - \cos^2(x)} = \lim_{x\to 0} \frac{x^2(1 + \cos(x))}{\sin^2(x)} = \lim_{x\to 0} \left[ \left(\frac{x}{\sin(x)}\right)^2 (1 + \cos(x)) \right]$$
   $$L_1 = (1)^2 \cdot (1 + 1) = 2$$
3. Calculamos $L_2$ factorizando $x^2$ en el numerador:
   $$L_2 = \lim_{x\to 0} \frac{x^2(x^2 + 1)}{\sin(x^2)} = \lim_{x\to 0} \left[ \frac{x^2}{\sin(x^2)} \cdot (x^2 + 1) \right]$$
   Haciendo el cambio de variable $u = x^2$ (donde $u \to 0$ cuando $x \to 0$):
   $$L_2 = \left( \lim_{u\to 0} \frac{u}{\sin(u)} \right) \cdot \left( \lim_{x\to 0} (x^2 + 1) \right) = 1 \cdot 1 = 1$$
4. Sumamos ambos resultados:
   $$L = L_1 + L_2 = 2 + 1 = 3$$

**Respuesta:**
$$\mathbf{3}$$

---

## II. Límites Laterales y Análisis de Existencia (Pregunta 2)

### Pregunta 2(a): Analizar la existencia de $\lim_{x\to 0} \frac{|x^3| - x^2}{|x|}$
> **Justificación Pedagógica:** Para analizar la existencia de este límite con valor absoluto, utilizaremos propiedades algebraicas elementales del valor absoluto ($|x^3| = |x|^3$ y $x^2 = |x|^2$) con el fin de simplificar la expresión para todo $x \neq 0$.

**Desarrollo:**
1. Reescribimos los términos en términos del valor absoluto $|x|$:
   $$\frac{|x|^3 - |x|^2}{|x|}$$
2. Factorizamos el numerador por el término común $|x|^2$:
   $$\frac{|x|^2(|x| - 1)}{|x|}$$
3. Dado que $x \neq 0$, simplificamos la fracción dividiendo por $|x|$:
   $$|x|(|x| - 1)$$
4. Evaluamos el límite mediante sustitución directa:
   $$\lim_{x\to 0} |x|(|x| - 1) = 0 \cdot (0 - 1) = 0$$
   Dado que el límite evaluado por ambos lados es único y finito, el límite existe.

**Respuesta:**
**Existe** y su valor es $\mathbf{0}$.

---

### Pregunta 2(b): Analizar la existencia de $\lim_{x\to 2^-} \frac{x^4 - 4x^2}{|x^2 - x - 2|}$
> **Justificación Pedagógica:** Evaluamos el límite lateral izquierdo en $x = 2$. Debemos determinar el signo de la expresión cuadrática dentro del valor absoluto en el intervalo lateral correspondiente para remover el operador absoluto de manera adecuada.

**Desarrollo:**
1. Factorizamos el numerador y el trinomio del denominador:
   - Numerador: $x^4 - 4x^2 = x^2(x^2 - 4) = x^2(x - 2)(x + 2)$
   - Denominador: $x^2 - x - 2 = (x - 2)(x + 1)$
2. Analizamos el signo de $(x - 2)(x + 1)$ cuando $x \to 2^-$ (es decir, $x < 2$ con $x$ cercano a 2):
   - Como $x < 2$, entonces $x - 2 < 0$.
   - Como $x \approx 2$, entonces $x + 1 > 0$.
   - Por lo tanto, el producto $(x - 2)(x + 1) < 0$.
3. Aplicamos la definición de valor absoluto para una cantidad negativa:
   $$|x^2 - x - 2| = -(x^2 - x - 2) = -(x - 2)(x + 1)$$
4. Reescribimos la función bajo el límite lateral y simplificamos el factor común $(x - 2)$ (ya que $x \neq 2$):
   $$\lim_{x\to 2^-} \frac{x^2(x - 2)(x + 2)}{-(x - 2)(x + 1)} = \lim_{x\to 2^-} -\frac{x^2(x + 2)}{x + 1}$$
5. Evaluamos el límite sustituyendo $x = 2$:
   $$-\frac{2^2(2 + 2)}{2 + 1} = -\frac{4 \cdot 4}{3} = -\frac{16}{3}$$

**Respuesta:**
**Existe** (como límite lateral izquierdo) y su valor es $\mathbf{-\frac{16}{3}}$.

---

### Pregunta 2(c): Analizar la existencia de $\lim_{x\to 3} \frac{-x^2 + 2x + 3}{|x - 3|}$
> **Justificación Pedagógica:** Para analizar el límite bidireccional en un punto crítico del valor absoluto ($x = 3$), calculamos los dos límites laterales. Si los resultados son distintos, el límite no existe.

**Desarrollo:**
1. Factorizamos el polinomio del numerador:
   $$-x^2 + 2x + 3 = -(x^2 - 2x - 3) = -(x - 3)(x + 1)$$
2. Evaluamos el límite lateral izquierdo ($x \to 3^-$), donde $x < 3 \implies |x - 3| = -(x - 3)$:
   $$\lim_{x\to 3^-} \frac{-(x - 3)(x + 1)}{-(x - 3)} = \lim_{x\to 3^-} (x + 1) = 3 + 1 = 4$$
3. Evaluamos el límite lateral derecho ($x \to 3^+$), donde $x > 3 \implies |x - 3| = x - 3$:
   $$\lim_{x\to 3^+} \frac{-(x - 3)(x + 1)}{x - 3} = \lim_{x\to 3^+} -(x + 1) = -(3 + 1) = -4$$
4. Comparamos los límites laterales:
   $$\lim_{x\to 3^-} f(x) = 4 \neq -4 = \lim_{x\to 3^+} f(x)$$
   Dado que los límites laterales difieren, el límite bidireccional no existe.

**Respuesta:**
**No existe** porque los límites laterales son distintos ($4 \neq -4$).

---

### Pregunta 2(d): Analizar la existencia de $\lim_{x\to 0^+} \frac{3|x| + 1}{x|x| - 3x}$
> **Justificación Pedagógica:** Evaluamos el límite por la derecha de $x = 0$. Reemplazamos $|x|$ por $x$ debido a la restricción $x > 0$, simplificamos y estudiamos la existencia de asíntotas verticales analizando el signo del denominador.

**Desarrollo:**
1. Dado que $x \to 0^+$, tenemos que $x > 0$, de donde $|x| = x$.
2. Sustituimos en la expresión:
   $$\lim_{x\to 0^+} \frac{3x + 1}{x^2 - 3x} = \lim_{x\to 0^+} \frac{3x + 1}{x(x - 3)}$$
3. Analizamos el comportamiento numérico de la fracción cuando $x \to 0^+$:
   - El numerador tiende a $3(0) + 1 = 1 > 0$.
   - El factor $(x - 3)$ en el denominador tiende a $0 - 3 = -3 < 0$.
   - El factor $x$ en el denominador tiende a $0$ a través de valores positivos.
   - El producto del denominador $x(x - 3)$ tiende a $0$ a través de valores negativos (se denota como $0^-$).
4. El límite resulta de la forma $\frac{1}{0^-} = -\infty$.

**Respuesta:**
**No existe** (diverge a $\mathbf{-\infty}$).

---

### Pregunta 2(e): Analizar la existencia de $\lim_{x\to 0^+} \frac{|x|}{x + |x|}$
> **Justificación Pedagógica:** En el entorno lateral derecho de $0$, la variable es estrictamente positiva ($x > 0$), por lo que removemos el valor absoluto reemplazándolo por la misma variable.

**Desarrollo:**
1. Dado que $x > 0$, sustituimos $|x| = x$:
   $$\lim_{x\to 0^+} \frac{x}{x + x} = \lim_{x\to 0^+} \frac{x}{2x}$$
2. Simplificamos la variable $x$ (ya que $x \neq 0$):
   $$\lim_{x\to 0^+} \frac{1}{2} = \frac{1}{2}$$

**Respuesta:**
**Existe** (como límite lateral derecho) y su valor es $\mathbf{\frac{1}{2}}$.

---

### Pregunta 2(f): Analizar la existencia de $\lim_{x\to 2^-} \frac{(x - 3)\sqrt{4 - x^2}}{x^2 - 4}$
> **Justificación Pedagógica:** Este límite lateral se analiza factorizando y simplificando el término indeterminado mediante raíces cuadradas. Debemos verificar si el límite diverge al infinito o converge.

**Desarrollo:**
1. Reescribimos el denominador utilizando una diferencia de cuadrados:
   $$x^2 - 4 = -(4 - x^2)$$
2. Expresamos el término $(4 - x^2)$ como $(\sqrt{4 - x^2})^2$ para $x \in (-2, 2)$:
   $$\frac{(x - 3)\sqrt{4 - x^2}}{-(4 - x^2)} = \frac{(x - 3)\sqrt{4 - x^2}}{-(\sqrt{4 - x^2})^2} = -\frac{x - 3}{\sqrt{4 - x^2}} = \frac{3 - x}{\sqrt{4 - x^2}}$$
3. Estudiamos el comportamiento del límite cuando $x \to 2^-$:
   - El numerador tiende a $3 - 2 = 1 > 0$.
   - El denominador $\sqrt{4 - x^2}$ tiende a $0$ a través de valores positivos ($0^+$).
4. La forma límite es $\frac{1}{0^+} = +\infty$.

**Respuesta:**
**No existe** (diverge a $\mathbf{+\infty}$).

---

### Pregunta 2(g): Analizar la existencia de $\lim_{x\to 0^+} \frac{\sqrt{x}}{\sqrt{x + \sqrt{x}}}$
> **Justificación Pedagógica:** Para resolver la indeterminación $0/0$ en este límite lateral derecho, simplificamos algebraicamente la fracción extrayendo el término $\sqrt{x}$ del radical del denominador.

**Desarrollo:**
1. Factorizamos $\sqrt{x}$ dentro del radical del denominador:
   $$\sqrt{x + \sqrt{x}} = \sqrt{\sqrt{x}(\sqrt{x} + 1)} = \sqrt[4]{x}\sqrt{\sqrt{x} + 1}$$
2. Reescribimos la fracción y simplificamos los exponentes de $x$:
   $$\frac{\sqrt{x}}{\sqrt[4]{x}\sqrt{\sqrt{x} + 1}} = \frac{x^{1/2}}{x^{1/4}\sqrt{\sqrt{x} + 1}} = \frac{x^{1/4}}{\sqrt{\sqrt{x} + 1}}$$
3. Evaluamos el límite haciendo $x \to 0^+$:
   $$\lim_{x\to 0^+} \frac{x^{1/4}}{\sqrt{\sqrt{x} + 1}} = \frac{0^{1/4}}{\sqrt{0 + 1}} = \frac{0}{1} = 0$$

**Respuesta:**
**Existe** y su valor es $\mathbf{0}$.

---

### Pregunta 2(h): (P) Analizar la existencia de $\lim_{x\to 2} \frac{x^2 + |2 - x| - 4}{x^2 - 4}$
> **Justificación Pedagógica:** La función contiene un valor absoluto con punto de transición en $x = 2$. Analizamos por separado los límites laterales por izquierda y por derecha.

**Desarrollo:**
1. **Límite lateral izquierdo ($x \to 2^-$):**
   - En este caso, $x < 2 \implies 2 - x > 0 \implies |2 - x| = 2 - x$.
   - Sustituimos y factorizamos:
     $$\lim_{x\to 2^-} \frac{x^2 + (2 - x) - 4}{x^2 - 4} = \lim_{x\to 2^-} \frac{x^2 - x - 2}{x^2 - 4} = \lim_{x\to 2^-} \frac{(x - 2)(x + 1)}{(x - 2)(x + 2)}$$
   - Cancelamos $(x - 2)$ y evaluamos:
     $$\lim_{x\to 2^-} \frac{x + 1}{x + 2} = \frac{2 + 1}{2 + 2} = \frac{3}{4}$$

2. **Límite lateral derecho ($x \to 2^+$):**
   - En este caso, $x > 2 \implies 2 - x < 0 \implies |2 - x| = -(2 - x) = x - 2$.
   - Sustituimos y factorizamos:
     $$\lim_{x\to 2^+} \frac{x^2 + (x - 2) - 4}{x^2 - 4} = \lim_{x\to 2^+} \frac{x^2 + x - 6}{x^2 - 4} = \lim_{x\to 2^+} \frac{(x - 2)(x + 3)}{(x - 2)(x + 2)}$$
   - Cancelamos $(x - 2)$ y evaluamos:
     $$\lim_{x\to 2^+} \frac{x + 3}{x + 2} = \frac{2 + 3}{2 + 2} = \frac{5}{4}$$

3. Comparamos los límites laterales:
   $$\lim_{x\to 2^-} f(x) = \frac{3}{4} \neq \frac{5}{4} = \lim_{x\to 2^+} f(x)$$
   Como difieren, el límite general no existe.

**Respuesta:**
**No existe** porque los límites laterales son diferentes ($\frac{3}{4} \neq \frac{5}{4}$).

---

### Pregunta 2(i): Analizar la existencia de $\lim_{x\to 1} f(x)$, donde $f(x)$ es:
$$f(x) = \begin{cases} \frac{x - 1}{2(\sqrt{5x} - \sqrt{5})} & \text{si } x < 1 \\ \frac{\sqrt{x^2 - 2x + 6} - \sqrt{x^2 + 2x + 2}}{x^2 - 4x + 3} & \text{si } x > 1 \end{cases}$$
> **Justificación Pedagógica:** Calculamos los límites laterales para la función definida a trozos en el punto de transición $x = 1$. Se racionalizarán los términos indeterminados por separado.

**Desarrollo:**
1. **Límite lateral izquierdo ($L^-$ para $x \to 1^-$):**
   - Usamos la primera rama:
     $$L^- = \lim_{x\to 1^-} \frac{x - 1}{2\sqrt{5}(\sqrt{x} - 1)}$$
   - Factorizamos el numerador como una diferencia de cuadrados $x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1)$:
     $$L^- = \lim_{x\to 1^-} \frac{(\sqrt{x} - 1)(\sqrt{x} + 1)}{2\sqrt{5}(\sqrt{x} - 1)} = \lim_{x\to 1^-} \frac{\sqrt{x} + 1}{2\sqrt{5}} = \frac{1 + 1}{2\sqrt{5}} = \frac{2}{2\sqrt{5}} = \frac{\sqrt{5}}{5}$$

2. **Límite lateral derecho ($L^+$ para $x \to 1^+$):**
   - Usamos la segunda rama y racionalizamos el numerador:
     $$L^+ = \lim_{x\to 1^+} \frac{\sqrt{x^2 - 2x + 6} - \sqrt{x^2 + 2x + 2}}{x^2 - 4x + 3} \cdot \frac{\sqrt{x^2 - 2x + 6} + \sqrt{x^2 + 2x + 2}}{\sqrt{x^2 - 2x + 6} + \sqrt{x^2 + 2x + 2}}$$
     $$= \lim_{x\to 1^+} \frac{(x^2 - 2x + 6) - (x^2 + 2x + 2)}{(x - 1)(x - 3)(\sqrt{x^2 - 2x + 6} + \sqrt{x^2 + 2x + 2})}$$
     $$= \lim_{x\to 1^+} \frac{-4x + 4}{(x - 1)(x - 3)(\sqrt{x^2 - 2x + 6} + \sqrt{x^2 + 2x + 2})}$$
     $$= \lim_{x\to 1^+} \frac{-4(x - 1)}{(x - 1)(x - 3)(\sqrt{x^2 - 2x + 6} + \sqrt{x^2 + 2x + 2})}$$
   - Cancelamos $(x-1)$ y evaluamos en $x = 1$:
     $$= \frac{-4}{(1 - 3)(\sqrt{5} + \sqrt{5})} = \frac{-4}{-2(2\sqrt{5})} = \frac{-4}{-4\sqrt{5}} = \frac{1}{\sqrt{5}} = \frac{\sqrt{5}}{5}$$

3. Comparamos los límites laterales:
   $$L^- = L^+ = \frac{\sqrt{5}}{5}$$
   Dado que ambos límites laterales coinciden, el límite general en $x = 1$ existe.

**Respuesta:**
**Existe** y su valor es $\mathbf{\frac{\sqrt{5}}{5}}$.

---

## III. Continuidad de Funciones (Preguntas 3 a 10)

### Pregunta 3: (P) Continuidad de $g(x)$ en $x = 2$
> **Enunciado:** Sea $f(x) = 1 - \sqrt{4x^2 - 7}$ y $g$ una función definida por:
> $$g(x) = \begin{cases} \frac{f(x) - f(2)}{x - 2} & \text{si } x \neq 2 \\ \frac{8}{3} & \text{si } x = 2 \end{cases}$$
> Determine si $g$ es continua en $x=2$.
>
> **Justificación Pedagógica:** Una función es continua en un punto $c$ si el límite cuando $x \to c$ existe y es igual al valor evaluado de la función $g(c)$. Analizaremos el límite racionalizando la diferencia bajo el límite.

**Desarrollo:**
1. Evaluamos $f(2)$ primero:
   $$f(2) = 1 - \sqrt{4(2^2) - 7} = 1 - \sqrt{16 - 7} = 1 - \sqrt{9} = 1 - 3 = -2$$
2. Formulamos el límite de $g(x)$ cuando $x \to 2$:
   $$\lim_{x\to 2} g(x) = \lim_{x\to 2} \frac{(1 - \sqrt{4x^2 - 7}) - (-2)}{x - 2} = \lim_{x\to 2} \frac{3 - \sqrt{4x^2 - 7}}{x - 2}$$
3. Racionalizamos el numerador multiplicando por el conjugado $(3 + \sqrt{4x^2 - 7})$:
   $$\lim_{x\to 2} \frac{(3 - \sqrt{4x^2 - 7})(3 + \sqrt{4x^2 - 7})}{(x - 2)(3 + \sqrt{4x^2 - 7})} = \lim_{x\to 2} \frac{9 - (4x^2 - 7)}{(x - 2)(3 + \sqrt{4x^2 - 7})}$$
   $$= \lim_{x\to 2} \frac{16 - 4x^2}{(x - 2)(3 + \sqrt{4x^2 - 7})}$$
4. Factorizamos el numerador: $16 - 4x^2 = -4(x^2 - 4) = -4(x - 2)(x + 2)$:
   $$= \lim_{x\to 2} \frac{-4(x - 2)(x + 2)}{(x - 2)(3 + \sqrt{4x^2 - 7})}$$
5. Cancelamos el término $(x - 2)$ para $x \neq 2$ y evaluamos:
   $$\lim_{x\to 2} \frac{-4(x + 2)}{3 + \sqrt{4x^2 - 7}} = \frac{-4(2 + 2)}{3 + \sqrt{9}} = \frac{-16}{6} = -\frac{8}{3}$$
6. Comparamos con el valor de la función:
   $$\lim_{x\to 2} g(x) = -\frac{8}{3} \neq \frac{8}{3} = g(2)$$
   Dado que el valor límite y el valor de la función no coinciden, la función es discontinua en $x = 2$.

**Respuesta:**
La función $g(x)$ **no es continua** en $x = 2$ (presenta una discontinuidad evitable).

---

### Pregunta 4: (P) Análisis de la función $f(x)$
> **Enunciado:** Sea $f$ la función definida por:
> $$f(x) = \begin{cases} \frac{\sin(x + 1)}{x + 1} & \text{si } x < -1 \\ \cos\left(\frac{\pi x}{2}\right) & \text{si } x \geq -1 \end{cases}$$
> (a) Analizar la existencia de $\lim_{x\to -1} f(x)$, $\lim_{x\to 0} f(x)$ y $\lim_{x\to -3} f(x)$.  
> (b) ¿Es $f$ una función continua en todo $\mathbb{R}$?  
> (c) Evaluar $\lim_{x\to 1} \frac{f(x)}{\sqrt{x} - 1}$.  
> *Indicación:* Considere que $\cos(\theta) = \sin(\pi/2 - \theta)$.

#### Desarrollo de 4(a):
1. **Límite en $x = -1$:** Calculamos los límites laterales.
   - Izquierdo ($x \to -1^-$): Usamos la primera rama. Con $u = x + 1 \to 0^-$:
     $$\lim_{x\to -1^-} \frac{\sin(x + 1)}{x + 1} = \lim_{u\to 0^-} \frac{\sin(u)}{u} = 1$$
   - Derecho ($x \to -1^+$): Usamos la segunda rama.
     $$\lim_{x\to -1^+} \cos\left(\frac{\pi x}{2}\right) = \cos\left(-\frac{\pi}{2}\right) = 0$$
   - Como los límites laterales difieren ($1 \neq 0$), **no existe** $\lim_{x\to -1} f(x)$.

2. **Límite en $x = 0$:**
   - Como $x = 0 > -1$, evaluamos la segunda rama directamente:
     $$\lim_{x\to 0} f(x) = \cos(0) = 1$$
   - El límite **existe** y es $1$.

3. **Límite en $x = -3$:**
   - Como $x = -3 < -1$, evaluamos la primera rama:
     $$\lim_{x\to -3} f(x) = \frac{\sin(-3 + 1)}{-3 + 1} = \frac{\sin(-2)}{-2} = \frac{\sin(2)}{2}$$
   - El límite **existe** y es $\frac{\sin(2)}{2}$.

#### Desarrollo de 4(b):
Para que $f$ sea continua en todo $\mathbb{R}$, debe serlo en cada punto. Sin embargo, en el punto de división $x = -1$, el límite $\lim_{x\to -1} f(x)$ no existe. Por tanto, la función no es continua en $x = -1$.

#### Desarrollo de 4(c):
1. Evaluamos $\lim_{x\to 1} \frac{f(x)}{\sqrt{x} - 1}$. Para $x$ cercano a $1$ (donde $x > -1$), $f(x) = \cos\left(\frac{\pi x}{2}\right)$.
2. Racionalizamos el denominador:
   $$\lim_{x\to 1} \frac{\cos\left(\frac{\pi x}{2}\right)}{\sqrt{x} - 1} \cdot \frac{\sqrt{x} + 1}{\sqrt{x} + 1} = \lim_{x\to 1} \frac{\cos\left(\frac{\pi x}{2}\right)(\sqrt{x} + 1)}{x - 1}$$
3. Usamos la indicación con $\theta = \frac{\pi x}{2}$:
   $$\cos\left(\frac{\pi x}{2}\right) = \sin\left(\frac{\pi}{2} - \frac{\pi x}{2}\right) = \sin\left(\frac{\pi}{2}(1 - x)\right) = -\sin\left(\frac{\pi}{2}(x - 1)\right)$$
4. Definimos el cambio de variable $u = x - 1 \implies u \to 0$ cuando $x \to 1$:
   $$\lim_{u\to 0} \frac{-\sin\left(\frac{\pi u}{2}\right)(\sqrt{u + 1} + 1)}{u} = \lim_{u\to 0} \left[ -\frac{\sin\left(\frac{\pi u}{2}\right)}{\frac{\pi u}{2}} \cdot \frac{\pi}{2} \cdot (\sqrt{u + 1} + 1) \right]$$
5. Evaluamos aplicando propiedades de límites:
   $$-\frac{\pi}{2} \cdot 1 \cdot (\sqrt{1} + 1) = -\frac{\pi}{2} \cdot 2 = -\pi$$

**Respuesta:**
- (a) $\lim_{x\to -1} f(x)$ **no existe**, $\lim_{x\to 0} f(x) = \mathbf{1}$, y $\lim_{x\to -3} f(x) = \mathbf{\frac{\sin(2)}{2}}$.
- (b) **No es continua en todo $\mathbb{R}$** (presenta discontinuidad inevitable de salto en $x = -1$).
- (c) El límite vale $\mathbf{-\pi}$.

---

### Pregunta 5: (P) Continuidad de $f$ en el intervalo $[0, 3]$
> **Enunciado:** Sea $f$ la función definida por:
> $$f(x) = \begin{cases} \frac{2 \sin(x - \pi/4)}{4x - \pi} & \text{si } 0 \leq x < \pi/4 \\ \frac{2x}{\pi} & \text{si } \pi/4 \leq x \leq 3 \end{cases}$$
> Estudiar la continuidad de $f$ en el intervalo $[0, 3]$.
>
> **Justificación Pedagógica:** Analizaremos la continuidad en los tramos abiertos y luego estudiaremos el punto de pegado $x = \pi/4$ calculando sus límites laterales y valor de la función.

**Desarrollo:**
1. **Tramos abiertos:**
   - En $[0, \frac{\pi}{4})$, la función es continua porque el denominador $4x - \pi$ no se anula en dicho intervalo (solo se anula en $x = \pi/4$).
   - En $(\frac{\pi}{4}, 3]$, la función $f(x) = \frac{2x}{\pi}$ es un polinomio lineal, el cual es continuo en toda la recta real.
2. **Estudio en $x = \frac{\pi}{4}$:**
   - Valor de la función: $f\left(\frac{\pi}{4}\right) = \frac{2(\pi/4)}{\pi} = \frac{1}{2}$.
   - Límite lateral izquierdo ($x \to \frac{\pi}{4}^-$):
     $$\lim_{x\to \frac{\pi}{4}^-} \frac{2 \sin(x - \pi/4)}{4x - \pi} = \lim_{x\to \frac{\pi}{4}^-} \frac{2 \sin(x - \pi/4)}{4(x - \pi/4)}$$
     Utilizando $u = x - \pi/4 \to 0^-$:
     $$\lim_{u\to 0^-} \frac{2 \sin(u)}{4u} = \frac{2}{4} \lim_{u\to 0^-} \frac{\sin(u)}{u} = \frac{1}{2} \cdot 1 = \frac{1}{2}$$
   - Límite lateral derecho ($x \to \frac{\pi}{4}^+$):
     $$\lim_{x\to \frac{\pi}{4}^+} \frac{2x}{\pi} = \frac{2(\pi/4)}{\pi} = \frac{1}{2}$$
3. Conclusión en $x = \frac{\pi}{4}$:
   $$\lim_{x\to \frac{\pi}{4}^-} f(x) = \lim_{x\to \frac{\pi}{4}^+} f(x) = f\left(\frac{\pi}{4}\right) = \frac{1}{2}$$
   La función es continua en $x = \frac{\pi}{4}$.

**Respuesta:**
La función $f$ **es continua en todo el intervalo $[0, 3]$**.

---

### Pregunta 6: Determinar el valor de $p$ para la continuidad en $x = 3$
> **Enunciado:** Encuentre un valor para $p$, si es posible, de modo que la función $f$ definida por:
> $$f(x) = \begin{cases} \frac{x - 3}{\sqrt{2x^2 - 2} - \sqrt{x^2 + 7}} & \text{si } 1 \leq x < 3 \\ 4p - 1 & \text{si } x = 3 \\ \frac{4x^2 - 12x}{x^2 + 3x - 18} & \text{si } x > 3 \end{cases}$$
> sea continua en $x = 3$.
>
> **Justificación Pedagógica:** Calculamos los límites laterales para $x \to 3$ en ambas ramas. Si ambos coinciden, igualamos ese valor a la definición de la función $f(3) = 4p - 1$ para despejar $p$.

**Desarrollo:**
1. **Límite lateral izquierdo ($x \to 3^-$):**
   - Racionalizamos el denominador:
     $$\lim_{x\to 3^-} \frac{(x - 3)(\sqrt{2x^2 - 2} + \sqrt{x^2 + 7})}{(2x^2 - 2) - (x^2 + 7)} = \lim_{x\to 3^-} \frac{(x - 3)(\sqrt{2x^2 - 2} + \sqrt{x^2 + 7})}{x^2 - 9}$$
   - Factorizamos el denominador $x^2 - 9 = (x - 3)(x + 3)$ y simplificamos:
     $$\lim_{x\to 3^-} \frac{(x - 3)(\sqrt{2x^2 - 2} + \sqrt{x^2 + 7})}{(x - 3)(x + 3)} = \lim_{x\to 3^-} \frac{\sqrt{2x^2 - 2} + \sqrt{x^2 + 7}}{x + 3}$$
   - Evaluamos:
     $$\frac{\sqrt{2(3^2) - 2} + \sqrt{3^2 + 7}}{3 + 3} = \frac{\sqrt{16} + \sqrt{16}}{6} = \frac{8}{6} = \frac{4}{3}$$

2. **Límite lateral derecho ($x \to 3^+$):**
   - Factorizamos numerador y denominador de la tercera rama:
     $$\lim_{x\to 3^+} \frac{4x(x - 3)}{(x - 3)(x + 6)} = \lim_{x\to 3^+} \frac{4x}{x + 6}$$
   - Evaluamos:
     $$\frac{4(3)}{3 + 6} = \frac{12}{9} = \frac{4}{3}$$

3. **Igualación para continuidad:**
   Para que sea continua, requerimos:
   $$4p - 1 = \frac{4}{3} \implies 4p = \frac{7}{3} \implies p = \frac{7}{12}$$

**Respuesta:**
El valor de $p$ requerido es $\mathbf{\frac{7}{12}}$.

---

### Pregunta 7: (P) Determinar los valores de $a$ y $b$ para la continuidad global
> **Enunciado:** Sean $a$ y $b$ dos constantes reales y $f$ la función definida por:
> $$f(x) = \begin{cases} \frac{\sin(\pi x)}{x + 1} & \text{si } x < -1 \\ ax^2 + b & \text{si } -1 \leq x \leq 5 \\ \frac{4x^2 - 40x + 100}{x^2 + 3x - 10} & \text{si } x > 5 \end{cases}$$
> Determine los valores de $a$ y $b$ para que $f$ sea continua en todo su dominio.
>
> **Justificación Pedagógica:** Imponemos la condición de continuidad en los dos puntos de cambio de definición: $x = -1$ y $x = 5$, lo que generará un sistema de dos ecuaciones lineales con dos incógnitas.

**Desarrollo:**
1. **Continuidad en $x = -1$:**
   - Límite por la izquierda ($x \to -1^-$):
     $$\lim_{x\to -1^-} \frac{\sin(\pi x)}{x + 1}$$
     Haciendo $u = x + 1 \implies x = u - 1$, donde $u \to 0^-$:
     $$\lim_{u\to 0^-} \frac{\sin(\pi(u - 1))}{u} = \lim_{u\to 0^-} \frac{\sin(\pi u - \pi)}{u} = \lim_{u\to 0^-} \frac{-\sin(\pi u)}{u} = -\pi \lim_{u\to 0^-} \frac{\sin(\pi u)}{\pi u} = -\pi(1) = -\pi$$
   - Límite por la derecha y valor de la función en $x = -1$:
     $$f(-1) = a(-1)^2 + b = a + b$$
   - Igualando ambos lados:
     $$a + b = -\pi \quad \text{--- (Ecuación 1)}$$

2. **Continuidad en $x = 5$:**
   - Límite por la derecha ($x \to 5^+$):
     $$\lim_{x\to 5^+} \frac{4x^2 - 40x + 100}{x^2 + 3x - 10} = \lim_{x\to 5^+} \frac{4(x - 5)^2}{(x + 5)(x - 2)} = \frac{4(0)^2}{(10)(3)} = 0$$
   - Límite por la izquierda y valor de la función en $x = 5$:
     $$f(5) = a(5^2) + b = 25a + b$$
   - Igualando ambos lados:
     $$25a + b = 0 \quad \text{--- (Ecuación 2)}$$

3. **Resolución del sistema de ecuaciones:**
   - De la Ecuación 2 despejamos $b$:
     $$b = -25a$$
   - Sustituimos en la Ecuación 1:
     $$a - 25a = -\pi \implies -24a = -\pi \implies a = \frac{\pi}{24}$$
   - Obtenemos $b$:
     $$b = -25\left(\frac{\pi}{24}\right) = -\frac{25\pi}{24}$$

**Respuesta:**
Los valores buscados son $a = \mathbf{\frac{\pi}{24}}$ y $b = \mathbf{-\frac{25\pi}{24}}$.

---

### Pregunta 8: Continuidad y redefinición por tramos
> **Enunciado:** Sea $f$ la función definida por:
> $$f(x) = \begin{cases} \sqrt{|x| + 2} & \text{si } x < 0 \\ \frac{3x^2 + 3}{x + 1} & \text{si } x > 2 \end{cases}$$
> (a) Justificar el hecho de que $f$ es continua en los intervalos $(-\infty, 0)$ y $(2, +\infty)$.  
> (b) Redefinir la función $f$ en el intervalo $[0, 2]$ de modo que resulte continua en todo $\mathbb{R}$.  
> *Indicación:* suponer que el gráfico de $f$ en $[0, 2]$ es un segmento de recta.

#### Desarrollo de 8(a):
- Para el intervalo $(-\infty, 0)$, tenemos $x < 0 \implies |x| = -x$. Así, $f(x) = \sqrt{-x + 2}$. Como $-x + 2 > 2$ para todo $x < 0$, el radicando siempre es positivo y, siendo la raíz cuadrada una función continua en su dominio real positivo, $f$ es continua en $(-\infty, 0)$.
- Para el intervalo $(2, +\infty)$, $f(x) = \frac{3x^2 + 3}{x + 1}$ es una función racional. El único punto de discontinuidad sería el polo del denominador $x = -1$, el cual no pertenece al intervalo analizado $(2, +\infty)$. Por lo tanto, $f$ es continua en este tramo.

#### Desarrollo de 8(b):
1. Calculamos los límites de la función en los extremos del intervalo $[0, 2]$ para garantizar que la nueva definición de $f$ pegue de forma continua:
   - En el extremo izquierdo $x = 0$:
     $$f(0) = \lim_{x\to 0^-} \sqrt{|x| + 2} = \sqrt{0 + 2} = \sqrt{2}$$
   - En el extremo derecho $x = 2$:
     $$f(2) = \lim_{x\to 2^+} \frac{3x^2 + 3}{x + 1} = \frac{3(4) + 3}{2 + 1} = \frac{15}{3} = 5$$
2. Suponiendo una trayectoria lineal en el intervalo $[0, 2]$, la función adopta la forma $f(x) = mx + k$:
   - Para $x = 0$: $f(0) = k = \sqrt{2}$.
   - Para $x = 2$: $f(2) = 2m + \sqrt{2} = 5 \implies m = \frac{5 - \sqrt{2}}{2}$.
3. La ecuación del segmento de recta es:
   $$f(x) = \left( \frac{5 - \sqrt{2}}{2} \right)x + \sqrt{2}, \quad x \in [0, 2]$$

**Respuesta:**
La función redefinida en todo $\mathbb{R}$ es:
$$f(x) = \begin{cases} 
\sqrt{|x| + 2} & \text{si } x < 0 \\ 
\left( \frac{5 - \sqrt{2}}{2} \right)x + \sqrt{2} & \text{si } 0 \leq x \leq 2 \\ 
\frac{3x^2 + 3}{x + 1} & \text{si } x > 2 
\end{cases}$$

---

### Pregunta 9: Continuidad global de una función a trozos
> **Enunciado:** Determinar los valores de $a$ y $b$ de modo que la función $f$ definida por:
> $$f(x) = \begin{cases} ax & \text{si } x < 2 \\ ax^2 + bx + 1 & \text{si } 2 \leq x \leq 5 \\ b & \text{si } x > 5 \end{cases}$$
> sea continua en todo su dominio.
>
> **Justificación Pedagógica:** Imponemos condiciones de continuidad en los dos puntos de pegado, $x = 2$ y $x = 5$, para plantear y resolver un sistema de ecuaciones lineales de $2 \times 2$.

**Desarrollo:**
1. **Continuidad en $x = 2$:**
   $$\lim_{x\to 2^-} f(x) = 2a$$
   $$\lim_{x\to 2^+} f(x) = f(2) = 4a + 2b + 1$$
   Igualando las dos expresiones:
   $$2a = 4a + 2b + 1 \implies 2a + 2b = -1 \quad \text{--- (Ecuación 1)}$$

2. **Continuidad en $x = 5$:**
   $$\lim_{x\to 5^-} f(x) = f(5) = 25a + 5b + 1$$
   $$\lim_{x\to 5^+} f(x) = b$$
   Igualando las dos expresiones:
   $$25a + 5b + 1 = b \implies 25a + 4b = -1 \quad \text{--- (Ecuación 2)}$$

3. **Resolución del sistema:**
   - Multiplicamos la Ecuación 1 por $2$:
     $$4a + 4b = -2$$
   - Restamos esta ecuación a la Ecuación 2:
     $$(25a + 4b) - (4a + 4b) = -1 - (-2) \implies 21a = 1 \implies a = \frac{1}{21}$$
   - Sustituimos $a$ en la Ecuación 1 para obtener $b$:
     $$2\left(\frac{1}{21}\right) + 2b = -1 \implies 2b = -1 - \frac{2}{21} = -\frac{23}{21} \implies b = -\frac{23}{42}$$

**Respuesta:**
Los parámetros requeridos son $a = \mathbf{\frac{1}{21}}$ y $b = \mathbf{-\frac{23}{42}}$.

---

### Pregunta 10: Análisis de continuidad en todo el dominio
> **Enunciado:** Analizar la continuidad de las funciones $f$ y $g$ en todo su dominio.
> $$(a)\ f(x) = \begin{cases} \frac{\sqrt{x + 1} - \sqrt{1 - x}}{|x|} & \text{si } -1 \leq x < 0 \\ \frac{x^2(x + 1)}{x^3 + 1} & \text{si } x \geq 0 \end{cases}$$
> $$(b)\ g(x) = \begin{cases} \frac{2x^2 - 6x}{x - 3} & \text{si } |x| < 3 \\ x^2 - 3 & \text{si } |x| \geq 3 \end{cases}$$

#### Desarrollo de 10(a):
1. **Tramos abiertos:**
   - Para $-1 \leq x < 0$: los términos bajo las raíces cumplen $x+1 \geq 0$ y $1-x > 0$. El denominador $|x| \neq 0$ en este tramo. La función es continua en $[-1, 0)$.
   - Para $x > 0$: el denominador del racional $x^3 + 1$ no posee raíces reales positivas (solo se anula en $x = -1$). La función es continua en $(0, +\infty)$.
2. **Estudio en el pegado $x = 0$:**
   - Valor de la función: $f(0) = \frac{0^2(0 + 1)}{0^3 + 1} = 0$.
   - Límite por la derecha ($x \to 0^+$):
     $$\lim_{x\to 0^+} \frac{x^2(x + 1)}{x^3 + 1} = 0$$
   - Límite por la izquierda ($x \to 0^-$): Como $x < 0 \implies |x| = -x$.
     $$\lim_{x\to 0^-} \frac{\sqrt{x + 1} - \sqrt{1 - x}}{-x}$$
     Racionalizamos multiplicando por el conjugado:
     $$\lim_{x\to 0^-} \frac{(x + 1) - (1 - x)}{-x(\sqrt{x + 1} + \sqrt{1 - x})} = \lim_{x\to 0^-} \frac{2x}{-x(\sqrt{x + 1} + \sqrt{1 - x})} = \lim_{x\to 0^-} \frac{-2}{\sqrt{x + 1} + \sqrt{1 - x}} = \frac{-2}{2} = -1$$
   - Al comparar los límites laterales ($\lim_{x\to 0^+} f(x) = 0 \neq -1 = \lim_{x\to 0^-} f(x)$), vemos que el límite en $x = 0$ no existe.

#### Desarrollo de 10(b):
1. Reescribimos la función analizando el valor absoluto $|x| \geq 3 \iff x \leq -3 \lor x \geq 3$:
   $$g(x) = \begin{cases} x^2 - 3 & \text{si } x \leq -3 \\ \frac{2x^2 - 6x}{x - 3} & \text{si } -3 < x < 3 \\ x^2 - 3 & \text{si } x \geq 3 \end{cases}$$
2. **Tramos abiertos:**
   - La rama $x^2 - 3$ es continua en $(-\infty, -3)$ y $(3, +\infty)$.
   - Para $-3 < x < 3$, simplificamos: $g(x) = \frac{2x(x - 3)}{x - 3} = 2x$. Esta función lineal es continua en $(-3, 3)$.
3. **Punto de pegado $x = -3$:**
   - $g(-3) = (-3)^2 - 3 = 6$.
   - Límite lateral izquierdo: $\lim_{x\to -3^-} (x^2 - 3) = 6$.
   - Límite lateral derecho: $\lim_{x\to -3^+} 2x = -6$.
   - Como difieren, $g$ **no es continua** en $x = -3$.
4. **Punto de pegado $x = 3$:**
   - $g(3) = 3^2 - 3 = 6$.
   - Límite lateral izquierdo: $\lim_{x\to 3^-} 2x = 6$.
   - Límite lateral derecho: $\lim_{x\to 3^+} (x^2 - 3) = 6$.
   - Como coinciden, $g$ **es continua** en $x = 3$.

**Respuesta:**
- (a) $f$ es continua en **$[-1, 0) \cup (0, +\infty)$** (discontinuidad inevitable de salto en $x = 0$).
- (b) $g$ es continua en **$\mathbb{R} \setminus \{-3\}$** (discontinuidad inevitable de salto en $x = -3$).

---

## IV. Aplicaciones del Teorema de Bolzano y Ceros (Preguntas 11 a 14)

### Pregunta 11: Decidir sobre la existencia de soluciones reales
> **Enunciado:** Decida si las siguientes ecuaciones poseen o no soluciones dentro del intervalo indicado. Justifique.
> $$(a)\ (P)\ \sin\left(\frac{\pi x}{2}\right) + e^x = 0,\ \text{con } x \in [-1, 0]$$
> $$(b)\ x^4 + x = 1,\ \text{con } x \in \left[ -\frac{3}{2}, 1 \right]$$
> *Indicación:* en (b) puede ser útil recordar el método de la bisección.
>
> **Justificación Pedagógica:** El Teorema de Bolzano establece que si una función continua $f(x)$ toma valores con diferente signo en los extremos de un intervalo $[A, B]$ ($f(A) \cdot f(B) < 0$), entonces existe al menos una raíz en el intervalo abierto $(A, B)$.

#### Desarrollo de 11(a):
1. Definimos la función continua en $[-1, 0]$: $f(x) = \sin\left(\frac{\pi x}{2}\right) + e^x$.
2. Evaluamos los extremos del intervalo:
   - $f(-1) = \sin\left(-\frac{\pi}{2}\right) + e^{-1} = -1 + \frac{1}{e}$. Como $e \approx 2.718 > 1$, entonces $\frac{1}{e} < 1 \implies f(-1) < 0$.
   - $f(0) = \sin(0) + e^0 = 1 > 0$.
3. Dado que $f$ es continua y cambia de signo en el intervalo ($f(-1) < 0 < f(0)$), por el Teorema de Bolzano se garantiza la existencia de al menos una solución en $[-1, 0]$.

#### Desarrollo de 11(b):
1. Definimos la función continua en $[-3/2, 1]$: $f(x) = x^4 + x - 1$.
2. Evaluamos los extremos:
   - $f(-3/2) = (-1.5)^4 - 1.5 - 1 = 5.0625 - 2.5 = 2.5625 > 0$.
   - $f(1) = 1^4 + 1 - 1 = 1 > 0$.
3. Dado que no hay cambio de signo entre los extremos exteriores, usamos la indicación de bisección evaluando la función en un punto intermedio, por ejemplo $x = 0 \in [-3/2, 1]$:
   - $f(0) = 0^4 + 0 - 1 = -1 < 0$.
4. Analizamos los subintervalos obtenidos:
   - En $[-3/2, 0]$: $f(-3/2) > 0$ y $f(0) < 0$. Al ser continua, hay una raíz en $(-3/2, 0)$.
   - En $[0, 1]$: $f(0) < 0$ y $f(1) > 0$. Al ser continua, hay otra raíz en $(0, 1)$.

**Respuesta:**
- (a) **Sí posee solución** en $[-1, 0]$ garantizada por Bolzano.
- (b) **Sí posee soluciones** en $[-3/2, 1]$ (de hecho, al menos dos raíces reales).

---

### Pregunta 12: (P) Continuidad y existencia de ceros para $f(x)$
> **Enunciado:** Sea $f : \mathbb{R} \to \mathbb{R}$ la función definida por:
> $$f(x) = \begin{cases} \frac{\sin(x^2) - \sin(3x)}{6x} & \text{si } x < 0 \\ \frac{2 - \sqrt{3 + x^2}}{x - 1} & \text{si } 0 \leq x < 1 \\ \frac{x^4 - x - 1}{2} & \text{si } x \geq 1 \end{cases}$$
> (a) ¿Es $f$ continua en el intervalo $[0, 1]$? Justifique adecuadamente su respuesta.  
> (b) Analice la continuidad de $f$ en los puntos $x_1 = -\pi/2$, $x_2 = 0$ y $x_3 = 1$.  
> (c) Muestre que la ecuación $f(x) = 0$ tiene al menos una solución en el intervalo $[1, +\infty[$.

#### Desarrollo de 12(a):
1. **Tramos abiertos:** Para $x \in (0, 1)$, $f(x) = \frac{2 - \sqrt{3 + x^2}}{x - 1}$. El denominador solo se anula en $x = 1$, por ende la expresión es continua en $(0, 1)$.
2. **Extremo izquierdo ($x = 0$):** Analizamos la continuidad por la derecha:
   - Valor: $f(0) = \frac{2 - \sqrt{3 + 0}}{0 - 1} = \sqrt{3} - 2$.
   - Límite: $\lim_{x\to 0^+} f(x) = \sqrt{3} - 2$. Como coinciden, es continua por la derecha en $x = 0$.
3. **Extremo derecho ($x = 1$):** Analizamos la continuidad por la izquierda:
   - Valor: $f(1) = \frac{1^4 - 1 - 1}{2} = -\frac{1}{2}$.
   - Límite por la izquierda: Racionalizamos la segunda rama:
     $$\lim_{x\to 1^-} \frac{2 - \sqrt{3 + x^2}}{x - 1} \cdot \frac{2 + \sqrt{3 + x^2}}{2 + \sqrt{3 + x^2}} = \lim_{x\to 1^-} \frac{1 - x^2}{(x - 1)(2 + \sqrt{3 + x^2})}$$
     $$= \lim_{x\to 1^-} \frac{-(x - 1)(x + 1)}{(x - 1)(2 + \sqrt{3 + x^2})} = \lim_{x\to 1^-} \frac{-(x + 1)}{2 + \sqrt{3 + x^2}} = \frac{-2}{2 + 2} = -\frac{1}{2}$$
   - Como coinciden ($\lim_{x\to 1^-} f(x) = f(1)$), la función es continua por la izquierda en $x = 1$.
   Por lo tanto, la función es continua en el intervalo cerrado $[0, 1]$.

#### Desarrollo de 12(b):
1. **En $x_1 = -\pi/2$:** Pertenece al intervalo abierto de la primera rama $(-\infty, 0)$. Dado que el denominador $6x$ no es cero allí, $f$ es continua en $x_1 = -\pi/2$.
2. **En $x_2 = 0$:** Calculamos los límites laterales.
   - Izquierdo ($x \to 0^-$):
     $$\lim_{x\to 0^-} \frac{\sin(x^2) - \sin(3x)}{6x} = \lim_{x\to 0^-} \left[ \frac{x}{6} \cdot \frac{\sin(x^2)}{x^2} - \frac{1}{2} \cdot \frac{\sin(3x)}{3x} \right]$$
     *(Nota de simplificación)*:
     $$\lim_{x\to 0^-} \frac{\sin(x^2)}{6x} = \lim_{x\to 0^-} \frac{x}{6} \frac{\sin(x^2)}{x^2} = 0 \cdot 1 = 0$$
     $$\lim_{x\to 0^-} \frac{\sin(3x)}{6x} = \lim_{x\to 0^-} \frac{1}{2} \frac{\sin(3x)}{3x} = \frac{1}{2} \cdot 1 = \frac{1}{2}$$
     Entonces $\lim_{x\to 0^-} f(x) = 0 - \frac{1}{2} = -\frac{1}{2}$.
   - Derecho ($x \to 0^+$): Ya calculamos que tiende a $\sqrt{3} - 2 \approx -0.268$.
   - Como difieren, la función es discontinua en $x_2 = 0$.
3. **En $x_3 = 1$:**
   - Límite por la izquierda: $\lim_{x\to 1^-} f(x) = -1/2$.
   - Límite por la derecha: $\lim_{x\to 1^+} \frac{x^4 - x - 1}{2} = -1/2$.
   - Valor: $f(1) = -1/2$.
   - Al ser todos iguales, la función es continua en $x_3 = 1$.

#### Desarrollo de 12(c):
1. Para $x \in [1, 2]$, la función $f(x) = \frac{x^4 - x - 1}{2}$ es continua por tratarse de un polinomio.
2. Evaluamos en los extremos de este intervalo cerrado:
   - $f(1) = -\frac{1}{2} < 0$.
   - $f(2) = \frac{16 - 2 - 1}{2} = \frac{13}{2} > 0$.
3. Por el Teorema de Bolzano, existe al menos una raíz en el intervalo $(1, 2)$, lo que prueba la existencia de solución en $[1, +\infty[$.

**Respuesta:**
- (a) **Sí, es continua** en $[0, 1]$.
- (b) Continua en $x_1 = -\pi/2$ y $x_3 = 1$; **discontinua** en $x_2 = 0$.
- (c) Solución garantizada en el intervalo abierto $(1, 2) \subset [1, +\infty[$ por el Teorema de Bolzano.

---

### Pregunta 13: Existencia de ceros en $[0, 2]$
> **Enunciado:** Sea $f : \text{Dom}(f) \subseteq \mathbb{R} \to \mathbb{R}$ la función definida por:
> $$f(x) = \begin{cases} 3x - 1 & \text{si } 0 \leq x \leq 1 \\ \sqrt{\frac{x + 3}{x}} & \text{si } 1 < x \leq 2 \end{cases}$$
> Probar que la ecuación $f(x) = 0$ tiene a lo menos una solución en el intervalo $[0, 2]$.
>
> **Justificación Pedagógica:** Evaluaremos primero la continuidad de la función en todo el intervalo $[0, 2]$ analizando el punto de pegado $x = 1$. Si es continua, evaluamos sus extremos y aplicamos el Teorema de Bolzano.

**Desarrollo:**
1. **Análisis de continuidad en $x = 1$:**
   - Valor de la función: $f(1) = 3(1) - 1 = 2$.
   - Límite por la izquierda ($x \to 1^-$): $\lim_{x\to 1^-} (3x - 1) = 2$.
   - Límite por la derecha ($x \to 1^+$): $\lim_{x\to 1^+} \sqrt{\frac{x + 3}{x}} = \sqrt{\frac{4}{1}} = 2$.
   - Como coinciden, $f$ es continua en el punto de transición y, dado que cada rama es continua en su respectivo dominio abierto, la función $f$ es continua en todo el intervalo cerrado $[0, 2]$.
2. **Evaluación de extremos del intervalo:**
   - $f(0) = 3(0) - 1 = -1 < 0$.
   - $f(2) = \sqrt{\frac{2 + 3}{2}} = \sqrt{2.5} \approx 1.58 > 0$.
3. **Conclusión:** Dado que $f$ es continua en $[0, 2]$ y presenta cambio de signo en sus extremos, por el Teorema de Bolzano existe al menos un valor $c \in (0, 2)$ tal que $f(c) = 0$.

**Respuesta:**
Queda demostrado por el Teorema de Bolzano (con cambio de signo entre $f(0) = -1$ y $f(2) = \sqrt{2.5}$).

---

### Pregunta 14: Existencia de ceros en $[-3, 2]$
> **Enunciado:** Sea $f : \text{Dom}(f) \subseteq \mathbb{R} \to \mathbb{R}$ la función definida por:
> $$f(x) = \begin{cases} x^3 - 4x - 8 & \text{si } x \leq -2 \\ x^3 - \sqrt{x + 2} & \text{si } x > -2 \end{cases}$$
> Probar que la ecuación $f(x) = 0$ tiene a lo menos una solución en el intervalo $[-3, 2]$.
>
> **Justificación Pedagógica:** Al igual que en los problemas anteriores, primero debemos verificar detalladamente la continuidad de la función en el intervalo $[-3, 2]$ para poder aplicar formalmente el Teorema de Bolzano.

**Desarrollo:**
1. **Análisis de continuidad en $x = -2$:**
   - Valor de la función: $f(-2) = (-2)^3 - 4(-2) - 8 = -8 + 8 - 8 = -8$.
   - Límite por la izquierda ($x \to -2^-$): $\lim_{x\to -2^-} (x^3 - 4x - 8) = -8$.
   - Límite por la derecha ($x \to -2^+$): $\lim_{x\to -2^+} (x^3 - \sqrt{x + 2}) = (-2)^3 - \sqrt{-2 + 2} = -8$.
   - Dado que los límites laterales y el valor de la función coinciden, $f$ es continua en $x = -2$ y, en consecuencia, continua en todo el intervalo $[-3, 2]$.
2. **Evaluación en los extremos:**
   - $f(-3) = (-3)^3 - 4(-3) - 8 = -27 + 12 - 8 = -23 < 0$.
   - $f(2) = 2^3 - \sqrt{2 + 2} = 8 - 2 = 6 > 0$.
3. **Conclusión:** Puesto que $f$ es una función continua en el intervalo cerrado $[-3, 2]$ y tiene signo opuesto en sus extremos ($f(-3) < 0$ y $f(2) > 0$), por el Teorema de Bolzano existe al menos un $c \in (-3, 2)$ tal que $f(c) = 0$.

**Respuesta:**
Queda demostrado por el Teorema de Bolzano (con cambio de signo de $f(-3) = -23$ a $f(2) = 6$).

---
[[Intro_Calculo_USS]]
