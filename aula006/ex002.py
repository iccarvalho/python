def main():
    alunos = []
    print("Registre 5 alunos")
    registarAlunos(alunos)
    response = input("Quer verificar se algum aluno foi cadastrado? [S/N]: ")
    verificarCadastro(alunos) if response.upper() == "S" else None
    media = mediaGeral(alunos)
    print(f"A média geral dos alunos é: {media:.2f}")

def registarAlunos(lista:list):
    cadastrados = []
    for i in range(1, 6):
        while True:
            cadastro = int(input(f"Informe o código de cadastro do {i}º aluno: "))

            if(i > 1 and cadastro in cadastrados):
                print("Cadastro inválido! Tente novamente")
            else:
                cadastrados.append(cadastro)
                break

        notas = []
        for i in range(1, 4):
            while True:
                nota = float(input(f"Informe a {i}ª nota do aluno de 0 a 10: "))

                if(nota >= 0 and nota <= 10):
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! Tente novamente")
                    
        
        media = mediaNotas(notas)

        aluno = {
            "cad": cadastro,
            "notas": notas,
            "media": media
        }

        lista.append(aluno)


def mediaNotas(notas:list):
    soma = 0
    for n in notas:
        soma += n

    return soma/len(notas)

def verificarCadastro(lista:list):
    while True:
        cad = int(input("Informe o cadastro que deseja verificar: "))
        encontrou = False
        for aluno in lista:
            if aluno["cad"] == cad:
                print("Aluno se encontra cadastrado!")
                encontrou = True
                break
        if not encontrou:
            print("Aluno não encontrado!")

        response = input("Deseja verificar outro código de cadastro? [S/N]: ")
        if response.upper() == "N":
            break

def mediaGeral(lista:list):
    soma = 0
    for aluno in lista:
        soma += aluno["media"]
    
    return soma/len(lista)

main()