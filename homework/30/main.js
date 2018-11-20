// 切换间隔
let switchInterval = 1000 * 3
// 首图索引
let currentIndex = 0
// 所有图片
let imgs = [
  '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE1',
  '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE2',
  '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE3',
  '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE4',
]

// 生成dom
let $images = $('#images')
let $windowBtnBar = $('#windowBtnBar')

for (let i = 0; i < imgs.length; i++) {
  $images.append(`<img class="image" src="${imgs[i]}" width=400>`)
  $windowBtnBar.append(`<button class="switch" data-index="${i}">第${i + 1}张</button>`)
}

// 切换
let switchImg = function (index) {
  let
    $btnTarget = $('#windowBtnBar button').eq(index),
    offset = -400 * index
  $images.css({'transform': `translateX(${offset}px)`})
  $btnTarget.siblings().removeClass('btnActive')
  $btnTarget.addClass('btnActive')
}

// 自动切换
let autoSwitch = function f() {
  return setInterval(function () {
    currentIndex += 1
    console.log(currentIndex)
    if (currentIndex >= imgs.length) {
      currentIndex = 0
    }
    switchImg(currentIndex)
  }, switchInterval)
}

// 启动
switchImg(currentIndex)
let timerId = autoSwitch()

// 手动切换，停留足够时间
$('.switch').on('click', function (e) {
  clearInterval(timerId)
  currentIndex = parseInt(e.currentTarget.dataset.index)
  switchImg(currentIndex)
  timerId = autoSwitch()
})

// hover 定格
$images.on('mouseenter', function() {
  $('.frozen').text('停止切换')
  clearInterval(timerId)
})

// hover 离开继续切换
$images.on('mouseleave', function() {
  $('.frozen').text('自动切换')
  timerId = autoSwitch()
})

