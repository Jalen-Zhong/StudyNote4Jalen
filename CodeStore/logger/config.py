'''
Author: Jalen-Zhong jelly_zhong.qz@foxmail.com
Date: 2024-04-16 11:05:00
LastEditors: Jalen-Zhong jelly_zhong.qz@foxmail.com
LastEditTime: 2024-04-16 15:28:59
FilePath: \logger\config.py
Description: 配置参数

Copyright (c) 2024 by Jalen-Zhong, All Rights Reserved. 
'''
from environs import Env

def get_config():
    env = Env()
    return {
            'log': {'path': env.str('LOG_PATH','log'),
                    'level': env.str('LOG_LEVEL', 'INFO'),
                    'name': {'basiclogger' : env.str('BASICLOG_NAME', 'basiclogger'),
                             'streamhanlder' : env.str('STREAMHANLDER', 'streamhanlder'),
                             'filehanlder' : env.str('FILEHANLDER', 'filehanlder'),
                             'timerotatehanlder' : env.str('TIMEROTATEHANLDER', 'timerotatehanlder')},
                    'format' : env.str('FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s')
                    },
            'debug': env.str('DEBUG','debug，用来打印一些调试信息，级别最低'),
            'info': env.str('INFO','info，用来打印一些正常的操作信息'),
            'warning': env.str('WARNING','waring，用来用来打印警告信息'),
            'error': env.str('ERROR','error，一般用来打印一些错误信息'),
            'critical': env.str('CRITICAL','critical，用来打印一些致命的错误信息，等级最高')
    }