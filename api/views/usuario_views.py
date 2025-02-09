from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
from ..models.usuario_model import Usuario

class UsuarioList(Resource):

    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        
        novo_usuario = usuario.Usuario(nome=nome, email=email, senha=senha)
        resultado = usuario_service.cadastrar_usuario(novo_usuario)
                
        return make_response(us.jsonify(resultado), 201)

api.add_resource(UsuarioList, '/usuario')