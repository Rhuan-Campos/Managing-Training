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
    # print(cadAlunos[0].nome, cadAlunos[0].cpf, cadAlunos[0].peso, cadAlunos[0].altura)
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


def recebeExercicio(aluno1):
    nomeExer = input("Insira o nome do exercício: ")
    rep = input(f"Insira a quantidade de repetições de {nomeExer}: ")
    peso = input(f"Insira o peso a ser utilizado em {nomeExer}: ")
    print(aluno1)
    
    for i in range(len(cadAlunos)):
        # print(cadAlunos[i].nomeExer)
        if aluno1 in cadAlunos[i].nome :
            idAluno= i
    # print(idAluno)
    insereExercicio(idAluno, nomeExer, rep, peso)
    

# Inserir um Exercício
def insereExercicio(idAluno, nome, rep, peso):
    exer = Exercicio()
    exer.nomeExercicio = nome
    exer.numRepeticoes = rep
    exer.pesoExercicio = peso
    # for i in treinoAlunos:
    #     for j in range(treinoAlunos.length):
    #         if i == treinoAlunos[j].exer.nome:
    #             return print("Esse exercício já existe")
    #         else:
    #             return print("Exercício adicionado")
    treinoAlunos[idAluno].append(exer)
    # print(treinoAlunos) 
    for i in range(len(treinoAlunos[idAluno])):
        print(treinoAlunos[idAluno][i].nomeExercicio) # novo exercício no treino do respectivo aluno

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
    aluno1 = input("Insira o nome do aluno que deseja gerenciar o treino: ")
    menuGerenciar = int(input(
        f"Qual operação deseja realizar? \n1. Incluir um novo exercício no treino de {aluno1}. \n2. Alterar um exercício existente no treino de {aluno1}. \n3. Excluir um exercício do treino de {aluno1}. \n4. Excluir todos os exercícios do treino de {aluno1}. \n")
    )
    if menuGerenciar == 1:
        recebeExercicio(aluno1)

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


# def consultarAluno():


# def atualizarDados():


# def excluirAluno():


# def relatorioAlunos():


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
