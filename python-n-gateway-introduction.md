<!--# CGI, FastCGI, WSGI, Web Server, proxy_pass，uwsgi，uWSGI-->


# 网关接口

## CGI / Common Gateway Interface
> 通用网关接口是一种重要的互联网技术，可以让一个客户端，从网页浏览器向执行在网络服务器上的程序请求数据。CGI描述了服务器和请求处理程序之间传输数据的一种标准。

## SCGI / Simple Common Gateway Interface
> 快速通用网关接口是一种让交互程序与Web服务器通信的协议。FastCGI是早期通用网关接口（CGI）的增强版本。
FastCGI致力于减少网页服务器与CGI程序之间交互的开销，从而使服务器可以同时处理更多的网页请求。

## FastCGI / Fast Common Gateway Interface
> 快速通用网关接口是一种让交互程序与Web服务器通信的协议。FastCGI是早期通用网关接口（CGI）的增强版本。
FastCGI致力于减少网页服务器与CGI程序之间交互的开销，从而使服务器可以同时处理更多的网页请求。

## WSGI / Web Server Gateway Interface
> Web服务器网关接口是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。

## uwsgi


# Web Server
网页服务器，通常有两种解释，一种是指服务器软件，另一种是指专门用于运行提供网络服务的软件的硬件（俗称电脑，其与一般的 PC 最大不同在于：1）一般不使用图形界面操作；2）只运行提供网络服务的相关软件；3）强调稳定性和可靠性；4）对环境要求高，例如温湿度、网络、供电、维护和监控等）。这里我们只讨论服务器软件。

## Nginx

## Apache

## 其他
### Tengine

### IIS

### Google Web Server

### lighttpd

典型的有 [Apache HTTP服务器](https://zh.wikipedia.org/wiki/Apache_HTTP_Server)(apache 2.x的版本也叫[httpd](https://github.com/apache/httpd)), [lighttpd](https://zh.wikipedia.org/wiki/Lighttpd), Nginx

# Application Server / WSGI Servers
应用服务器, 一般用在反向代理，也可以作为http服务器, 不过一般不会这么做.
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
https://uwsgi-docs.readthedocs.io/en/latest/Protocol.html

wsgi
pep：https://www.python.org/dev/peps/
https://www.python.org/dev/peps/pep-3333/
https://www.python.org/dev/peps/pep-0333/
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
http://nginx.org/en/docs/http/ngx_http_uwsgi_module.html
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
