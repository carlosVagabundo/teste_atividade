
def dividir_material(total, equipes):
    if total < 0 or equipes < 0:
        raise ValueError("Valores não podem ser negativos")

    resultado = total / equipes
    return resultado


print("Divisão de materiais")

try:
    total = int(input("Digite a quantidade de materiais: "))
    equipes = int(input("Digite o número de equipes: "))

    resultado = dividir_material(total, equipes)

    print("Cada equipe vai receber:", resultado, "materiais")

except ValueError:
    print("Digite apenas números válidos!")

except ZeroDivisionError:
    print("Não é possível dividir por zero!")

finally:
    print("Fim do programa")
