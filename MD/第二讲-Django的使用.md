#  **二、Django的使用**
### **1. 新建项目**
    # pip安装Django
    $ pip install django
    # 查看Dgango的版本号
    $ python3 -c "import django; print(django.get_version())"
    # 在命令行中新建项目
    $ django-admin startproject 项目名称
    # 在命令行中新建apps
    $ python manage.py startapp app名称
    # 在新建app后要将app配置到setting文件中的INSTALL_APP列表中
    # 配置格式例如：
    # PollsConfig:应用的首字母大写Config固定格式
    'polls.apps.PollsConfig'
    # 查看manage的用法
    $ python manage.py
    
### **2. 运行项目**
    # 不加端口和主机地址时默认是127.0.0.1端口是8000
    python manage.py runserver $host:$prot
    
### **Django中文件的说明**
 * urls: 在用户在网页中输入的域名，在该文件中通过正则去匹配域名，匹配成功后调用对应的函数对象
 * views： 视图函数，和urls绑定
 * models： 数据库表结构，一个类就是一张表，每个属性是表中的字段，每个表中默认的主键是id号，默认会创建
 * setting： django的配置文件
 * test: 单元测试文件
 * 


#  **3. 数据库**
    # 在models中创建好数据库表结构后开始将表结构创建到数据库中
    # 第一步先生成迁移记录
    $ python manage.py makemigrations
    # 查看要创建表结构的sql语句
    # polls是对应model的app名称
    $ python manage.py sqlmigrate polls 0001_initial
    # 应用到数据库
    $ python manage.py migrate

#  **4. 通过manage shell 查看数据库数据**
    # 进入manage shell
    $ python manage.py shell
    # 导入model中的类
    from django.utils import timezone
    from polls.models import Question, Choice
    # 实例化类
    # 插入数据时，需要实例化类，填好参数后将其保存就插入到数据库中了，不需要在写sql语句
    # 实例化类（字段名=‘新数据’）
    q = Question(question_text="whit's ne2w", pub_date=timezone.now())
    # 将数据保存到数据库中
    q.save()
    # 查询数据
    q.id;q.pk;q.question_text;q.pub_time;
    # 查询所有数据
    Question.objects.all()
    Question.objects.filter(question_text="What's up?")
    Question.objects.get(id=1)
    
## **4.1 在数据库中新增数据**
    from django.utils import timezone
    from polls.models import Question, Choice
    # 直接将数据保存到数据库中
    # 方法一
    q = Question.objects.create(question_text='mao', pub_date=timezone.now())
    # 方法二
    # 字段名=‘新增的数据’
    q = Question(question_text='mao', pub_date=timezone.now())
    q.save()
    
## **4.2 在数据库中查看数据**
    from django.utils import timezone
    from polls.models import Question, Choice
    # 查询所有内容，返回的是一个列表
    Question.objects.all() 
    # 通过过滤查询数据
    # filter后面跟的是条件
    Question.objects.filter(question_text='mao')
    # 通过get获取，get返回的结果只有一个，如果是多个或是没有结果都会报错
    # 如果删除过记录，那么主键不会重置，会在原有基础上增加
    Question.objects.get(id=1)
    
## **4.3 在数据库中更新数据**
    from django.utils import timezone
    from polls.models import Question, Choice
    # 方法一
    # 使用get查找出需要更新的字段
    # 指定字段名称更新字段内容，使用save保存数据
    q = Question.objects.get(id=7)
    q.question_text="maodan"
    q.save()
    # 方法二
    # 通过filter过滤条件，查找出需要更新的字段，再使用update将字段作为参数更新该字段内容
    Question.objects.filter(id=7).update(question_text="maodan")
    
## **4.4 在数据库中删除数据**
    from django.utils import timezone
    from polls.models import Question, Choice
    # 方法一
    # 使用get查找出要删除的内容，使用delete删除内容
    q = Question.objects.get(id=7)
    q.delete()
    # 方法二
    # 根据条件删除内容
    Question.objects.filter(id=7).delete()
    # 清空数据库表
    Question.objects.all().delete()
    
# **5. 反解URL地址**
    from django.shortcuts import reverse
    # detail 是定义url是name的值
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
    reverse('detail', kwargs={'question_id': '1'})
    
    