function mostrar_model_addSemestre() {
    let model_addSesmestre = document.getElementById('model-janela-addSemestre')
    model_addSesmestre.style.display = 'flex'
}
function fechar_model_addSemestre() {
    let model_addSesmestre = document.getElementById('model-janela-addSemestre')
    model_addSesmestre.style.display = 'none'
}

function selecionar_pares() {
    console.log('pares')
    let select_disciplinas = document.getElementById('select-disciplinas')
    for (let i = 0; i < select_disciplinas.children.length; i++) {
        console.log(select_disciplinas[i])
        if (select_disciplinas.children[i].classList.value % 2 == 0) {
            select_disciplinas[i].selected = true
        }
    }


}


  var selectedOptions = [];

  document.getElementById("select-disciplinas").addEventListener("click", function (event) {
    var option = event.target;

    // Se a opção já estiver selecionada, remova-a do array
    if (selectedOptions.includes(option.value)) {
      selectedOptions = selectedOptions.filter(value => value !== option.value);
    } else {
      // Se não estiver selecionada, adicione-a ao array
      selectedOptions.push(option.value);
    }

    // Atualize as opções selecionadas
    document.getElementById("select-disciplinas").value = selectedOptions;
  });
