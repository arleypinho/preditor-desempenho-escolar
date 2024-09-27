Preditor de Desempenho Escolar
Este projeto utiliza algoritmos de machine learning para prever a aprovação ou reprovação de alunos, analisando diferentes fatores que influenciam o desempenho acadêmico, como hábitos de estudo, frequência, envolvimento dos pais, entre outros. O sistema treina vários modelos de aprendizado de máquina para identificar padrões e fornecer predições precisas sobre o desempenho futuro dos alunos.

Funcionalidades
Previsão de aprovação ou reprovação de alunos.
Análise de múltiplos fatores que influenciam o desempenho escolar.
Treinamento e avaliação de diversos algoritmos de machine learning.
Interface web para inserção de novos dados e visualização das predições.
Suporte a diferentes modelos de machine learning:
KNN (K-Nearest Neighbors)
Árvore de Decisão
Naive Bayes
SVM (Support Vector Machines)
Tecnologias Utilizadas
Back-end: Python com Flask
Front-end: HTML, CSS, JavaScript
Machine Learning:
Bibliotecas: pandas, numpy, scikit-learn
Modelos: DecisionTreeClassifier, KNeighborsClassifier, GaussianNB, SVC
Ambiente de Desenvolvimento: Google Colab, Jupyter Notebook
Como Rodar o Projeto
Pré-requisitos
Certifique-se de ter o Python 3.7+ instalado no seu ambiente. Você também precisará de um ambiente virtual (venv) para gerenciar as dependências.

Como executar
Será necessário ter todas as bibliotecas Python listadas no requirements.txt instaladas. Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

É fortemente indicado o uso de ambientes virtuais do tipo virtualenv.

Instalar dependências:

bash
Copiar código
(env)$ pip install -r requirements.txt
Este comando instala as dependências/bibliotecas descritas no arquivo requirements.txt.

Executar a API:

bash
Copiar código
(env)$ flask run --host 0.0.0.0 --port 5000
Em modo de desenvolvimento, é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código-fonte:

bash
Copiar código
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
Acessar a API: Abra o navegador e vá para http://localhost:5000/#/ para verificar o status da API em execução.

Documentação da API: Após iniciar o aplicativo, você pode acessar a documentação da API para explorar e testar os endpoints disponíveis. A documentação está disponível em /openapi, com opções para Swagger, Redoc ou RapiDoc.

Executar o Front-end
Para executar o front-end, siga as instruções abaixo:

Certifique-se de que a API está rodando.
Faça o download do projeto e, com o simulador de servidor (aconselhável o Five Server), abra o arquivo index.html no seu navegador para testar a interface web.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para reportar bugs ou propor melhorias.
