
def dividir_material(total, equipes):
    if total < 0 or equipes < 0:
        raise ValueError
    return total / equipes


print("Divisão de materiais")

try:
    total = int(input("Digite o total de materiais: "))
    equipes = int(input("Digite a quantidade de equipes: "))
    resultado_divisao_ref = dividir_material(total, equipes)
except ValueError:
    print("Entrada inválida")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
else:
    print("Itens por equipe:", resultado_divisao_ref)
finally:
    print("Processamento encerrado")
