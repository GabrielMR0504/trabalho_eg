from models import Pedido, Pizza, Bebida

# Criar três pizzas diferentes
pizzas = [
    {
        "nome": "Pizza de Calabresa",
        "descricao": "Deliciosa pizza de calabresa com cebola e queijo derretido",
        "preco": 30.0,
        "tamanho": 12,
        "bordaRecheada": True
    },
    {
        "nome": "Pizza Margherita",
        "descricao": "Clássica pizza margherita com tomate, queijo e manjericão",
        "preco": 28.0,
        "tamanho": 10,
        "bordaRecheada": False
    },
    {
        "nome": "Pizza Quatro Queijos",
        "descricao": "Pizza com uma deliciosa combinação de quatro queijos",
        "preco": 35.0,
        "tamanho": 14,
        "bordaRecheada": True
    }
]

for pizza_data in pizzas:
    pizza = Pizza(**pizza_data)
    pizza.save()

# Criar três bebidas diferentes
bebidas = [
    {
        "nome": "Refrigerante",
        "descricao": "Bebida refrescante",
        "preco": 5.0,
        "tamanho": 500
    },
    {
        "nome": "Suco de Laranja",
        "descricao": "Suco natural de laranja",
        "preco": 7.0,
        "tamanho": 300
    },
    {
        "nome": "Água Mineral",
        "descricao": "Água mineral sem gás",
        "preco": 3.0,
        "tamanho": 500
    }
]

for bebida_data in bebidas:
    bebida = Bebida(**bebida_data)
    bebida.save()