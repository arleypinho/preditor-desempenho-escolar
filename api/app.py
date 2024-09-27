import os
import joblib
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError
from model import Aluno, Session
from logger import logger
from schemas import AlunoSchema, AlunoViewSchema, ListaAlunosSchema, AlunoBuscaSchema, ErrorSchema, apresenta_aluno, apresenta_alunos
from flask_cors import CORS
from urllib.parse import unquote

# Inicializando a aplicação Flask OpenAPI
info = Info(title="API de Predição de Alunos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Tags para documentação
home_tag = Tag(name="Documentação", description="Escolha entre Swagger, Redoc ou RapiDoc")
aluno_tag = Tag(name="Alunos", description="Adição, visualização, remoção e predição de alunos")

# Definindo o caminho do modelo SVM
model_path = os.path.join("MachineLearning", "models", "modelo_svm_aprovacao_reprovacao.pkl")
modelo_svm = joblib.load(model_path)

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi."""
    return redirect('/openapi')

# Rota para listar todos os alunos
@app.get('/alunos', tags=[aluno_tag], responses={"200": ListaAlunosSchema, "404": ErrorSchema})
def get_alunos():
    """Lista todos os alunos cadastrados."""
    session = Session()
    alunos = session.query(Aluno).all()
    
    if not alunos:
        logger.warning("Nenhum aluno encontrado.")
        return {"message": "Nenhum aluno cadastrado."}, 404
    else:
        logger.info(f"{len(alunos)} alunos encontrados.")
        return apresenta_alunos(alunos), 200

# Rota para adicionar um novo aluno
@app.post('/aluno', tags=[aluno_tag], responses={"200": AlunoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def add_aluno(form: AlunoSchema):
    """Adiciona um novo aluno e faz a predição do resultado."""
    session = Session()

    # Criando o aluno a partir dos dados do formulário
    aluno = Aluno(
        name=form.name,
        age=form.age,
        gender=form.gender,
        ethnicity=form.ethnicity,
        parental_education=form.parental_education,
        study_time_weekly=form.study_time_weekly,
        absences=form.absences,
        tutoring=form.tutoring,
        parental_support=form.parental_support,
        extracurricular=form.extracurricular,
        sports=form.sports,
        music=form.music,
        volunteering=form.volunteering,
    )
    
    try:
        # Verificando se o aluno já existe
        if session.query(Aluno).filter(Aluno.name == form.name).first():
            return {"message": "Aluno já cadastrado."}, 409

        # Preparando os dados para a previsão
        features = [[
            form.age,
            form.gender,
            form.ethnicity,
            form.parental_education,
            form.study_time_weekly,
            form.absences,
            form.tutoring,
            form.parental_support,
            form.extracurricular,
            form.sports,
            form.music,
            form.volunteering,
        ]]
        
        # Fazendo a previsão com o modelo
        prediction = modelo_svm.predict(features)
        aluno.outcome = int(prediction[0])  # 0 ou 1

        session.add(aluno)
        session.commit()
        logger.info(f"Aluno {aluno.name} adicionado com sucesso! Previsão: {aluno.outcome}")
        return apresenta_aluno(aluno), 200
    
    except Exception as e:
        logger.error(f"Erro ao adicionar aluno: {str(e)}")
        return {"message": "Erro ao adicionar aluno."}, 400

# Rota para buscar um aluno pelo nome
@app.get('/aluno', tags=[aluno_tag], responses={"200": AlunoViewSchema, "404": ErrorSchema})
def get_aluno(query: AlunoBuscaSchema):
    """Busca um aluno pelo nome."""
    session = Session()
    aluno = session.query(Aluno).filter(Aluno.name == query.name).first()

    if not aluno:
        logger.warning(f"Aluno {query.name} não encontrado.")
        return {"message": "Aluno não encontrado."}, 404
    else:
        logger.info(f"Aluno {aluno.name} encontrado.")
        return apresenta_aluno(aluno), 200

# Rota para remover um aluno
@app.delete('/aluno', tags=[aluno_tag], responses={"200": AlunoViewSchema, "404": ErrorSchema})
def delete_aluno(query: AlunoBuscaSchema):
    """Remove um aluno pelo nome."""
    session = Session()
    aluno = session.query(Aluno).filter(Aluno.name == unquote(query.name)).first()

    if not aluno:
        logger.warning(f"Aluno {query.name} não encontrado para remoção.")
        return {"message": "Aluno não encontrado."}, 404
    else:
        session.delete(aluno)
        session.commit()
        logger.info(f"Aluno {query.name} removido com sucesso!")
        return {"message": f"Aluno {query.name} removido."}, 200

if __name__ == '__main__':
    app.run(debug=True)
