#-*- coding: utf-8 -*-
import re
def op_prior(char_op:str):
    if char_op=="^":
        return 6
    elif char_op=="*":
        return 5
    elif char_op=="/":
        return 5
    elif char_op=="%":
        return 3
    elif char_op=="+":
        return 2
    elif char_op=="-":
        return 2
    
def isOp(c:str)->bool:
    if c=="-" or c=="+" or c=="*" or c=="/" or c=="^":return True
    return False
    
#DOES NOT WORK
def opn(code:str)->None: 
    p=0
    op_stack:list=[]
    res:list=[]
    while True: 
        v=code[p]
        p+=1
        if v==';':
            break 
        if re.match("[0-9]+[.]*[0-9]*",v) or re.match("[A-Z]+[a-z]+",v):
            res.append(v)
        elif isOp(v):#i -бинарная операция
            token_tmp=''#смотрим на вверх стека
            
            if len(op_stack)>0:
                token_tmp=op_stack[len(op_stack)-1]#смотрим на вверх стека
                while(len(op_stack)>0 and isOp(token_tmp)):#пока стек >0
                    if (op_prior(v)<=op_prior(token_tmp)):#сравнием приоритет токена в строке и приоритет операци  в стеке операций
                        res.append(op_stack.pop())#если в стеке операция выше,то выталкиваем его в выходную строку
                    else:#bиначе выходим из данного цикла
                        break     
            op_stack.append(v)#тогда выйдя из цикла,добавим операцию в стек        
        elif v=='(':
           op_stack.append(v)
        elif v==')':#закрывающая )
            token_tmp=op_stack[len(op_stack)-1]#смотрим на вверх стека
            while (token_tmp!='(' or len(op_stack)>1):
                    res.append(op_stack.pop())
                    token_tmp=op_stack[len(op_stack)-1]
                    if token_tmp=='(':
                       op_stack.pop()                                  
                    if (len(op_stack)==0):
                        raise RuntimeError("No left paren")                                                          
               
    while len(op_stack)>0 :
        token_tmp=op_stack[len(op_stack)-1]
        if token_tmp=="(":
            raise RuntimeError("No right paren")
        res.append(op_stack.pop())
       
    return res         
        
                         
def load_file(fName:str):
    f=open(fName)
    cont=f.read()
    f.close()
    return cont

def tokenze(code:str)->list:
    return code.split() 
#main interpriter    
def parse(code:list)->None:
    tp=0
    while tp<len(code):
        if code[tp]=='define':
            tp+=1
            while code[tp]!=';':
                v=code[tp]                 
                if type(v)==float:
                    print('dconst',v)
                elif type(v)==str:
                    print('dstore',ord(v))
                tp+=1
        elif code[tp]=='set!':
          tp+=1
          while code[tp]!=';':
             pass             
        tp+=1        

f="code.txt"
#parse(tokenze(load_file(f)))