import sys
input=sys.stdin.readline
s=input().rstrip()
s=input().rstrip()
ss=[]
while s!='</body>':
    ss.append(s)
    s=input().rstrip()

def make_table(start,end):
    table=[]
    while start<end:
        if s[start:start+4]=='<tr>':
            start+=4
            tr=[]
        elif s[start:start+5]=='</tr>':
            start+=5
            table.append(tr)
        elif s[start:start+4]=='<td>':
            start+=4
            if s[start:start+7]=='<table>':            
                start+=7
                table_end=s[start:].find('</table>')
                table_start=s[start:].find('<table>')
                table_list=[]
                if table_start<table_end and table_start!=-1:
                    table_list.append(table_start)
                while table_list:
                    tmp=s[start+table_start+7:].find('<table>')
                    if table_start<table_end and tmp!=-1:
                        table_start+=tmp+7  
                        table_list.append(table_start)
                    else:
                        table_list.pop()
                        table_end+=s[start+table_end+8:].find('</table>')+8
                tmp=make_table(start,start+table_end+8)
                while len(tmp)==1:
                     tmp=tmp[0]
                if tmp:
                    tr.append(tmp)
                start+=table_end+13
            else:
                td_end=s[start:].find('</td>')
                tr.append(s[start:start+td_end])
                start+=td_end+5
        elif s[start:start+8]=='</table>':
            start+=8
    return table

def make_code(table):
    print(table)
    
    start=11
    inner=dict()
    code='<table>'
    if not table:
        code+='<tr><td></td></tr>'
    else:
        for i in range(len(table)):
            code+='<tr>'
            t_idx=-1
            if not table[i]:
                code+='<td></td>'
            else:
                for j,t in enumerate(table[i]):
                    if type(t)==type([]):
                        r=len(t)
                        c=len(t[0])
                        t_idx=j
                        inner[(i,j)]=(r,c)
                        for tt in t[0]:
                            code+='<td>'+tt+'</td>'
                    else:
                        code+='<td>'+t+'</td>'
            code+='</tr>'
            if t_idx!=-1 and r>1:
                for cnt in range(len(table[i])):
                    if cnt!=t_idx:
                        tmp=code[start:].find('<td>')
                        code=code[:start+tmp+3]+' rowspan="'+str(r)+'"'+code[start+tmp+3:]
                        start+=code[start:].find('</td>')+5
                    else:
                        for _ in range(c):
                            start+=code[start:].find('</td>')+5
                for j in range(1,r):
                    code+='<tr>'
                    for tt in table[i][t_idx][j]:
                        code+='<td>'+tt+'</td>'
                    code+='</tr>'
                    start+=code[start:].find('</tr>')+5
            start+=code[start:].find('</tr>')+5
    
    for (i,j),(r,c) in inner.items():
        top=0
        left=0
        for row in range(len(table)):
            start=0
            if i!=row:
                row_tmp=1   
                for col_i,col in enumerate(table[row]):
                    if col_i<j:
                        if type(col)==type([]):
                            left+=len(col[0])
                        else:
                            left+=1
                    if type(col)==type([]):
                        row_tmp=len(col)
                for _ in range(top):
                    start+=code[start:].find('</tr>')+5
                for _ in range(left):
                    start+=code[start:].find('</td>')+5
                if c>1:
                    if left==0:
                        start+=code[start:].find('<tr>')+4
                    tmp=code[start:].find('>')
                    code=code[:start+tmp]+' colspan="'+str(c)+'"'+code[start+tmp:]
                top+=row_tmp
            else:
                top+=r
    code+='</table>'
    return code

print('<body>')
for s in ss:
    print(make_code(make_table(7,len(s))))
print('</body>')