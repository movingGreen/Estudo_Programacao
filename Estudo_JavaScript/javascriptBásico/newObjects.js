function Calculator() {
    this.valorA;
    this.valorB;

    this.read = function() {
        this.valorA = +prompt("Digite um valor: ");
        this.valorB = +prompt("Digite um valor: ");
    };

    this.sum = function() {
         return this.valorA + this.valorB;
    };

    this.mul = function() {
        return this.valorA * this.valorB;
    };
}
/*
let calculator = new Calculator();
calculator.read();

let outraCalculadora = new Calculator();
outraCalculadora.read();

alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );
alert( "soma=" + outraCalculadora.sum() );
*/

function Accumulator(valorInicial){
    this.valor = valorInicial;

    this.read = function() {
        this.valor += +prompt("Digite um valor para adicionar ao acumulador", 0);
    };
}

let accumulator = new Accumulator(1); // initial value 1

accumulator.read(); // adds the user-entered value
accumulator.read(); // adds the user-entered value

alert(accumulator.valor); // shows the sum of these values