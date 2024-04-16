'''
Author: Jalen-Zhong jelly_zhong.qz@foxmail.com
Date: 2024-04-16 11:02:39
LastEditors: Jalen-Zhong jelly_zhong.qz@foxmail.com
LastEditTime: 2024-04-16 15:28:09
FilePath: \logger\loggers.py
Description: 定义日志记录器 —— 
            简单的日志记录器 、 streamhanlder 、 filehanlder 、 timerotatehanlder

Copyright (c) 2024 by Jalen-Zhong, All Rights Reserved. 
'''
import logging
from logging import handlers
from config import get_config
import os
import re

def basiclogger(config):
    logger = logging.getLogger(config['log']['name']['basiclogger'])
    log_name = os.path.join(config['log']['path'], config['log']['name']['basiclogger'] + '.log')
    if not os.path.exists(config['log']['path']):
        os.makedirs(config['log']['path'])
    # 设置打印日志的级别，level级别以上的日志会打印出
    # level=logging.DEBUG 、INFO 、WARNING、ERROR、CRITICAL
    logging.basicConfig(filename=log_name, 
                        format=config['log']['format'],
                        level=config['log']['level'])
    return logger


def streamhanlder(config):
    # 创建一个Logger
    logger = logging.getLogger(config['log']['name']['streamhanlder'])
    logger.setLevel(config['log']['level'])  # 设置Logger的日志级别
    
    # 创建一个流Handler，用于输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(config['log']['level'])  # 设置控制台Handler的日志级别
    
    # 设置日志格式
    formatter = logging.Formatter(config['log']['format'])
    console_handler.setFormatter(formatter)
    
    # 将Handler添加到Logger
    logger.addHandler(console_handler)

    return logger

def filehanlder(config):
    # 创建一个Logger
    logger = logging.getLogger(config['log']['name']['filehanlder'])
    logger.setLevel(config['log']['level'])  # 设置Logger的日志级别

    # 创建一个文件Handler，用于写入日志文件
    log_name = os.path.join(config['log']['path'], config['log']['name']['filehanlder'] + '.log')
    file_handler = logging.FileHandler(log_name)
    file_handler.setLevel(logging.DEBUG)  # 设置文件Handler的日志级别

    # 设置日志格式
    formatter = logging.Formatter(config['log']['format'])
    file_handler.setFormatter(formatter)  # 重复使用前面定义的格式
 
    # 将Handler添加到Logger
    logger.addHandler(file_handler)

    return logger

def timerotatehanlder(config):
    # 创建一个Logger
    logger = logging.getLogger(config['log']['name']['timerotatehanlder'])
    logger.setLevel(config['log']['level'])  # 设置Logger的日志级别

    # 创建一个文件Handler，用于写入日志文件
    log_name = os.path.join(config['log']['path'], config['log']['name']['timerotatehanlder'] + '.log')
    # when 按什么日期格式切分，接收指定字符串参数
    # “S”: Seconds
    # “M”: Minutes
    # “H”: Hours
    # “D”: Days
    # “W”: Week day (0=Monday)
    # “midnight”: Roll over at midnight
    # interval 是指等待多少个单位when的时间后，Logger会自动重建文件，这个文件的创建取决于filename + suffix，若这个文件跟之前的文件有重名，则会自动覆盖掉以前的文件，所以有些情况suffix要定义不能因为when而重复。
    # backupCount 是保留日志个数。默认的0是不会自动删除掉日志。若设为5，则在文件的创建过程中库会判断是否有超过这个5，若超过，则会从最先创建的开始删除。
    trt_handler = handlers.TimedRotatingFileHandler(
        filename=log_name,
        when='s',
        interval=1,
        backupCount=30
    )
    
    # 设置时刻断点文件保存名称
    trt_handler.suffix = "%Y-%m-%d_%H-%M-%S.log" # 设置日志文件名的后缀
    trt_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$") # 它是一个正则表达式对象，用于匹配在清理旧日志文件时应该删除的文件
    formatter = logging.Formatter(config['log']['format'])
    trt_handler.setFormatter(formatter)
    logger.addHandler(trt_handler)

    return logger

def log_record(config, logger):
    logger.debug(config['debug'],)
    logger.info(config['info'],)
    logger.warning(config['warning'],)
    logger.error(config['error'],)
    logger.critical(config['critical'],)

