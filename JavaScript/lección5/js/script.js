/* Concatenación de Cadena */
var nombre = "Pedro ";
var apellido = "Michelli";
var nombreCompleto = nombre + " " + apellido;
console.log(nombreCompleto);
var nombreCompleto2 = "Nelson" + " " + "Lassa";
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izq a der siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17; // Aqui se puede diferenciar a traves de los parensis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos); // Contexto str o contexto cadena

nombre += apellido; // Tercera Concatenación usando el operador simplificado
console.log(nombre);
