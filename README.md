# O que é

Programa básico em Python que usa leitura de arquivos de dados e orientação à objetos para representar disciplinas/cursos e currículos, de forma que eu possa analisar a melhor sequência de disciplinas a serem feitas na minha graduação. 

## O problema

A grade de Ciências Exatas na UFJF é um tanto flexível, permitindo que cada aluno construa sua grade de acordo com seus interesses de estudo. Como vim de outra graduação, já tinha feito muitas disciplinas, e quero realizar disciplinas da Ciência da Computação (para depois completar também tal graduação), se tornou um tanto confuso saber exatamente quais disciplinas eu poderia fazer que contribuísse no cumprimento do currículo das duas graduações, respeitando os pré-requisitos das Ciências Exatas, e concluindo-a no menor tempo possível. Além disso, são mais de 30 páginas de tabelas descrevendo as disciplinas eletivas possíveis, o que tornaria o processo ainda mais complicado.

## A solução

A conversão dos dados em PDF para arquivos csv, como o seguinte, permitiu a fácil leitura dos dados e construção dos objetos que representa as diciplinas (cursos) e o currículo, que é um conjunto de cursos com outros atributos e métodos relacionados.

```
PERÍODO,CÓDIGO,NOME,CH,REQ
2,FIS114,Física Prática I,30,---
2,MAC013,Representação Gráfica e Modelagem Geométrica,60,MAT155
...
```
A partir de então, com o uso de boas práticas na nomeação das variáveis, abstração e encapsulamento, foi possível usar esse programa abstrato e intuitivo para determinar quais disciplinas eu poderia fazer de tal currículo, considerando meu histórico escolar atual:

![](assets/usage.png) 

## Resultado

Uma lista dizendo exatamente quais disciplinas devo fazer em cada período, para que eu conclua a graduação em Ciências Exatas no menor tempo possível, e ao mesmo tempo contribua no cumprimento da carga horária da minha futura graduação em Ciência da Computação.

```
 ========== OBRIGATÓRIAS - PERÍODO 2 ========== 

FIS077 | LABORATÓRIO DE FÍSICA I
MAT143 | INTRODUÇÃO À TEORIA DOS NÚMEROS
DCC013 | ESTRUTURA DE DADOS
DCC160 | LÓGICA E FUNDAMENTOS PARA A COMPUTAÇÃO
DCC070 | ORGANIZAÇÃO DE COMPUTADORES
DCC163 | PESQUISA OPERACIONAL
EST029 | CÁLCULO DE PROBABILIDADES I
DCC025 | ORIENTAÇÃO A OBJETOS

 ========== OBRIGATÓRIAS - PERÍODO 3 ========== 

DCC001 | ANÁLISE E PROJETO DE ALGORITMOS
DCC012 | ESTRUTURA DE DADOS II
DCC059 | TEORIA DOS GRAFOS
DCC063 | LINGUAGENS FORMAIS E AUTÔMATOS
DCC042 | REDES DE COMPUTADORES
DCC062 | SISTEMAS OPERACIONAIS
DCC117 | MODELAGEM DE SISTEMAS
```
