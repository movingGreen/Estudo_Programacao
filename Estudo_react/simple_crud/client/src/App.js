import './App.css';
import { useState } from "react";


function App() {
  const [nome, setNome] = useState('');
  const [idade, setIdade] = useState(0);
  const [nacionalidade, setNacionalidade] = useState('');
  const [posicao, setPosicao] = useState('');
  const [salario, setSalario] = useState(0);

  return (
    <div className="App">
      <div className="Informacoes">
        <label for="nome">Nome do funcionario:</label>
        <input type="text" name="nome"></input>
        <br/><br/>
        <label for="idade">Idade:</label>
        <input type="number" name="idade"></input>
        <br/><br/>
        <label for="nacionalidade">Nacionalidade:</label>
        <input type="text" name="nacionalidade"></input>
        <br/><br/>
        <label for="posicao">Posição:</label>
        <input type="text" name="posicao"></input>
        <br/><br/>
        <label for="salario">Valor do salário (mês):</label>
        <input type="number" name="salario"></input>
        <button>Adicionar funcionario</button>
      </div>
    </div>
  );
}

export default App;
