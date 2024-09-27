import pandas as pd

class Carregador:

    def carregar_dados(self, url: str, atributos: list):
        """Carrega e retorna um DataFrame a partir de um arquivo CSV.

        Args:
            url (str): O caminho ou URL do arquivo CSV.
            atributos (list): Lista de nomes de colunas para o DataFrame.

        Returns:
            pd.DataFrame: DataFrame com os dados carregados.

        Raises:
            FileNotFoundError: Se o arquivo não for encontrado.
            pd.errors.EmptyDataError: Se o arquivo estiver vazio.
            pd.errors.ParserError: Se houver um erro ao analisar o CSV.
        """
        return pd.read_csv(url, names=atributos, header=0, skiprows=0, delimiter=',')
