let
  imgs = [
    '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE1',
    '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE2&bg=007AFF',
    '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE3&bg=777AFF',
    '//iph.href.lu/400x300?text=%E8%BD%AE%E6%92%AD%E5%9B%BE4&bg=9900FF',
  ],
  slideInterval = 2000,  // 滑动间隔
  currentIndex = 1;  // 初始位置

// 初始化
(() => {
  // 插入图片
  let $images = $('.images')
  for (let src of imgs) {
    $images.append(`<img class="image" src="${src}">`)
  }

  // 设置状态
  $(`.images > img:nth-child(${currentIndex})`).addClass('current')
    .siblings().addClass('wait')
})()

// 启动
setInterval(() => {
  let old = currentIndex
  setImageLeave(old).one('transitionend', () => setImageWait(old))
  currentIndex = old === imgs.length ? 1 : currentIndex + 1
  setImageCurrent(currentIndex)
}, slideInterval)


// 状态转换
let getImageByIndex = n => $(`.images > img:nth-child(${n})`)
let setImageCurrent = n => getImageByIndex(n).removeClass('wait leave').addClass('current')
let setImageLeave = n => getImageByIndex(n).removeClass('wait current').addClass('leave')
let setImageWait = n => getImageByIndex(n).removeClass('leave current').addClass('wait')
