def main():
    cadastro = []
    while True:
        cadastrarAluno(cadastro)
        res = input("Gostaria de cadastrar mais um aluno? [S/N]\n")
        if res.upper() == "N":
            break
    
    print("\nRelatório escolar\n")
    print(f"{len(cadastro)} alunos foram cadastrados")
    print(f"Média geral das notas: {calcularMedia(cadastro):.2f}")
    print(f"Maior nota: {maiorNota(cadastro)}")
    print(f"Menor nota: {menorNota(cadastro)}")
    print(f"Percentual de alunos aprovados: {aprovados(cadastro):.2f}%\n")
    mostrarAlunos(cadastro)

def cadastrarAluno(cadastro:list):
    nome = input("Informe o nome do aluno: ")
    while True:
        nota = float(input(f"Informe a nota de {nome} de 0 a 10: "))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("Nota inválida! Tente novamente.")
        nota
    situacao = "Aprovado" if nota >= 7 else "Reprovado"
    
    aluno = {
        "nome": nome,
        "nota": nota,
        "situacao": situacao
    }
    cadastro.append(aluno)

def calcularMedia(cadastro:list):
    soma = 0
    for aluno in cadastro:
        soma += aluno["nota"]
    
    media = soma/len(cadastro)
    return media

def maiorNota(cadastro:list):
    notas = []
    for aluno in cadastro:
        notas.append(aluno["nota"])
    
    maiorNota = max(notas)
    return maiorNota

def menorNota(cadastro:list):
    notas = []
    for aluno in cadastro:
        notas.append(aluno["nota"])
    
    menorNota = min(notas)
    return menorNota

def aprovados(cadastro:list):
    cont = 0
    for aluno in cadastro:
        if aluno["nota"] >= 7:
            cont += 1
    
    percent = (cont / len(cadastro)) * 100
    return percent

def mostrarAlunos(cadastro:list):
    for aluno in cadastro:
        print(f"Nome: {aluno["nome"]} - Nota: {aluno["nota"]} - Situação: {aluno["situacao"]}")

main()