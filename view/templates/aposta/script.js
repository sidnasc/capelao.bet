const numeroSecreto = Math.floor(Math.random() * 11); 
let tentativas = 0;
const limiteTentativas = 5;

function verificarPalpite() {
  const input = document.getElementById('guessInput');
  const mensagem = document.getElementById('mensagem');
  const tentativasSpan = document.getElementById('tentativas');
  const botao = document.querySelector('button');

  const palpite = Number(input.value);

  if (isNaN(palpite) || palpite < 0 || palpite > 10) {
    mensagem.textContent = "Digite um número válido entre 0 e 10.";
    mensagem.style.color = "orange";
    return;
  }

  tentativas++;

  if (palpite === numeroSecreto) {
    mensagem.textContent = `🎉 Parabéns! Você acertou o número ${numeroSecreto} em ${tentativas} tentativas.`;
    mensagem.style.color = "green";
    input.disabled = true;
    botao.disabled = true;
  } else if (tentativas >= limiteTentativas) {
    mensagem.textContent = `❌ Fim de jogo! O número era ${numeroSecreto}.`;
    mensagem.style.color = "black";
    input.disabled = true;
    botao.disabled = true;
  } else if (palpite < numeroSecreto) {
    mensagem.textContent = "Muito baixo. Tente um número maior.";
    mensagem.style.color = "red";
  } else {
    mensagem.textContent = "Muito alto. Tente um número menor.";
    mensagem.style.color = "red";
  }

  tentativasSpan.textContent = tentativas;
  input.value = '';
  input.focus();
}
