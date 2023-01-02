'use strict';
function sum_phone_digit(phone_number) {
    let total = 0
    for (let i = 0; i < phone_number.length; i++) {
        total += parseInt(phone_number[i])
    }
    return total
}

function interpret(number) {
    let meaning = ""
    if ([9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65].includes(number)) {
        meaning = "ดีมาก"
    } else if ([69, 79].includes(number)) {
        meaning = "โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุข"
    } else if ([10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61].includes(number)) {
        meaning = "ดีปานกลาง"
    } else if ([62, 66, 68, 74, 75].includes(number)) {
    meaning = "เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม"
    } else if ([11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80].includes(number)) {
        meaning = "เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น"
    }
    return meaning;
}
    
let phone_number = "0891236666"
let n = sum_phone_digit(phone_number)
console.log(phone_number, interpret(n));
