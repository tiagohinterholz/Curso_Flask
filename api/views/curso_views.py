from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service

class CursoList(Resource):
    
    def get(self):
        return 'Olá Mundo'

    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']
        
        novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
        resultado = curso_service.cadastrar_curso(novo_curso)
                
        return make_response(cs.jsonify(resultado), 201)
        
api.add_resource(CursoList, '/cursos')
