SELECT DescSistemaOrigem,
       sum(QtdePontos) AS qtdePontos,
       avg(QtdePontos) AS avgPontos,
       count(IdTransacao) AS qtdeTransacao

--FODASSEEEE

FROM transacoes
GROUP BY DescSistemaOrigem