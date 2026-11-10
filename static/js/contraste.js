const controle = document.getElementById("contraste");
const estado = document.getElementById("estado-contraste");
const chave = "organizador.altoContraste";

function mostrarContraste(ativo) {
    document.documentElement.classList.toggle("alto-contraste", ativo);
    controle.setAttribute("aria-pressed", String(ativo));
    estado.textContent = ativo ? "· ativado" : "· desativado";
}

let inicial = window.matchMedia("(prefers-contrast: more)").matches;
try {
    const salvo = localStorage.getItem(chave);
    if (salvo !== null) inicial = salvo === "true";
} catch {
    // O controle continua disponível quando o navegador bloqueia o armazenamento.
}
mostrarContraste(inicial);
controle.hidden = false;

controle.addEventListener("click", () => {
    const ativo = controle.getAttribute("aria-pressed") !== "true";
    mostrarContraste(ativo);
    try {
        localStorage.setItem(chave, String(ativo));
    } catch {
        // A preferência continua válida nesta página.
    }
});
