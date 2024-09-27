from model.modelo import Model
from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/data/dados_treinamento.csv"
colunas = ['StudentID', 'Age', 'Gender', 'Ethnicity', 'ParentalEducation', 
           'StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport',
           'Extracurricular', 'Sports', 'Music', 'Volunteering', 'GPA', 'GradeClass']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

## Simolificando a variavel alvo para 0 ou 1 e separando X e Y
dataset['GradeClass'] = dataset['GradeClass'].apply(lambda x: 1 if x in [0, 1, 2] else 0)
X = dataset.drop(columns=['StudentID', 'GradeClass', 'GPA'])
y = dataset['GradeClass']

def test_modelo_svm():
    # Importando modelo de SVM
    svm_path = './MachineLearning/models/modelo_svm_aprovacao_reprovacao.pkl'
    model_instance = Model()  # Criar uma instância da classe Model
    modelo_svm = model_instance.carrega_modelo(svm_path)

    # Obtendo as métricas do SVM
    acuracia_svm = avaliador.avaliar(modelo_svm, X, y)

