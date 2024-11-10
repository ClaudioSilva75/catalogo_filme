let intervalo;

function scrollEsquerda(id) {
    var scroller = document.getElementById("scroller-" + id);
    scroller.scrollLeft -= 220; // Desloca o conteúdo para a esquerda
}
  
function scrollDireita(id) {
var scroller = document.getElementById("scroller-" + id);
scroller.scrollLeft += 220; // Desloca o conteúdo para a direita
}
  
// Função para parar a rolagem
function clearScroll() {
    if (intervalo) {
        clearInterval(intervalo);
        intervalo = null;
    }
}
