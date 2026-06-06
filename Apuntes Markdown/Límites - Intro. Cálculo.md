--- 
title: Límites - Intro. Cálculo
origin: Notion
---

## **INFORMACIÓN RELEVANTE:**

## NOTAS**:**

# Idea intuitiva de límite

— Se una función con variable real y arbitraria, definida como: 

$$f: I \longrightarrow \R \\ \ \ \ \ \ \ \ \ \ \ \ x \longrightarrow f(x)$$

— Donde *I *es un intervalo abierto en la recta real. Si se escoge un punto $a \in I$, donde incluso la función puede no estar definida y **se analiza el comportamiento de las imágenes***** f (x)*****, para puntos *****x***** próximos de *****a*****, pero diferentes de *****a***. Entonces, se denota como: 

$$\lim_{x \rightarrow a} f(x) = L$$

- Se lee como: “**el límite de *****f(x) *****cuando *****x***** tiende a *****a***** es igual a *****L***”.
- Una notación alternativa es: 
— La definición anterior, quiere decir que los valores de *f(x)* se aproximan a *L* cuando *x* tiende a *a *(por ambos lados de *a*), pero $x \not= a$.

# Definición precisa de límite

—  Se una función con **variable real** y arbitraria, definida como: 

$$f: I \longrightarrow \R \\ \ \ \ \ \ \ \ \ \ \ \ x \longrightarrow f(x)$$

-  Donde $I$ es el dominio de la función, además, $I$ \subseteq \R \land $I$ \text{ no vacío}.
— Se dice que el límite de *f(x)* cuando *x* tiende a *a* es *L*, denotado como: $\lim_{x\rightarrow a} = L$, **si y solo sí**: 

$$|f(x)-L|<\epsilon \iff \color{red} L- \epsilon < f(x)<L+ \epsilon$$

— Por otro lado, considerando que: 

$$0<|x-a|< \delta \Longrightarrow x \in \  ]a-\delta, a+ \delta[ \ \land \  x \not=a $$

$$|f(x) - L| < \epsilon \Longrightarrow f(x) \in \ ] L- \epsilon , L + \epsilon[$$

## Observaciones importantes

- Puede existir un número *L* que cumpla con la definición de límite, en tal caso, se dice que **$\lim_{x\rarr a} f(x)$**** existes.**
- En caso contrario, puede no existir un número *L* que cumplan con la definición de límite, en cuyo caso, el **$\lim_{x\rarr a} f(x)$**** no existe.**
- Aún más, **el valor del límite es único**, es decir, no puede haber dos valores $L_1 \lor L_2$ que cumplan con la definición de límite.
- $\delta >0$ no es único, se puede elegir cualquier valor menor a $\epsilon$.
# Límites laterales

$$\lim_{x \rarr a^{+}} f(x) = L \ \ \ \ \ \lor \ \ \ \ \ \lim_{\begin{matrix}
   x \rarr a \\
   x > a  
\end{matrix}} f(x) = L$$

### Límite por izquierda

— Sea $f: I \subseteq \R \longrightarrow \R $,  $a \in \R$ y $L \in \R$. Si se denota como $a^{-} = I \  \cap \ ]a - \delta, a[$. Además,

$$\forall \ \epsilon > 0, \exist \ \delta, \forall \ x \in I : a - \delta < x < a \Longrightarrow |f(x) - L| < \epsilon $$

— Entonces, el límite por izquierda de $f(x)$ se denota como: 

$$\lim_{x \rarr a^{-}} f(x) = L \ \ \ \ \ \lor \ \ \ \ \ \lim_{\begin{matrix}
   x \rarr a \\
   x < a  
\end{matrix}} f(x) = L$$

# Propiedades de los límites

## Prop. básicas.

— Dado un límite, con $a \in \text{Dom } f(x)$, siempre se cumple: 

## Álgebra de límites

— Sean *f* y *g* funciones tales que $\lim_{x \rarr a}f(x) = L \land \lim_{x \rarr a} g(x) = M$, además, sea $a,c \in \R$, se tiene: 

$$\lim_{x \rarr a} [f(x) \pm g(x)] = \lim_{x \rarr a} f(x) \pm \lim_{x \rarr a} g(x) = L \pm M $$

- Ley de la suma y diferencia.
$$\lim_{x \rarr a}[c \cdot f(x)] = c \cdot \lim_{x \rarr a}f(x) = c \cdot L$$

- Ley del múltiplo constante.
$$\lim_{x \rarr a}[f(x) \cdot g(x)] = \lim_{x \rarr a} f(x) \cdot \lim_{x \rarr a} g(x) = L \cdot M$$

- Ley del producto.
$$\lim_{x \rarr a} \left[  \frac{f(x)}{g(x)} \right] = \frac{\lim_{x \rarr a} f(x)}{\lim_{x \rarr a} g(x)} = \frac{L}{M}$$

-  Siempre y cuando, $M \not= 0$.
- Ley del cociente.
## Teorema de sustitución de límites

## Teoremas adicionales

### Teorema

— Si $f(x) \leq g(x)$ cuando *x* tiende a *a*, y los límites de $f(x) \land g(x)$ existen cuando *x* tiende a *a*, entonces se cumple que:

$$\lim_{x \rarr a} f(x) \leq \lim_{x \rarr a} g(x)$$

### Teorema de comprensión o acotamiento

## Límites trigonométricos

— D$a$do un límite, con **$$a$ \in \text{Dom } $f$(x)$**** **y con $f$ continu$a$ en $a$, se tiene que: 

# Continuidad

— Se$a$ $$f$: I \subseteq \R \longright$a$rrow \R  \l$a$nd I \in \R$, se dice que **$f$**** es continu$a$ en ****$a$**** si y solo sí **

$$\lim_{x \rarr a} f(x) = f(a)$$

— Además, se debe de cumplir: 

## Continuidad lateral

— Una función es continua por derecha si, 

$$\lim_{x \rarr a^{+}} f(x) = f(a)$$

— Una función es continua por izquierda si, 

$$\lim_{x \rarr a^{-}} f(x) = f(a)$$

## Continuidad en un intervalo

### Intervalo abierto

— Dada una $f$unción $f$, está será continua en un intervalo abierto $$]a,b[$$, **si esta es continua en todos los puntos del intervalo ****$$]a,b[$$****.**

### Intervalo cerrado

— Por otro lado, la función será continua en un intervalo cerrado $[a,b]$, **si es continua en ****$]a,b[$**** y, además, se cumple:**

$$\lim_{x \rarr a^+} f(x)= f(a) ,f \text{ es continua por derecha en a.} \\ \lim_{a\rarr b^-} f(x) = f(b), f \text{ es continua por izquierda en b.}$$

# Límites infinitos

## Definición formal de límites infinitos

### Límite infinito positivo por derecha

$$\lim_{x \rarr a^+} f(x) = + \infin$$

$$ x \in \text{Dom}(f) : a < x < a+ \delta \implies f(x) > m$$

- Con $\forall \ m >0 \land \exist \ \delta >0$.
### Límite infinito positivo por izquierda

