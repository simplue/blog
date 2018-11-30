<!--# CGI, FastCGI, WSGI, Web Server, proxy_pass，uwsgi，uWSGI-->


# 网关接口

Web 服务器（这里指服务器软件）自身通常只负责处理静态内容，动态内容（例如用户的个人信息）需要借助外部的应用程序。那么 Web 服务器和外部应用程序通讯时就需要借助一种协议，这类协议一般统称为网关接口。

## CGI
通用网关接口（全称 Common Gateway Interface），最早期的网关接口协议，目前在 Web 开发中用的很少。

## FastCGI
快速通用网关接口，（全称：Fast Common Gateway Interface），一种 CGI 的改进版本，二进制协议。

## SCGI
简单通用网关接口（全称：Simple Common Gateway Interface），一种 CGI 的改进版本，与 FastCGI 类似但更容易解析。

## WSGI
Python Web 服务器网管接口（全称：Web Server Gateway Interface），其实叫 PWSGI（Python Web Server Gateway Interface）或许更准确。一种 Python 应用程序与 Web 服务器的网关接口协议。最早在 [PEP0333](https://www.python.org/dev/peps/pep-0333/) 中定义，后面的为了适应 Python3 又在此基础上更新一版 [PEP3333](https://www.python.org/dev/peps/pep-3333/)。

## uwsgi
uWSGI（注意是大写）的私有二进制协议，用在反向代理时 Web 服务器与 uWSGI 的通讯，需要借助插件（如 [ngx_http_uwsgi_module](http://nginx.org/en/docs/http/ngx_http_uwsgi_module.html)），更详细的协议信息：https://uwsgi-docs.readthedocs.io/en/latest/Protocol.html 。

# Web Server
网页服务器，通常有两种解释，一种是指服务器软件，另一种是指专门用于运行提供网络服务的软件的硬件（俗称电脑，其与一般的 PC 最大不同在于：1）一般不使用图形界面操作；2）只运行提供网络服务的相关软件；3）强调稳定性和可靠性；4）对环境要求高，例如温湿度、网络、供电、维护和监控等）。这里我们只讨论服务器软件。

## Nginx
在目前的 Web 开发中使用最广泛的一种服务器，以高性能著称，也许是未来的 Apache。

## Apache
有时也称 httpd，是另一种广泛使用的服务器，历史悠久，占有率高。

## 其他
### Tengine
淘宝网基于 Nginx 并结合自身业务定制开发的一款开源服务器。

### IIS
微软的，不多说。

### Google Web Server
谷歌的，不多说。

### lighttpd
号称轻量高性能，不了解。

### Caddy
标榜默认 HTTP/2 和 HTTPS，不了解。

# WSGI Servers
实现了 WSGI 协议的应用服务器（Application Server）。一般用在反向代理，也可以作为 Web 服务器使用, 不过通常不会这么做。

## Gunicorn
从 ruby unicorn 移植

## uWSGI


## Tornado
异步

## 其他
- mod_python https://github.com/grisha/mod_python
- mod_wsgi https://github.com/GrahamDumpleton/mod_wsgi
- CherryPy https://github.com/cherrypy/cherrypy
- Waitress https://github.com/Pylons/waitress
- Uvicorn https://github.com/encode/uvicorn
- AIOHTTP https://github.com/aio-libs/aiohttp/
- Daphne https://github.com/django/daphne/


# Web FrameWork
Web 框架
## Django
https://github.com/django/channels

## Tornado

## Flask

## gevent
https://github.com/gevent/gevent
https://github.com/douban/greenify

## 其他
- pyramid https://trypyramid.com/
- masonite https://docs.masoniteproject.com/
- Falcon https://falconframework.org/
- bottle https://github.com/bottlepy/bottle
- aiohttp https://github.com/aio-libs/aiohttp/
- sanic https://github.com/huge-success/sanic


# 部署
## 反向代理

## woker model

## Docker

## supervisor

# FAQ
## 反向代理
FastCGI、HTTP、unix domain socket、uwsgi



https://docs.python-guide.org/scenarios/web/


protocol
https://en.wikipedia.org/wiki/Common_Gateway_Interface
https://en.wikipedia.org/wiki/FastCGI
https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface
https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

wsgi
pep：https://www.python.org/dev/peps/

https://www.fullstackpython.com/wsgi-servers.html
https://grisha.org/blog/2013/10/25/mod-python-the-long-story/
https://docs.python.org/2/howto/webservers.html
https://www.digitalocean.com/community/tutorials/a-comparison-of-web-servers-for-python-based-web-applications

wsgi tool
https://github.com/pallets/werkzeug

web server framework
https://en.wikipedia.org/wiki/List_of_application_servers#Python
https://en.wikipedia.org/wiki/Comparison_of_web_server_software
https://en.wikipedia.org/wiki/Comparison_of_web_frameworks#Python

unicorn
https://github.com/defunkt/unicorn
https://blog.github.com/2009-10-09-unicorn/

gunicorn
https://github.com/benoitc/gunicorn
http://docs.gunicorn.org/en/latest/design.html
https://docs.gunicorn.org/en/stable/faq.html

uwsgi

https://github.com/unbit/uwsgi

nginx openresty
http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass
http://nginx.org/
http://www.ituring.com.cn/article/504549
https://openresty.org/
https://w3techs.com/technologies/overview/web_server/all


server woker model
[python使用master worker管理模型开发服务端](http://xiaorui.cc/2015/07/13/python%E4%BD%BF%E7%94%A8master-worker%E7%AE%A1%E7%90%86%E6%A8%A1%E5%9E%8B%E5%BC%80%E5%8F%91%E6%9C%8D%E5%8A%A1%E7%AB%AF/)
[深入理解uwsgi和gunicorn网络模型[上]](http://xiaorui.cc/2017/02/16/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3uwsgi%E5%92%8Cgunicorn%E7%BD%91%E7%BB%9C%E6%A8%A1%E5%9E%8B%E4%B8%8A/)
[gunicorn设计 pre-fork模式](http://gunicorn.readthedocs.io/en/latest/design.html#pre-fork)


deployment
[阿里云部署 Flask + WSGI + Nginx 详解](http://www.cnblogs.com/Ray-liang/p/4173923.html?utm_source=tuicool&utm_medium=referral)
[部署Tornado](http://demo.pythoner.com/itt2zh/ch8.html)
[gunicorn配置](http://docs.gunicorn.org/en/stable/settings.html)


nginx
[Nginx开发从入门到精通](http://tengine.taobao.org/book/)
[agentzh 的 Nginx 教程](http://openresty.org/download/agentzh-nginx-tutorials-zhcn.html)
[OpenResty 最佳实践](https://moonbingbing.gitbooks.io/openresty-best-practices/content/)


extensive
[知乎-uWSGI 服务器的 uwsgi 协议究竟用在何处？](https://zhihu.com/question/46945479/answer/104066078)
[知乎-使用了Gunicorn或者uWSGI,为什么还需要Nginx？](https://www.zhihu.com/question/30560394)
https://www.zhihu.com/question/19761434
https://www.zhihu.com/question/38528616
http://ningning.today/2017/11/28/python/tornado-use-gevent-wsgi/
https://en.wikipedia.org/wiki/Web_service
