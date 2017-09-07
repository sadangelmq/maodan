#  **一、Python 基础**
### **1. 字节数组**
    >>>byt = b'hello word'
    >>> byt
    b'hello word'
    >>> type(byt)
    <class 'bytes'>
    >>> byt.decode('utf-8')
    'hello word'
    >>> type(byt.decode('utf-8'))
    <class 'str'>
    
### **2. 字符集编码值之间的转换**
    # ord函数可以将一个字符作为参数，返回ASCLL或Unicode的数值
    s = '广'
    >>> ord(s)
    24191
    # 将ord函数返回后的数值返回对应该数值的字符
    >>> chr(24191)
    '广'

### **3. 格式化字符串**
    >>>name = '毛球'
    >>>print('我的名字叫：%s' % name)
    我的名字叫：毛球
    >>>print('我的名字叫：{}'.format(name))
    我的名字叫：毛球
    >>>'MAOQIU'.lower()
    'maoqiu'

### **4. 字典**
    >>> mao = {'maoqiu':{'mao': 'qiu', 'age': 99, 'sex': '男'},'qiu':{'name':'maoqiu'}}
    >>> mao['maoqiu']
    {'age': 99, 'sex': '男', 'mao': 'qiu'}
    >>> mao['maoqiu'].get('age')
    99
    >>> for i in mao:
	print(i)
    # 循环后两个字典变为str
    maoqiu
    qiu
    >>> for i in mao:
	print(type(i))
    <class 'str'>
    <class 'str'>
    >>> mao.keys()
    dict_keys(['maoqiu', 'qiu'])
    # 遍历字典
    >>> ss = {'name': 'guang', 'age': 7 }
    >>> for i in ss:
	print(ss.get(i))

	# 结构
    7
    guang
    # 使用items函数对字典进行遍历
    >>> for k,v in ss.items():
	print(k, '--->', v)

	# 结果
    age ---> 7
    name ---> guang
    
### **5. 集合**
    >>> a = {'cat', 'dog'}
    >>> b = {'dog', 'pig'}
    >>> type(a)
    <class 'set'>
    # 并集
    >>> a | b
    {'cat', 'dog', 'pig'}
    # 交集
    >>> a & b
    {'dog'}
    
### **6. 函数**
    >>> def hello(name, s='Mr.'):
	print('hello,', s, '{}'.format(name))
	>>> def hello(name, s='Mr.'):
	print('hello,', s+'{}'.format(name))
	>>> hello('maoqiu')
    hello, Mr. maoqiu
   
### **7. 类的继承：super().__init__()**
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
	# 在Wujing类中使用的film函数中使用的self.name是Peole中的self.name
	# 是通过Wujing类中super初始化参数时获取的
	>>> wu.film()
	wujing is filming
	
### **8. 类中使用使用的特殊方法**
* __init__ : 实例化时初始化实例
* __str__  : 执行print（对象）时显示的内容，而不是\<__main__.Class at 0x10623ab70\>默认的形式
* __len__  ： 执行len（对象）时显示的对象长度

#### **8.1 样例**
    >>> class Asd(Male):
	    def __init__(self):
		    super().__init__('毛球')
		# 使用str后可以返回类中可视化的参数
	    def __str__(self):
		    return '{} - 想毛一样的球'.format(self.name)
	    def __len__(self):
		    return len(self.name)
		
    >>> mao = Asd()
    >>> print(mao)
    毛球 - 想毛一样的球
    >>> len(mao)
    2
    >>>
### **9. 自定义抛出异常信息**
    >>> def hello(name):
	    if name != 'maoqiu':
		    raise NameError('用户名不是maoqiu')
    # 执行函后抛出异常信息： 用户名不是maoqiu
    >>> hello('mao')
    Traceback (most recent call last):
      File "<pyshell#121>", line 1, in <module>
        hello('mao')
      File "<pyshell#120>", line 3, in hello
        raise NameError('用户名不是maoqiu')
    NameError: 用户名不是maoqiu
