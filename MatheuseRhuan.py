# Classe dos Estudantes
class Student:
    name = None
    cpf = None
    weight = 0
    height = 0
    email = None
    imc = None
    status = False

# Classe dos Exercícios
class Exercise:
    exerciseName = None
    numberRepetitions = 0
    exerciseWeight = 0

# Variáveis globais:
registredStudent = []  # lista de estudantes
exerciseStudent = []  # matriz de treinos

# Recebe os dados para cadastrar o estudantes
def cadastreReceive():
    check_if_name_already_exist = 0
    name = input("Insira o nome do novo Aluno: ")
    if len(name) > 1:
        for i in registredStudent:
            if name == i.name:
                check_if_name_already_exist += 1
        if check_if_name_already_exist == 0:
            cpf = input(f"Insira o CPF de {name}: ")
            if validateCPF(cpf) == True:
                email = input(f"Insira o email de {name}: ")
                if validateEmail(email) == True:
                    weight = float(input(f"Insira o peso de {name} em quilogramas: "))
                    height = float(input(f"Insira a altura de {name} em centímetros: "))
                    imc = calculatingIMC(weight, height)
                    studentCadastre(name, cpf, weight, height, email, imc)
                    print()
                    print(f"Aluno adicionado com sucesso!")
                else:
                    print("Email inválido, tente novamente.")
            else:
                print("CPF inválido, tente novamente.")
        else:
            print()
            print(f"O Aluno {name} já existe!")
    else:
        print()
        print("Por favor, insira um nome adequado!")

# Cadastra o estudante.
def studentCadastre(name, cpf, weight, height, email, imc):
    new = Student()
    new.name = name
    new.cpf = cpf
    new.weight = weight
    new.height = height
    new.email = email
    new.imc = imc
    new.classingIMC = classifyingIMC(imc)
    new.status = False
    registredStudent.append(new)  # cadastra estudante
    exerciseStudent.append([])  # insere um vetor de treinos vazio

# Descobre o Id do Estudante.
def searchStudentID(name):
    for i in range(len(registredStudent)):
        if name == registredStudent[i].name:
            return i
# Recebe os dados do exercício a ser inserido.
def receiveExercise(idStudent):
    check_if_exercise_already_exist = 0
    nameExer = input("Insira o nome do exercício: ")
    for i in exerciseStudent:
        for j in i:
            if nameExer == j.exerciseName:
                check_if_exercise_already_exist += 1
    if check_if_exercise_already_exist == 0:
        rep = int(input(f"Insira a quantidade de repetições de {nameExer}: "))
        weight = int(input(f"Insira o peso a ser utilizado em {nameExer}: "))
        addExercise(idStudent, nameExer, rep, weight)
    else:
        print("Esse exercício já existe!")

# Insere o exercício.
def addExercise(idStudent, name, rep, weight):
    exer = Exercise()
    exer.exerciseName = name
    exer.numberRepetitions = rep
    exer.exerciseWeight = weight
    registredStudent[idStudent].status = True
    exerciseStudent[idStudent].append(exer)
    for i in range(len(exerciseStudent[idStudent])):
        print(
            f"\nExercício: {exerciseStudent[idStudent][i].exerciseName} \nNúmero de repetições: {exerciseStudent[idStudent][i].numberRepetitions} \nPeso a ser utilizado: {exerciseStudent[idStudent][i].exerciseWeight}"
        )  # novo exercício no treino do respectivo estudante
    print("Exercício adicionado!")

# Altera um exercício existente.
def alterExercise(idStudent, exerciseName):
    check_student_exercise = 0
    for i in exerciseStudent:
        for j in i:
            if j.exerciseName == exerciseName:
                check_student_exercise += 1
    if check_student_exercise > 0:
        for i in exerciseStudent:
            for j in exerciseStudent[idStudent]:
                if j.exerciseName == exerciseName:
                    print(
                        f"Exercício: {j.exerciseName} \nNúmero de repetições: {j.numberRepetitions} \nPeso a ser utilizado: {j.exerciseWeight}"
                    )
                    j.exerciseName = input("Insira o novo nome do exercício: ")
                    j.numberRepetitions = int(
                        input(f"Insira o número de repetições de {j.exerciseName}: ")
                    )
                    j.exerciseWeight = int(
                        input(f"Insira o peso a ser utilizado em {j.exerciseName}: ")
                    )
                    print("Exercício alterado!")
    else:
        print("Exercício não encontrado!")

# Exclui um exercício existente.
def deleteExercise(idStudent, ExerciseExcluir):
    check_exercise_exists = 0
    if len(exerciseStudent[idStudent]) == 0:
        check_exercise_exists += 1
        print("Por favor, primeiro adicione um exercício ao treino!")
    for Exercise in exerciseStudent[idStudent]:
        if ExerciseExcluir == Exercise.exerciseName:
            check_exercise_exists += 1
            print(f"Exercício {Exercise.exerciseName} removido!")
            exerciseStudent[idStudent].remove(Exercise)
            if len(exerciseStudent[idStudent]) == 0:
                registredStudent[idStudent].status = False
    if check_exercise_exists == 0:
        print("Exercício não encontrado!")

# Exclui todos os exercícios do treino de um estudante.
def deleteAllExercises(idStudent):
    if len(exerciseStudent[idStudent]) != 0:
        exerciseStudent[idStudent].clear()
        print("Exercícios removidos!")
        registredStudent[idStudent].status = False
    else:
        print("Para remover os exercícios, primeiro adicione eles ao treino!")

# Consulta os dados de um estudante.
def viewStudent():
    showStudents()
    search_by_name = input("Insira o nome do aluno que desejas ver os dados: ")
    idStudent = searchStudentID(search_by_name)
    for i in range(len(registredStudent)):
        if search_by_name in registredStudent[i].name:
            print()
            print("Dados do Aluno: ")
            print(f" Nome: {registredStudent[i].name} \n CPF: {registredStudent[i].cpf} \n Peso: {registredStudent[i].weight} kg \n Altura: {registredStudent[i].height} cm\n Email: {registredStudent[i].email} \n IMC: {registredStudent[i].imc:.2f}\n Classificação do IMC: {registredStudent[i].classingIMC}")
            print(" Status:", "Ativo" if registredStudent[i].status == True else "Inativo")
            print()

            if exerciseStudent[i] != []:
                print(f"Treino de {registredStudent[i].name}: ")
                for j in exerciseStudent[idStudent]:
                    print(
                        f"Nome do Exercício: {j.exerciseName}\nNúmero de Repetições: {j.numberRepetitions}\nPeso do Exercício: {j.exerciseWeight} kg\n")
            else:
                print(f"O aluno {search_by_name} ainda não tem um exercício registrado")
        else:
            print(f"O aluno {search_by_name} não está registrado ")

# Atualiza os dados de um estudante a partir de seu Id.
def updateData(idStudent):
    print("Se você inserir '0' o elemento previamente cadastrado se manterá!")

    old_CPF = registredStudent[idStudent].cpf
    old_email = registredStudent[idStudent].email

    new_name = input(f"O nome atualmente cadastrado é: {registredStudent[idStudent].name}. O que você deseja inserir no lugar?\n")
    if new_name != "0":
        registredStudent[idStudent].name = new_name
    new_cpf = input(f"O CPF atualmente cadastrado é: {registredStudent[idStudent].cpf}. O que você deseja inserir no lugar?\n")
    if new_cpf != "0":
        if (validateCPF(new_cpf) == True):
            registredStudent[idStudent].cpf = new_cpf
        else:
            print("CPF Inválido!! Esse campo não será alterado.")
            registredStudent[idStudent].cpf = old_CPF
    
    new_weight = float(input(f"O peso atualmente cadastrado é: {registredStudent[idStudent].weight}. O que você deseja inserir no lugar?\n"))
    if new_weight != 0:
        registredStudent[idStudent].weight = new_weight
        weight_change = True
    else:
        weight_change = False

    new_height = int(input(f"A altura atualmente cadastrada é: {registredStudent[idStudent].height}. O que você deseja inserir no lugar?\n"))
    if new_height != 0:
        registredStudent[idStudent].height = new_height
        height_change = True
    else:
        height_change = False

    new_email = input(f"O email atualmente cadastrado é: {registredStudent[idStudent].email}. O que você deseja inserir no lugar?\n")
    if new_email != "0":
        if validateEmail(new_email) == True:
            registredStudent[idStudent].email = new_email
        else:
            print("Email Inválido!! Esse campo não será alterado.")
            registredStudent[idStudent].cpf = old_email

    if height_change == True or weight_change == True:
        registredStudent[idStudent].imc = calculatingIMC(registredStudent[idStudent].weight, registredStudent[idStudent].height)

# Exclui um estudante.
def deleteStudent():
    check_student_exists = 0
    showStudents
    name_delete_student = input("Insira o nome do aluno que queres excluir: ")
    for i in registredStudent:
        if name_delete_student == i.name:
            check_student_exists += 1
            print(f"Aluno {i.name} removido!")
            registredStudent.remove(i)
    if check_student_exists == 0:
        print()
        print("Aluno não encontrado!")

# Exibe o relatório de todos os estudantes.
def reportStudents():
    report_view = input(
        "Escolha que alunos deseja ver: \n1. Todos os alunos\n2. Apenas alunos ativos\n3. Apenas alunos inativos\n"
    )
    match report_view:
        case "1":
            print()
            print("    Aluno", "   CPF   ", "Peso", "Altura", "     Email     ", "IMC", "Classificação IMC","Status", sep="    |    ")
            for i in range(len(registredStudent)):
                print(f"    {registredStudent[i].name}",registredStudent[i].cpf, registredStudent[i].weight, f"  {registredStudent[i].height}", registredStudent[i].email, f" {registredStudent[i].imc:.2f}", f"      {registredStudent[i].classingIMC}", "       Ativo" if registredStudent[i].status == True else "     Inativo", sep="       ")
        case "2":
            verificator = 0
            for i in range(len(registredStudent)):
                if registredStudent[i].status == True:
                    verificator += 1
            if verificator > 0:
                print()
                print("    Aluno", "   CPF   ", "Peso", "Altura", "     Email     ", "IMC", "Classificação IMC","Status", sep="    |    ")
                for i in range(len(registredStudent)):
                    if registredStudent[i].status == True:
                        print(f"    {registredStudent[i].name}",registredStudent[i].cpf, registredStudent[i].weight, f"  {registredStudent[i].height}", registredStudent[i].email, f" {registredStudent[i].imc:.2f}", f"      {registredStudent[i].classingIMC}", "       Ativo" if registredStudent[i].status == True else "     Inativo", sep="       ")
            else:
                print("Dentre os Alunos, atualmente nenhum está Ativo!")
        case "3":
            verificator = 0
            for i in range(len(registredStudent)):
                if registredStudent[i].status == False:
                    verificator += 1
            if verificator > 0:
                print()
                print("    Aluno", "   CPF   ", "Peso", "Altura", "     Email     ", "IMC", "Classificação IMC","Status", sep="    |    ")
                for i in range(len(registredStudent)):
                    if registredStudent[i].status == False:
                        print(f"    {registredStudent[i].name}",registredStudent[i].cpf, registredStudent[i].weight, f"  {registredStudent[i].height}", registredStudent[i].email, f" {registredStudent[i].imc:.2f}", f"      {registredStudent[i].classingIMC}", "       Ativo" if registredStudent[i].status == True else "     Inativo", sep="       ")
            else:
                print("Dentre os Alunos, atualmente nenhum está Inativo!")
        case _:
            print("Operador inválido!")


# Menu principal
def mainMenu():
    openMenu = int(input("Desejas iniciar o Menu?\n1. Sim\n2. Não \n"))
    if openMenu == 1:
        print("Bem vindo ao sistema")
        menu = int(input("Qual operação desejas realizar? \n 1. Cadastrar aluno. \n 2. Gerenciar treino. \n 3. Consultar alunos. \n 4. Atualizar cadastro do aluno. \n 5. Excluir aluno. \n 6. Relatório de aluno. \n 7. Sair \n"))
        if menu == 1:
            print()
            cadastreReceive()
            return True
        if menu == 7:
            return False
        if registredStudent != []:
            if menu == 2:
                print()
                menuManage()
                return True
            elif menu == 3:
                print()
                viewStudent()
                return True
            elif menu == 4:
                print()
                showStudents()
                nameStudent = input("Insira o nome do aluno que desejais atualizar os dados: ")
                idStudent = searchStudentID(nameStudent)
                updateData(idStudent)
                return True
            elif menu == 5:
                print()
                deleteStudent()
                return True
            elif menu == 6:
                print()
                reportStudents()
                return True
            else:
                print("\nPor favor, digite um número válido!")
                return True
        else:
            print("Não há nenhum aluno Cadastrado, por favor, antes de tentar qualquer uma dessas operações, cadastre um aluno!!")
            return True
    elif openMenu == 2:
        return False
    else:
        print()
        print("Operação inválida, tente novamente!")
        return True
    
# Menu Gerenciar Treino
def menuManage():
    showStudents()
    student_to_manage_workout = input("Insira o nome do Aluno que deseja gerenciar o treino: ")
    idStudent = searchStudentID(student_to_manage_workout)
    if idStudent != None:
        menuManage = int(
            input(f"Qual operação deseja realizar? \n 1. Incluir um novo exercício no treino de {student_to_manage_workout}. \n 2. Alterar um exercício existente no treino de {student_to_manage_workout}. \n 3. Excluir um exercício do treino de {student_to_manage_workout}. \n 4. Excluir todos os exercícios do treino de {student_to_manage_workout}. \n"))
        if menuManage == 1:
            print()
            receiveExercise(idStudent)

        elif menuManage == 2:
            print()
            showStudentExercises(idStudent)
            Exercisename = input("Insira o nome do exercício que deseja alterar: ")
            print()
            alterExercise(idStudent, Exercisename)

        elif menuManage == 3:
            print()
            ExerciseExcluir = input("Insira o nome do exercício que deseja excluir: ")
            print()
            deleteExercise(idStudent, ExerciseExcluir)
        elif menuManage == 4:
            print()
            confirmation = int(
                input(f"Tem certeza que deseja excluir todos os exercícios de {student_to_manage_workout}? \n1. Sim \n2. Não \n"))
            print()
            if confirmation == 1:
                deleteAllExercises(idStudent)
            elif confirmation == 2:
                print(f"Os exercícios de {student_to_manage_workout} não foram excluídos!")
            else:
                print("Por favor, digite um número válido.")
        else:
            print("Por favor digite um número válido.")
    else:
        print("Aluno não encontrado.")

#Exibe os estudantes cadastrados no sistema.
def showStudents():
    if registredStudent == []:
        print("Não há, atualmente, nenhum aluno cadastrado!!")
        
    else:
        print(f"A academia tem atualmente: {(len(registredStudent))} alunos.")
        for i in range(len(registredStudent)):
            print(f"Aluno {i + 1}: {registredStudent[i].name}")

def showStudentExercises(idStudent):
    print(f"Os exercícios do Estudante {registredStudent[idStudent].name} são:")
    for i in range(len(exerciseStudent[idStudent])):
        print(f"Exercío {i}: {exerciseStudent[idStudent][i].exerciseName}")

    

#Funções para validar CPF e Email, e funções para cálculo e classificação de IMC.
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
    elements_to_multiplicate = range(10,1,-1) 

    def multiplePerDigit(rearranging_cpf, elements_to_multiplicate):
        for i in range(len(rearranging_cpf)):
            result = rearranging_cpf[i] * elements_to_multiplicate[i]
            result_of_multiplication.append(result)

    multiplePerDigit(rearranging_cpf, elements_to_multiplicate)
    sum_of_multiplication = sum(result_of_multiplication)

    def calculateVerificationDigits(sum):
        leftover = sum % 11

        if leftover == 0 or leftover == 1 or leftover > 10:
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
        if realCPF == rearranging_cpf and len(realCPF) == 11:
            return True
        else:
            return False

    return finalCheck(realCPF, rearranging_cpf)

def classifyingIMC(imc):
    imc = float(imc)
    if imc < 16.9:
        return "Muito Abaixo do Peso"
    if imc >= 17 and imc <= 18.4:
        return "Abaixo do Peso"
    if imc >= 18.5 and imc <= 24.9:
        return "Normal"
    if imc >= 25 and imc <= 29.9:
        return "Acima do Peso"
    if imc >= 30 and imc <= 34.9:
        return "Obesidade Grau I"
    if imc >= 35 and imc <= 40:
        return "Obesidade Grau II"
    if imc > 40:
        return "Contagem Regressiva"

def calculatingIMC(weight, height):
    if height > 2.2:
        height = height / 100
    IMC = weight / (height * height)
    rounded_imc = round(IMC)
    return rounded_imc

import re
def validateEmail(email):
    r = re.compile(r"^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
    if r.match(email):
        return True
    else:
        return False

# main
print("Bem vindo à academia do Xandão Biblical\nO estabelecimento tornou-se público por tempo indeterminado!")
while True:
    try:
        onWorking = mainMenu()
        print()
        if onWorking == True:
            continue
        else:
            print("Encerrando programa...")
            break

    except ValueError:
        print("Operador não identificado, encerrando programa...")
        break