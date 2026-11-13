
def dividir_material(total, equipes):
    if total < 0 or equipes < 0:
        raise ValueError

    return total / equipes


print("Divisão de materiais")

try:
    total = int(input("Quantidade de materiais: "))
    equipes = int(input("Quantidade de equipes: "))

    resultado = dividir_material(total, equipes)

    print("Materiais para cada equipe:", resultado)

except ValueError:
    print("Valor inválido! Digite números positivos.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

finally:
    print("Programa encerrado!")
