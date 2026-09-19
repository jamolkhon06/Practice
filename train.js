// K-Task
// Shunday function yozing, u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.MASALAN: countVowels("string") return 1;
function countVowels(str) {
    let lowStr = str.toLowerCase()
    let count = 0;
    for(let char of lowStr) {
        if(char === "a" || char === "o" || char === "e" || char === "i" || char === "u") {
            count++;
        }
    }
    return count
}
const result = countVowels("agentic")
console.log(result)


// G-Task
// Yagona parametrga ega function tuzing. Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin. Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin. MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini Yuqoridagi misolda, birinchi indeksda 21 joylashgan. Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.

/* function getHighestIndex(arr) {
    let maxNum = arr[0];
    let maxIndex = 0;
    arr.forEach((element, index) => {
        if(element > maxNum) {
            maxNum = element
            maxIndex = index
        }
    });
    return maxIndex
}
const result = getHighestIndex([5, 21, 12, 31, 8])
console.log(result) */

// F-Task
// Yagona string argumentga ega findDoublers nomli function tuzing. Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa true yokida false natija qaytarsin. MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

/* function findDoublers(string) {
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
console.log(result); */

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