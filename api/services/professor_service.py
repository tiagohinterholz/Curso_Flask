from ..models import professor_model
from api import db

def cadastrar_professor(professor):
    professor_db = professor_model.Professor(nome=professor.nome, idade=professor.idade)
    db.session.add(professor_db)
    db.session.commit()
    return professor_db

def listar_professores():
    professores = professor_model.Professor.query.all()
    return professores

def listas_professor_id(id):
    professor = professor_model.Professor.query.filter_by(id=id).first()
    return professor

def atualiza_professor(professor_db, professor_novo):
    professor_db.nome = professor_novo.nome
    professor_db.idade = professor_novo.idade
    db.session.commit()

def remove_professor(professor):
    db.session.delete(professor)
    db.session.commit()