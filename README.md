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