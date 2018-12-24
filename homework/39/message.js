!function () {
  let view = document.querySelector('section.message')

  let model = {
    init: function () {
      AV.init({appId: 'SbCKSWF63eNlKfoiYbkx7jQC-gzGzoHsz', appKey: 'MujX39qI4ejGWtFxxn3Oqy2d'})
    },
    fetch: function () {
      let query = new AV.Query('Message')
      return query.find()
    },
    save: function (name, content) {
      let
        Message = AV.Object.extend('Message'),
        message = new Message()
      return message.save({
        'name': name,
        'content': content
      })
    }
  }

  let controller = {
    view: null,
    model: null,
    messageList: null,
    init: function (view, model) {
      this.view = view
      this.messageList = view.querySelector('#messageList')
      this.form = view.querySelector('form')
      this.model = model
      this.model.init()
      this.loadMessages()
      this.bindEvents()
    },
    loadMessages: function () {
      this.model.fetch().then(
        messages => {
          let array = messages.map((item) => item.attributes)
          array.forEach((item) => {
            let li = document.createElement('li')
            li.innerText = `${item.name}: ${item.content}`
            this.messageList.appendChild(li)
          })
        }
      )
    },
    bindEvents: function () {
      this.form.addEventListener('submit', e => {
        e.preventDefault()
        this.saveMessage()
      })
    },
    getInputByName: function (name) {
      return this.form.querySelector(`input[name=${name}]`).value
    },
    saveMessage: function () {
      let form = this.form
      this.model.save(this.getInputByName('name'), this.getInputByName('content')).then(
        object => {
          let
            li = document.createElement('li'),
            messageList = document.querySelector('#messageList')
          li.innerText = `${object.attributes.name}: ${object.attributes.content}`
          messageList.appendChild(li)
          form.querySelector('input[name=content]').value = ''
        }
      )
    }
  }

  controller.init(view, model)
}.call()
