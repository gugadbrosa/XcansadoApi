from .models import Loja, Produto, Promocao
from rest_framework import serializers

class LojaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Loja
        fields = ['id', 'nome', 'cidade', 'uf', 'email']

class ProdutoSerializer(serializers.ModelSerializer):   
    # permite trazer o campo do objeto e não o ID 
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'imagem', 'descricao', 'categoria']

class PromocaoSerializer(serializers.ModelSerializer):   
    # permite trazer o campo do objeto e não o ID
    produto =  ProdutoSerializer(many=False, read_only=False)
    loja =  LojaSerializer(many=False, read_only=False)
    class Meta:
        model = Promocao
        fields = ['id','produto', 'loja', 'preco', 'cupom', 'destaque']
