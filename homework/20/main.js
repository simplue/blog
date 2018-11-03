var
  canvas = document.getElementById('canvas'),
  context = canvas.getContext('2d'),
  eraserEnabled = false


initCanvas(canvas)
listenToUser(canvas)



// 设置画布初始化
function initCanvas(canvas) {
  initCanvasSize(canvas)
  initPen()
  fillCanvasWithWhite(canvas)
}

// 设置背景
function fillCanvasWithWhite(canvas) {
  const context = canvas.getContext('2d');
  context.save();
  context.globalCompositeOperation = 'destination-over';
  context.fillStyle = 'white';
  context.fillRect(0, 0, canvas.width, canvas.height);
  context.restore();
}

// 设置画布尺寸
function initCanvasSize(canvas) {
  canvas.width = document.documentElement.clientWidth
  canvas.height = document.documentElement.clientHeight
  window.onresize = function () {
    initCanvasSize(canvas)
  }
}

// 设置画笔颜色尺寸
function initPen() {
  context.lineWidth = 5
  context.fillStyle = 'red'
  context.strokeStyle = 'red'
}

// 画笔颜色设置
function resetPenColorIcon() {
  red.classList.remove('active')
  green.classList.remove('active')
  blue.classList.remove('active')
}

function setPenColor(color, colorId) {
  resetPenColorIcon()
  context.fillStyle = color
  context.strokeStyle = color
  colorId.classList.add('active')
}

red.onclick = function () {
  setPenColor('red', red)
}

green.onclick = function () {
  setPenColor('green', green)
}

blue.onclick = function () {
  setPenColor('blue', blue)
}

// 画笔粗细设置
function resetPenSizeIcon() {
  thin.classList.remove('active')
  thick.classList.remove('active')
}

function setPenSize(size, id) {
  resetPenSizeIcon()
  context.lineWidth = size
  id.classList.add('active')
}

thin.onclick = function () {
  setPenSize(5, thin)
}

thick.onclick = function () {
  setPenSize(10, thick)
}

// 功能选择
pen.onclick = function () {
  eraserEnabled = false
  pen.classList.add('active')
  eraser.classList.remove('active')
}

eraser.onclick = function () {
  eraserEnabled = true
  eraser.classList.add('active')
  pen.classList.remove('active')
}

// 清屏
clear.onclick = function () {
  context.clearRect(0, 0, canvas.width, canvas.height);
}

// 保存图画
download.onclick = function () {
  var
    url = canvas.toDataURL("image/png"),
    a = document.createElement('a')

  document.body.appendChild(a)
  a.href = url
  a.download = 'canvas.png'
  a.target = '_blank'
  a.click()
}

// 画线
function drawLine(x1, y1, x2, y2) {
  context.beginPath();
  context.moveTo(x1, y1) // 起点
  context.lineTo(x2, y2) // 终点
  context.stroke()
  context.closePath()
}


// 触屏设备检测
function isTouchDevice() {
  return document.body.ontouchstart !== undefined
}

// 获取事件坐标
function getPosByEvent(event) {
  var canTouch = isTouchDevice()

  return {
    x: canTouch ? event.touches[0].clientX : event.clientX,
    y: canTouch ? event.touches[0].clientY : event.clientY
  }
}

// 监听画笔
function listenToUser(canvas) {
  var
    using = false,
    lastPoint = {
      x: undefined,
      y: undefined
    }

  canvas.ontouchend = canvas.onmouseup = function () { using = false }
  canvas.ontouchstart = canvas.onmousedown = drawStartAction
  canvas.ontouchmove = canvas.onmousemove = drawMoveAction

  // 画笔起始响应
  function drawStartAction(event) {
    var
      pos = getPosByEvent(event),
      x = pos.x,
      y = pos.y

    using = true
    if (eraserEnabled) {
      context.clearRect(x - 5, y - 5, 10, 10)
    } else {
      lastPoint = {
        "x": x,
        "y": y
      }
    }
  }

  // 画笔移动响应
  function drawMoveAction(event) {
    var
      pos = getPosByEvent(event),
      x = pos.x,
      y = pos.y

    if (!using) {
      return
    }

    if (eraserEnabled) {
      context.clearRect(x - 5, y - 5, 10, 10)
    } else {
      drawLine(lastPoint.x, lastPoint.y, x, y)
      lastPoint = pos
    }
  }
}