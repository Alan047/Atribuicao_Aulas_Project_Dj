function mostrar_model_addSemestre(id) {
  console.log(id)
    let model_addSesmestre = document.getElementsByClassName(id)
    model_addSesmestre[0].style.display = 'flex'
    console.log('clicou')
}
function fechar_model_addSemestre(id) {
    let model_addSesmestre = document.getElementById(id)
    model_addSesmestre.style.display = 'none'
}





