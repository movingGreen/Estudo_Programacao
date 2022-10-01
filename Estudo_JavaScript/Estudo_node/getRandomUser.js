fetch("https://randomuser.me/api").then((resposta) => {
  let dados = JSON.stringify(resposta, null, 2);
  console.log(dados);
});
