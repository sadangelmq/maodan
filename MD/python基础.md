#  **һ��Python ����**
### **1. �ֽ�����**
    >>>byt = b'hello word'
    >>> byt
    b'hello word'
    >>> type(byt)
    <class 'bytes'>
    >>> byt.decode('utf-8')
    'hello word'
    >>> type(byt.decode('utf-8'))
    <class 'str'>
    
### **2. �ַ�������ֵ֮���ת��**
    # ord�������Խ�һ���ַ���Ϊ����������ASCLL��Unicode����ֵ
    s = '��'
    >>> ord(s)
    24191
    # ��ord�������غ����ֵ���ض�Ӧ����ֵ���ַ�
    >>> chr(24191)
    '��'

### **3. ��ʽ���ַ���**
    >>>name = 'ë��'
    >>>print('�ҵ����ֽУ�%s' % name)
    �ҵ����ֽУ�ë��
    >>>print('�ҵ����ֽУ�{}'.format(name))
    �ҵ����ֽУ�ë��
    >>>'MAOQIU'.lower()
    'maoqiu'

### **4. �ֵ�**
    >>> mao = {'maoqiu':{'mao': 'qiu', 'age': 99, 'sex': '��'},'qiu':{'name':'maoqiu'}}
    >>> mao['maoqiu']
    {'age': 99, 'sex': '��', 'mao': 'qiu'}
    >>> mao['maoqiu'].get('age')
    99
    >>> for i in mao:
	print(i)
    # ѭ���������ֵ��Ϊstr
    maoqiu
    qiu
    >>> for i in mao:
	print(type(i))
    <class 'str'>
    <class 'str'>
    >>> mao.keys()
    dict_keys(['maoqiu', 'qiu'])
    # �����ֵ�
    >>> ss = {'name': 'guang', 'age': 7 }
    >>> for i in ss:
	print(ss.get(i))

	# �ṹ
    7
    guang
    # ʹ��items�������ֵ���б���
    >>> for k,v in ss.items():
	print(k, '--->', v)

	# ���
    age ---> 7
    name ---> guang
    
### **5. ����**
    >>> a = {'cat', 'dog'}
    >>> b = {'dog', 'pig'}
    >>> type(a)
    <class 'set'>
    # ����
    >>> a | b
    {'cat', 'dog', 'pig'}
    # ����
    >>> a & b
    {'dog'}
    
### **6. ����**
    >>> def hello(name, s='Mr.'):
	print('hello,', s, '{}'.format(name))
	>>> def hello(name, s='Mr.'):
	print('hello,', s+'{}'.format(name))
	>>> hello('maoqiu')
    hello, Mr. maoqiu
   
### **7. ��ļ̳У�super().__init__()**
    >>> class Peole():
	        MAX_AGE= 150
	        def __init__(self, name):
		        self.name = name
	        def eat(self, food):
		        print('Eating {}....'.format(food))

		
    >>> class Male(Peole):
	        def __init__(self, name):
		        super().__init__(name)
		        self.sex = 'Mail'
	        def make_money(self):
		        print('Making money...')

		
    >>> class Wujing(Male):
	        def __init__(self):
	    	    super().__init__('wujing')
	        def film(self):
	    	    print('{} is filming'.format(self.name))
	>>> wu = Wujing('maoqiu')
	>>> wu.eat('ma')
	Eating ma....
	# ��Wujing����ʹ�õ�film������ʹ�õ�self.name��Peole�е�self.name
	# ��ͨ��Wujing����super��ʼ������ʱ��ȡ��
	>>> wu.film()
	wujing is filming
	
### **8. ����ʹ��ʹ�õ����ⷽ��**
* __init__ : ʵ����ʱ��ʼ��ʵ��
* __str__  : ִ��print������ʱ��ʾ�����ݣ�������\<__main__.Class at 0x10623ab70\>Ĭ�ϵ���ʽ
* __len__  �� ִ��len������ʱ��ʾ�Ķ��󳤶�

#### **8.1 ����**
    >>> class Asd(Male):
	    def __init__(self):
		    super().__init__('ë��')
		# ʹ��str����Է������п��ӻ��Ĳ���
	    def __str__(self):
		    return '{} - ��ëһ������'.format(self.name)
	    def __len__(self):
		    return len(self.name)
		
    >>> mao = Asd()
    >>> print(mao)
    ë�� - ��ëһ������
    >>> len(mao)
    2
    >>>
### **9. �Զ����׳��쳣��Ϣ**
    >>> def hello(name):
	    if name != 'maoqiu':
		    raise NameError('�û�������maoqiu')
    # ִ�к����׳��쳣��Ϣ�� �û�������maoqiu
    >>> hello('mao')
    Traceback (most recent call last):
      File "<pyshell#121>", line 1, in <module>
        hello('mao')
      File "<pyshell#120>", line 3, in hello
        raise NameError('�û�������maoqiu')
    NameError: �û�������maoqiu
