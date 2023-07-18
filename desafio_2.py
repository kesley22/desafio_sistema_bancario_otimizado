
def  menu ():
    menu = """\n
    ----------MENU----------
    [1]\tDepositar
    [2]\tExtrato
    [3]\tSacar
    [4]\tNova conta
    [5]\tNovo usuário
    [6]\tListar contas
    [0]\tSair
    -->"""


def depositar(saldo, valor,extrato,/):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n ---Depósito realizado com sucesso! ----")
    else:
            print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo= valor > saldo
    excedeu_limite= valor > limite
    excedeu_saques= numero_saque > limite_saque

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numeros_saques += 1
        print("\n Saque realizado com sucesso!")

    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=========EXTRATO=========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================")

def criar_usuario(usuarios):
     cpf = input("informe o CPF (SOMENTE NÚMEROS): ")
     usuarios = filtrar_usuario(cpf, usuarios)

     if usuarios:
          print("\n Ja existe um usuário com este CPF! ")
          return
     
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento: ")
     endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado):")

     usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "CPF": cpf, "endereço": endereco})

     print("----USUÁRIO CADASTRADO COM SUCESSO!----")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuarios for usuarios in usuarios if usuarios["cpf" == cpf]]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuarios = filtrar_usuario(cpf, usuarios)

     if usuarios:
          print("\n Conta criada com sucesso! ")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}
     
     print("\n Usuário não encontrado!")

def listar_conta(contas):
     for contas in contas:
          linha = f"""\
        Agência:\t{contas['agencia']}
        C/C: \t{contas['numero_conta']}
        Titular: \t{contas['usuario']['nome']}
    """
          print("=" * 100)

def main():
    saldo = 0 
    limite = 500
    extrato = ""
    numeros_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
         opcao = menu()

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao =="2":
         valor = float(input("Informe o valor do saque: "))

         saldo, extrato = sacar(
              saldo=saldo,
              valor=valor,
              extrato=extrato,
              limite=limite,
              numero_saque=numero_saque,
              limite_saque=LIMITE_SAQUES,
         )
    
    elif opcao == "3":
         exibir_extrato(saldo, extrato=extrato)

    elif opcao == "5":
         criar_usuario(usuarios)

    elif opcao == "4":
         numero_conta = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)

         if conta:
            conta.append(contas)
        
    elif opcao == "6":
         listar_conta(contas)

    #elif opcao == "0":
         #break
    
    else:
         print("Operação inválida, por favor selecione novamente a opção desejada. ")
    


main()

