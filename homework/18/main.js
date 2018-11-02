
var keys = loadConfig() || JSON.stringify() || [
  {
    'q': 'www.qq.com',
    'w': 'weibo.com',
    'e': 'ele.me',
    'r': 'renren.com',
    't': 'tianya.com',
    'y': 'youtube.com',
    'u': 'uc.com',
    'i': 'iqiyi.com',
    'o': 'opera.com',
    'p': ''
  },
  {
    'a': 'acfun.tv',
    's': 'sohu.com',
    'd': '',
    'f': '',
    'g': '',
    'h': '',
    'j': '',
    'k': '',
    'l': ''
  },
  {
    'z': 'zhihu.com',
    'x': '',
    'c': '',
    'v': '',
    'b': '',
    'n': '',
    'm': 'www.mcdonalds.com.cn'
  },
]


function loadConfig() {
  return JSON.parse(localStorage.getItem('navConfig') || 'null')
}

function setConfig() {
  return localStorage.setItem('navConfig', JSON.stringify(keys))
}

function createTag(tagName, attrs) {
  var el = document.createElement(tagName)
  for (var k in attrs) {
    el[k] = attrs[k]
  }
  return el
}

for (var keyMap of keys) {
  var keyMapContainer = createTag('div', {className: 'keyRow'})
  for (var keyItem in keyMap) {
    var key = createTag('div', {className: 'key', id: 'key' + keyItem}),
      keyCap = createTag('div', {className: 'keyCap'}),
      keyIcon = createTag('img', {src: 'http://' + keyMap[keyItem] + '/favicon.ico', width: 16, height: 16}),
      keySpan = createTag('span'),
      keyEditBtn = createTag('button')

    keyIcon.onerror = function (event) {
      event.target.src = '/NA.png'
    }

    keyEditBtn.onclick = function (event) {
      var btn = event.target,
          url = prompt('输入新链接'),
          keyId = btn.parentNode.parentNode.id

      btn.previousElementSibling.src = 'http://' + url + '/favicon.ico'

      for (var keyMap of keys) {
        for (var keyItem in keyMap) {
          if (keyItem === keyId.slice(3)) {
            keyMap[keyItem] = url
            setConfig()
            return
          }
        }
      }
    }

    keySpan.textContent = keyItem.toUpperCase()
    keyEditBtn.textContent = '改'

    keyCap.appendChild(keySpan)
    keyCap.appendChild(keyIcon)
    keyCap.appendChild(keyEditBtn)
    key.appendChild(keyCap)

    keyMapContainer.appendChild(key)
  }
  keyBoardWrapper.appendChild(keyMapContainer)
}

document.onkeypress = function (event) {
  var el = document.getElementById('key' + event.key)
  el.classList.add('pressed');
}

document.onkeyup = function (event) {
  var el = document.getElementById('key' + event.key)
  el.classList.remove('pressed');
  for (var keyMap of keys) {
    for (var keyItem in keyMap) {
      if (keyItem === event.key) {
        location.href = 'http://' + keyMap[keyItem]
        return
      }
    }
  }
}





