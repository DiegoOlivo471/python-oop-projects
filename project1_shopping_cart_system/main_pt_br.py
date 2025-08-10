# We’re tasked with creating an online shopping cart system where users can 
# add items to their cart, view the total cost, and apply discounts based 
# on their membership type.

# Key OOP Concepts: -> mind map com melhor visualização da aplicaçãõ de cada um no site

#    Polymorphism: Implement different discount strategies based on user membership type.
#    Encapsulation: Hide internal details like product pricing from the user.
#    Inheritance: Create a base User class and extend it for RegularUser and PremiumUser.

# -----------------------------------------------------------------------------------------

# minha ideia, passo a passo:

# 1 - Criar uma classe principal para usuários.
# 2 - Criar uma classe para usuários regulares e usuários premiums.
# 3 - Cada usuário pode comprar algo, mas seu tipo de conta define seus descontos nos produtos.

# -> Criar uma classe pro carrinho de compras, onde podemos adicionar os itens e depois
#    calcular o valor total.


# IDEIAS TRABALHADAS:
# - Criação de classes
# - staticmethods e lógica
# - Herança
# - Polimorfismo
# - Encapsulamento

# -----------------------------------------------------------------------------------------

class User:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo
    
    # NOTA: Seguindo uma dica do GPT, ao definir o tipo de usuário, iremos
    #       chamar uma nova função que decidirá se temos um usuário
    #       regular ou premium.

    # Usei um staticmethod pois a ideia seria apenas regular logicamente
    # a criação de uma instância em uma classe filha específica, a depender
    # do tipo de usuário dado.
    @staticmethod
    def criar_user(nome: str, tipo: str):
        tipo = tipo.lower()
        if tipo == "regular":
            return UserRegular(nome, tipo)
        elif tipo == "premium":
            return UserPremium(nome, tipo)
        else:
            print("Tipo de usuário invalido.")

    def desconto(self, total):  # Esse método não é chamado diretamente, mas serve de base
        return total            # para o polimorfismo.

# A depender do que o @staticmethod concluiu, temos um tipo de usuário com funções
# parecidas, mas diferentes, a depender de cada instância.
class UserRegular(User):          # -> HERANÇA
    def desconto(self, total):
        return total

class UserPremium(User):
    def desconto(self, total):
        return total * 0.9

class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, item: str, preço: float, quantidade: int):
        # Dá append em um dicionário com as informações do item à lista de itens do carrinho.
        self.itens.append({'item': item, 'preço': preço, 'quantidade': quantidade})

    def calcular_total(self, usuario):
        total = 0
        # Fazemos a soma de todos os preços dos itens do carrinho, levando em conta a
        # quantidade de cada um.
        for item in self.itens:
            total += item['preço'] * item['quantidade']
        return usuario.desconto(total)


# Criando as instâncias e chamando os métodos:

user1 = User.criar_user("Alice", "Premium")
user2 = User.criar_user("Beto", "Regular")
user3 = User.criar_user("Carlos", "Premium")

carrinho1 = Carrinho()
carrinho2 = Carrinho()
carrinho3 = Carrinho()

carrinho1.adicionar_item("Notebook", 3000, 1)   # (3000 + 3000) * 0.9 = 5400
carrinho1.adicionar_item("Celular", 1500, 2)
carrinho2.adicionar_item("Notebook", 2500, 1)   # (2500 + 240) * 1 = 2740
carrinho2.adicionar_item("Camiseta", 60, 4)
carrinho3.adicionar_item("Celular", 1500, 1)    # (1500 + 180) * 0.9 = 1512
carrinho3.adicionar_item("Camiseta", 60, 3)

print(f"Total com desconto: R${carrinho1.calcular_total(user1):.2f}")
print(f"Total com desconto: R${carrinho2.calcular_total(user2):.2f}")
print(f"Total com desconto: R${carrinho3.calcular_total(user3):.2f}")