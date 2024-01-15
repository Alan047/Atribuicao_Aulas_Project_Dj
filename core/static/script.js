let select = document.getElementById('disciplinas-mostrar-select')
let select_dic = document.getElementById('select-dicplinas-periodo')
select.addEventListener('click', function () {
    let select_disciplinas = document.getElementById('id_disciplinas')
    display = window.getComputedStyle(select_disciplinas).getPropertyValue('display')
    if (display == 'none') {
        select_dic.style.display = 'none'
        select_disciplinas.style.display = 'block'
        select.innerHTML = 'seleção automática'
    } else {
        select_disciplinas.style.display = 'none'
        select_dic.style.display = 'block'
        select.innerHTML = 'seleção manual'
    }


})