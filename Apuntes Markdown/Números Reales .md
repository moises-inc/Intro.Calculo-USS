--- 
title: Números Reales 
origin: Notion
---

## **INFORMACIÓN RELEVANTE:**

## NOTAS**:**

## Axiomas de Orden o Campo

— Los axiomas, en matemáticas, son cosas que no se demuestran, son la base de las cosas, se asume que todas son verdades.

— Una forma abreviada de decir que $\R$ cumple con las propiedades, es decir que **(****$\R$, +, \cdot****) es un campo o cuerpo conmutativo.**

— Notar que ($\mathbb{Q}, +, \cdot$) también es un campo, pero ($\Z, +, \cdot$) no lo es, dado que no te cumple A.8, $a^{-1}$ no pertenece a Z.

### Consecuencia de los axiomas de cuerpo en R

— Leyes de cancelación:

— Prop. Absorbente.

# Ecuaciones

## Ecuaciones lineales o de primer grado

— Una ecuación es una igualdad que involucra a una o más incógnitas

— Las ecuaciones son de la forma: 

$$ax+b=0$$

- $a, b \in \R \land a \not= 0$
- En este caso **$x= \frac {-b} a$**. Así, el conjunto solución es $S=\{ \frac b a \}$
— Al resolver una ecuación, se debe poner restricciones.

## Ecuaciones cuadráticas o de segundo grado

— Son ecuaciones de la forma:

$$ax^2 +bx+c = 0$$

- $a,b,c \in \R \land a \not = 0$
— Una ecuación cuadrática se puede resolver utilizando la siguiente fórmula:

$$x=\frac{-b \pm \sqrt{b^2-4ac}}{2a}$$

### Discriminante

— Dada la fórmula general para ecuaciones cuadráticas, se define como discrimínate $(\Delta)$:

$$\Delta = b^{2} - 4ac$$

— De lo anterior se puede deducir:

— En el caso de haber dos soluciones para una ecuación, estas se representan como $x_1 , x_2$. Las cuales sirven para expresar la ecuación de la forma: 

$$ax^2 +bx+c = a(x-x_1)(x-x_2)=0$$

# Valor absoluto

— Se define valor absoluto de $a \in \R$, denotado como $|a|$, como:

$$|a| = \begin{cases}
   a &\text{si } a \geq 0 \\
   -a &\text{si } a < 0
\end{cases}$$

— Si la definición se extiende a polinomios, por ejemplo: 

$$|x-2| = \begin{cases}
   x-2 &\text{si } x \geq 2 \\
   2-x &\text{si } x < 2
\end{cases}$$

## Propiedades de valor absoluto

-  $\forall \  a \in \R, |a| \geq0$
- $|a| = 0 \iff a=0$
-  $\forall \ a \in \R, |a|= |-a|$
-  $\color{red} \forall \ x \in \R, |a|^2 = a^2$
- $\color{red} |a| = \sqrt{a^2}$
- $|ab| = |a| \cdot |b|$
- $\left |\frac ab \right|= \frac {|a|} {|b|}$ ; con $b \not=0$. 
- Desigualdad triangular:
- Si $c \in \R^{+} \land x \in \R$, entonces:
# Intervalos

— Sean $a,b \in $\R$$ tales que $a<b $. Los siguientes subconjuntos de $\R$ se conocen como intervalos.

### Operaciones con intervalos

— Recordar teoría de conjuntos.

### Unión de intervalos

— Sean $A, B$ dos intervalos y $x$ un elemento que está en la **unión** de $A,B$. La $A \cup B$ se define como:

$$x \in A \cup B \iff x \in A \lor x \in B$$

### Intersección de intervalos

— Sean $A, B$ dos intervalos y $x$ un elemento que está en la **intersección** de $A,B$. La $A \cap B$ se define como:

$$x \in A \cap B \iff x \in A \land x \in B$$

# Inecuaciones

— Son aquellas expresiones algebraicas separadas por algún símbolo de relación $( \textcolor{red}{<, >, \leq, \ge} )$. La solución de una inecuación se representa por un **conjunto solución**, el cual contiene todos los puntos que cumplen con la desigualdad. 

## Propiedades de las inecuaciones

— Dado la existencia de $$$\R$$^{+}$, un conjunto no vacío y subconjunto de $$\R$$. En $$\R$$⁺ se pueden definir relaciones de orden sobre $$\R$$.

— Para cada $a,b,c \in \R$:

## Resolución de inecuaciones lineales

— Para resolver una inecuación lineal, esta se hace de la misma manera que una ecuación, lo importante es **tener presente las propiedades de las inecuaciones** a la hora de resolver.

— Ejemplo:

$$x - 5 < 4 \\ $$

$$\begin{equation*}
\begin{split}   
	x-5 < 4&\iff  x < 9\\
      & \iff x \in ]- \infin , 9 [ \\  

\end{split} \\ 

\end{equation*} \\ 
\therefore S = ]- \infin , 9 [ = \{x \in \R : x < 9 \}$$

$$2 - 3x \leq 5$$

$$\begin{equation*}
\begin{split}   
	2 - 3x  \leq 5 &\iff  -3x \leq 3 \\

& \iff -x \leq 1 \\ 

& \iff x \geq -1 \\   

& \iff x \in [-1  , + \infin [ \\  

\end{split} \\ 

\end{equation*} \\ 
\therefore S = [-1 , + \infin [ = \{x \in \R : x \geq -1 \}$$

## Resolución de ecuaciones cuadráticas

— Para resolver inecuaciones del tipo $ax² + bx + c \geq 0 \lor ax² + bx + c \leq 0$ se utiliza** tabla de signos o método de puntos críticos.**

### Tabla de signos o método de puntos críticos

— Para la explicación, se utiliza la ecuación $\color{red} 2x^2 + 3 +1 \geq 0$.

- **Evaluar discriminante.**
$$\triangle = \begin{Bmatrix} \triangle  >0 , \text {La ecuación se puede  factorizar} \\ \triangle < 0 ,  \text {La ecuación no se puede  factorizar} \end{Bmatrix}$$

$$\triangle = b^2 -4ac \newline 3^2 -4 \times 2 \times 1 = 1 \newline \color{red}1 \geq 0$$

- **Factorizar.**
- **Encontrar puntos críticos.**
- **Realizar tabla de signos.**
- **Realizar recta numérica.**
- **Analizar resultados según la inecuación.**
## Inecuaciones de grado $n >2$

— Se resuelven utilizando el mismo método de tabla de signos, solo que ahora, las expresiones deben factorizarse primero. 

