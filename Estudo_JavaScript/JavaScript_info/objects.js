
let user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete";
delete user.name;

for (let chave in user) {
    alert( user[chave] );
}

function isEmpty(objeto) {
    for (let chave in objeto) {
        return false;
    }
    return true;
}

let schedule = {};

alert( isEmpty(schedule) ); // true

schedule["8:30"] = "get up";

alert( isEmpty(schedule) ); // false