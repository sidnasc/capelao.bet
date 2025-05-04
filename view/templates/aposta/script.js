let saldoGlobal = 0;
const numeroSecreto = Math.floor(Math.random() * 11); 
let tentativas = 0;
const limiteTentativas = 5;

function depositar() {
  const valorAposta = Number(document.querySelector("#valorAposta").value);
  const mensagemSaldo = document.querySelector("#mensagemSaldo");

  if (isNaN(valorAposta) || valorAposta <= 0) {
    return mensagemSaldo.textContent = "Insira um valor válido.";
  }

  saldoGlobal += Number(valorAposta);
  mensagemSaldo.textContent = `Saldo depositado: ${saldoGlobal.toLocaleString("pt-br", { style: "currency", currency: "BRL" })}`;
}

function verificarPalpite() {
  const input = document.getElementById('palpite');
  const mensagem = document.getElementById('mensagem');
  const tentativasSpan = document.getElementById('tentativas');
  const botao = document.querySelector('enviar');
  const mensagemSaldo = document.querySelector("#mensagemSaldo");

  const palpite = Number(input.value);

  if (isNaN(palpite) || palpite < 0 || palpite > 10) {
    mensagem.textContent = "Digite um número válido entre 0 e 10.";
    mensagem.style.color = "orange";
    return;
  }

  const custoTentativa = saldoGlobal * 0.07;

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
    input.disabled = true;
    botao.disabled = true;
    valorAposta.disabled = true;
    saldoGlobal = (saldoGlobal * 1.1);
    mensagemSaldo.textContent = `Saldo multiplicado: ${saldoGlobal.toLocaleString("pt-br", { style: "currency", currency: "BRL" })}`;
  } else {
    saldoGlobal -= custoTentativa;

    if (tentativas >= limiteTentativas || saldoGlobal < saldoGlobal * 0.07) {
      mensagem.textContent = `❌ Fim de jogo! O número era ${numeroSecreto}.`;
      mensagem.style.color = "black";
      input.disabled = true;
      botao.disabled = true;
      valorAposta.disabled = true;
    } else if (palpite < numeroSecreto) {
      mensagem.textContent = "Muito baixo. Tente um número maior.";
      mensagem.style.color = "red";
    } else {
      mensagem.textContent = "Muito alto. Tente um número menor.";
      mensagem.style.color = "red";
    }
  }

  // ✅ Exibe saldo e valor descontado formatado
  mensagemSaldo.textContent = `Saldo atual: ${saldoGlobal.toLocaleString("pt-br", { style: "currency", currency: "BRL" })}`;

  tentativasSpan.textContent = tentativas;
  input.value = '';
  input.focus();
}
