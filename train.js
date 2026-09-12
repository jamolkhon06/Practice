// F-Task
// Yagona string argumentga ega findDoublers nomli function tuzing. Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa true yokida false natija qaytarsin. MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

function findDoublers(string) {
    for(let i = 0; i <= string.length; i++) {
        for(let k = 0; k < string.length; i++) {
            if(string[i] === string[k]) {
                return true
            }
        }
    }
    return false
}
const result = findDoublers("hello");
console.log(result)

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