// document.querySelectorAll('body > *:not(:first-child)').style.display = 'none'
var minIndex = 0
var specialBlock = []
setTimeout(function () {
  app.classList.remove('prepare')
  siteWelcome.classList.remove('active')

  specialBlock = document.querySelectorAll('[data-x]')
  for (let el of specialBlock) {
    el.classList.add('offset')
  }
  highlightNav()
}, 2500)


window.onscroll = function () {
  var y = window.scrollY
  if (y > 0) {
    topNavBar.classList.add('sticky')
  } else {
    topNavBar.classList.remove('sticky')
  }
  highlightNav()

}

function highlightNav() {
  for (let i = 0; i < specialBlock.length; i++) {
    if (Math.abs(specialBlock[i].offsetTop - window.scrollY - 200) < Math.abs(specialBlock[minIndex].offsetTop - window.scrollY)) {
      minIndex = i
      break
    }
  }

  var eee = document.querySelector(`[href="#${specialBlock[minIndex].id}"]`)
  var li = eee.parentNode

  for (let iii of li.parentNode.children) {
    for (let iiii of iii.children) {
      iiii.classList.remove('highlight')
    }
  }
  specialBlock[minIndex].classList.remove('offset')
  eee.classList.add('highlight')
}

var menuTriggers = document.getElementsByClassName('menuTrigger')
for (let el of menuTriggers) {
  el.onmouseenter = function (e) {
    e.currentTarget.classList.add('active')
  }
  el.onmouseleave = function (e) {
    e.currentTarget.classList.remove('active')
  }
}

function animate(time) {
  requestAnimationFrame(animate);
  TWEEN.update(time);
}

requestAnimationFrame(animate);

var anchor = document.querySelectorAll('.topNavInner > ul > li > a')
for (let el of anchor) {
  el.onclick = function (e) {
    e.preventDefault()
    var
      scrollTarget = document.getElementById(e.currentTarget.getAttribute('href').replace('#', '')),
      targetTop = scrollTarget.offsetTop,
      currentTop = window.scrollY,
      coords = {y: currentTop},
      usedTime = (Math.abs(currentTop - (targetTop - 80)) / 100) * 100

    usedTime = usedTime > 1000 ? 1000 : usedTime
    new TWEEN.Tween(coords)
      .to({y: scrollTarget.offsetTop - 80}, usedTime)
      .easing(TWEEN.Easing.Quadratic.In)
      .onUpdate(function () {
        window.scrollTo(0, coords.y)
      })
      .start();
  }
}
