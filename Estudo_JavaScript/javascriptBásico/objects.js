
let user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete";
delete user.name;

// for (let chave in user) {
//     alert( user[chave] );
// }

function isEmpty(objeto) {
    for (let chave in objeto) {
        return false;
    }
    return true;
}

let schedule = {};

// alert( isEmpty(schedule) ); // true

schedule["8:30"] = "get up";

// alert( isEmpty(schedule) ); // false

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
}

function somaDeSalarios(salarios) {
    sum = 0;
    for (let valor in salarios) {
        sum += salarios[valor];
    }
    return sum;
}

// alert( somaDeSalarios(salaries) );
console.log( somaDeSalarios(salaries) );

let menu = {
    width: 200,
    height: 300,
    title: "My menu"
};

function multiplyNumeric(menu) {
    for (const item in menu) {
        if (typeof menu[item] == "number") {
            menu[item] *= 2;
        }
    }
}

// console.log(menu);
// multiplyNumeric(menu);
// console.log(menu);

let calculator = {
    a: 0,
    b: 0,
    read(valorA, valorB) {
        this.a = valorA;
        this.b = valorB;
    },
    sum() {
        return this.a + this.b;
    },
    mul() {
        return this.a * this.b;
    }
    };
  
// calculator.read(3, 4);
// alert( calculator.sum() );
// alert( calculator.mul() );

let ladder = {
    step: 0,
    up() {
      this.step++;
      return this;
    },
    down() {
      this.step--;
      return this;
    },
    showStep: function() { // shows the current step
      alert( this.step );
      return this;
    }
};

// ladder.up();
// ladder.up();
// ladder.down();
// ladder.showStep(); // 1
// ladder.down();
// ladder.showStep(); // 0

ladder.up().up().up().down().showStep().down().showStep();