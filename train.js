// F-Task
// Yagona string argumentga ega findDoublers nomli function tuzing. Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa true yokida false natija qaytarsin. MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

<<<<<<< HEAD
function findDoublers(string) {
    for(let i = 0; i <= string.length; i++) {
        for(let k = 0; k < string.length; i++) {
            if(string[i] === string[k]) {
=======
function findDoublers(str) {
    for(let i = 0; i <= str.length; i++) {
        for(let k = 0; k < str.length; i++) {
            if(str[i] === str[j]) {
>>>>>>> 08557d785d25579412fdc3f560c968a4e750677b
                return true
            }
        }
    }
    return false
}
const result = findDoublers("hello");
<<<<<<< HEAD
console.log(result);
=======
console.log(result)
>>>>>>> 08557d785d25579412fdc3f560c968a4e750677b

// E-Task
// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin. MASALAN: getReverse("hello") return qilsin "olleh"
// function reverseString(str) {
//     // 1-usul
//     /* let reverseStr = str.split("").reverse().join("");
//     return reverseStr */

//     // 2-usul
//     let reverseStr = "";
//     for(let i = str.length - 1; i >= 0; i--) {
//         reverseStr += str[i];
//     }
//     return reverseStr
// }
// const result = reverseString("hello");
// console.log(result);