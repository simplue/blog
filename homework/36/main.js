!(() => {
  let request = new XMLHttpRequest()
  request.open('get', '/')
  request.send()
  request.onreadystatechange = () => {
    if (request.readyState === 4) {
      if (request.status >= 400) {
        console.log('请求失败')
      } else if (request.status >= 200) {
        console.log('请求成功，响应：', request.responseText)
      }
    }
  }
})()


!(() => {
  let ajax = function (url, method, body, success, fail) {
    let request = new XMLHttpRequest()
    request.open(method, url)
    request.onreadystatechange = () => {
      if (request.readyState === 4) {
        if (request.status >= 400) {
          fail(request)
        } else if (request.status >= 200) {
          success(request.responseText)
        }
      }
    }
    request.send(body)
  }
  ajax('/', 'get', 'this is the body', () => console.log('ok'), () => console.log('fuck'))
})()


!(() => {
let ajax = function ({url, method, body}) {
  return new Promise(function (resolve, reject) {
    let request = new XMLHttpRequest()
    request.open(method, url)
    request.onreadystatechange = () => {
      if (request.readyState === 4) {
        if (request.status >= 400) {
          reject(request)
        } else if (request.status >= 200) {
          resolve(request.responseText)
        }
      }
    }
    request.send(body)
  })
}

  ajax({
    url: '/',
    method: 'get'
  }).then((resp) => {
    console.log('success')
  }, (resp) => {
    console.log('fail')
  })
})()
