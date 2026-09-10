// E-Task
// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin. MASALAN: getReverse("hello") return qilsin "olleh"
function reverseString(str) {
    // 1-usul
    /* let reverseStr = str.split("").reverse().join("");
    return reverseStr */

    // 2-usul
    let reverseStr = "";
    for(let i = str.length - 1; i >= 0; i--) {
        reverseStr += str[i];
    }
    return reverseStr
}
const result = reverseString("hello");
console.log(result);