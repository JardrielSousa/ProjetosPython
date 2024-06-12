

quantidadeProdutos = 0 
tecla = "c"
total = 0.0

while(quantidadeProdutos<5 and tecla!='p'):
    print("======================")
    print("caixa rápido : somente 10 unidades")
    print("======================")
    quantidadeProdutos = quantidadeProdutos + 1
    preco = float(input("valor:"))
    total = preco + total
    print("Pressione :  C  / para continuar /n ")
    print("Pressione :  P  / para sair /n ")
    tecla = input("tecla:")

print("total dos produtos é :"+str(total))

            
