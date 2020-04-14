# encoding: utf-8
"""
@author: lmh
@software: PyCharm
@file: google.py
@time: 2020/4/14 9:58
"""
import re,execjs,requests
from concurrent.futures import ThreadPoolExecutor

googlejs = """
            function TL(a) {
            var k = "";
            var b = 406644;
            var b1 = 3293161072;

            var jd = ".";
            var $b = "+-a^+6";
            var Zb = "+-3^+b+-f";

            for (var e = [], f = 0, g = 0; g < a.length; g++) {
                var m = a.charCodeAt(g);
                128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
                e[f++] = m >> 18 | 240,
                e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
                e[f++] = m >> 6 & 63 | 128),
                e[f++] = m & 63 | 128)
            }
            a = b;
            for (f = 0; f < e.length; f++) a += e[f],
            a = RL(a, $b);
            a = RL(a, Zb);
            a ^= b1 || 0;
            0 > a && (a = (a & 2147483647) + 2147483648);
            a %= 1E6;
            return a.toString() + jd + (a ^ b)
        };

        function RL(a, b) {
            var t = "a";
            var Yb = "+";
            for (var c = 0; c < b.length - 2; c += 3) {
                var d = b.charAt(c + 2),
                d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
                d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
                a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
            }
            return a
        }
        """


class Google():
    def __init__(self):
        self.ctx = execjs.compile(googlejs)
        self .s = self.__s()
    def __max(self,text):
        if len(text) > 4891: return text[0:4850] + '(...)'
        return text

    def __s(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        }
        s = requests.session()

        s.headers.update(headers)
        s.keep_alive = False
        s.get(url='https://translate.google.cn/')
        return s

    def __split(self,content):
        '''分割任务'''
        if not content:return content
        if isinstance(content,str):return self.__max(content)
        elif isinstance(content,list):
            length = 0;result = [];temp=''
            for each in content:
                text = self.__max(each)
                length += len(text) +len("\n\n\n\n\n")
                if length > 4891:#4891
                    result.append(temp)
                    length,temp = len(text),text
                else:
                    if temp:temp +="\n\n\n\n\n"
                    temp += text
            if temp:result.append(temp)
            return result
    def __result(self,result):
        result = result.json()
        content = ''
        for each in result[0]:
            if not each[0]:break
            content += each[0]
        return content

    def __thread(self,content,url):
        task_list  =  []
        result = []
        with ThreadPoolExecutor(32) as pool:
            for each in content:
                tk = self.ctx.call("TL", each)
                param = {'tk': tk, 'q': each}
                task_list.append(pool.submit(self.s.get,**{'url':url,'params':param}))
            for g in task_list:
                temp = self.__result(g.result())
                result.extend(temp.split("\n\n\n\n\n"))
        return result

    def __url(self,name):
        url = """https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=t&otf=1&ssel=0&tsel=0&kc=1"""
        if name == 'cn':
            url = """https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=0&tsel=0&kc=1"""
        return url

    def __trans(self,content,name):
        content = self.__split(content)
        url = self.__url(name)
        if isinstance(content,list):return self.__thread(content,url)
        else:
            tk = self.ctx.call("TL", content)
            param = {'tk': tk, 'q': content}
            result = self.s.get(url=url,params=param)
            return self.__result(result)
    def to_en(self,content):
        return  self.__trans(content,'en')


    def to_cn(self,content):
        return  self.__trans(content,'cn')


    def trans(self,content):
        if not content:return content
        if isinstance(content,list):check = content[0]
        else:check = content
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        match = zhPattern.search(check)
        if match:return self.to_en(content)
        else:return self.to_cn(content)