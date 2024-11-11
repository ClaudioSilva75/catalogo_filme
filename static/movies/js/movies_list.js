console.log("JavaScript carregado");

var interval;

function scrollDireita(id) {
    console.log("Rolando para a direita: " + id);
    var scroller = document.getElementById('scroller-' + id);
    if (scroller) {
        clearScroll(); // Limpa intervalos anteriores, se houver
        interval = setInterval(function() {
            if (typeof scroller.scrollLeft === 'number') {
                scroller.scrollLeft += 5;
                console.log('scrollLeft: ' + scroller.scrollLeft);
            }
        }, 10);
    }
}

function scrollEsquerda(id) {
    console.log("Rolando para a esquerda: " + id);
    var scroller = document.getElementById('scroller-' + id);
    if (scroller) {
        clearScroll(); // Limpa intervalos anteriores, se houver
        interval = setInterval(function() {
            if (typeof scroller.scrollLeft === 'number') {
                scroller.scrollLeft -= 5;
                console.log('scrollLeft: ' + scroller.scrollLeft);
            }
        }, 10);
    }
}

function clearScroll() {
    console.log("Parando rolagem");
    clearInterval(interval);
}
