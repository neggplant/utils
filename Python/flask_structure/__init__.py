"""
在小型程序中使用简单结构公用一同模板以及静态文件
├── __init__.py
├── statics
│   └── code.png
├── templates
│   └── login.html
└── views
    ├── account.py
    ├── blog.py
    └── user.py


在稍大型程序中每个模块配置单独的模板以及静态文件
├── admin
│   ├── __init__.py
│   ├── static
│   ├── templates
│   └── views.py
├── __init__.py
└── web
    ├── __init__.py
    ├── static
    ├── templates
    └── views.py
"""