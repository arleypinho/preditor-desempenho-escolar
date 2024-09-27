from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Pregnancies,Glucose,BloodPressure,SkinThickness,test,BMI,DiabetesPedigreeFunction,Age,Outcome

class Aluno(Base):
    __tablename__ = 'alunos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)  # 0: Masculino, 1: Feminino
    ethnicity = Column(Integer, nullable=False)
    parental_education = Column(Integer, nullable=False)
    study_time_weekly = Column(Integer, nullable=False)
    absences = Column(Integer, nullable=False)
    tutoring = Column(Integer, nullable=False)  # 0: Não, 1: Sim
    parental_support = Column(Integer, nullable=False)
    extracurricular = Column(Integer, nullable=False)  # 0: Não, 1: Sim
    sports = Column(Integer, nullable=False)  # 0: Não, 1: Sim
    music = Column(Integer, nullable=False)  # 0: Não, 1: Sim
    volunteering = Column(Integer, nullable=False)  # 0: Não, 1: Sim
    outcome = Column(Integer, nullable=True)  # 1: Aprovado, 0: Reprovado
    data_insercao = Column(DateTime, default=datetime.now)
    
    def __init__(self, name: str, age: int, gender: int, ethnicity: int, parental_education: int,
                 study_time_weekly: int, absences: int, tutoring: int, parental_support: int,
                 extracurricular: int, sports: int, music: int, volunteering: int,
                 outcome: Union[int, None] = None, data_insercao: Union[DateTime, None] = None):
        """
        Cria um Aluno

        Arguments: 
            Age (Idade): Idade do aluno.
            Gender (Gênero): Gênero do aluno (por exemplo, 1 para masculino e 0 para feminino).
            Ethnicity (Etnia): Etnia do aluno (codificada numericamente).
            ParentalEducation (Educação dos Pais): Nível de educação dos pais (por exemplo, 1 para ensino médio, 2 para faculdade, etc.).
            StudyTimeWeekly (Tempo de Estudo Semanal): Número médio de horas que o aluno estuda por semana.
            Absences (Faltas): Número de faltas acumuladas pelo aluno.
            Tutoring (Apoio Escolar): Se o aluno recebe ou não tutoria (1 para sim, 0 para não).
            ParentalSupport (Apoio dos Pais): Grau de apoio dos pais no 
            acompanhamento dos estudos (codificado numericamente).
            Extracurricular (Atividades Extracurriculares): Participação em atividades extracurriculares (1 para sim, 0 para não).
            Sports (Esportes): Participação em esportes (1 para sim, 0 para não).
            Music (Música): Participação em atividades musicais (1 para sim, 0 para não).
            Volunteering (Voluntariado): Participação em atividades de voluntariado (1 para sim, 0 para não)
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.ethnicity = ethnicity
        self.parental_education = parental_education
        self.study_time_weekly = study_time_weekly
        self.absences = absences
        self.tutoring = tutoring
        self.parental_support = parental_support
        self.extracurricular = extracurricular
        self.sports = sports
        self.music = music
        self.volunteering = volunteering
        self.outcome = outcome

        if data_insercao:
            self.data_insercao = data_insercao
