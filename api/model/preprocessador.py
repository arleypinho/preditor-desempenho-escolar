from sklearn.model_selection import train_test_split
import numpy as np

class PreProcessador:

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """ Cuida de todo o pré-processamento. """
        # limpeza dos dados e eliminação de outliers

        # feature selection

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        # normalização/padronização
        
        return (X_train, X_test, Y_train, Y_test)
    
    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target é 'GradeClass'.
        O parâmetro test_size é o percentual de dados de teste.
        """
        # Simplificando a variável-alvo
        dataset['GradeClass'] = dataset['GradeClass'].apply(lambda x: 1 if x == 1 else 0)

        # Seleciona as colunas para X e Y
        X = dataset.drop(columns=['StudentID', 'GradeClass', 'GPA'])
        Y = dataset['GradeClass']

        # Divisão dos dados em treino e teste
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed, stratify=Y)
    
    def preparar_form(self, form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([form.age, 
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
                            form.volunteering
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        return X_input
