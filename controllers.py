from serializers import diretor_from_web, diretor_from_db, \
                        genero_from_web, genero_from_db, \
                        filme_from_web, filme_from_db, \
                        usuario_from_web, usuario_from_db, \
                        delete_id_from_web, delete_id_from_db, \
                        locacao_from_web, locacao_from_db, \
                        pagamento_from_web, pagamento_from_db

from flask import Flask, jsonify, request
import validators
import models
from datetime import timedelta, datetime
from random import randint, choice
                   
app = Flask(__name__)

# CREATE
@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if validators.valida_diretor(**diretor):
        id_diretor = models.insert_diretor(**diretor)
        diretor_cadastrado = models.get_diretor(id_diretor)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor Inválido."})

@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if validators.valida_genero(**genero):
        id_genero = models.insert_genero(**genero)
        genero_cadastrado = models.get_genero(id_genero)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Gênero Inválido."})

@app.route("/filmes", methods=["POST"]) # SALVAR
def inserir_filme():
    filme = filme_from_web(**request.json)
    if validators.valida_filme(**filme):
        id_filme = models.insert_filme(**filme)
        filme_cadastrado = models.get_filme(id_filme)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "Filme Inválido."})

@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if validators.valida_usuario(**usuario):
        id_usuario = models.insert_usuario(**usuario)
        usuario_cadastrado = models.get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacao_from_web(**request.json)
    status_dos_pagamentos = ("aprovado", "em analise", "reprovado")
    tipos_de_pagamentos = ("debito", "credito", "paypal")
    status_atual = choice(status_dos_pagamentos)
    tipo_atual = choice(tipos_de_pagamentos)
    codigo = randint(0, 1000)
    dia_da_locacao = datetime.now()
    prazo = timedelta(hours=48, minutes=0, seconds=0)
    prazo_final = dia_da_locacao + prazo
    if validators.valida_locacao(**locacao):
        id1 = models.insert_locacao(dia_da_locacao, prazo_final, **locacao)
        preco = models.get_preco(id)
        locacao_id = models.get_locacao_id(id1)
        id2 = models.insert_pagamento(tipo_atual, status_atual, codigo, preco, dia_da_locacao, locacao_id)
        locacao_inserido = models.get_locacao(id1, id2)
        return jsonify(locacao_from_db(locacao_inserido))
    else:
        return jsonify({"erro": "Locação inválida"})

@app.route("/pagamentos", methods=["POST"])
def inserir_pagamento():
    pagamento = pagamento_from_web(**request.json)
    status_dos_pagamentos = ("aprovado", "em analise", "reprovado")
    status_atual = choice(status_dos_pagamentos)
    codigo = randint(0, 1000)
    data_pagamento = datetime.now()
    if validators.valida_pagamento(**pagamento):
        id_pagamento = models.insert_pagamento(status_atual, codigo, data_pagamento, **pagamento)
        pagamento_registrado = models.get_pagamento(id_pagamento)
        return jsonify(pagamento_from_db(pagamento_registrado))
    else:
        return jsonify({"erro": "Pagamento inválido"})

# PUT/PATCH
@app.route("/diretores/<int:id>", methods=["PUT"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if validators.valida_diretor(**diretor):
        models.update_diretor(id, **diretor)
        diretor_cadastrado = models.get_diretor(id)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor Inválido."})

@app.route("/generos/<int:id>", methods=["PUT"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if validators.valida_genero(**genero):
        models.update_genero(id, **genero)
        genero_cadastrado = models.get_genero(id)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Genêro Inválido."})

@app.route("/filmes/<int:id>", methods=["PUT"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if validators.valida_filme(**filme):
        models.update_filme(id, **filme)
        filme_cadastrado = models.get_filme(id)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "Filme Inválido."})

@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if validators.valida_usuario(**usuario):
        models.update_usuario(id, **usuario)
        usuario_cadastrado = models.get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

# @app.route("/locacoes/<int:id>", methods=["PUT", "PATCH"])
# def alterar_locacao(id):
#     locacao = locacao_from_web(**request.json)
#     if validators.valida_locacao(**locacao):
#         models.update_locacao(id, **locacao)
#         locacao_cadastrada = models.get_locacao(id)
#         return jsonify(locacao_from_web(locacao_cadastrada))
#     else:
#         return jsonify({"erro": "Locação inválida"})

# DELETE
@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        models.delete_diretor(id)
        return ('', 204)
    except:
        return jsonify({"erro": "É impossível apagar este diretor."})

@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        models.delete_genero(id)
        return ('', 204)
    except:
        return jsonify({"erro": "É impossível apagar este gênero."})

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        models.delete_filme(id)
        return ('', 204)
    except:
        return jsonify({"erro": "É impossível apagar este filme."})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        models.delete_usuario(id)
        return ('', 204)
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})

# @app.route("/locacoes/<int:id>", methods=["DELETE"])
# def apagar_locacao(id):
#     try:
#         models.delete_locacao(id)
#         return ('', 204)
#     except:
#         return jsonify({"erro": "É impossível apagar este dado do banco."})

# SELECT
@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    diretor = diretor_from_web(**request.args)
    diretores = models.select_diretor(diretor["nome_completo"])
    diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
    return jsonify(diretores_from_db) 

@app.route("/generos", methods=["GET"])
def buscar_generos():
    genero = genero_from_web(**request.args)
    generos = models.select_genero(genero["nome"])
    generos_from_db = [genero_from_db(genero) for genero in generos]
    return jsonify(generos_from_db)

@app.route("/filmes", methods=["GET"])
def buscar_filmes():
    filme = filme_from_web(**request.args)
    filmes = models.select_filme(filme["titulo"])
    filmes_from_db = [filme_from_db(filme) for filme in filmes]
    return jsonify(filmes_from_db)

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = usuario_from_web(**request.args)
    usuarios = models.select_usuario(nome_completo["nome_completo"])
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)

@app.route("/locacoes", methods=["GET"])
def buscar_locacao():
    id = locacao_from_web(**request.args)
    locacoes = models.query_locacao(id["id"])
    locacao_from_db = [locacao_from_db(locacao) for locacao in locacoes]
    return jsonify(locacao_from_db)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
