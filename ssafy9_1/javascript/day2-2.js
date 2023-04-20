// for(let i = 1, j = 0; i<=5; i++){
//   console.log(" ".repeat(5 - i) + "*".repeat(i + j));
//   j = j + 1;
// }

const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  let count = [0]*(N) + [0]
  let position = K //위치
  let cnt = 1
  // while K < N:
  //   cnt++
  //  K = K + K
  // for i in Range(K):
  // if f-i in charge:
  //   f = f-i
  // else:
  //  cnt = 0

}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}