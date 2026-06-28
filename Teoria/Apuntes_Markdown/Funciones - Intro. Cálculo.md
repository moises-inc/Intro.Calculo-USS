--- 
title: Funciones - Intro. Cálculo
origin: Notion
---

## **INFORMACIÓN RELEVANTE:**

## NOTAS**:**

# Relación

— Sea *A *y *B *dos conjuntos, siempre se puede construir $A \times B$, donde la relación (*R), **R \subseteq $A \times B$*

— Si $(a,b) \in R$ se lee como “a está relacionado con b”, y se denota como “$aRb$”.

— Se pueden usar las relaciones para definir ciertas condiciones de forma que se cumplan $aRb$

— Las cónicas son casos especiales de relaciones.

# Definición de una función

— Una función de A en B, es un **tipo de relación A en B, pero exigente**, donde todo elemento de **A se relaciona con un único elemento de B**. Para este curso se considera como $A = B = \R$

## Partes de una función

### Dominio $(\text{Dom} f(x))$ $ \in \R$

— Dado dos conjuntos A y B, se define como Dom $f(x) = \{ x\in A : f(x) \in B\}$

— “Elementos pertenecientes al conjunto $A$, para que la función funcione”.

— Se llama: “preimagen de $y$”.

— Calcular dominio de la función: $w(x) = \log(3x - 2) + \frac{3}{2} \sqrt[4]{7x - 1}$.

1. Restricción del argumento del logaritmo.
$$\begin{align*}
3x - 2 &> 0 \\
3x &> 2 \\
x &> \frac{2}{3}
\end{align*}$$

1. Restricción de la raíz de índice par.
$$\begin{align*}
7x - 1 &\ge 0 \\
7x &\ge 1 \\
x &\ge \frac{1}{7}
\end{align*}$$

1. Intersección (Dominio final).
$$\text{Dom}(w) = \left] \frac{2}{3}, +\infty \right[$$

### Recorrido $(\text{Rec} f(x))$ $ \in \R$

— Dado dos conjuntos A y B, tal que Rec $ f(x) = \{y \in B : y=f(x) \land x\in \text{ Dom } f\}$

— “Elementos de salida de la función”.

— Se suele llamar: “imagen de x”.

### Condominio $(\text{Cod} f(x))$ $ \in \R$

— “Todos los valores posibles de una función”.

# Plano cartesiano

# Álgebra de funciones

— Sean $f$ y $g $ $f$unciones y D = \text{Dom}($f$) \cap \text{Dom}(g) \not =  \varnothing. Se de$f$ine:

# Inyectividad

— Ejemplo, ver si $f(x)= \sqrt{\frac{3x+2}{x-2}}$ es inyectiva.

$$\text{1° Decir que:  }a,b \in \text{Dom}(f), \text{tal que} f(a) = f(b), \newline  \text{mostrar que } \sqrt{\frac{3a+2}{a-2}} =\sqrt{\frac{3b+2}{b-2}}$$

$$\text{Bueno, lo anterior se resuelve como:}\newline\Longrightarrow \frac{3a+2}{a-2} =\frac{3b+2}{b-2} \newline \Longrightarrow (3a+2)(b-2)=(3b+2)(a-2) \newline \Longrightarrow 3ab-6b+2-4=3ab+2a-6b-4 \newline \Longrightarrow 8a=8b  \newline a=b$$

* Resolver utilizando solo implicancias lógicas ($\Longrightarrow $).

$$\color{red} \therefore f \text{ es inyectiva}$$

—** Tener presente que**, si resolviendo $a,b \in \text{Dom}(f), \text{tal que} f(a) = f(b)$, nos damos cuenta de que hay que poner restricciones para seguir resolviendo la inecuación, **automáticamente la función no será inyectiva**.

### Inyectividad - Representación grafica

# Sobreyectividad

— Se define que una función es sobreyectiva siempre y cuando ***$\text{Rec}(f) = \text{Cod}(f).$***

# Biyectividad

— Se define como una función biyectiva si esta es inyectiva y sobreyectiva.

— La importancia de las funciones biyectivas, viene dada por el siguiente resultado, el cual permite dar una respuesta a la existencia de una función inversa.

# Funciones Inversas

—  Sea $$f$: A\longrightarrow B$ una $f$unción. Se de$f$ine **$f$unción inversa** de $f$, denotada como $f$^{-1}, como aquella $f$unción $f$^{-1}: B \longrightarrow A.  Además, se cumple:

$$\color{red} f(x)= y \iff f^{-1}(y)=x$$

- $\forall \ x \in A \land x \in B$
— Se necesita que la función sea **inyectiva** y **sobreyectiva, **es decir, que la función sea biyectiva.

## Modificación de una función inversa

— Dado una función que no sea inversa, ya sea que cumple con una o ninguna de las condiciones de la biyectividad, se puede modificar la función para que esta pueda ser una función inversa.

— **Ejemplo**, considerando la función $f: \text{Dom}(f) \subseteq \R, \longmapsto f(x)=\sqrt{x²-4x}$, determinar su inversa.

### Verificación de una función inversa

— Se puede verificar dada la prop. $(f \circ f^{-1})(x)=f(f^{-1}(x))=x, \forall x \in \text{Dom}(f^{-1}) \iff \color{red}(f^{-1}\circ f)(x)=f^{-1}(f(x))=x, \forall x \in \text{Dom}(f)$ 

# Funciones compuesta

— Observar que en general la composición de funciones no es conmutativa, es decir, $\color{red}(f \circ g)(x) \not = (g \circ f)(x)$.

— **Ejemplo**: 

$$\text{Considerar } f(x)=\frac{x²}{4-x²} \land g(x)=\sqrt{x+1} \text{, definir } g\circ f$$

$$\text{Primero, definir Dom}(g\circ f): \{x \in \R: x \in \text{Dom}(f) \land f(x)\in \text{Dom}(g)\} \newline \iff : \{ x \in \R: x\ne \pm 2 \land  \frac{x²}{4-x²}  \geq -1\}$$

* Notar que el $\text{Dom}(f)$ tiene que ser $x \ne \pm 2$ para que la **fracción no se indetermine**.

* Notar que el $\text{Dom}(g)$ tiene que ser $x+1 \geq 0 \iff x \geq -1$ para que la **raíz no se indetermine**.

$$\iff : \{ x \in \R: x\ne \pm 2 \land  \frac{x²}{4-x²} +1 \geq 0\} \newline \iff \{ x \in \R: x\ne \pm 2 \land  \frac{4}{4-x²}  \geq 0\}$$

* Notar que, para que $\frac{4}{4-x^2}  \geq 0$ solo basta con decir que $4-x² > 0 $, ya que, la fracción tiene el número 4 positivo, por lo tanto, para que la fracción, sea positiva, $4-x² >0$, donde, $4-x² > 0 $\iff x^2 <4 \iff |x| < 2 \iff -2 < x < 2. 

* Sin embargo, dada la restricción de *$x$*, se debe modificar el intervalo de solución.

 

$$\iff :\{ x \in \R: x\ne \pm 2 \land  4-x>0\} \newline \iff :\{ x \in \R: x\ne \pm 2 \land  -2<x<2\} \newline \iff ]-2,2[$$

* El intervalo $]-2,2[$ pasa a ser el $\text{Dom}$ $g \circ f$

$$\therefore g \circ f= ]-2,2[ \longrightarrow \R \newline g(f(x)) = x  \longmapsto \sqrt{\frac{4}{4-x²}}$$

* Forma correcta de concluir una composición de funciones.

******** “******$f(x)$***** entra a *****$g(x)$*****”.**

# Paridad de funciones

## Función Par

## Función Impar

# Monotonía de funciones

— Una función, según su gráfico, se puede clasificar como: 

## **Creciente**

## **Decreciente**

## **Constante**

# Transformaciones en una función 

## Desplazamiento vertical y horizontal de funciones en el Plano Coordenado $x,y$

