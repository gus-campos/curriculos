# O que é

Programa básico em Python que usa leitura de arquivos de dados e orientação à objetos para representar disciplinas/cursos e currículos, de forma que eu possa analisar a melhor sequência de disciplinas a serem feitas na minha graduação. 

## O problema

A grade de Ciências Exatas na UFJF é um tanto flexível, permitindo que cada aluno construa sua grade de acordo com seus interesses de estudo. Como vim de outra graduação e já tinha feito muitas disciplinas, e quero realizar disciplinas da Ciência da Computação (para depois completar também tal graduação), se tornou um tanto confuso saber exatamente quais disciplinas eu poderia fazer que contribuísse no cumprimento do currículo das duas graduações, respeitando os pré-requisitos das Ciências Exatas, e concluindo-a no menor tempo possível. Além disso, são mais de 30 páginas de tabelas descrevendo as disciplinas eletivas possíveis, o que torna o processo ainda mais complicado.

## A solução

A conversão dos dados em PDF para arquivos csv, como o seguinte, permitiu a fácil leitura dos dados e construção dos objetos que representa as diciplinas (cursos) e o currículo, que é um conjunto de cursos com outros atributos e métodos relacionados.

```
PERÍODO,CÓDIGO,NOME,CH,REQ
2,FIS114,Física Prática I,30,---
2,MAC013,Representação Gráfica e Modelagem Geométrica,60,MAT155
2,MAT049,Álgebra Linear II,60,MAT155
2,MAT122,Geometria Plana,60,---
2,MAT133,Fundamentos de Matemática Elementar,60,---
```
