
from pythonping import ping

for i in range(3):
    for j in range(3):
        ipaddresss=str('192.168.%s.%s'%(i,j))
        ping(ipaddresss,count=1,verbose=True)

