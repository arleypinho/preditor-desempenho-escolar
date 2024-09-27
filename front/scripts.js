/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/alunos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.alunos.forEach(item => insertList(item.name,             
                                                item.age, 
                                                item.gender,
                                                item.ethnicity,
                                                item.parental_education,
                                                item.study_time_weekly,
                                                item.absences,
                                                item.tutoring,
                                                item.parental_support,
                                                item.extracurricular,
                                                item.sports,
                                                item.music,
                                                item.volunteering,
                                                item.outcome
                                                
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()

/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputAluno, inputAge, inputGender,
                        inputEthnicity, inputParental_education, inputStudy_time_weekly, 
                        inputAbsences, inputTutoring, inputParental_support, inputExtracurricular, inputSports,
                        inputMusic, inputVolunteering) => {
                          
            
  const formData = new FormData();
  formData.append('name', inputAluno);
  formData.append('age', inputAge);
  formData.append('gender', inputGender);
  formData.append('ethnicity', inputEthnicity);
  formData.append('parental_education', inputParental_education);
  formData.append('study_time_weekly', inputStudy_time_weekly);
  formData.append('absences', inputAbsences);
  formData.append('tutoring', inputTutoring);
  formData.append('parental_support', inputParental_support);
  formData.append('extracurricular', inputExtracurricular);
  formData.append('sports', inputSports);
  formData.append('music', inputMusic);
  formData.append('volunteering', inputVolunteering);

  let url = 'http://127.0.0.1:5000/aluno';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (aluno) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  aluno.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/aluno?name='+item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputAluno = document.getElementById("newInput").value;
  let inputAge = document.getElementById("newAge").value;
  let inputGender = document.getElementById("newGender").value;
  let inputEthnicity = document.getElementById("newEthnicity").value;
  let inputParental_education = document.getElementById("newParentalEducation").value;
  let inputStudy_time_weekly = document.getElementById("newStudyTimeWeekly").value;
  let inputAbsences = document.getElementById("newAbsences").value;
  let inputTutoring = document.getElementById("newTutoring").value;
  let inputParental_support = document.getElementById("newParentalSupport").value;
  let inputExtracurricular = document.getElementById("newExtracurricular").value;
  let inputSports = document.getElementById("newSports").value;
  let inputMusic = document.getElementById("newMusic").value;
  let inputVolunteering = document.getElementById("newVolunteering").value;
  

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/alunos?nome=${inputAluno}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.alunos && data.alunos.some(item => item.name === inputAluno)) {
        alert("O Aluno já está cadastrado.\nCadastre o Aluno com um nome diferente ou atualize o existente.");
      } else if (inputAluno === '') {
        alert("O nome do Aluno não pode ser vazio!");
      } else if (isNaN(inputAge) || isNaN(inputGender) || isNaN(inputEthnicity) || isNaN(inputParental_education) || isNaN(inputStudy_time_weekly) || isNaN(inputAbsences) || isNaN(inputTutoring) || isNaN(inputParental_support) || isNaN(inputExtracurricular) || isNaN(inputMusic) || isNaN(inputVolunteering)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputAluno, inputAge, inputGender,
                  inputEthnicity, inputParental_education, inputStudy_time_weekly, 
                  inputAbsences, inputTutoring, inputParental_support, inputExtracurricular, inputSports,
                  inputMusic, inputVolunteering);
        postItem(inputAluno, inputAge, inputGender,
                  inputEthnicity, inputParental_education, inputStudy_time_weekly, 
                  inputAbsences, inputTutoring, inputParental_support, inputExtracurricular, inputSports,
                  inputMusic, inputVolunteering);
        alert("Item adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (name, age, gender,ethnicity, parental_education, study_time_weekly, absences, tutoring, parental_support, extracurricular,sports,music,volunteering,outcome) => {
  var item = [name, age, gender,ethnicity, parental_education, study_time_weekly, absences, tutoring, parental_support, extracurricular,sports,music,volunteering,outcome];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newInput").value = "";
  document.getElementById("newAge").value = "";
  document.getElementById("newGender").value = "";
  document.getElementById("newEthnicity").value = "";
  document.getElementById("newParentalEducation").value = "";
  document.getElementById("newStudyTimeWeekly").value = "";
  document.getElementById("newAbsences").value = "";
  document.getElementById("newTutoring").value = "";
  document.getElementById("newParentalSupport").value = "";
  document.getElementById("newExtracurricular").value = "";
  document.getElementById("newSports").value = "";
  document.getElementById("newMusic").value = "";
  document.getElementById("newVolunteering").value = "";

  removeElement();
}