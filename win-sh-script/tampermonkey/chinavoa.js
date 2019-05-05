// ==UserScript==
// @name         chinavoa
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http*://www.chinavoa.com/show-*.html
// @match        http*://m.chinavoa.com/show-*.html
// @match        http*://www.chinavoa.com/list-*.html
// @match        http*://m.chinavoa.com/list-*.html
// @require      https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js
// @require      file://d:\tampermonkey\chinavoa.js
// @grant        none
// ==/UserScript==

(function () {
    main()
})();

var main = function () {
    var url = location.href
    if (RegExp('m.chinavoa.com/show-').test(url) || RegExp('m.chinavoa.com/index.php').test(url)) {
        return location.href = url.replace('//m', '//www')
    }

    var $contentContainer = $('#tab_fanyi_con1')
    var translated = $('#tab_fanyi_1').length > 0

    var setTitle = function (title) {
        if (title === 'VOA') {
            var _arr = document.title.split(':')
            var _title = _arr[_arr.length - 1]
            var _arr_pre = _title.split('-')
            return document.title = _arr_pre[0]
        }
        document.title = title
    }

    var reload = function () {
        var _newBlock = newBlock()
        var contentSelector = '#tab_fanyi_con1'
        var contentBlockClassList = ['group', 'clearfix']
        var contentRawChildNodeName = 'P'
        $(`${contentSelector} > *`).each(function () {
            var el = this
            if (el.nodeName !== contentRawChildNodeName) {
                return $(this).appendTo(contentSelector)
            }

            if (_newBlock.children().length > 0) {
                _newBlock.append(el).appendTo(contentSelector)
                _newBlock = newBlock()
            } else {
                _newBlock.addClass(contentBlockClassList).append(el)
            }
        })

        if (_newBlock.children().length > 0) {
            _newBlock.appendTo(contentSelector)
        }
    }

    var chongpai = function () {
        $contentContainer.addClass('translated')
        reload()
    }

    var caiyun = function () {
        // return
        try {
            var trs = document.createElement('script');
            trs.type = 'text/javascript';
            trs.charset = 'UTF-8';
            trs.src = '//caiyunapp.com/dest/trs.js';
            document.body.appendChild(trs);
        } catch (e) {
            alert(e);
        }
    }

    document.querySelectorAll('a').forEach(function (e) {
        e.target = '_blank';
        e.href = e.href.replace('//m.chinavoa.com/show-', '//www.chinavoa.com/show-')
        e.href = e.href.replace('//m.chinavoa.com/index.php', '//www.chinavoa.com/index.php')
    })

    !function () {
        var link = document.createElement('link');
        link.href = 'https://favicon.yandex.net/favicon/voanews.com';
        link.rel = 'shortcut icon';
        document.head.appendChild(link);
    }()

    if ($contentContainer.length) {
        var titleEl = document.querySelector('#tab_fanyi_con1 p > strong')
        if (titleEl) {
            setTitle(titleEl.innerText)
        } else {
            setTitle('VOA')
        }
        $('body > *:not(.area)').remove()
        $('body > .containter').remove()
        $('#rightContainer > *:not(#content)').remove()
        $('#content > *:not(.Showbox)').remove()
        $('a.btn_zhankai').remove()
        $('#content').contents().filter(function () {
            return this.nodeType === 3
        }).remove()
        $('p > strong').filter(function () {
            var el = this
            if (el.innerText.endsWith('___')) {
                el.innerText = '________________________________'
                var elP = $(el).parent()
                elP.clone().insertAfter(elP)
            }
        })
        $('p').filter(function () {
            return !this.innerText.trim()
            // return this.children.length === 0 && !this.innerText.trim()
        }).remove()
        $('#tab_fanyi_con1 > *:not(p)').remove()

        $('p > img').filter(function () {
            var $el = $(this)
            $el.parent().replaceWith($('<div/>', {
                class: 'reload-block',
                style: 'text-align: center',
            }).append($el.clone()))
        })
    } else {
        setTitle('VOA')
    }

    var newBlock = function () {
        return $('<div/>')
    }
    if (translated) {
        chongpai()
    } else if ($contentContainer.length > 0) {
        $contentContainer.addClass('rawEnglish')
        caiyun()
    }

    $(document).keyup(function (e) {
        if (e.key === 'r') {
            chongpai()
            // $('body > *:not(.area)').remove()
        } else if (e.key === 't') {
            caiyun()
        }
    })
}
