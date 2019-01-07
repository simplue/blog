log = console.log

var object = {}
log(object.__proto__ === Object.prototype)

var fn = function () {
}
log(fn.__proto__ === Function.prototype)
log(fn.__proto__.__proto__ === Object.prototype)

var array = []
log(array.__proto__ === Array.prototype)
log(array.__proto__.__proto__ === Object.prototype)

log(Function.__proto__ === Function.prototype)
log(Array.__proto__ === Function.prototype)
log(Object.__proto__ === Function.prototype)

log(true.__proto__ === Boolean.prototype)

log(Function.prototype.__proto__ === Object.prototype)

!function () {
  function fn() {
    console.log(this)
    foo = this
  }

  x = new fn()
  console.log(foo === x, '##~~~~~~~~~~')
  console.log(x.constructor === fn, '!!~~~~~~~~~~')
  console.log(fn.__proto__ === Function.prototype)
  console.log(fn.prototype)
  console.log('x.__proto__ === fn.prototype:', x.__proto__ === fn.prototype)
  console.dir(x)
  console.dir(x.__proto__)
}.call()

let promiseOperation = () => {
  return new Promise(function (resolve, reject) {
    // 执行异步代码 ...
    success = true
    if (success) {
      resolve('value');
    } else {
      reject('error');
    }
  })
}

function Human(name, sex) {
  this.name = name;
  this.sex = sex
}

Human.prototype.talk = function () {
  console.log('bla bla bla...')
}

var man = new Human('李四', '男');
console.log(man.name, man.sex)
man.talk()

!function () {
  let view = document.querySelector('view')

  let model = {
    init: function () {
      // 初始化
    },
    fetch: function () {
      // 获取
    },
    insert: function () {
      // 新增
    },
    update: function () {
      // 更新
    },
    remove: function () {
      // 删除
    }
  }

  let controller = {
    view: null,
    model: null,
    data: null,
    init: function (view, model) {
      this.view = view
      this.model = model
      this.model.init()
      this.bindEvents()
      this.loadDataToView()
    },
    loadDataToView: function () {
      // 加载数据到view
      this.data = this.model.fetch()
      // code ...
    },
    bindEvents: function () {
      // 绑定事件
      this.view.on('clickSaveEvent', (e) => {
        this.saveEvent(e)
      })
    },
    saveEvent: function (e) {
      // 保存事件操作
      // data = {...}
      this.model.insert(data)
    },
  }

  controller.init(view, model)
}.call()
