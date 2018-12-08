let log = console.log
let print = log
// let array = [NaN, NaN, 1, '1', 1, undefined, '1', '', '', 0, 0, null, null, undefined, false, false]
// let unique = []
// let existsNaN = false
// array.forEach(item => {
//   let index = unique.indexOf(item)
//   if (index < 0) {
//     if (isNaN(item) && item !== undefined) {
//       if (!existsNaN) {
//         existsNaN = true
//         unique.push(item)
//       }
//     } else {
//       unique.push(item)
//     }
//   }
// })

// print(unique)
//
// print(Array.from(new Set(array)))


function unique(array) {
  var obj = {};
  return array.filter(function (item) {
    return obj.hasOwnProperty(typeof item + JSON.stringify(item)) ? false : (obj[typeof item + JSON.stringify(item)] = true)
  })
}
console.log(unique([NaN, NaN, 1, '1', 1, undefined, '1', '', '', 0, 0, null, null, undefined, false, false, 3, 4, 5, 6, 3, 4, 4, 5, 5, 5]))

// let unique = array => Array.from(new Set(array))
// console.log(unique([NaN, NaN, 1, '1', 1, undefined, '1', '', '', 0, 0, null, null, undefined, false, false, 3, 4, 5, 6, 3, 4, 4, 5, 5, 5]))
