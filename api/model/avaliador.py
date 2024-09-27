from sklearn.metrics import accuracy_score
from model.modelo import Model

class Avaliador:

    def avaliar(self, model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        model_instance = Model()  # Criar uma instância da classe Model
        predicoes = model_instance.preditor(model, X_test)  # Passando o modelo e os dados de teste
        
        return accuracy_score(Y_test, predicoes)
