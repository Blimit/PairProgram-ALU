import re
class Feature:
    def __init__(self,string,symbol):
        number,op = self.information(string)
        self.problem = string           #问题
        self.sym = self.turn(symbol)    #最后化简式
        self.num = '-'.join(number)     #操作数
        self.op = ''.join(op)           #操作符


    def information(self,string):
        number=[]
        op_list = []
        sym = string.replace("×", "*").replace(" ", "").replace("=", '').replace('÷', '/')

        # 生成操作数的数组：
        # 插入假分数
        data_list = re.findall(r"(\d+'\d+/\d+)", sym)
        sym = re.sub(r"(\d+'\d+/\d+)", ' ', sym)
        # 插入真分数
        data_list += re.findall(r"(\d+/\d+)", sym)
        sym = re.sub(r"(\d+/\d+)", ' ', sym)
        # 插入整数
        data_list += re.findall(r"(\d+)", sym)

        for x in data_list:
            if "'" in x:
                y = x.replace("'", '+')
                number.append(str(round(eval(y), 3)))
            else:
                number.append(str(round(eval(x), 3)))

        number.sort()
        #print(number)
        #生成操作符数组
        op = re.compile(r"[+\-*/]+")
        op_list = op.findall(sym)

        return number,op_list

    def turn(self,symbol):
        data_list ,op = self.information(symbol)
        return ' '.join(data_list+op)



