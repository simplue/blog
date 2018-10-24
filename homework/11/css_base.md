
层叠样式表（英语：Cascading Style Sheets，简写CSS）。一种用来为结构化文档（如HTML文档或XML应用）添加样式（字体、间距和颜色等）的计算机语言，由W3C定义和维护。

CSS不能单独使用，必须与HTML或XML一起协同工作，为HTML或XML起装饰作用。下面是四种引入CSS的方式：
```
<!--1 内联-->
<h1 style="color: red;">Hello</h1>

<!--2 style 标签-->

<style>
    h1 {
        color: red;
    }
</style>

<!--3 外部文件-->
<link rel="stylesheet" linke="xxx.css">

<!--4 import-->
@import("xxx.css")
```


## 动手写
选择器参考：
[CSS选择器笔记-阮一峰](https://www.ruanyifeng.com/blog/2009/03/css_selectors.html)
[CSS选择器笔记-MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Selectors)

![简易导航.png](https://upload-images.jianshu.io/upload_images/4430947-7012a047a8fa9c92.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

简易顶部导航栏：
```
<!--使用float做横向布局（float + claerfix）-->
<!--css-->
.clearfix::after {
    content: '';
    display: block;
    clear: both;
}

.topNav > .logo {
    float: left;
}

.topNav > ul {
    list-style: none;
    float: right;
}

.topNav > ul li {
    float: left;
    margin: 0 15px;
}

<!--html-->
<!--在浮动元素的父元素加入clearfix-->
<nav class="topNav clearfix">
    <a href="" class="logo clearfix">
        <span>LOGO</span>
    </a>

    <ul class="clearfix">
        <li><a href="#">首页</a></li>
        <li><a href="#">项目</a></li>
        <li><a href="#">关于</a></li>
        <li><a href="#">联系</a></li>
    </ul>
</nav>
```


## 元素高度
这里以span和div两个典型的元素做示例

### div 高度
取决于（非相等）其内部文档流元素的高度总和。
文档流：也称常规流（英文 normal flow），是文档内元素的流动方向，内联元素从左往右（超出宽度则换行），块级元素从上往下（每个元素单独一行）。

### span 高度
span的高度计算相较于div，就复杂不少，取决于`line-height`（行高），`padding（-top, -bottom）`（上下内边距），`font-family`（字体），`font-size`（字体大小）等

#### line-height
`line-height`的四种取值
```
<!--不继承父元素行高时可用-->
<!--1）px；直接设置行高像素-->
line-height: 15px;
<!--2）系数；如果此元素 font-size: 20px，则行高： 20 x 1.5 = 30px-->
line-height: 1.5;

<!--继承父元素行高时可用（先按照父元素的字体大小计算出行高，然后给子元素用）-->
<!--3）em；如果父元素 font-size: 30px，则行高： 30 x 1.5(em) = 45px-->
line-height: 1.5em;
<!--4）%（百分比）；如果父元素 font-size: 30px，则行高： 30 x 150% = 45px-->
line-height: 150%;
```

### 含 span 的 div 高度
这个问题涉及到CSS的行内格式上下文（英文：Inline Formatting Context，IFC），是一个很复杂的问题，我也没有完全弄懂，这里只列举几项已经了解的影响因素

#### 换行
内联元素在换行时需要考虑`word-break`的值，当内容超出宽度时，默认情况下中英文会隔断，超长的英文单词独立一行且不会换行；值为`break-word`时，与默认情况的区别是长单词虽然也会单独一行，但当其内容超出宽度时会换行；值为`break-all`时，将不顾及英文单词，只要超出宽度就换行。因此建议当内容以中文为主时使用`break-all`，内容以英文为主时使用`break-word`。

![word-break:initial](https://upload-images.jianshu.io/upload_images/4430947-717a2f6cf1facc2d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![word-break: break-all](https://upload-images.jianshu.io/upload_images/4430947-d12f20c2372b23a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![word-break: break-word](https://upload-images.jianshu.io/upload_images/4430947-bd3a9d803253842f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### font-size，line-height，padding（-left, -right），margin（-left, -right）
`font-size`的内容大小意义
`line-height`小于`content-area`时 span 的高度不变，如果`line-height`逐渐缩小至0，那么div的高度也会按照“某种的规律”缩小，但是其高度一般不会变零（不过`textarea`会）
无效的padding top bottom（但是设置了背景色后就不同了），margin top bottom 就是设置了也没用，真没用

#### span 包含的`<sup>` `<sub>`元素
这两个元素貌似不影响`<span>`高度，但是会影响`div`的高度


## CSS辅助工具
取色：colorpix（或浏览器插件）
量尺寸：QQ/微信截图（或浏览器插件）
预览字体：Word
查看/调试样式：chrome F12/加border
图标库：[Iconfont-阿里巴巴矢量图标库](http://iconfont.cn)
背景（壁纸）：[wallhaven](https://alpha.wallhaven.cc/)

## CSS学习资源
- [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS)
- [CSS 2.1 Spec 中文](http://www.ayqy.net/doc/css2-1/cover.html)
- [CSS Tricks](https://css-tricks.com/)
- [阮一峰博客](http://www.ruanyifeng.com/blog/developer/)
- [张鑫旭博客](https://www.zhangxinxu.com/wordpress/category/css/)
- [Codrops 炫酷 CSS 效果](https://tympanus.net/codrops/category/playground/)
- [CSS揭秘](https://book.douban.com/subject/26745943/)
- [Magic of CSS](https://adamschwartz.co/magic-of-css/)