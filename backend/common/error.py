#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import traceback
import logging

# Create your views here.

'''
errorno=1 表示需要重新登录
errorno='S9999' 表示异常
'''

class ErrorInfo():
    def error(self, request, error):
        print(error)
        return_data = dict(errorno='S9999', error_msg_en='Error', error_msg_zh='error')
        return return_data
    
def error_decorator(func):
    def wrapper(request, *args, **kwargs):
        logger = logging.getLogger('django')
        try:
            return func(request, *args, **kwargs)
        except:
            logger.error(traceback.format_exc())
            
            return ErrorInfo().error(request, traceback.format_exc())

    return wrapper