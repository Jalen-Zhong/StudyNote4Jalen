'''
Author: Jalen-Zhong jelly_zhong.qz@foxmail.com
Date: 2024-04-16 11:09:54
LastEditors: Jalen-Zhong jelly_zhong.qz@foxmail.com
LastEditTime: 2024-04-16 15:28:25
FilePath: \logger\main.py
Description: 运行主函数

Copyright (c) 2024 by Jalen-Zhong, All Rights Reserved. 
'''
from loggers import (basiclogger, 
                    streamhanlder, 
                    filehanlder,
                    timerotatehanlder,
                    log_record)
from config import get_config

def log_testing():
    config = get_config()
    # logger定义
    logger_basic = basiclogger(config)
    log_record(config, logger_basic)

    # StreamHandler：把日志输出到控制台
    logger_steamhanlder = streamhanlder(config)
    log_record(config, logger_steamhanlder)

    # FileHandler：把日志输出到指定文件
    logger_filehanlder = filehanlder(config)
    log_record(config, logger_filehanlder)

    # TimeRotatingFileHandler：设置日志拆分逻辑，日志输出到指定文件
    logger_timerotatehanlder = timerotatehanlder(config)
    log_record(config, logger_timerotatehanlder)

if __name__=='__main__':
    log_testing()

