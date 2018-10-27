
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

<!--![简易导航.png](https://upload-images.jianshu.io/upload_images/4430947-7012a047a8fa9c92.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)-->

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
div高度取决于（非相等）其内部文档流元素的高度总和。因此在写CSS时，应尽量避免`height: *px`这种写法，通过控制内部文档流元素的高度来控制div高度。
文档流：也称常规流（英文 normal flow），是文档内元素的流动方向，内联元素从左往右（超出宽度则换行），块级元素从上往下（每个元素单独一行）。

### span 高度
span的高度计算相较于div，就复杂不少，取决于`line-height`（行高），`padding（-top, -bottom）`（上下内边距），`font-family`（字体），`font-size`（字体大小）等

#### 字体与行高
`font-family`用于设置字体，`font-size`用于设置字体大小，单位有：px、pt、pc、%、em、rem、keyword、vw、vh、vmin和vmax等。一般使用px，那么当我们设置`font-size: 100px`时，意为着什么？这就涉及到一点字体设计的知识，如下图所示，Ascender到Descender的距离就是100px。

<!--![font-size](https://upload-images.jianshu.io/upload_images/4430947-cea320ae1a772625.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)-->

实际上我们可以发现，文字占据的高度在一般情况下并不等于字体大小，而是和行高`line-height`相等。即便我们只设置了字体大小，并没有指定行高，浏览器也会将字体设计文件给出的对应默认行高设置在字体上。另外，`font-size`相同的两种字体，在默认情况下占据的高度未必相同，因为其默认行高很可能不一样。

`line-height`用于设置字体行高，是一个分厂重要的决定span高度的属性。需要注意的是，行高并不是两条baseline的间距，参考下图：

<!--![realLineHeight](https://upload-images.jianshu.io/upload_images/4430947-23834afb57c6fb54.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)-->

常用的四种行高单位如下
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

#### padding，margin，width，height
`padding-top`和`padding-bottom`并不能“撑大”span，而`margin-top`和`margbin-bottom`也不能让“撑大”span的上下间距，同样`width`和`height`也不能改变span的尺寸。不过这其中的`padding-top`和`padding-bottom`还是有一些特殊作用的，如果span设置了背景色，那么背景色就会延展到`padding-top`和`padding-bottom`设置的范围上。使用`padding-left`、`padding-right`、`margin-left`和`margin-right`都能改变span的间距。


#### 含 span 的 div 高度
这个问题涉及到CSS的行内格式上下文（英文：Inline Formatting Context，IFC），是一个很复杂的问题，我也没有完全弄懂，这里只列举几项已经了解的影响因素

##### 换行
内联元素在换行时需要考虑`word-break`的值，当内容超出宽度时，默认情况下中英文会隔断，超长的英文单词独立一行且不会换行；值为`break-word`时，与默认情况的区别是长单词虽然也会单独一行，但当其内容超出宽度时会换行；值为`break-all`时，将不顾及英文单词，只要超出宽度就换行。因此建议当内容以中文为主时使用`break-all`，内容以英文为主时使用`break-word`。

<!--![word-break:initial](https://upload-images.jianshu.io/upload_images/4430947-717a2f6cf1facc2d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)-->

<!--![word-break: break-all](https://upload-images.jianshu.io/upload_images/4430947-d12f20c2372b23a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)-->

<!--![word-break: break-word](https://upload-images.jianshu.io/upload_images/4430947-bd3a9d803253842f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)-->

##### `line-height`小于内容高度
`line-height`小于内容时span的高度不变，如果`line-height`逐渐缩小至0，那么div的高度也会按照“某种的规律”缩小，但是其高度一般不会变零（不过`textarea`会）

##### 包含`<sup>`和`<sub>`
见下图

```
<h1 style="margin-top: 50px;">一般情况</h1>
<div style="border: 2px solid green;">
    <span style="font-size: 50px; border: 2px solid red;">正常</span>
</div>

<h1 style="margin-top: 50px;">行高小于内容</h1>
<div style="border: 2px solid grey; margin-top: 50px;">
    <div style="border: 2px dashed darkcyan; display: inline-block; margin-right: 20px;">
        <span style="font-size: 50px; border: 2px solid red; line-height: 0;">span行高是0</span>
    </div>

    <div style="border: 2px dashed darkcyan; display: inline-block; margin-right: 20px; line-height: 0;">
        <span style="font-size: 50px; border: 2px solid red; line-height: 0;">div和span行高是0</span>
    </div>

    <div style="border: 2px dashed darkcyan; display: inline-block; margin-right: 20px; height: 0;">
        <span style="font-size: 50px; border: 2px solid red; line-height: 0;">div高是0</span>
    </div>
</div>

<h1 style="margin-top: 50px;">含 sub sup</h1>
<div style="border: 2px solid grey;">
    <div style="border: 2px dashed darkcyan; display: inline-block; margin-right: 20px;">
        <span style="border: 2px solid red; margin: 0; font-size: 50px;">对照</span>
    </div>

    <div style="border: 2px dashed darkcyan;display: inline-block;">
        <span style="border: 2px solid red; margin: 0; font-size: 50px;">H<sub>2</sub>O；3<sup>2</sup>=9；我没高，但是我爹高了</span>
    </div>
</div>
```

<!--![sup&sub](https://upload-images.jianshu.io/upload_images/4430947-d7ada8149b831d8d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)-->


##### 其他
当div包含多个span时（单行情况下），div的高度由其中最高的span的高度决定。

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

参考链接:
CSS Font Sizing：https://bitsofco.de/css-font-sizing/
深入了解css的行高Line Height属性：http://www.cnblogs.com/fengzheng126/archive/2012/05/18/2507632.html
深入理解 CSS：字体度量、line-height 和 vertical-align：https://zhuanlan.zhihu.com/p/25808995