
from vendas.calc_preco import aumento, reducao


preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15)
print(preco_com_aumento)


preco_com_reducao = reducao(valor=preco, porcentagem=15)
print(preco_com_reducao)
