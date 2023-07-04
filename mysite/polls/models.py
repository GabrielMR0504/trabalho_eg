from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=30)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=30)

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=45)
    endereco = models.ManyToManyField(Endereco)

class ItemDoMenu(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    preco = models.FloatField()

class Pizza(ItemDoMenu):
    tamanho = models.IntegerField()
    bordaRecheada = models.BooleanField()

class Bebida(ItemDoMenu):
    tamanho = models.IntegerField()

class Cardapio(models.Model):
    ItemsDoMenu = models.ManyToManyField(ItemDoMenu)
    ativo = models.BinaryField()

class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    itensDoMenu = models.ManyToManyField(ItemDoMenu)

class ItemPedido(models.Model):
    itemDoMenu = models.ManyToManyField(ItemDoMenu)
    desconto = models.FloatField()

class Pedido(models.Model):
    cliente = models.ManyToManyField(Cliente)
    itemsDePedido = models.ManyToManyField(ItemPedido)
    data = models.DateField()
    STATUS_CHOICES = (
        ('FINALIZADO', 'Finalizado'),
        ('A_CAMINHO', 'A caminho'),
        ('PREPARANDO_PEDIDO', 'Preparando pedido'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Restaurante(models.Model):
    cardapio = models.ManyToManyField(Cardapio)
    carrinho = models.ManyToManyField(Carrinho)
    

##dsdalç
    










