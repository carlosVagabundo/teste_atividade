pedidos = 0  


def calcular_total(preco, quantidade=1):
    global pedidos
    subtotal_pedido_ref = preco * quantidade  
    pedidos = pedidos + 1
    return subtotal_pedido_ref


print("Primeiro pedido:", calcular_total(4))
print("Segundo pedido:", calcular_total(4, 3))
print("Terceiro pedido:", calcular_total(quantidade=2, preco=5))
print("Quantidade de pedidos:", pedidos)
