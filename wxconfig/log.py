#!/usr/bin/env python
# coding: utf-8

#===================================================
from constant import Constant
import sys
sys.path.append(r'/disk200g/hn/WeixinBot/wxbot_project_py2.7/')
print(sys.path)
from config_manager import ConfigManager
#---------------------------------------------------
import logging
import logging.config
#===================================================

cm = ConfigManager()

logging.config.fileConfig(Constant.WECHAT_CONFIG_FILE)
# create logger
Log = logging.getLogger(Constant.LOGGING_LOGGER_NAME)

# 'application' code
# Log.debug('debug message')
# Log.info('info message')
# Log.warn('warn message')
# Log.error('error message')
# Log.critical('critical message')
