def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }

def diretor_from_db(*args):
    return {
        "id": args[0][0][0],
        "nome_completo": args[0][0][1]
    }

def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else "",
    }

def genero_from_db(*args):
    return {
        "nome": args[0]
    }

def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }

def filme_from_db(*args):
    return {
        "titulo": args[0][0][0],
        "ano": args[0][0][1],
        "classificacao": args[0][0][2],
        "preco": str(args[0][0][3]),
        "diretores_id": args[0][0][4],
        "generos_id": args[0][0][5]
    }

def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "cpf" in kwargs else ""
    }

def usuario_from_db(*args):
    return {
        "id": args[0],
        "nome_completo": args[0],
        "CPF": args[0]
    }

def delete_id_from_web(**kwargs):
    return {
        "id": kwargs["id"] if "id" in kwargs else ""
    }

def delete_id_from_db(*args):
    return {
        "id": args[0]
    }