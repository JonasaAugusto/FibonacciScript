Criei um Script que verifica se o número dado é da sequencia de fibonacci ou não.

Para calcular a sequência, eu utilizei o seguinte raciocínio:
n = a + b
Onde "a" e "b" são os números anteriores a "n" na sequencia de Fibonacci,

Invertendo a equação eu obtive: n - b = a 
Que substituindo a por "n - b" adquiri: n = (n - b) + b

Aplicando o quadrado dos números e multiplicando ambos os lados por 5n temos: 5n² = 5n(n - b) + 5nb
Adicionando ou subtraindo em ambos os lados, temos o resultado: 5n² + 4b² = 5n(n - b) + 5nb + 4b²

Porém ainda sabendo que "n - b" é igual a "a", substituindo eu obtive: 5n² + 4b² = 5na + 5nb + 4b²V

Vendo que "5na + 5nb" é igual a "5n(a + b)", que é igual a "5n²" porque "a + b" é igual a "n" na sequência de Fibonacci. Então simplificando a equação ficou: 5n² + 4b² = 5n² + 4b²

E simplificando mais ainda eu tive o resultado: 5n² + 4b² = (5n ± 2)²

Assim entrando a expressão no código na linha 31: "5*n*n + 4" ou "5*n*n - 4"
Sendo possível verificar se 'n' pertence ou não à sequência de fibonacci.
