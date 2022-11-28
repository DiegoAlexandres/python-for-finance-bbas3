import pandas as pd
import yfinance as yf

#Extraindo os dados do Banco do Brasil do Yahoo Finance
bbas3 = yf.Ticker('BBAS3.SA')
historico = bbas3.history(period= '5y')
print(historico)

#Extraindo os historico de dividendos dos  ultimos 5 anos
dividendos = bbas3.dividends
dados = pd.DataFrame(dividendos).reset_index()
print(dados)

#Calculando a média de pagamentos de dividendos
soma_dividendos = dados.Dividends.sum()
print(soma_dividendos)

pagamento_medio = soma_dividendos / 5
print(pagamento_medio)

#Calculando o preço teto da ação 
def preco_teto(pagamento_medio, dividendos_esperado):
    return print(pagamento_medio / dividendos_esperado)

preco_teto(pagamento_medio, 0.08)

#Conclusão da análise
preco_teto_da_acao = 26.43
preco_atual = 34.21

# O preço atual da ação está maior que o preço teto considerando 8% de retorno anual
