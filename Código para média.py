aluno = str(input("Digite seu nome: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 7:
    print(f"Media inferior a 7", aluno, "Reprovado")
elif 7 <= media <= 8.5:
    print(f"Aluno: ", aluno, "está aprovado porém na média")
else:
    print(f"Aluno: ", aluno, "está aprovado com excelência")
