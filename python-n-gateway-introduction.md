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

## Tengine

## IIS

## Google Web Server

## lighttpd

典型的有 [Apache HTTP服务器](https://zh.wikipedia.org/wiki/Apache_HTTP_Server)(apache 2.x的版本也叫[httpd](https://github.com/apache/httpd)), [lighttpd](https://zh.wikipedia.org/wiki/Lighttpd), Nginx
> 网页服务器（Web server）一词有两个意思：
一台负责提供网页的电脑，主要是各种编程语言构建而成，通过HTTP协议传给客户端（一般是指网页浏览器）。
一个提供网页的服务器程序。
每一台网页服务器（第1个意思）会运行最少一个网页服务器程序（第2个意思）。作为第1个意思，大陆地区称为网站服务器。此外，也通称作Web服务器。

为什么gunicorn前面还要nginx
> - Nginx更安全Nginx能更好地处理静态资源（通过一些http request header）
- Nginx也可以缓存一些动态内容
- Nginx可以更好地配合CDN
- ginx可以进行多台机器的负载均衡
- 不需要在wsgi server那边处理keep alive
- 让Nginx来处理slow client还有一个更隐蔽的区别是，像uWSGI支持的是wsgi协议，Nginx支持的是http协议，它们之间是有区别的。

# Application Server
应用服务器, 一般用在反向代理，也可以作为http服务器, 不过一般不会这么做.
## Gunicorn

## uWSGI

## Tornado

# Web FrameWork
Web 框架
## Django

## Tornado

## Flask

# 部署
## 反向代理

## woker model

## Docker

## supervisor

# FAQ
## 反向代理


WSGI 对server和application都有要求, 除了实现server和application, 还要实现中间件
> WSGI有两方：“服务器”或“网关”一方，以及“应用程序”或“应用框架”一方。服务方调用应用方，提供环境信息，以及一个回调函数（提供给应用程序用来将消息头传递给服务器方），并接收Web内容作为返回值。

> 所谓的 WSGI中间件同时实现了API的两方，因此可以在WSGI服务和WSGI应用之间起调解作用：从WSGI服务器的角度来说，中间件扮演应用程序，而从应用程序的角度来说，中间件扮演服务器。 “中间件”组件可以执行以下功能：
- 重写环境变量后，根据目标URL，将请求消息路由到不同的应用对象。
- 允许在一个进程中同时运行多个应用程序或应用框架。
- 负载均衡和远程处理，通过在网络上转发请求和响应消息。
- 进行内容后处理，例如应用XSLT样式表。
- 管理web app的进程应该也算是一个, 我猜


WSGI HTTP Server / 软件 (一种应用服务器, 实现了WSGI协议)
是Web Server的一种, 实现了WSGI, HTTP, 类CGI(想不到合适命名)等协议, 管理着Web app.

proxy_pass / 反向代理
通常情况下使用Nginx部署Python应用的方式有FastcCGI和HTTP两种, HTTP


uwsgi与uWSGI / uwsgi是一种协议, 可以理解为和CGI, FastCGI是平级的, uWSGI则是一个应用服务器

Gunicorn 也是一个应用服务器, 从Ruby上一个叫unicorn的移植过来的

protocol
https://en.wikipedia.org/wiki/Common_Gateway_Interface
https://en.wikipedia.org/wiki/FastCGI
https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface
https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

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
https://uwsgi-docs.readthedocs.io/en/latest/Protocol.html
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
