from collections import defaultdict,deque
N,M,K=map(int,input().split())
dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
fireball=[defaultdict(deque) for _ in range(K+1)]
for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    fireball[K][(r,c)].append((m,s,d))
    

while K>0:
    
    for (r,c),flist in fireball[K].items():
        for m,s,d in flist:
            dr,dc=dir[d]
            dr*=s
            dc*=s
            nr=(r+dr-1)%(N)+1
            nc=(c+dc-1)%(N)+1
            fireball[K-1][(nr,nc)].append((m,s,d))

    for (r,c),flist in fireball[K-1].items():
        f_num=len(flist)
        if f_num>1:
            m_sum=0
            s_sum=0
            dflag=[False,False]
            while flist:
                m,s,d=flist.popleft()
                m_sum+=m
                s_sum+=s
                dflag[d%2]=True
            
            if m_sum//5!=0:
                if not dflag[0] or not dflag[1]:
                    flist.append((m_sum//5,s_sum//f_num,0))
                    flist.append((m_sum//5,s_sum//f_num,2))
                    flist.append((m_sum//5,s_sum//f_num,4))
                    flist.append((m_sum//5,s_sum//f_num,6))
                else:
                    flist.append((m_sum//5,s_sum//f_num,1))
                    flist.append((m_sum//5,s_sum//f_num,3))
                    flist.append((m_sum//5,s_sum//f_num,5))
                    flist.append((m_sum//5,s_sum//f_num,7))
    
    K-=1

ans=0
for (r,c),flist in fireball[0].items():
    for m,s,d in flist:
        ans+=m

print(ans)