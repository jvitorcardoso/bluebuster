from flask import Flask, jsonify, request
from serializers import diretor_from_web, diretor_from_db, genero_from_web, genero_from_db, filme_from_web, filme_from_db, usuario_from_db, usuario_from_web, delete_id_from_web, delete_id_from_db
from validators import valida_diretor, valida_genero, valida_filme, valida_usuario, valida_id
from models import insert_diretor, insert_genero, insert_filme, insert_usuario, update_diretor, update_genero, update_filme, update_usuario, delete_diretor, delete_genero, delete_filme, delete_usuario, select_diretor, get_diretor, get_filme, get_genero

app = Flask(__name__)

# CREATE
@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        insert_diretor(**diretor)
        diretor_inserido = get_diretor(diretor["nome_completo"])
        return jsonify(diretor_from_db(diretor_inserido))
    else:
        return jsonify({"erro": "Diretor Inválido."})

@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        insert_genero(**genero)
        return jsonify(genero_from_db(genero))
    else:
        return jsonify({"erro": "Gênero Inválido."})

@app.route("/filmes", methods=["POST"]) # SALVAR
def inserir_filme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id = insert_filme(**filme)
        filme_inserido = get_filme(id)
        return jsonify(filme_from_db(filme_inserido))
    else:
        return jsonify({"erro": "Filme Inválido."})

@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        insert_usuario(**usuario)
        return jsonify(usuario_from_db(usuario))
    else:
        return jsonify({"erro": "Usuário Inválido."})

# PUT/PATCH
@app.route("/diretores/<int:id>", methods=["PUT"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if valida_id(id):
        update_diretor(id, **diretor)
        return jsonify(diretor_from_db(diretor))
    else:
        return jsonify({"erro": "Diretor Inválido."})

@app.route("/generos/<int:id>", methods=["PUT"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if valida_id(id):
        update_genero(id, **genero)
        return jsonify(genero_from_db(genero))
    else:
        return jsonify({"erro": "Genêro Inválido."})

@app.route("/filmes/<int:id>", methods=["PUT"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if valida_id(id):
        update_filme(id, **filme)
        return jsonify(filme_from_db(filme))
    else:
        return jsonify({"erro": "Filme Inválido."})

@app.route("/usuarios/<int:id>", methods=["PUT"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_id(id):
        update_usuario(id, **usuario)
        return jsonify(usuario_from_db(usuario))
    else:
        return jsonify({"erro": "Usuário Inválido."})

# DELETE
@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    diretor_id = delete_id_from_web(**request.json)
    try:
        if valida_id(id):
            delete_diretor(**diretor_id)
            return jsonify(delete_id_from_db(diretor_id))
    except:
        return jsonify({"erro": "É impossível apagar este diretor."})

@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    genero_id = delete_id_from_web(**request.json)
    try:
        if valida_id(id):
            delete_genero(**genero_id)
            return jsonify(delete_id_from_db(genero_id))
    except:
        return jsonify({"erro": "É impossível apagar este gênero."})

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    filme_id = delete_id_from_web(**request.json)
    try:
        if valida_id(id):
            delete_filme(**filme_id)
            return jsonify(delete_id_from_db(filme_id))
    except:
        return jsonify({"erro": "É impossível apagar este filme."})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    usuario_id = delete_id_from_web(**request.json)
    try:
        if valida_id(id):
            delete_usuario(**usuario_id)
            return jsonify(delete_id_from_db(usuario_id))
    except:
        return jsonify({"erro": "É impossível apagar este usuário."})

# SELECT
@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    diretor = diretor_from_web(**request.json)
    select_diretor(**diretor)
    diretor_selecionado = get_diretor(diretor["nome_completo"])
    if diretor_selecionado != None:
        return jsonify(diretor_from_db(diretor_selecionado))
    elif diretor_selecionado == None:
        return jsonify({"erro": "Diretor não encontrado."})

@app.route("/generos", methods=["GET"])
def buscar_generos():
    genero = genero_from_web(**request.json)
    select_genero(**genero)
    genero_selecionado = get_genero(genero["nome"])
    if genero_selecionado != None:
        return jsonify(genero_from_db(genero_selecionado))
    elif diretor_selecionado == None:
        return jsonify({"erro": "Diretor não encontrado."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
