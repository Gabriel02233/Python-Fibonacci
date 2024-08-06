Python-Fibonacci
Um script python simples que calcula e imprime a sequência de Fibonacci!

O que é a sequência de Fibonacci?
A sequência de Fibonacci é uma série de números que começa com 0 e 1, e cada número subsequente na sequência é a soma dos dois precedentes. Então, é assim:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Dividido passo a passo:

Comece com 0 e 1. Some esses dois números para obter o próximo número na sequência: 0 + 1 = 1. O próximo número é encontrado somando os dois últimos números: 1 + 1 = 2. Novamente, some os dois últimos números: 1 + 2 = 3. Repita esse processo para gerar o restante da sequência. Você pode continuar isso indefinidamente para gerar mais números na sequência de Fibonacci.

Matematicamente, isso pode ser expresso com uma relação de recorrência como esta:

F(0) = 0 F(1) = 1 F(n) = F(n-1) + F(n-2) para n > 1

Aqui, F(n) representa o n-ésimo número na sequência de Fibonacci. Então, para encontrar qualquer número específico na sequência, esta fórmula é usada, desde que os valores de F(0) e F(1) sejam conhecidos. Por exemplo, para encontrar F(5), calcule:

F(5) = F(4) + F(3) = 3 + 2 = 5
