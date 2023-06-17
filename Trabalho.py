# Classe dos Alunos
class Aluno:
    nome = None
    cpf = None
    peso = 0
    altura = 0
    status = False


# Classe dos Exercícios
class Exercicio:
    nomeExercicio = None
    numRepeticoes = 0
    pesoExercicio = 0


# Variáveis globais:
cadAlunos = []  # lista de alunos
treinoAlunos = []  # matriz de treinos

def recebeCadastro():
    nome = input("Insira o nome do novo aluno: ")
    cpf = input("Insira o cpf de " + nome + ": ")
    # if validateCPF(cpf) == True:
    peso = float(input(f"Insira, em quilogramas, o peso de {nome}: "))
    altura = int(input(f"Insira a altura de {nome}: "))
    print()
    cadastroAluno(nome, cpf, peso, altura)
    print(cadAlunos[0].nome, cadAlunos[0].cpf, cadAlunos[0].peso, cadAlunos[0].altura)
    # else:
            # print("CPF inválido, tente novamente.")

# Cadastro do Aluno
def cadastroAluno(nome, cpf, peso, altura):
    novo = Aluno()
    novo.nome = nome
    novo.cpf = cpf
    novo.peso = peso
    novo.altura = altura
    novo.status = False
    cadAlunos.append(novo)  # cadastra aluno
    treinoAlunos.append([])  # insere um treino vazio


def recebeExercicio(aluno):
    nome = input("Insira o nome do exercício: ")
    rep = input(f"Insira a quantidade de repetições de {nome}: ")
    peso = input(f"Insira o peso a ser utilizado em {nome}: ")
    idAluno = cadAlunos.index(aluno)
    insereExercicio(idAluno, nome, rep, peso)
# Inserir um Exercício
def insereExercicio(idAluno, nome, rep, peso):
    exer = Exercicio()
    exer.nomeExercicio = nome
    exer.numRepeticoes = rep
    exer.pesoExercicio = peso
    for i in treinoAlunos:
        for j in range(treinoAlunos.length):
            if i == treinoAlunos[j].exer.nome:
                return print("Esse exercício já existe")
            else:
                return print("Exercício adicionado")
    treinoAlunos[idAluno].append(exer)  # novo exercício no treino do respectivo aluno


# Menu principal
def menuPrincipal():
    print("Bem vindo ao sistema")
    menu = int(
        input(
            "Qual operação deseja realizar? \n1. Cadastrar aluno. \n2. Gerenciar treino. \n3. Consultar aluno. \n4. Atualizar cadastro do aluno. \n5. Excluir aluno. \n6. Relatório de alunos. \n7. Sair \n" 
        )
    )
    if menu == 1:
        recebeCadastro()
        return True
    elif menu == 2:
        menuGerenciar()
        return True
    # elif menu == 3:

    # elif menu == 4:

    # elif menu == 5:

    # elif menu == 6:

    elif menu == 7:
        return False
    else:
        print("Por favor digite um número válido.")


# Menu Gerenciar Treino
def menuGerenciar():
    aluno = input("Insira o nome do aluno que deseja gerenciar o treino: ")
    menuGerenciar = input(
        f"Qual operação deseja realizar? \n1. Incluir um novo exercício no treino de {aluno}. \n2. Alterar um exercício existente no treino de {aluno}. \n3. Excluir um exercício do treino de {aluno}. \n4. Excluir todos os exercícios do treino de {aluno}. \n"
    )
    if menuGerenciar == 1:
        recebeExercicio(aluno)

    # elif menuGerenciar == 2:

    # elif menuGerenciar == 3:

    # elif menuGerenciar == 4:

    else:
        print("Por favor digite um número válido.")


# def incluiNovoExercicio():
# Talvez dá pra colocar na própria insere exercício dnv, só verificar se ele já não existe.


def validateCPF(cpf):

    sum_of_multiplication = []
    result_of_multiplication = []
    verifications_digits = []

    rearranging_cpf = list(cpf)


    for j in rearranging_cpf:
        if j == '.' or j == '-':
            rearranging_cpf.remove(j)
    realCPF = rearranging_cpf
    rearranging_cpf = list(map(int, rearranging_cpf))

    rearranging_cpf.pop(-1)
    rearranging_cpf.pop(-1)

    elements_to_multiplicate = [range(10,1,-1)]

    def multiplePerDigit(rearranging_cpf, elements_to_multiplicate):
        for i in range(len(rearranging_cpf)):
            result = rearranging_cpf[i] * elements_to_multiplicate[i]
            result_of_multiplication.append(result)

    multiplePerDigit(rearranging_cpf, elements_to_multiplicate)

    sum_of_multiplication = sum(result_of_multiplication)

    def calculateVerificationDigits(sum):
        leftover = sum % 11

        if leftover < 2 or leftover == 10:
            return verifications_digits.append(0)
        else:
            first_digit = 11 - leftover
            return verifications_digits.append(first_digit)

    calculateVerificationDigits(sum_of_multiplication)
    elements_to_multiplicate = [*range(11,1,-1)]
    rearranging_cpf.append(verifications_digits[0])

    result_of_multiplication.clear()

    multiplePerDigit(rearranging_cpf, elements_to_multiplicate)

    sum_of_multiplication = sum(result_of_multiplication)

    calculateVerificationDigits(sum_of_multiplication)

    rearranging_cpf.append(verifications_digits[1])

    def finalCheck(realCPF, rearranging_cpf):
        realCPF = list(map(int, realCPF))
        if realCPF == rearranging_cpf:
            return True
        else:
            return False

    return finalCheck(realCPF, rearranging_cpf)


def calculatingIMC(peso, altura):
    IMC = peso / (altura * altura)
    return print(f"O índice de massa corporal é: {IMC:.2f}")


# peso = 68.0
# altura = 1.80
# calculatingIMC(peso, altura)

import re


def validateEmail(email):
    r = re.compile(r"^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
    if r.match(email):
        return print(f"O email: {email} é válido!!")
    else:
        return print(f"O email informado não é válido!!")


# email = 'matheusbalbinotzuchi@edu.com'
# validateEmail(email)


def alteraExercicio(idAluno, nome):
    treinoAlunos[idAluno]


# def excluirExercicio():

# def excluirExTodos():


def consultarAluno(idAluno):
    search_by_name = input("Input the name of the pupil you want to view the data: ")

    for i in range(len(cadAlunos)):
        if search_by_name in cadAlunos[i].nome:
            if treinoAlunos[i] != []:
                print("Pupil Data: ")
                print(f"Nome: {cadAlunos[i].nome}\nCPF: {cadAlunos[i].cpf}\nPeso: {cadAlunos[i].peso}\nAltura:{cadAlunos[i].Altura}\n")
                print(f"Pupil Training: ")
                for j in range(len(treinoAlunos[idAluno][0])):
                    print(f"Nome do Exercício: {treinoAlunos[idAluno][j].nomeExercicio}\n Número de Repetições: {treinoAlunos[idAluno][j].numRepeticoes}\n Peso do Exercício: {treinoAlunos[idAluno][j].pesoExercicio}\n")
            else:
                print(f"The Pupil {search_by_name} does't have a registred workout")
        else:
            print(f"The Pupil {search_by_name} is not registred ")


def atualizarDados(idAluno):
    # edit_by_name = input("Input the name of the pupil you want to edit data: ")
    print("if you enter 0 will stay the same): ")
    cadAlunos[idAluno].nome = input(f'The actual Name is: {cadAlunos[idAluno].nome}. What do you want to put?')
    cadAlunos[idAluno].cpf = input(f'The actual CPF is: {cadAlunos[idAluno].cpf}. What do you want to put?')
    cadAlunos[idAluno].peso = input(f'The actual Weight is: {cadAlunos[idAluno].peso}. What do you want to put?')
    cadAlunos[idAluno].altura = input(f'The actual Height is: {cadAlunos[idAluno].altura}. What do you want to put?')
            

def excluirAluno():
    name_delete_pupil = input("Input the name of the pupil you want to delete data: ")
    for i in range(len(cadAlunos)):
        if name_delete_pupil in cadAlunos[i].nome:
            cadAlunos[i].clear()

def relatorioAlunos():
    ## Atribuir status de "Ativo", "Passivo", "Inativo"
    report_view = input("Choose what you want to view: \n 1 - All Pupils \n 2 - Just Active Pupils\n 3 - All Pupils")
    match report_view:
        case "1":
            for i in range(len(cadAlunos)):
                print("Pupil Data: ")
                print(f"Nome: {cadAlunos[i].nome}\nCPF: {cadAlunos[i].cpf}\nPeso: {cadAlunos[i].peso}\nAltura:{cadAlunos[i].Altura}\n")
        case "2":
            print('a')
        case "3":
            print('a')



# main
while True:
    try:
        confirmacao = menuPrincipal()
        if confirmacao == True:
            continue
        else:
            break

    except EOFError:
        print("Por favor Andressa, insira alguma coisa.")
        break
