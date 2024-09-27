## Preditor de Desempenho Escolar
Este projeto utiliza algoritmos de machine learning para prever a aprovação ou reprovação de alunos, analisando diferentes fatores que influenciam o desempenho acadêmico, como hábitos de estudo, frequência, envolvimento dos pais, entre outros. O sistema treina vários modelos de aprendizado de máquina para identificar padrões e fornecer predições precisas sobre o desempenho futuro dos alunos.

## Funcionalidades
Previsão de aprovação ou reprovação de alunos.
Análise de múltiplos fatores que influenciam o desempenho escolar.
Treinamento e avaliação de diversos algoritmos de machine learning.
Interface web para inserção de novos dados e visualização das predições.

## Treino de diferentes modelos de machine learning:
KNN
Árvore de Decisão
Naive Bayes
SVM

## Tecnologias Utilizadas
Back-end: Python com Flask
Front-end: HTML, CSS, JavaScript
Machine Learning:
Bibliotecas: pandas, numpy, scikit-learn
Modelos: DecisionTreeClassifier, KNeighborsClassifier, GaussianNB, SVC
Ambiente de Desenvolvimento: Google Colab, Jupyter Notebook

## Como Rodar o Projeto
Pré-requisitos
Certifique-se de ter o Python 3.7+ instalado no seu ambiente. Você também precisará de um ambiente virtual (venv) para gerenciar as dependências.

## Como executar
Será necessário ter todas as bibliotecas Python listadas no arquivo requirements.txt instaladas. Após clonar o repositório, vá ao diretório raiz pelo terminal para executar os comandos abaixo.

É fortemente indicado o uso de ambientes virtuais, como o virtualenv.

Instale as dependências com o comando:

pip install -r requirements.txt

Este comando instala todas as bibliotecas descritas no arquivo requirements.txt.

Para rodar a API, utilize o comando:

flask run --host 0.0.0.0 --port 5000

Em modo de desenvolvimento, recomenda-se rodar com o parâmetro --reload para que o servidor reinicie automaticamente a cada alteração no código.

Acesse o endereço http://localhost:5000/#/ no navegador para verificar o status da API.

## Documentação da API
Após rodar a aplicação, você pode acessar a documentação da API para explorar e testar os endpoints disponíveis. A documentação estará disponível em /openapi com as opções Swagger, Redoc ou RapiDoc.

## Executar o Front-end
Para rodar o front-end, faça o download do projeto, rode a API e abra o arquivo index.html no seu navegador. Para uma experiência otimizada, recomenda-se usar um simulador de servidor como o Five Server.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, reportar bugs ou propor melhorias. A comunidade de desenvolvedores e colaboradores é essencial para o aprimoramento contínuo deste projeto.

