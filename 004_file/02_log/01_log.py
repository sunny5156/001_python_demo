#一、python日志生成的写法
############1、按照文件大小备份

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import logging
import logging.handlers

# logging初始化工作
logging.basicConfig()

# myapp的初始化工作
myapp = logging.getLogger('myapp')
myapp.setLevel(logging.INFO)

# 写入文件，如果文件超过100个Bytes，仅保留5个文件。
handler = logging.handlers.RotatingFileHandler(
    'log/myapp.log', maxBytes=2*1000, backupCount=5)

# 设置后缀名称，跟strftime的格式一样
myapp.addHandler(handler)

while True:
    time.sleep(0.01)
    myapp.info("file test")
##################2、按照日期时间备份

    #!/usr/bin/env python3  
      
    import time  
    import logging  
    import logging.handlers  
      
    # logging初始化工作  
    logging.basicConfig()  
      
    # myapp的初始化工作  
    myapp = logging.getLogger('myapp')  
    myapp.setLevel(logging.INFO)  
      
    # 添加TimedRotatingFileHandler  
    # 定义一个1秒换一次log文件的handler  
    # 保留3个旧log文件  
    filehandler = logging.handlers.TimedRotatingFileHandler("logs/myapp.log", when='S', interval=1, backupCount=3)  
    # 设置后缀名称，跟strftime的格式一样  
    filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"  
    myapp.addHandler(filehandler)  
      
    while True:  
        time.sleep(0.1)  
        myapp.info("test")  


# flask生成日志的写法
############### 1、不设置备份的日志生成写法
#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import logging
from flask import current_app

app = Flask(__name__)


@app.route('/')
def root():
    #第一种写法
    app.logger.info('info log')
    app.logger.warning('warning log')

    #第二种写法
    current_app.logger.debug('A value for debugging')
    current_app.logger.warning('A warning occurred (%d apples)', 42)
    current_app.logger.error('An error occurred')
    return 'hello'

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)

    app.run()
###########2、按照时间日志生成写法
#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import logging,time
from logging.handlers import TimedRotatingFileHandler
from flask import current_app


app = Flask(__name__)
@app.route('/')
def root():
    #第一种写法
    print "==="
    for i in range(10000):
        print time.time()
        app.logger.info('info log %s'%(time.time()))
        app.logger.warning('warning log %s'%(time.time()))
        # time.sleep(1)
    return 'hello'

if __name__ == '__main__':
    Rthandler = TimedRotatingFileHandler('../log/test/flask03.log', when='S', interval=1, backupCount=3) #设置日志文件的大小，以及备份的次数
    # 设置后缀名称，跟strftime的格式一样
    Rthandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
    app.logger.addHandler(Rthandler)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(Rthandler)

    app.run()

###########3、按照文件大小分割日志生成写法

#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import logging,time
from logging.handlers import RotatingFileHandler
from flask import current_app
app = Flask(__name__)
@app.route('/')
def root():
    #第一种写法
    print "==="
    for i in range(100):
        print time.time()
        app.logger.info('info log %s'%(time.time()))
        app.logger.warning('warning log %s'%(time.time()))
        time.sleep(1)

        # #第二种写法
        # current_app.logger.debug('A value for debugging')
        # current_app.logger.warning('A warning occurred (%d apples)', 42)
        # current_app.logger.error('An error occurred')
    return 'hello'

if __name__ == '__main__':
#备份形式是一直在文件后边增加.n，并且新产生的日志n比较小，并随着日志的产生不断地向后推写
    Rthandler = RotatingFileHandler('../log/test/flask01.log', maxBytes=1024,backupCount=2) 
#设置日志文件的大小，以及备份的次数
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(Rthandler)

    app.run()

