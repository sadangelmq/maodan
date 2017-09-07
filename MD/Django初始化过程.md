初始化过程?

应用是如何载入的?

当Django 启动时，django.setup() 负责填充应用注册表。

setup()[source]?
配置Django：

加载设置。
设置日志。
初始化应用注册表。
自动调用此函数︰

当运行一个通过Django 的WSGI 支持 的HTTP 服务器。
当调用管理命令。
在其他情况下它必须显式调用，例如在普通的 Python 脚本中。

应用注册表初始化分三个阶段。在每个阶段，Django 以INSTALLED_APPS 中的顺序处理所有应用。

首先，Django 会导入INSTALLED_APPS中的所有应用。

如果它是一个应用配置类，Django 导入应用的根包，通过其name 属性。如果它是一个Python 包，Django 创建应用的一个默认配置。

在这个阶段，你的代码不应该将任何模型导入！

换句话说，你的应用程序的根包和定义应用配置类的模块不应该导入任何模型，即使是间接导入。

严格地讲，Django 允许应用配置加载后导入模型。然而，为了避免INSTALLED_APPS 的顺序带来不必要的约束，强烈推荐在这一阶段不导入任何模型。

这一阶段完成后，操作应用配置的API 开始变得可用，例如get_app_config()。

然后Django 试图导入每个应用的models 子模块，如果有的话。

你必须在应用的models.py 或models/__init__.py 中定义或导入所有模型。否则，应用注册表在此时可能不会完全填充，这可能导致ORM 出现故障。

一旦完成该步骤,  get_model() 之类的 model API 可以使用了.

最后，Django 运行每个应用程序配置的ready() 方法。

故障排除?

下面是一些在你初始化的时候可能经常碰到的问题:

AppRegistryNotReady发生这种情况是当导入应用的配置或模型模块时触发取决于应用注册表的代码。

例如，ugettext() 使用应用注册表来查找应用中的翻译目录。若要在导入时翻译，你需要ugettext_lazy()。（使用ugettext() 将是一个bug，因为翻译会发生在导入的时候，而不是取决于每个请求的语言。）

模型模块中在导入时使用ORM 执行数据库查询也会引发此异常。ORM 直到所有的模型都可用才能正常运转。

另一个常见的罪魁祸首，是django.contrib.auth.get_user_model()。请在导入时使用AUTH_USER_MODEL 设置来引用用户模型。

如果在一个独立的 Python 脚本中你忘了调用django.setup()，也会发生此异常。

ImportError： 不能 导入 名称 ...如果导入出现循环，则会发生这种情况。

要消除这种问题，应尽量减少模型模块之间的依赖项，并在导入时尽可能少做工作。为了避免在导入时执行代码，你可以移动它到一个函数和缓存其结果。当你第一次需要其结果时，将执行该代码。这一概念被称为"惰性求值"。

django.contrib.admin 在安装的应用中自动发现admin。要阻止它，请更改你的INSTALLED_APPS 以包含 'django.contrib.admin.apps.SimpleAdminConfig' 而不是 'django.contrib.admin'。