// 切换间隔
let switchInterval = 1000 * 3
// 首图索引
let currentIndex = 0
// 所有图片
let imgs = [
  '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/macbook.jpg',
  '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/iphone.jpg',
  '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/imac.jpg',
  '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/info.jpg',
],
  btnImgs = [
    '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/thumb_macbook.png',
    '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/thumb_iphone.png',
    '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/thumb_imac.png',
    '//demo.tutorialzine.com/2009/11/beautiful-apple-gallery-slideshow/img/sample_slides/thumb_about.png',
  ]


// 生成dom
let $images = $('#images')
let $windowBtnBar = $('#windowBtnBar')

for (let i = 0; i < imgs.length; i++) {
  $images.append(`<img class="image" src="${imgs[i]}" width=920>`)
  $windowBtnBar.append(`<a href="javascript:;" class="switch" data-index="${i}"><img src="${btnImgs[i]}"></a>`)
}

// 切换
let switchImg = function (index) {
  // return
  let
    $btnTarget = $('#windowBtnBar .switch').eq(index),
    offset = -920 * index
  $images.css({'transform': `translateX(${offset}px)`})
  $btnTarget.siblings().removeClass('btnActive')
  $btnTarget.addClass('btnActive')
}

// 自动切换
let autoSwitch = function () {
  console.log('fopo')
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

