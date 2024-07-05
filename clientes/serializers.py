from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos'})
        return data

    '''def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome não pode possuir números')
        return nome
    
    def validate_rg(self, rg):
        if len(rg)!=9:
            raise serializers.ValidationError('O rg deve ter 9 digitos')
        return rg
    
    def validate_celular(self, celular):
        if len(celular)<11:
            raise serializers.ValidationError('O celular deve ter 11 digitos')
        return celular'''