# encoding: utf-8
"""
@author: lmh
@software: PyCharm
@file: pyname.py
@time: 2020/4/14 15:29
"""
import numpy as np
import json,re
from  abc import ABCMeta,abstractmethod
from .data import ming,duoyinxing,fuxing

class NamePrototype(metaclass=ABCMeta):

    def strPreprocessing(self,x):
        tR = x
        reTrimall = re.compile('\A\s*|(?<=[\u4e00-\u9fa5])\s*(?=[\u4e00-\u9fa5])|\s*\Z')
        reWtoS = re.compile('\W')
        reSS = re.compile('\s{2,}')
        subtR = re.sub(reTrimall, '', tR)
        subtR = re.sub(reWtoS, ' ', subtR)
        subtR = re.sub(reSS, ' ', subtR)
        return subtR

    def ming(self,x):
        rStr = ''
        for i in x:
            if i in ming:
                rStr = rStr + ming[i]
            else:
                rStr = rStr + i
        return rStr

    def jxming(self,x):
        rStr = ''
        for i in x:
            if i in ming:
                rStr = rStr + ming[i][0]
            else:
                rStr = rStr + i
        return rStr

    @abstractmethod
    def qc(self,x):
        pass

    @abstractmethod
    def jc(self,x):
        pass

class Myname(NamePrototype):

    def qc(self,x):
        result = self.quancheng(x)
        if result:result = result.upper()
        return result

    def jc(self,x):
        result = self.jiancheng(x)
        if result:result = result.upper()
        return result

    def quancheng(self,x):
        if not (x and x == x):
            return None

        strP = self.strPreprocessing(x)

        if len(strP) == 1:
            if strP in ming:
                return ming[strP]
            else:
                return strP
        elif len(strP) == 2:
            if strP[0] in duoyinxing:
                strX = duoyinxing[strP[0]]
            elif strP[0] in ming:
                strX = ming[strP[0]]
            else:
                strX = strP

            if strP[1] in ming:
                return strX + ' ' + ming[strP[1]]
            else:
                return strX + strP[1]
        elif len(strP) >= 3:
            strI = ''
            if " " in strP:
                return self.ming(strP)
            else:
                if strP[:2] in fuxing:
                    strI = strI + fuxing[strP[:2]] + ' '
                    strP = strP[2:]
                    strI = strI + self.ming(strP)
                    return strI
                elif strP[:1] in duoyinxing:
                    strI = strI + duoyinxing[strP[:1]] + ' '
                    strP = strP[1:]
                    strI = strI + self.ming(strP)
                    return strI
                else:
                    if strP[:1] in ming:
                        strI = strI + ming[strP[:1]] + ' '
                    else:
                        strI = strI + strP[:1]
                    strP = strP[1:]
                    strI = strI + self.ming(strP)
                    return strI

    def jiancheng(self,x):
        if not (x and x == x):
            return None

        strP = self.strPreprocessing(x)

        if len(strP) == 1:
            if strP in ming:
                return ming[strP]
            else:
                return strP
        elif len(strP) == 2:
            if strP[0] in duoyinxing:
                strX = duoyinxing[strP[0]]
            elif strP[0] in ming:
                strX = ming[strP[0]]
            else:
                strX = strP

            if strP[1] in ming:
                return strX + ' ' + ming[strP[1]][0]
            else:
                return strX + strP[1]
        elif len(strP) >= 3:
            strI = ''
            if " " in strP:
                return self.jxming(strP)
            else:
                if strP[:2] in fuxing:
                    strI = strI + fuxing[strP[:2]] + ' '
                    strP = strP[2:]
                    strI = strI + self.jxming(strP)
                    return strI
                elif strP[:1] in duoyinxing:
                    strI = strI + duoyinxing[strP[:1]] + ' '
                    strP = strP[1:]
                    strI = strI + self.jxming(strP)
                    return strI
                else:
                    if strP[:1] in ming:
                        strI = strI + ming[strP[:1]] + ' '
                    else:
                        strI = strI + strP[:1]
                    strP = strP[1:]
                    strI = strI + self.jxming(strP)
                    return strI

    @staticmethod
    def wos():
        return WosAuthor()

class WosAuthor(NamePrototype):

    def qc(self,x):
        if not x: return np.nan
        if not isinstance(x, list): Author = json.loads(x)
        result = []
        for each_author in x:
            guize = re.compile('(?<=\().*?(?=\))')
            each_author = guize.findall(each_author)[0]
            each_author = re.sub('(?<=\w)+\W+', 'zkcy2020', each_author, 1)
            each_author = re.sub('\W+', '', each_author)
            each_author = re.sub('zkcy2020', ' ', each_author, 1).upper()
            result.append(each_author)
        return result

    def jc(self,x):
        if not x: return np.nan
        if not isinstance(x, list): Author = json.loads(x)
        result = []
        for each_author in x:
            guize = re.compile('^.*?(?=\()')
            each_author = guize.findall(each_author)[0]
            each_author = re.sub('(?<=\w)+\W+', 'zkcy2020', each_author, 1)
            each_author = re.sub('\W+', '', each_author, 1)
            each_author = re.sub('zkcy2020', ' ', each_author, 1).upper()
            result.append(each_author)
        return result


