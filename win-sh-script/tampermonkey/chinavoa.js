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
// @grant        none
// ==/UserScript==

(function () {

    'use strict';
    document.title = 'Google'
    !function () {
        var link = document.createElement("link");
        link.href = "https://www.google.com/favicon.ico";
        link.rel = "shortcut icon";
        document.head.appendChild(link);
    }()

    try {
        location.href.match('http://m.chinavoa.com/show-').length
        location.href = location.href.replace('//m', '//www')
    } catch (e) {
        // pass
    }

    // Your code here...
    document.querySelector('#content').childNodes.forEach(function (n) {
        if (n.nodeName !== 'div') {
            try {
                n.parentNode.removeChild(n)
            } catch (e) {
            }
        }
    })

    document.querySelector('#tab_fanyi_con1 > div').remove()
    document.querySelectorAll('p > img').forEach(function (e) {
        e.parentNode.remove()
    })
    document.querySelectorAll('p > strong').forEach(function (e) {
        console.dir(e)
        if (e.innerText.startsWith('______')) {
            e.parentNode.remove()
        }

    })
    document.querySelectorAll('p').forEach(function (e) {
        if (!e.textContent.trim()) {
            e.remove()
        }
    })

    function newDiv() {
        var __div = document.createElement('div')
        __div.classList.add('group')
        __div.classList.add('clearfix')
        return __div
    }

    function chongpai() {
        var arr = []

        contentContainer.classList.add('translated')
        var _div = newDiv()
        document.querySelectorAll('#tab_fanyi_con1 > p').forEach(function (e) {
            arr.push(e)
            if (arr.length > 1) {
                _div.appendChild(arr.pop())
                _div.appendChild(arr.pop())
                contentContainer.appendChild(_div)
                _div = newDiv()
            }
        })

        if (arr.length > 0) {
            _div = newDiv()
            _div.appendChild(arr.pop())
            contentContainer.appendChild(_div)
        }
    }

    var contentContainer = document.querySelector('#tab_fanyi_con1')

    if (document.querySelector('#tab_fanyi_1')) {
        chongpai()
    } else {
        contentContainer.classList.add('rawEnglish')
    }

    var pai = document.createElement('div')
    pai.id = 'pai'
    pai.onclick = function () {
        chongpai()
    }

    document.body.appendChild(pai)

})();
