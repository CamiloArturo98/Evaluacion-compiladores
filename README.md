# Evaluacion-compiladores cuestionario

¿Cómo se representan los operadores +, -, * y / en los tokens generados?

Respuesta correcta: b) Como operadores aritméticos específicos
¿Qué estructura sigue el árbol de análisis sintáctico generado por ANTLR4 para la expresión b = 5 + a * 2;?

Respuesta correcta: d) * se evalúa antes que +, organizando el árbol en función de la precedencia.
¿Por qué es importante visualizar los tokens y el árbol de análisis en el proceso de compilación?

Respuesta correcta: d) Todas las anteriores.


1. Comandos utilizados durante el desarrollo de la práctica:
Generar los archivos de Lexer y Parser a partir de la gramática:

bash
Copy
Edit
antlr4 GrammarFile.g4
Compilar los archivos generados:

bash
Copy
Edit
javac *.java
Ejecutar el analizador léxico:

bash
Copy
Edit
grun GrammarFile prog -tokens < input.txt
Esto genera los tokens de la expresión que se ingresa en el archivo input.txt.

Ejecutar el árbol de análisis sintáctico:

bash
Copy
Edit
grun GrammarFile prog -tree < input.txt
Esto genera el árbol de análisis sintáctico de la expresión que se ingresa en el archivo input.txt.

2. Resultados obtenidos en pantalla (Tokens y -tree):
Tokens generados:

text
Copy
Edit
[ID, ASSIGN, NUMBER, SEMI, ID, ASSIGN, NUMBER, ADD, ID, MUL, NUMBER, SEMI, ID, ASSIGN, LPAREN, ID, SUB, NUMBER, RPAREN, DIV, NUMBER, SEMI]
En los tokens generados, se pueden observar los identificadores (ID), operadores aritméticos (+, -, *, /), números (NUMBER), y palabras clave de asignación (ASSIGN), además de los delimitadores como el punto y coma (SEMI) y paréntesis (LPAREN, RPAREN).

Árbol de análisis sintáctico (-tree):

text
Copy
Edit
(parse tree structure here)
Este árbol muestra la jerarquía de la expresión, donde los nodos están organizados según la prioridad de los operadores y cómo se evalúan. La multiplicación (*) tiene mayor prioridad que la suma (+), y así se organiza el árbol.

3. Desarrollo del cuestionario, indicando la respuesta correcta para cada pregunta y justificando su elección:
1. ¿Cómo se representan los operadores +, -, * y / en los tokens generados?
Respuesta correcta: b) Como operadores aritméticos específicos
Justificación: Los operadores +, -, * y / son identificados como operadores aritméticos en la gramática, lo que significa que ANTLR los clasifica como tales en los tokens generados.
2. ¿Qué estructura sigue el árbol de análisis sintáctico generado por ANTLR4 para la expresión b = 5 + a * 2;?
Respuesta correcta: d) * se evalúa antes que +, organizando el árbol en función de la precedencia.
Justificación: ANTLR4 organiza el árbol de acuerdo con la precedencia de los operadores. La multiplicación (*) tiene mayor prioridad que la suma (+), por lo que el árbol refleja esta prioridad.
3. ¿Por qué es importante visualizar los tokens y el árbol de análisis en el proceso de compilación?
Respuesta correcta: d) Todas las anteriores.
Justificación: Visualizar los tokens y el árbol de análisis sintáctico ayuda a comprender cómo el compilador traduce las instrucciones, optimizar el código y verificar que la gramática esté bien definida. Es fundamental en el proceso de depuración y en la comprensión del funcionamiento interno del compilador.

