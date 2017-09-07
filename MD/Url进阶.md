# **1. Django处理请求**
1. 项目启动后根据setting中ROOT_URLCONF决定根的URLconf（当项目的名称更改后需要到setting文件中修改该值）
2. url文件中的urlpatterns是django.conf.url.url()实例的一个列表，用户请求时会根据列表中的url进行匹配
3. Djangp依次匹配每个url模式，和请求的url匹配时就停止匹配
4. 匹配成功后会调用url对应的视图（views）
5. 视图的参数：1.第一个参数是HttpRequest实例（request）；2. 如果匹配的正则表达式返回了没有命名的组，那么正则匹配的内容将作为位置参数提供给视图；3. 关键字参数由震泽匹配的命名组组成，但是可以被django.conf.url.url()的可选参数kwargs覆盖
6. 如果url和正则不匹配，或如果过程中抛出一个异常，Django将调用一个适当的错误处理视图

# **2. 多种url**
    from django.conf.urls import url
    from . import views
    
    urlpatterns = [
        url(r'^articles/2003/$', views.special_case_2003),
        url(r'^articles/([0-9]{4})/$', views.year_archive),
        url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
        url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
    ]
    
## **2.1 说明**
* 若要从URL中捕获一个值，只需要在它周围放置一堆圆括号
* 每个正则前面的‘r’是可选的，但是建议加上。它告诉python这个字符串是原始的，字符串中任何字符都不应该转义
* 默认捕捉到的都是字符串
* /articles/2005/03/ 请求将匹配列列表中的第三个模式。Django 将调用函数：views.month_archive(request, '2005', '03')
* /articles/2005/3/ 不不匹配任何URL 模式，因为列列表中的第三个模式要求?月份应该是两个数
字。

# **3. Url的多种组合写法**
    from django.conf.urls import url, include
    
    urlpatterns = [
    url(r'^community/', incloude('django_website.community.urls'))
    ]
    
# **4. 捕获参数的继承**
    # In settings/urls/main.py
    from django.conf.urls import include, url
    
    urlpatterns = [
        url(r'^(?P<username>\w+)/bolg', include('foo.urls.blog'))
    ]
    
    # In foo/urls/blog.py
    from django.conf.urls import url
    from . import views
    urlpatterns = [
        url(r'^$', views.bolg.index),
        url(r'^archive/$', views.blog.archive),
    ]

