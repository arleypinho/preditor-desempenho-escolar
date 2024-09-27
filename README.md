## Preditor de Desempenho Escolar 📊
Este projeto utiliza algoritmos de machine learning para prever a aprovação ou reprovação de alunos, analisando diferentes fatores que influenciam o desempenho acadêmico, como hábitos de estudo, frequência, envolvimento dos pais, entre outros. O sistema treina vários modelos de aprendizado de máquina para identificar padrões e fornecer predições precisas sobre o desempenho futuro dos alunos.

## Funcionalidades 🚀
 - Previsão de aprovação ou reprovação de alunos.
 - Análise de múltiplos fatores que influenciam o desempenho escolar.
 - Treinamento e avaliação de diversos algoritmos de machine learning.
 - Interface web para inserção de novos dados e visualização das predições.
 - Suporte a diferentes modelos de machine learning:
 - KNN
 - Árvore de Decisão
 - Naive Bayes
 - SVM

## Tecnologias Utilizadas 🛠️
Back-end: Python com Flask
Front-end: HTML, CSS, JavaScript
Machine Learning:
Bibliotecas: pandas, numpy, scikit-learn

## Modelos Testes: 
DecisionTreeClassifier, KNeighborsClassifier, GaussianNB, SVC

## Ambiente de Desenvolvimento: 
Google Colab, Jupyter Notebook, Visual Studio Code

## Como executar ⚙️
Será necessário ter todas as libs python listadas no requirements.txt instaladas. Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

É fortemente indicado o uso de ambientes virtuais do tipo virtualenv.

(env)$ pip install -r requirements.txt
Este comando instala as dependências/bibliotecas, descritas no arquivo requirements.txt.

Para executar a API basta executar: 📚

(env)$ flask run --host 0.0.0.0 --port 5000
Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

(env)$ flask run --host 0.0.0.0 --port 5000 --reload
Abra o http://localhost:5000/#/ no navegador para verificar o status da API em execução.

Após iniciar o aplicativo, você pode acessar a documentação da API para explorar e testar os endpoints disponíveis. Documentação disponível em /openapi, escolha entre Swagger, Redoc ou RapiDoc.

## Para executar a Front-End 🌐
Basta fazer o download do projeto rodar a API e abrir o index.html no seu browser com o simulador de Servidor (Aconselhavel o Five Server).

## Contribuições 🤝
Contribuições são bem-vindas! Sinta-se à vontade para abrir questionamentos para reportar bugs ou propor melhorias.
