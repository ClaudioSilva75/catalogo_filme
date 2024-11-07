// movies_list.js

let intervalo;

// Função para rolar para a direita
function scrollDireita(genreId) {
    clearScroll();
    const scroller = document.getElementById('scroller-' + genreId);
    if (scroller) {
        intervalo = setInterval(() => {
            scroller.scrollLeft += 2; // Aumentar ou diminuir para ajustar a velocidade
        }, 10);
    }
}

// Função para rolar para a esquerda
function scrollEsquerda(genreId) {
    clearScroll();
    const scroller = document.getElementById('scroller-' + genreId);
    if (scroller) {
        intervalo = setInterval(() => {
            scroller.scrollLeft -= 2; // Aumentar ou diminuir para ajustar a velocidade
        }, 10);
    }
}

// Função para parar a rolagem
function clearScroll() {
    if (intervalo) {
        clearInterval(intervalo);
        intervalo = null;
    }
}
