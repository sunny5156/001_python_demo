# 需求：
# 输出log到控制台以及将日志写入log文件。保存2种类型的log， all.log 保存debug, info, warning, critical 信息， error.log则只保存error信息，同时按照时间自动分割日志文件。

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File      :    logger.py
@Time      :    2021/11/01 10:57:56
@Author   :    Scheaven 
@Version :    1.0
@Contact :    snow_mail@foxmail.com
@License :    (C)Copyright 2021-2022, Scheaven 360
@Desc      :    日志库文件
'''
import logging
import sys
from logging import handlers
class Logger(object):
      level_relations = {
            'debug':logging.DEBUG,
            'info':logging.INFO,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'crit':logging.CRITICAL
      }#日志级别关系映射
      def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(message)s'):
            self.logger = logging.getLogger(filename)
            format_str = logging.Formatter(fmt)#设置日志格式
            self.logger.setLevel(self.level_relations.get(level))#设置日志级别
            sh = logging.StreamHandler()#往屏幕上输出
            sh.setFormatter(format_str) #设置屏幕上显示的格式
            th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
            #实例化TimedRotatingFileHandler
            #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            # S 秒
            # M 分
            # H 小时、
            # D 天、
            # W 每星期（interval==0时代表星期一）
            # midnight 每天凌晨
            th.setFormatter(format_str)#设置文件里写入的格式
            self.logger.addHandler(sh) #把对象加到logger里
            self.logger.addHandler(th)
log = Logger('01_test.log', level='debug')
def SDEBUG(message):
      _levelname = "DEBUG"
      _pathname = sys._getframe().f_back.f_code.co_filename
      _def_name = sys._getframe().f_back.f_code.co_name
      _lineno = sys._getframe().f_back.f_lineno
      line = '%(def_name)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' \
            %{'pathname' : _pathname , 'def_name' : _def_name , 'lineno' : _lineno , 'levelname' : _levelname, 'message':message}
      log.logger.debug(line)
def SINFO(message):
      _levelname = "INFO"
      _pathname = sys._getframe().f_back.f_code.co_filename
      _def_name = sys._getframe().f_back.f_code.co_name
      _lineno = sys._getframe().f_back.f_lineno
      line = '%(def_name)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' \
            %{'pathname' : _pathname , 'def_name' : _def_name , 'lineno' : _lineno , 'levelname' : _levelname, 'message':message}
      log.logger.info(line)
def SWARNING(message):
      _levelname = "WARNING"
      _pathname = sys._getframe().f_back.f_code.co_filename
      _def_name = sys._getframe().f_back.f_code.co_name
      _lineno = sys._getframe().f_back.f_lineno
      line = '%(def_name)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' \
            %{'pathname' : _pathname , 'def_name' : _def_name , 'lineno' : _lineno , 'levelname' : _levelname, 'message':message}
      log.logger.warning(line)
def SERROR(message):
      _levelname = "ERROR"
      _pathname = sys._getframe().f_back.f_code.co_filename
      _def_name = sys._getframe().f_back.f_code.co_name
      _lineno = sys._getframe().f_back.f_lineno
      line = '%(def_name)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' \
            %{'pathname' : _pathname , 'def_name' : _def_name , 'lineno' : _lineno , 'levelname' : _levelname, 'message':message}
      log.logger.error(line)
def SCRITICAL(message):
      _levelname = "CRITICAL"
      _pathname = sys._getframe().f_back.f_code.co_filename
      _def_name = sys._getframe().f_back.f_code.co_name
      _lineno = sys._getframe().f_back.f_lineno
      line = '%(def_name)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' \
            %{'pathname' : _pathname , 'def_name' : _def_name , 'lineno' : _lineno , 'levelname' : _levelname, 'message':message}
      log.logger.critical(line)
if __name__=="__main__":
      SDEBUG("test")
      SINFO("info")
      SWARNING("警告")
      SERROR("报错")
      SCRITICAL("严重")
#       log.logger.debug('debug')
#       log.logger.info('info')
#       log.logger.warning('警告')
#       log.logger.error('报错')
#       log.logger.critical('严重')
#       Logger('error.log', level='error').logger.error('error')

# 复制代码
# 屏幕上的结果如下：
# 2018-03-13 21:06:46,092 - D:/write_to_log.py[line:25] - DEBUG: debug
# 2018-03-13 21:06:46,092 - D:/write_to_log.py[line:26] - INFO: info
# 2018-03-13 21:06:46,092 - D:/write_to_log.py[line:27] - WARNING: 警告
# 2018-03-13 21:06:46,099 - D:/write_to_log.py[line:28] - ERROR: 报错
# 2018-03-13 21:06:46,099 - D:/write_to_log.py[line:29] - CRITICAL: 严重
# 2018-03-13 21:06:46,100 - D:/write_to_log.py[line:30] - ERROR: error
