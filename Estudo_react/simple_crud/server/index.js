const express = require('express');
const app = express();
const mysql = require('mysql')

const db = mysql.createConnection({
  user: 'root',
  host: 'localhost',
  password: '',
  database: "new_schema",
});


app.post('criar', (req, res) => {
  const nome = req.body.nome;
  const idade = req.body.idade;
  const nacionalidade = req.body.nacionalidade;
  const posiçao = req.body.posiçao;
  const salario = req.body.salario;

  db.query('INSERT INTO new_schema (nome, idade, nacionalidade, posiçao, salario) VALUES (?,?,?,?,?)', 
  [nome, idade, nacionalidade, posiçao, salario], 
  (err, result) => {
    if (err) {
      console.log(err);
    } else {
      res.send("Valores inseridos");
    }
  })
})


app.listen(3001, () => {
  console.log("legal, seu servidor está rodando na porta 3001");
})