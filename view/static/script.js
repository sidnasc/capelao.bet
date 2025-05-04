let saldoGlobal = 0;
const numeroSecreto = Math.floor(Math.random() * 11); 
let tentativas = 0;
const limiteTentativas = 5;

async function depositar() {
  const valorAposta = Number(document.querySelector("#valorAposta").value);
  const mensagemSaldo = document.querySelector("#mensagemSaldo");

  if (isNaN(valorAposta) || valorAposta <= 0) {
    return mensagemSaldo.textContent = "Insira um valor válido.";
  }

    // Pega saldo real do banco
    const res = await fetch("/get_saldo");
    const data = await res.json();
    const saldoBanco = data.saldo;
  
    if (valorAposta > saldoBanco) {
      mensagemSaldo.textContent = "❌ Você não tem saldo suficiente para essa aposta.";
      return;
    }
  
    saldoGlobal = valorAposta;

  saldoGlobal += Number(valorAposta);
  mensagemSaldo.textContent = `Saldo depositado: ${saldoGlobal.toLocaleString("pt-br", { style: "currency", currency: "BRL" })}`;
}

function finalizar() {
  fetch("/definir_saldo", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ saldo: saldoGlobal })  // saldoGlobal calculado no JS
  })
  .then(res => res.json())
  .then(data => {
    mensagemSaldo.textContent = `Saldo sincronizado: R$ ${data.novo_saldo.toFixed(2)}`;
    location.reload();
  });
}

async function verificarPalpite() {
  const input = document.getElementById('palpite');
  const mensagem = document.getElementById('mensagem');
  const tentativasSpan = document.getElementById('tentativas');
  const botao = document.querySelector('enviar');
  const mensagemSaldo = document.querySelector("#mensagemSaldo");

  const palpite = Number(input.value);

  const custoTentativa = valorAposta * 0.07;

  if (isNaN(palpite) || palpite < 0 || palpite > 10) {
    mensagem.textContent = "Digite um número válido entre 0 e 10.";
    mensagem.style.color = "orange";
    return;
  }


  if (saldoGlobal < custoTentativa) {
    mensagem.textContent = "Saldo insuficiente para continuar jogando.";
    mensagem.style.color = "gray";
    input.disabled = true;
    botao.disabled = true;
    return;
  }

  tentativas++;

  if (palpite === numeroSecreto) {
    mensagem.textContent = `🎉 Parabéns! Você acertou o número ${numeroSecreto} em ${tentativas} tentativas.`;
    mensagem.style.color = "green";
    saldoGlobal = (saldoGlobal * 1.7);
    mensagemSaldo.textContent = `Saldo multiplicado: ${saldoGlobal.toLocaleString("pt-br", { style: "currency", currency: "BRL" })}`;
    
    finalizar()
  } else {
    saldoGlobal -= custoTentativa;

    if (tentativas >= limiteTentativas || saldoGlobal < saldoGlobal * 0.07) {
      mensagem.textContent = `❌ Fim de jogo! O número era ${numeroSecreto}.`;
      mensagem.style.color = "black";


      finalizar()
    }  else {
      mensagem.textContent = "Tente novamente.";
      mensagem.style.color = "red";
    }
  }

  // ✅ Exibe saldo e valor descontado formatado
  mensagemSaldo.textContent = `Saldo atual: ${saldoGlobal.toLocaleString("pt-br", { style: "currency", currency: "BRL" })}`;

  tentativasSpan.textContent = tentativas;
  input.value = '';
  input.focus();
}
