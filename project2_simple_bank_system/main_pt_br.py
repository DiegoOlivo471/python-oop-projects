# Problem Statement:

# Build a bank system where users can create accounts, deposit or withdraw
# money, and check their balance. There should be different types of accounts
# like Savings and Current accounts.

# ------------------------------------------------------------------------------------------

# Ideia principal: - Criar uma classe principal pra conta bancária, e depois criar sub clases
#                    para conta corrente e conta de poupança.
#                  - Criar uma balança de controle de depósitos e sacagens.
#                  - Usar de abstração pra "esconder" a 'balança'(balance, o dinheiro que tem) da conta.

# IDEIAS TRABALHADAS:
# - Abstração
# - Herança
# - Encapsulamento

# ------------------------------------------------------------------------------------------

# Classe Cliente para guardar as informações do cliente.
class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
    
# Aqui usamos self.cliente como o nome do cliente para simplificar o estudo, mas seria mais
# inteligente usar o cpf dele.
class ContaBancaria:
    def __init__(self, cliente, saldo, tipo):
        self.cliente = cliente
        self.saldo = saldo
        self.tipo = tipo

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def checar_saldo(self):
        print(f"O saldo disponível atual é R${self.saldo:.2f}.")

    # Esse método exibir_detalhes é um extra dado pelo GPT, para testar didadicamente os dados
    # guardados nas instâncias.
    def exibir_detalhes(self):
        print("----- DADOS DA CONTA -----")
        print(f"Titular: {self.cliente.nome}")
        print(f"CPF: {self.cliente.cpf}")
        print(f"E-mail: {self.cliente.email}")
        print(f"Telefone: {self.cliente.telefone}")
        print(f"Tipo de conta: {self.tipo.capitalize()}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("---------------------------\n")

    @staticmethod
    def criar_conta(cliente, saldo, tipo):
        tipo = tipo.lower()
        if tipo == "corrente":
            return ContaCorrente(cliente, saldo, tipo)
        elif tipo == "poupança":
            return ContaPoupanca(cliente, saldo, tipo)
        else:
            print("Tipo de conta bancária inexistente.")


# Contas correntes costumam poder realizar: saques, depósitos, trasnferências pra outra conta
# e mostrar o extrato (mas não rendem juros e permitem saldo negativo até um certo limite definido).
class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        saldo_negativo_limite = -2000
        if self.saldo - valor < saldo_negativo_limite:
            print("Limite de saldo negativo atingido.")
        elif valor == 0:
            print("Impossível sacar zero reais.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}.")

    def depositar(self, valor):
        if valor >= 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}.")
        else:
            print(f"Depósitos de valores negativos ({valor}) não são permitidos.")
    
# Contas poupanças costumam poder realizar: saques, depósitos, render juros (mensal, anual, ou
# simplificado no código) e mostrar o saldo (mas não podem entrar no negativo).
class ContaPoupanca(ContaBancaria): 
    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Limite de saldo negativo atingido.")
        elif valor == 0:
            print("Impossível sacar zero reais.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}.")

    def depositar(self, valor):
        if valor >= 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}.")
        else:
            print(f"Depósitos de valores negativos ({valor}) não são permitidos.")

    def render_juros(self):
        taxa_de_juros = 1.01 # 1% 
        self.saldo *= taxa_de_juros


# NOTA: Dados de clientes gerados pelo GPT, dados fakes e "aleatórios"

# Supondo que a classe Cliente tenha o seguinte construtor: Cliente(nome, cpf, email, telefone)

cliente1 = Cliente("João Silva", "123.456.789-00", "joao.silva@email.com", "(11) 91234-5678")
cliente2 = Cliente("Maria Oliveira", "987.654.321-00", "maria.oliveira@email.com", "(21) 99876-5432")
cliente3 = Cliente("Carlos Pereira", "456.789.123-00", "carlos.pereira@email.com", "(31) 98888-1122")
cliente4 = Cliente("Ana Souza", "321.654.987-00", "ana.souza@email.com", "(41) 98765-4321")
cliente5 = Cliente("Lucas Mendes", "654.123.789-00", "lucas.mendes@email.com", "(51) 99999-0000")

# Teste manuais gerados pelo GPT:

# Criando contas
conta1 = ContaBancaria.criar_conta(cliente1, 1000, "corrente")
conta2 = ContaBancaria.criar_conta(cliente2, 2000, "poupança")

# Teste 1: Exibir saldo inicial
conta1.checar_saldo()
conta2.checar_saldo()

# Teste 2: Sacar valor válido
conta1.sacar(500)  # deve funcionar
conta1.checar_saldo()

# Teste 3: Sacar além do limite
conta1.sacar(3000)  # deve bloquear

# Teste 4: Depositar
conta1.depositar(1000)
conta1.checar_saldo()

# Teste 5: Saque normal da poupança
conta2.sacar(1000)
conta2.checar_saldo()

# Teste 6: Tentativa de saque além do saldo da poupança
conta2.sacar(2000)  # deve bloquear

# Teste 7: Depósito na poupança
conta2.depositar(500)

# Teste 8: Juros da poupança
conta2.render_juros()
conta2.checar_saldo()

# Teste 9: Exibir dados completos (você pode criar esse método se quiser)
print(f"Conta de {conta1.cliente.nome}: saldo R${conta1.saldo:.2f}")
print(f"Conta de {conta2.cliente.nome}: saldo R${conta2.saldo:.2f}")

print()
conta1.exibir_detalhes()
conta2.exibir_detalhes()


# Teste 10: Depositar valor negativo
conta1.depositar(-100)

# Teste 11: Sacar valor zero
conta1.sacar(0)

# Teste 12: Criar conta com tipo inválido
conta_errada = ContaBancaria.criar_conta(cliente3, 500, "investimento")  # deve mostrar mensagem de erro

# Teste 13: Render juros em saldo zero
conta_vazia = ContaBancaria.criar_conta(cliente4, 0, "poupança")
conta_vazia.render_juros()
conta_vazia.checar_saldo()