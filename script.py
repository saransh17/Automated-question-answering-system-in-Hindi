from __future__ import print_function
import subprocess as sp
import re
import sys
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate


out = []
key = []
count = ''
dest = ''
src = ''
dtime = ''
atime = ''
tnum = ''
places = ['अहमदाबाद','कालका','पुने','दिल्ली','आगरा','गोआ','जयपुर','कानपुर','सूरत']
typeq = ['कितनी',1,'कब',2,'कहा',3,'कौनसी',4]
typet = ['एक्सप्रेस','शताब्दी','एक्सप्रेस','दुरोंतो']
def hindi_transliterate(data):
    text = transliterate(data,sanscript.ITRANS,sanscript.DEVANAGARI)
    out.append(text)
    out.append(" ")
    return

def eng():
    
    inp = str(input("अपना प्रश्न दर्ज करें : "))
    #inp = re.sub(r'[^\w\s]','',inp)
    arr = inp.split()

    for i in arr:
        if i.isdigit():
            text=i
        elif ':' in i:
            text=i
        else:
            text=transliterate(i,sanscript.ITRANS,sanscript.DEVANAGARI)
        out.append(text)
        out.append(" ")

    str1 = ''.join(out)
    with open('temp.txt', 'a') as f:
        f.truncate(0)
        print(str1,file=f)
    #print(key)
    #print(str2)    
    return

def hindi():
    #key[:] = []
    str2 = []
    inp = str(input("अपना प्रश्न दर्ज करें : "))
    #inp = re.sub(r'[^\w\s]','',inp)
    arr = inp.split()

    for i in arr:
        str2.append(i)
        str2.append(" ")

    str1 = ''.join(str2)
    with open('temp.txt', 'a') as f:
        f.truncate(0)
        print(str1,file=f)

    #print(key)
    #print(str2)

    return

def extract():
    global dest,src,tnum,dtime,atime,count
    with open('temp.txt','r') as f:
        key = f.readline()
    # for i in key:
        # print(i)
    key = key.split(' ')
    for i in range(0,len(key)):
        if key[i].isdigit():
            tnum=key[i]
    
    for i in range(0,len(key)):
        if key[i] in ['को','तक']: 
            dest=key[i-1]
            
    
    for i in range(0,len(key)):
        if key[i]=='से':
            src=key[i-1]
    
    for i in range(0,len(key)):
        if ':' in key[i]:
            if key[i-1] in ['से']:
                dtime=key[i]
            elif key[i+1] in ['निकलेगी','चलेगी','चलती','निकलती']:
                dtime=key[i]
            else:
                atime=key[i]
    for i in range(0,len(key)):
            if key[i]=='कहा':
                if key[i+1]=='से':
                    src='X'
                else:
                    dest='X'
            elif key[i]=='कब':
                if key[i-1]=='से':
                    dtime='X'
                else:
                    atime='X'
            elif key[i]=='कौनसी':
                tnum=X
            elif key[i]=='कितनी':
                count = 'X'


            typeq = ['कितनी',1,'कब',2,'कहा',3,'कौनसी',4]
    '''print(tnum)
    print(src)
    print(dest)
    print(dtime)
    print(atime)
    print(count)'''


def execute():
    global dtime,atime,src,dest,tnum,count
    #print("गाड़ी संख्या","स्रोत स्टेशन",sep="\t",end=' ')
    #print("लक्ष्य स्रोत","प्रस्थान समय",sep="\t",end='	')
    #print("पोहोचने का समय")
    qlist = [tnum,src,dest,dtime,atime]
    qcop = [tnum,src,dest,dtime,atime]
    templ = ["गाड़ी संख्या","स्रोत स्टेशन","लक्ष्य स्रोत","प्रस्थान समय","पोहोचने का समय"]
    print(templ)
    #print(qlist)
    with open('data_ff.txt','r') as f:
        x=f.readlines()
    data=[]
    for i in x:
    #i = re.sub(r'[^\w\s]','',i)
        arr = i.split()
        data.append(arr)

    #print(data)
    num=0
    fir=0
    sr=''
    for i in range(0,len(qlist)):
        if qlist[i]:
            if qlist[i] not in ['X']:
                num+=1
                if fir==0:
                    sr=qlist[i]
                    qlist[i]=""
                    fir=1
    
    #print(num)
    #print(sr)
    with open('res.txt','w') as f:
        for sublist in x:
            if sr in sublist:
                f.write(sublist)

    for y in range(1,num):
        fir=0
        for i in range(0,len(qlist)):
            if qlist[i]:
                if qlist[i] not in ['X']:
                    if fir==0:
                        sr=qlist[i]
                        qlist[i]=""
                        fir=1
        with open('res.txt','r') as f:
            x=f.readlines()
        data[:]=[]
        for i in x:
            arr = i.split()
            data.append(arr)
        with open('res.txt','w') as f:
            for sublist in x:
                if sr in sublist:
                    f.write(sublist)
    
    #print(qlist)
    num_lines = sum(1 for line in open('res.txt'))
    #print(num_lines)
    with open('res.txt','r') as f:
        x=f.readlines()
    #print(x)
    #print(x)
    comp=[]
    comp1=[]
    comp2=[]
    '''for i in range (0,5):
        if (len(qlist[i])>0):
            print(qlist[i])'''
    
    #print(len(x))
    
    c=0
    for i in range (0,num_lines):
        comp[:]=[]
        num=0
        comp=x[i].split(" ")
        #print(comp)
        for j in range(0,5):
            if qcop[j]:
                if qcop[j] not in ['X']:
                    if(qcop[j]!=comp[j]):
                        num=1;
        if num==0:
            print(x[i],sep="\t")
            c+=1
            #print(x[1],"से",x[2],"तक",x[3],'बजे चलती और',x[4],'बजे','पोहोचती है',sep="\t")
            



    '''for i in range (0,num_lines):
        print(x[i])'''
    inp=input("Press any key to continue > ")


    

while(1):
    tmp=sp.call('clear',shell=True)
    out[:]=[]
    key[:]=[]
    atime = ''
    dtime = ''
    src = ''
    dest = ''
    count = ''
    tnum = ''
    print("1. भाषा: हिन्दी ")
    print("2. भाषा: अंग्रेज़ी ")
    print("3. समाप्त ")
    choice = int(input("आपकी पसंद>  "))

    if (choice==1):
        hindi()
    elif (choice==2):
        eng()
    elif (choice==3):
        print("धन्यवाद")
        break
    else:
        print("अमान्य!!")

    extract()
    execute()
