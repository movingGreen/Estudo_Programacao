
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

