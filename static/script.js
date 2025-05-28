const formulario = document.getElementById("formulario");
const resultados = document.getElementById("resultados");

formulario.addEventListener("submit", async (e) => {
  e.preventDefault();

  const nombre = document.getElementById("nombre").value;
  const generos = [...document.querySelectorAll("input[name='generos']:checked")].map(el => el.value);

  const res = await fetch("/recomendar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ nombre, generos_favoritos: generos })
  });

  const data = await res.json();

  resultados.innerHTML = "";
  data.forEach(c => {
    resultados.innerHTML += `
      <li>
        <strong>${c.titulo}</strong> — ${c.artista} (${c.genero})<br>
        ${c.url_preview ? `<audio controls src="${c.url_preview}"></audio>` : "Sin preview"}<br>
        <a href="${c.url_spotify}" target="_blank">Escuchar en Spotify</a>
      </li>
    `;
  });
});