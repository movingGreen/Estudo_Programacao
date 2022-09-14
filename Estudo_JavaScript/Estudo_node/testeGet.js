const https = require("https");
const { json } = require("stream/consumers");

const resposta = https.get(
  "https://www.fruityvice.com/api/fruit/all",
  (resposta) => {
    resposta.setEncoding("utf-8");
    let dados = "";
    resposta.on("data", (parte) => {
      dados += parte;
    });
    resposta.on("end", () => {
      // const parseDados = JSON.parse(dados);
      console.log(dados);
    });
  }
);
