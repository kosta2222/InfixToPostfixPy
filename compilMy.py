(define,set_)=range(2)
def op_prior(char_op:str):
    #if char_op=="(" or char_op==")":
        #return 1
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

def opn(code:list)->None: 
    p=0
    op_stack:list=[]
    res:list=[]
    while True: 
        v=code[p]
        p+=1
        #print("p",p)        
        #print('type(v)',type(v),v)
        if v==';':
            break 
        if type(v)==float:
            res.append(v)
        elif v not in ["*","/","%","+","-","(",")"]:
            res.append(v)
        elif v in ["*","/","%","+","-"]:
            token_tmp=""
            if len(op_stack)!=0:
                token_tmp=op_stack[len(op_stack)-1]
            if token_tmp!="":    
              while (len(op_stack)>0):
                 token_tmp=op_stack[len(op_stack)-1]
                 if token_tmp=='(':
                     break
                 if  op_prior(v)<=op_prior(token_tmp) :
                    res.append(op_stack.pop())        
            op_stack.append(v)
        elif v=='(':
           op_stack.append(v)
        elif v==')':
           token_tmp=op_stack[len(op_stack)-1]
           while (token_tmp!='('):
               res.append(op_stack.pop())
               token_tmp=op_stack[len(op_stack)-1]
               if  token_tmp=='(':
                 op_stack.pop()
               if len(op_stack)==0:
                   print("V virajenii propushena levaya skobka")
               
    while len(op_stack)>0 :
        token_tmp=op_stack[len(op_stack)-1]
        if token_tmp=="(":
            raise RuntimeError("V virajenii net pravoi skobki")
        res.append(op_stack.pop())
       
    return res         
        
def float_or_str(v:str):
                try:return float(v)
                except ValueError:
                 return str(v)
                         
def load_file(fName:str):
    f=open(fName)
    cont=f.read()
    f.close()
    return cont

def tokenze(code:str)->list:
    toks_nms_strs=code.split() 
    p=0
    while(p<len(toks_nms_strs)):
       toks_nms_strs[p]=float_or_str(toks_nms_strs[p])
       p+=1         
    return toks_nms_strs
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