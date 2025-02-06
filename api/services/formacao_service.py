from ..models import formacao_model
from api import db
from .professor_service import listas_professor_id

def cadastrar_formacao(formacao):
    formacao_db = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao)
    for i in formacao.professores:
        professor = listas_professor_id(i)
        formacao_db.professores.append(professor)
    db.session.add(formacao_db)
    db.session.commit()
    return formacao_db

def listar_formacoes():
    formacoes = formacao_model.Formacao.query.all()
    return formacoes

def listas_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

def atualiza_formacao(formacao_db, formacao_novo):
    formacao_db.nome = formacao_novo.nome
    formacao_db.descricao = formacao_novo.descricao
    for i in formacao_novo.professores:
        professor = listas_professor_id(i)
        formacao_db.professores.append(professor)
    db.session.commit()

def remove_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()