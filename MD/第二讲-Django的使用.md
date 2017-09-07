#  **����Django��ʹ��**
### **1. �½���Ŀ**
    # pip��װDjango
    $ pip install django
    # �鿴Dgango�İ汾��
    $ python3 -c "import django; print(django.get_version())"
    # �����������½���Ŀ
    $ django-admin startproject ��Ŀ����
    # �����������½�apps
    $ python manage.py startapp app����
    # ���½�app��Ҫ��app���õ�setting�ļ��е�INSTALL_APP�б���
    # ���ø�ʽ���磺
    # PollsConfig:Ӧ�õ�����ĸ��дConfig�̶���ʽ
    'polls.apps.PollsConfig'
    # �鿴manage���÷�
    $ python manage.py
    
### **2. ������Ŀ**
    # ���Ӷ˿ں�������ַʱĬ����127.0.0.1�˿���8000
    python manage.py runserver $host:$prot
    
### **Django���ļ���˵��**
 * urls: ���û�����ҳ��������������ڸ��ļ���ͨ������ȥƥ��������ƥ��ɹ�����ö�Ӧ�ĺ�������
 * views�� ��ͼ��������urls��
 * models�� ���ݿ��ṹ��һ�������һ�ű�ÿ�������Ǳ��е��ֶΣ�ÿ������Ĭ�ϵ�������id�ţ�Ĭ�ϻᴴ��
 * setting�� django�������ļ�
 * test: ��Ԫ�����ļ�
 * 


#  **3. ���ݿ�**
    # ��models�д��������ݿ��ṹ��ʼ����ṹ���������ݿ���
    # ��һ��������Ǩ�Ƽ�¼
    $ python manage.py makemigrations
    # �鿴Ҫ������ṹ��sql���
    # polls�Ƕ�Ӧmodel��app����
    $ python manage.py sqlmigrate polls 0001_initial
    # Ӧ�õ����ݿ�
    $ python manage.py migrate

#  **4. ͨ��manage shell �鿴���ݿ�����**
    # ����manage shell
    $ python manage.py shell
    # ����model�е���
    from django.utils import timezone
    from polls.models import Question, Choice
    # ʵ������
    # ��������ʱ����Ҫʵ�����࣬��ò������䱣��Ͳ��뵽���ݿ����ˣ�����Ҫ��дsql���
    # ʵ�����ࣨ�ֶ���=�������ݡ���
    q = Question(question_text="whit's ne2w", pub_date=timezone.now())
    # �����ݱ��浽���ݿ���
    q.save()
    # ��ѯ����
    q.id;q.pk;q.question_text;q.pub_time;
    # ��ѯ��������
    Question.objects.all()
    Question.objects.filter(question_text="What's up?")
    Question.objects.get(id=1)
    
## **4.1 �����ݿ�����������**
    from django.utils import timezone
    from polls.models import Question, Choice
    # ֱ�ӽ����ݱ��浽���ݿ���
    # ����һ
    q = Question.objects.create(question_text='mao', pub_date=timezone.now())
    # ������
    # �ֶ���=�����������ݡ�
    q = Question(question_text='mao', pub_date=timezone.now())
    q.save()
    
## **4.2 �����ݿ��в鿴����**
    from django.utils import timezone
    from polls.models import Question, Choice
    # ��ѯ�������ݣ����ص���һ���б�
    Question.objects.all() 
    # ͨ�����˲�ѯ����
    # filter�������������
    Question.objects.filter(question_text='mao')
    # ͨ��get��ȡ��get���صĽ��ֻ��һ��������Ƕ������û�н�����ᱨ��
    # ���ɾ������¼����ô�����������ã�����ԭ�л���������
    Question.objects.get(id=1)
    
## **4.3 �����ݿ��и�������**
    from django.utils import timezone
    from polls.models import Question, Choice
    # ����һ
    # ʹ��get���ҳ���Ҫ���µ��ֶ�
    # ָ���ֶ����Ƹ����ֶ����ݣ�ʹ��save��������
    q = Question.objects.get(id=7)
    q.question_text="maodan"
    q.save()
    # ������
    # ͨ��filter�������������ҳ���Ҫ���µ��ֶΣ���ʹ��update���ֶ���Ϊ�������¸��ֶ�����
    Question.objects.filter(id=7).update(question_text="maodan")
    
## **4.4 �����ݿ���ɾ������**
    from django.utils import timezone
    from polls.models import Question, Choice
    # ����һ
    # ʹ��get���ҳ�Ҫɾ�������ݣ�ʹ��deleteɾ������
    q = Question.objects.get(id=7)
    q.delete()
    # ������
    # ��������ɾ������
    Question.objects.filter(id=7).delete()
    # ������ݿ��
    Question.objects.all().delete()
    
# **5. ����URL��ַ**
    from django.shortcuts import reverse
    # detail �Ƕ���url��name��ֵ
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
    reverse('detail', kwargs={'question_id': '1'})
    
    