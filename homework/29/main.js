// window.jQuery = function (nodeOrSelector) {
//   let nodes
//
//   if (typeof nodeOrSelector === 'string') {
//     nodes = document.querySelectorAll(nodeOrSelector)
//   } else {
//     nodes = {
//       0: nodeOrSelector,
//       length: 1,
//     }
//   }
//
//   nodes.addClass = function () {
//     let classArray = arguments
//     nodes.forEach(function (el) {
//       for (let className of classArray) {
//         el.classList.add(className)
//       }
//     })
//   }
//
//   nodes.setText = function (text) {
//     nodes.forEach(function (el) {
//       el.textContent = text
//     })
//   }
//
//   return nodes
// }
//
//
// window.$ = window.jQuery
//
// // setTimeout(function () {
// //   let $div = $('div')
// //   $div.addClass('red', 'foo', 'bar')
// //   $div.setText('hi')
// // }, 1000)
//
//
// addClass = function (nodes, className) {
//   nodes.forEach(function (el) {
//     el.classList.add(className)
//   })
// }
//
// addClass = function (nodes) {
//   console.log(nodes)
//   let args = arguments
//   nodes.forEach(function (el) {
//     for (let i = 1; i < args.length; i++) {
//       el.classList.add(args[i])
//     }
//   })
// }
//
// addClass = function (nodeOrSelector) {
//   let args = arguments
//   if (typeof nodeOrSelector === 'string') {
//     nodes = document.querySelectorAll(nodeOrSelector)
//   } else {
//     nodes = nodeOrSelector
//   }
//   nodes.forEach(function (el) {
//     for (let i = 1; i < args.length; i++) {
//       el.classList.add(args[i])
//     }
//   })
// }
//
// window.$ = {
//   addClass: function (nodeOrSelector) {
//     let args = arguments
//     if (typeof nodeOrSelector === 'string') {
//       nodes = document.querySelectorAll(nodeOrSelector)
//     } else {
//       nodes = nodeOrSelector
//     }
//     nodes.forEach(function (el) {
//       for (let i = 1; i < args.length; i++) {
//         el.classList.add(args[i])
//       }
//     })
//   }
// }
//
// setTimeout(function () {
//   // let nodes = document.querySelectorAll('div')
//   // addClass.call(undefined, nodes, 'red')
//   // addClass.call(undefined, nodes, 'red', 'foo')
//   //   addClass.call(undefined, 'div', 'red', 'foo')
//   $.addClass.call(undefined, 'div', 'red', 'foo')
// }, 1000)
//
//
//
window.jQuery = function (nodeOrSelector) {
  let nodes

  if (typeof nodeOrSelector === 'string') {
    nodes = document.querySelectorAll(nodeOrSelector)
  } else {
    nodes = {
      0: nodeOrSelector,
      length: 1,
    }
  }

  nodes.addClass = function () {
    let classArray = arguments
    nodes.forEach(function (el) {
      for (let className of classArray ){
        el.classList.add(className)
      }
    })
  }

  nodes.setText = function (text) {
    nodes.forEach(function (el) {
      el.textContent = text
    })
  }

  return nodes
}

window.$ = window.jQuery

setTimeout(function () {
  let $div = $('div')
  $div.addClass('red', 'foo', 'bar')
  $div.setText('changed')
}, 1000)