function writeCss(prefix, code, fn) {
  let domCode = document.querySelector('#code')
  let n = 0
  let id = setInterval(() => {
    n += 1
    domCode.innerHTML = Prism.highlight(prefix + code.substring(0, n), Prism.languages.css);
    styleTag.innerHTML = prefix + code.substring(0, n)
    domCode.scrollTop = domCode.scrollHeight
    if (n >= code.length) {
      window.clearInterval(id)
      fn && fn.call()
    }
  }, 0)
}

let css1 = `/* 画个辛普森 */
*{
    transition: all 1s;
}

html{
    background: #272822;
}

#code{
    border: 1px solid #aaa;
    padding: 16px;
}

/* 代码没有高亮怎么行 */
.token.selector{ 
    color: #A6E22E; 
    font-weight: bold; 
}

.token.property{ 
    color: #66D9EF; 
    font-weight: bold; 
}

/* 要有纸！*/
#code-wrapper{
    width: 50%; 
    left: 0; 
    position: fixed; 
    height: 100%;
}

#paper > .content {
    display: block;
    background-color: orange;
}

/* 开始吧 */
`

let css2 = `
.body {
    width: 170px;
    margin: 50px auto 0;
    position: relative;
}

/* 眼睛 */
.eyes {
    position: absolute;
    top: 100px;
}

.eye {
    width: 100px;
    height: 100px;
    background-color: #fff;
    margin-right: 2px;
    border-radius: 50%;
    border: 2px solid #000;
}

/* 左眼 */
.left-eye {
    position: absolute;
    left: -10px;
}

/* 右眼 */
.right-eye {
    position: absolute;
    float: left;
    left: 84px;
    box-shadow: inset -3px -3px 0 2px rgba(0, 0, 0, .2), inset 3px 2px 0 2px rgba(255, 250, 196, .3);
}

.left-pupil, .right-pupil {
    width: 12px;
    height: 12px;
    background-color: #000;
    border-radius: 100%;
    position: relative;
    top: 35px;
    left: 32px;
}

/* 脸 */
.face {
    position: relative;
    height: 350px;
    background: #fed61e;
    border: 5px solid #000;
    border-radius: 80px;
    box-shadow: inset -5px -5px 0 2px rgba(0, 0, 0, .2), inset 5px 5px 0 2px rgba(255, 250, 196, .3);
}

/* 胡子 */
.beard {
    height: 140px;
    background: #d3a64b;
    position: relative;
    width: 180px;
    border-color: black;
    border-style: solid;
    border-width: 2px 5px;
    border-radius: 50%;
    top: 100px;
    left: -15px;
    box-shadow: inset -5px -5px 0 2px rgba(0, 0, 0, .2), inset 5px 5px 0 2px rgba(255, 250, 196, .3);
}

/* 嘴巴 */
.mouth {
    width: 120px;
    height: 55px;
    border-bottom: 5px solid #000;
    position: absolute;
    margin: 0 auto;
    left: 30px;
    top: 35px;
    border-radius: 80%;
}

.mouth:before, .mouth:after {
    content: "";
    display: block;
    width: 20px;
    height: 20px;
    position: absolute;
    top: 28px;
    left: -5px;
    border-left: 2px solid #000;
    border-radius: 40%;
    transform: rotate(45deg);
}

.mouth:after {
    left: auto;
    right: -3px;
    border-left: none;
    border-right: 2px solid #000;
    transform: rotate(-45deg);
}

/* 下巴 */
.chin {
    width: 40px;
    height: 20px;
    border-bottom: 2px solid #000;
    position: absolute;
    top: 95px;
    left: 70px;
    margin: 0 auto;
    border-radius: 30%;
}

/* 鼻子 */
.nose {
    height: 50px;
    width: 60px;
    position: absolute;
    z-index: 2;
    border-radius: 50%;
    margin: 0 auto;
    left: 45px;
    top: 70px;
    border-color: black;
    border-style: solid;
    border-width: 1px 4px;
    background-color: #fed61e;
    box-shadow: inset -5px -5px 0 2px rgba(0, 0, 0, .2), inset 5px 5px 0 2px rgba(255, 250, 196, .3);
}

/* 头发 */
.hair-1 {
    width: 80px;
    height: 50px;
    border-top: 2px solid #000;
    border-radius: 50%;
    position: absolute;
    left: 45px;
    top: -12px;
}

/* 耳朵 */
.ears {
    position: absolute;
    top: 80px;
    left: -25px;
    right: -5px;
}

.ear {
    height: 40px;
    width: 40px;
    position: relative;
    background: #fed61e;
    border: 5px solid #000;
    border-radius: 50%;
    z-index: -10;
    float: left;
}

.ear:last-child {
    float: right;
    box-shadow: inset -5px -5px 0 2px rgba(0, 0, 0, .05);
    top: 5px;
}

/* 眉毛 */
.eyebrows {
    position: absolute;
    top: 97px;
    left: -10px;
    right: -15px;
}

.eyebrow {
    height: 36px;
    width: 40px;
    position: relative;
    float: left;
    transform: rotate(-15deg);
    background: #fed61e;
    border-left: 2px solid #000;
    border-radius: 50%;
    box-shadow: inset 5px 5px 0 2px rgba(255, 250, 196, .3);
}

.eyebrow:last-child {
    float: right;
    border-left: 0px;
    border-right: 2px solid #000;
    top: -2px;
}

/* 完 */
`

writeCss('', css1, () => {
  writeCss(css1, css2)
})
