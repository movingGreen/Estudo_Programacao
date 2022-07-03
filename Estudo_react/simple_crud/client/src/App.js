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
        <label htmlFor="nome">Nome do funcionario:</label>
        <input 
          type="text" 
          name="nome" 
          onChange={(event) => {
            setNome(event.target.value);
          }}
        />
        <label htmlFor="idade">Idade:</label>
        <input 
          type="number" 
          name="idade"
          onChange={(event) => {
            setIdade(event.target.value);
          }}
        />
        <label htmlFor="nacionalidade">Nacionalidade:</label>
        <input 
          type="text" 
          name="nacionalidade" 
          onChange={(event) => {
            setNacionalidade(event.target.value);
          }}
        />
        <label htmlFor="posicao">Posição:</label>
        <input 
          type="text" 
          name="posicao" 
          onChange={(event) => {
            setPosicao(event.target.value);
          }}
        />
        <label htmlFor="salario">Valor do salário (mês):</label>
        <input 
          type="number" 
          name="salario"
          onChange={(event) => {
            setSalario(event.target.value);
          }}
        />
        <button>Adicionar funcionario</button>
      </div>
    </div>
  );
}

export default App;
