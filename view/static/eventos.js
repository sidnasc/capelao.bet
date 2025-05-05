fetch('/get_eventos')
      .then(res => res.json())
      .then(dados => {
        const container = document.getElementById("eventos");

        dados.forEach(item => {
          const div = document.createElement("div");
          div.className = "evento";

          div.innerHTML = `
            <div class="tituloAposta">${item.evento}</div>
            <div class="odd">
              <button>Casa ${item.odd_casa}</button> X
              <button>Visitante ${item.odd_visitante}</button> 
            </div>
            <div class="input_aposta">
              <input type="number" name="valorAposta" id="valorAposta" placeholder="Digite o valor da aposta:"> 
            </div>
          `;

          container.appendChild(div);
        });
      })
      .catch(err => {
        console.error("Erro ao buscar eventos:", err);
      });