from pydantic import BaseModel
from typing import List

class AlunoSchema(BaseModel):
    """ Define como um novo aluno a ser inserido deve ser representado """
    name: str = "Letícia"
    age: int = 20
    gender: int = 1  # 0: Masculino, 1: Feminino
    ethnicity: int = 1
    parental_education: int = 2
    study_time_weekly: int = 10
    absences: int = 5
    tutoring: int = 0  # 0: Não, 1: Sim
    parental_support: int = 1
    extracurricular: int = 1  # 0: Não, 1: Sim
    sports: int = 0  # 0: Não, 1: Sim
    music: int = 1  # 0: Não, 1: Sim
    volunteering: int = 0  # 0: Não, 1: Sim

class AlunoViewSchema(BaseModel):
    """ Define como um aluno será retornado """
    id: int
    name: str = "Letícia"
    age: int = 20
    gender: int = 1
    ethnicity: int = 1
    parental_education: int = 2
    study_time_weekly: int = 10
    absences: int = 5
    tutoring: int = 0
    parental_support: int = 1
    extracurricular: int = 1
    sports: int = 0
    music: int = 1
    volunteering: int = 0
    outcome: int  # Previsão do resultado (1: Aprovado, 0: Reprovado)

class AlunoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. """
    name: str = "Letícia"

class ListaAlunosSchema(BaseModel):
    """ Define como uma lista de alunos será representada """
    alunos: List[AlunoSchema]

class AlunoDelSchema(BaseModel):
    """ Define como um aluno para deleção será representado """
    name: str = "Letícia"

# Função para apresentar um aluno
def apresenta_aluno(aluno):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    return {
        "id": aluno.id,
        "name": aluno.name,
        "age": aluno.age,
        "gender": aluno.gender,
        "ethnicity": aluno.ethnicity,
        "parental_education": aluno.parental_education,
        "study_time_weekly": aluno.study_time_weekly,
        "absences": aluno.absences,
        "tutoring": aluno.tutoring,
        "parental_support": aluno.parental_support,
        "extracurricular": aluno.extracurricular,
        "sports": aluno.sports,
        "music": aluno.music,
        "volunteering": aluno.volunteering,
        "outcome": aluno.outcome  # O outcome agora vem do modelo de ML
    }

# Função para apresentar uma lista de alunos
def apresenta_alunos(alunos: List):
    """ Retorna uma representação da lista de alunos seguindo o schema definido em
        AlunoViewSchema.
    """
    result = []
    for aluno in alunos:
        result.append(apresenta_aluno(aluno))

    return {"alunos": result}
