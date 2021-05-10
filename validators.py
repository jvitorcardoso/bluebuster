from models import get_diretor, get_genero, get_filme, get_usuario, get_locacao

def valida_diretor(nome_completo, **kwargs):
    if len(nome_completo) == 0:
        return False

    return True

def valida_genero(nome, **kwargs):
    if len(nome) == 0:
        return False

    return True

def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id, **kwargs):
    if len(titulo) == 0:
        return False
    elif ano == 0:
        return False
    elif int(classificacao) < 0 or int(classificacao) > 18:
        return False
    elif preco == 0:
        return False
    elif diretores_id == 0:
        return False
    elif generos_id == 0:
        return False

    return True

def valida_id(id):
    if id == 0:
        return False

    return True

# HARUAN
def valida_usuario(nome_completo, CPF, **kwargs):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True

def valida_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    if data_inicio == 0:
        return False
    if data_fim == 0:
        return False
    if filmes_id == 0:
        return False
    if usuarios_id == 0:
        return False

    return True

def valida_pagamento(tipo, valor, locacoes_id):

    if tipo != "debito" or tipo != "credito" or tipo != "paypal":
        return False

    if valor == 0:
        return False

    if locacoes_id == 0:
        return False