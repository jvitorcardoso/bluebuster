from cmd_banco import insert, update, delete, select, select_like
from controllers import inserir_diretor, inserir_genero, inserir_filme, inserir_usuario
import decimal, json

# BLOCO INSERT

def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])

def insert_genero(nome):
    return insert("generos", ["nome"], [nome])

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
        [titulo, ano, classificacao, preco, diretores_id, generos_id])

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

# BLOCO UPDATE

def update_diretor(id_diretor, nome_completo):
    update("diretores", "id", id_diretor, ["nome_completo"], [nome_completo])

def update_genero(id_genero, nome):
    update("generos", "id", id_genero, ["nome"], [nome])

def update_filme(id_filme, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id_filme, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])

# BLOCO DELETE

def delete_diretor(id_diretor):
    delete("diretores", "id", id_diretor)

def delete_genero(id_genero):
    delete("generos", "id", id_genero)

def delete_filme(id_filme):
    delete("filmes", "id", id_filme)

def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)

# SELECTS

# diretor
def select_diretor(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)

def get_diretor(id_nome_completo):
    return select("diretores", "id", id_nome_completo)[0]


# gênero
def select_genero(nome):
    return select_like("generos", "nome", nome)

def get_genero(id_nome):
    return select("generos", "id", id_nome)[0]


# filme
def select_filme(titulo):
    return select_like("filmes", "titulo", titulo)

def get_filme(id_filme):
    return select("filmes", "id", id_filme)[0]


# usuário
def select_usuario(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]