// Gauss cuenta la suma de n números consecutivos


console.log("Prueba 1:")
console.time("Tiempo de ejecución");

let n = 100;
let suma = 0;

for (let i = 1; i < n+1; i++) {
    suma+=i;
}
console.log(suma)

console.timeEnd("Tiempo de ejecución");

console.log(".-.-.-.-.-.-.-.-.-.-")
console.log("Prueba 2:")
console.time("Tiempo de ejecución");

suma = 0;

suma = (1+n)*(n/2)
console.log(suma)
console.timeEnd("Tiempo de ejecución");