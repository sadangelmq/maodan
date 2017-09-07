# **1. Django��������**
1. ��Ŀ���������setting��ROOT_URLCONF��������URLconf������Ŀ�����Ƹ��ĺ���Ҫ��setting�ļ����޸ĸ�ֵ��
2. url�ļ��е�urlpatterns��django.conf.url.url()ʵ����һ���б��û�����ʱ������б��е�url����ƥ��
3. Djangp����ƥ��ÿ��urlģʽ���������urlƥ��ʱ��ֹͣƥ��
4. ƥ��ɹ�������url��Ӧ����ͼ��views��
5. ��ͼ�Ĳ�����1.��һ��������HttpRequestʵ����request����2. ���ƥ���������ʽ������û���������飬��ô����ƥ������ݽ���Ϊλ�ò����ṩ����ͼ��3. �ؼ��ֲ���������ƥ�����������ɣ����ǿ��Ա�django.conf.url.url()�Ŀ�ѡ����kwargs����
6. ���url������ƥ�䣬������������׳�һ���쳣��Django������һ���ʵ��Ĵ�������ͼ

# **2. ����url**
    from django.conf.urls import url
    from . import views
    
    urlpatterns = [
        url(r'^articles/2003/$', views.special_case_2003),
        url(r'^articles/([0-9]{4})/$', views.year_archive),
        url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
        url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
    ]
    
## **2.1 ˵��**
* ��Ҫ��URL�в���һ��ֵ��ֻ��Ҫ������Χ����һ��Բ����
* ÿ������ǰ��ġ�r���ǿ�ѡ�ģ����ǽ�����ϡ�������python����ַ�����ԭʼ�ģ��ַ������κ��ַ�����Ӧ��ת��
* Ĭ�ϲ�׽���Ķ����ַ���
* /articles/2005/03/ ����ƥ�����б��еĵ�����ģʽ��Django �����ú�����views.month_archive(request, '2005', '03')
* /articles/2005/3/ ����ƥ���κ�URL ģʽ����Ϊ���б��еĵ�����ģʽҪ��?�·�Ӧ����������
�֡�

# **3. Url�Ķ������д��**
    from django.conf.urls import url, include
    
    urlpatterns = [
    url(r'^community/', incloude('django_website.community.urls'))
    ]
    
# **4. ��������ļ̳�**
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

