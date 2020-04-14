# lmhtools
----------------------------------
commen tools


# lmhtools package
-------------------------------------

``` 
pip install lmh_tools
```

# Google
-------------------------------------
``` 
from lmhtools import Google
g = Google()

#传入列表
content = ['i love you','you love he','he love her']
g.to_cn(content)

#传入字符串
content = '我爱你中国'
g.to_en(content)

#智能翻译 速度慢
content = '我爱你中国 very more'
g.trans(content)
```

# Myname
-------------------------------------
```
from lmhtools import Myname
author = '刘蒙华'
p = Myname()

#获取姓名全称
p.qc(author)

#获取姓名简称
p.jc(author)

#处理wos作者
wos = Myname.wos()

#支持json/list
author = ["Sun, Y (Sun, Ya)", "Liu, Y (Liu, Ya)"]

#获取全称列表
wos.qc(author)

#获取简称列表
wos.jc(author)
```
