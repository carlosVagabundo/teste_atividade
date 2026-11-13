
tema1 = input("Digite o primeiro tema de estudo: ")
tema2 = input("Digite o segundo tema de estudo: ")
tema3 = input("Digite o terceiro tema de estudo: ")

arquivo_estudos_ref = open("estudos.txt", "w", encoding="utf-8")
arquivo_estudos_ref.write(tema1 + "\n")
arquivo_estudos_ref.writelines([tema2 + "\n", tema3 + "\n"])
arquivo_estudos_ref.close()

arquivo_estudos_ref = open("estudos.txt", "r", encoding="utf-8")
print("\nConteúdo completo do arquivo:")
print(arquivo_estudos_ref.read())
arquivo_estudos_ref.close()

arquivo_estudos_ref = open("estudos.txt", "r", encoding="utf-8")
print("Primeira linha do arquivo:")
print(arquivo_estudos_ref.readline(), end="")
arquivo_estudos_ref.close()

arquivo_estudos_ref = open("estudos.txt", "r", encoding="utf-8")
print("\nLista de linhas do arquivo:")
print(arquivo_estudos_ref.readlines())
arquivo_estudos_ref.close()
