// 1번 
//for (let i = 0; i < 6; i++) {
//   console.log('*'.repeat(i))
// }


// 2번
// words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

// function palindrome(word) {
//     // word가 회문인지 아닌지 판별
//     return word === word.split("").reverse().join('') ? true:false
//   }
  
// for (const word of words) {
//   console.log(palindrome(word))
// }

// // 출력 예시
// // true
// // true
// // true
// // false
// // false
// // false

//3번




// //과제

// // 1번
// const nums = [1,2,3,4,5,6,7,8]

// for (let i = 0; i < nums.length; i++) {
//   console.log('nums[' + i + ']: ' + nums[i])
// }

// // for (const i = 0; i < nums.length; i++) {
// //                                     ^

// // TypeError: Assignment to constant variable.
// // 최초 정의한 i를 재할당하면서 사용하기 때문에 const가 아닌 let을 사용해야함

// // 2번
// for (num of nums) {
//   console.log(num, typeof num)
// }

// // 0 string
// // 1 string
// // 2 string
// // 3 string
// // 4 string
// // 5 string
// // 6 string
// // 7 string
