var interval;

function scrollDireita(id) {
    clearScroll(); // Limpa intervalos anteriores, se houver
    interval = setInterval(function() {
        document.getElementById('scroller-' + id).scrollLeft += 5;
    }, 10);
}

function scrollEsquerda(id) {
    clearScroll(); // Limpa intervalos anteriores, se houver
    interval = setInterval(function() {
        document.getElementById('scroller-' + id).scrollLeft -= 5;
    }, 10);
}

function clearScroll() {
    clearInterval(interval);
}
