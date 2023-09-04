const rls = require("readline-sync")

var palavra = rls.question("digite uma palavra: ");
var primeira = palavra[0]
var ultima = palavra[palavra.length-1]
console.log("a primeira letra eh " +primeira, "a ultima letra eh " +ultima)