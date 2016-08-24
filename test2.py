from logger import Logging_file,Logging_Router
import time
a=Logging_file().logger
#a=Logging_Router().logger
c=0
while 1:
    c+=1
    a.debug('hello:%s' % c)
    time.sleep(1)
