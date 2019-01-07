/*把code写到#code和style标签里*/
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

function writeMarkdown(markdown, fn) {
  let domPaper = document.querySelector('#paper>.content')
  let n = 0
  let id = setInterval(() => {
    n += 1
    domPaper.innerHTML = markdown.substring(0, n)
    domPaper.scrollTop = domPaper.scrollHeight
    if (n >= markdown.length) {
      window.clearInterval(id)
      fn && fn.call()
    }
  }, 0)
}

var css1 = `/* 听说简历也能动 */
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

/* 要有纸！ */
#code-wrapper{
  width: 50%; 
  left: 0; 
  position: fixed; 
  height: 100%;
}

#paper > .content {
  display: block;
  background-color: #F5F5D5;
}

/* 开始吧
 * ........
 */
`

var md = `
# 自我介绍

我是张三，JiaLiDun University 毕业，一名 Web 开发者。
# 联系方式
- Email：8848@qq.com
- 手机：15623336666

# 专业技能
- HTML
- CSS
- JavaScript
- Node.js

# 工作经验
## 鸡厂 20xx~至今 饲养员 

## 猪厂 20xx~20xx 屠夫 
`

let css3 = `/* 完 */`

writeCss('', css1, () => { // writeCss call the function
  createPaper(() => {
    writeMarkdown(md, () => {
      convertMarkdownToHtml(() => {
        writeCss(css1, css3)
      })
    })
  })
})


function createPaper(fn) {
  var paper = document.createElement('div')
  paper.id = 'paper'
  var content = document.createElement('pre')
  content.className = 'content'
  paper.appendChild(content)
  document.body.appendChild(paper)
  fn && fn.call()
}

function convertMarkdownToHtml(fn) {
  var div = document.createElement('div')
  div.className = 'html markdown-body'
  div.innerHTML = marked(md)
  let markdownContainer = document.querySelector('#paper > .content')
  markdownContainer.replaceWith(div)
  fn && fn.call()
}

