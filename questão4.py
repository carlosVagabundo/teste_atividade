
def salvar_pontos(pontos, nome_arquivo="pontos.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        caracteres_escritos = arquivo.write(str(pontos))
    return caracteres_escritos


def ler_pontos(nome_arquivo="pontos.txt"):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo_pontos_ref = arquivo.read()
        return int(conteudo_pontos_ref)

salvar_pontos(pontos=30)

nome_arquivo_ler = input("Digite o nome do arquivo que deseja ler: ")

try:
    pontos_lidos = ler_pontos(nome_arquivo=nome_arquivo_ler)
except FileNotFoundError:
    print("Arquivo não encontrado")
except ValueError:
    print("Conteúdo inválido")
else:
    print("Pontos:", pontos_lidos)
