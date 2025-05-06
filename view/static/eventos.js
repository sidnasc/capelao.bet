// Função para criar a estrutura HTML de um evento
function criarEventoElemento(item) {
  const div = document.createElement("div");
  div.className = "evento";

  div.innerHTML = `
            <div class="tituloAposta">${item.evento}</div>
            <div class="odd">
              <button data-tipo="casa">Casa ${item.odd_casa}</button> x
              <button data-tipo="visitante">Visitante ${item.odd_visitante}</button> 
            </div>
            <div class="input_aposta">
              <input type="number" name="valorAposta" id="valorAposta" class="valor-aposta" placeholder="Digite o valor da aposta:"> 
            </div>
          `;;

  adicionarListeners(div, item);
  return div;
}

function criarAposta(aposta) {
  const div = document.createElement("div");
  div.className = "evento";

  div.innerHTML = `
            <div>
              <li>Evento ${aposta.Eventos} | Valor: ${ aposta.valor } | Ganhador : ${ aposta.tipoOdd}</li>
              <button class='excluirAposta' data-id="${aposta.id}">EXCLUIR</button>
            </div>
          `;;

  div.querySelector(".excluirAposta").addEventListener("click", () => {
    excluirAposta(aposta.id);
  });

  return div;
}

// Função para adicionar listeners aos botões do evento
function adicionarListeners(div, item) {
  const botoes = div.querySelectorAll("button");
  botoes.forEach(botao => {
    botao.addEventListener("click", () => registrarAposta(botao, div, item));
  });
}

// Função para registrar uma aposta
function registrarAposta(botao, div, item) {
  const tipo = botao.dataset.tipo;
  const valorInput = div.querySelector(".valor-aposta");
  const valor = parseFloat(valorInput.value);

  if (!valor || valor <= 0) {
    alert("Digite um valor válido!");
    return;
  }

  fetch('/reg_aposta', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      tipoOdd: tipo,
      valor: valor,
      idEvento: item.id
    })
  })
    .then(res => {
      if (res.ok) {
        carregarApostas()
      }
      else alert("Erro ao registrar aposta.");
    });
}

// Função principal para buscar eventos e exibir
function carregarEventos() {
  fetch('/get_eventos')
    .then(res => res.json())
    .then(dados => {
      const container = document.getElementById("eventos");
      container.innerHTML = ""; // limpa antes
      dados.forEach(item => {
        const eventoElemento = criarEventoElemento(item);
        container.appendChild(eventoElemento);
      });
    })
    .catch(err => {
      console.error("Erro ao buscar eventos:", err);
    });
}

function carregarApostas() {
  fetch('/get_apostas')
    .then(res => res.json())
    .then(dados => {
      const container = document.getElementById("apostas");
      container.innerHTML = ""; // limpa antes
      dados.forEach(item => {
        const eventoElemento = criarAposta(item);
        container.appendChild(eventoElemento);
      });
    })
    .catch(err => {
      console.error("Erro ao buscar eventos:", err);
    });
}

function excluirAposta(id) {
  fetch('/del_aposta', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id: id })
  })
    .then(res => {
      if (res.ok) {
        carregarApostas();
      } else {
        alert("Erro ao excluir aposta.");
      }
    });
}

// Inicializa
carregarEventos();
carregarApostas();