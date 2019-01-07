function Human(options){
  this.name = options.name
  this.city = options.city
}

Human.prototype.species = '人'
Human.prototype.walk = function () { console.log('walking...') }
Human.prototype.useTools = function () { console.log('using tools...') }

var human = new Human({name:'Frank', city: 'Hangzhou'})
var human2 = new Human({name:'Jack', city: 'Hangzhou'})

human.walk()
human.useTools()

log = console.log
log('human.__proto__.constructor === Human: ', human.__proto__.constructor === Human)
log('human.species: ', human.species)
log('human.name: ', human.name)
log('human.city: ', human.city)
