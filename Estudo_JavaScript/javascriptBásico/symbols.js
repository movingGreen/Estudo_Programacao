let lib = {
    name: "ABC",
};
    
lib["id"] = 5;
lib["id"] = 6; // The value is changed because it is String [KEY]!!

lib[Symbol("id")] = 123;
lib[Symbol("id")] = 124; //Not changed

console.log(lib); // { name: "ABC", id: 6, Symbol(id): 123, Symbol(id): 124 }

let globalSymbol = Symbol.for("name");
let localSymbol = Symbol("name");

alert( Symbol.keyFor(globalSymbol) ); // name, global symbol
alert( Symbol.keyFor(localSymbol) ); // undefined, not global

alert( localSymbol.description ); // name