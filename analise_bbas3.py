import pandas as pd
import yfinance as yf

#Extraindo os dados da Transmissão Paulista do Yahoo Finance
trpl4 = yf.Ticker('BBAS3.SA')
historico = trpl4.history(period= '5y')
print(historico)

#Extraindo os historico de dividendos dos  ultimos 5 anos
dividendos = trpl4.dividends
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
preco_teto_da_acao = 34.20
preco_atual = 26.43

# O preço atual da ação está menor que o preço teto considerando 8% de retorno anual