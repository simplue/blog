let runGame = () => {
  console.log('game start\n')
  let players = [player('foo'), player('bar')],
    randomOne = players.splice(Math.floor(Math.random() * 2), 1)[0],
    anotherOne = players.pop(),
    result = randomOne.pk(anotherOne),
    loser = result.loser

  loser.rebirth().revenge(result.winner)
  console.log('game over\n')
}

let player = name => {
  let blood = 5

  console.log(`${name} birth with blood ${blood}\n`)
  return {
    whoami: function () {
      return name
    },
    health: function () {
      return blood
    },
    deaded: function () {
      return blood === 0
    },
    lose: function () {
      console.log(`${name} is dead`)
    },
    win: function () {
      console.log(`winner is ${name}\n`)
    },
    attackMiss: function () {
      return (parseInt(Math.random() * 100) + 1) > 70;
    },
    attack: function (player) {
      if (this.deaded() || player.deaded()) return
      console.log(`${name} attack ${player.whoami()}`)
      if (!player.hurt()) {
        console.log(`${name} attack miss!`)
      }
    },
    hurt: function () {
      if (this.deaded()) return
      if (!this.attackMiss()) {
        blood -= 1
        if (blood < 1) this.lose()
        return true
      }
      return false
    },
    pk: function (player) {
      let
        round = 1,
        pName = player.whoami(),
        winner,
        loser

      console.log(`pk begin, ${name} vs ${pName} \n`)

      while (true) {
        let
          _td = this.deaded(),
          _pd = player.deaded()

        if (_td || _pd) {
          if (_td) {
            player.win()
            winner = player
            loser = this
          } else {
            this.win()
            winner = this
            loser = player
          }
          break
        }

        this.attack(player)
        player.attack(this)
        console.log(`round (${round}) ${blood} : ${player.health()}\n`)
        round += 1
      }

      console.log('pk over\n')
      return {
        winner,
        loser
      }
    },
    rebirth: function () {
      if (this.deaded()) {
        blood += 2
        console.log(`${name} rebirth with blood ${blood}\n`)
        return this
      }
    },
    revenge: function (player) {
      console.log(`${name} go to revenge\n`)
      result = this.pk(player)
      console.log(`${name} revenge ${result.winner.whoami() === name ? 'success' : 'fail'}\n`)
      return result
    }
  }
}

runGame()
