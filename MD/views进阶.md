    #永久重定向
    permante=True
    
# **1.vuews中的装饰器**
* require_http_methods(request_method_list)
* require_GET()
* require_POST()
* require_safe()
* gzip_page()
* cache_control(**kwargs)： This decorator patches the response’s Cache-Control header
* never_cache()
* login_required()
* transaction.atomic


# 2. 查看request对象

- Django:  [request对象-1.10] (https://docs.djangoproject.com/en/1.10/ref/request-response/)
- Django:[request对象-1.11] (https://docs.djangoproject.com/en/1.11/ref/request-response/)