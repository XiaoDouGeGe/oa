# coding = utf-8

from django.shortcuts import render
import traceback
import importlib
from django.views.generic import View
from django.http import JsonResponse
from common import error


class UploadView(View):  
    impl = ''
    
    def post(self, request, *args, **kwargs):
        ret = self._process(request, args, kwargs)
        return JsonResponse(ret)
    
    def _process(self, request, *args, **kwargs):
        """
        处理请求
        """
        ret = dict(errorno=0, date={})
        func_dict = {'GET':'get_data', 'POST':'do_post', 'PATCH':'do_patch'}
        if request.method not in func_dict:
            ret['errorno'] = 2
        else:
            func_name = func_dict[request.method]
            _model = importlib.import_module('.%s' % self.impl, __name__.rsplit('.', 1)[0])
            importlib.reload(_model)
            if hasattr(_model, func_name):
                func = getattr(_model, func_name)
                if callable(func):
                    ret = func(request, args, kwargs)
        return ret


class ListView(View):
    impl = ''
    
    def get(self, request, *args, **kwargs):
        ret = self._process(request, args, kwargs)
        return JsonResponse(ret)
    
    def _process(self, request, *args, **kwargs):
        ret = dict(errorno=0, date={})
        func_dict = {'GET':'get_data', 'POST':'do_post', 'PATCH':'do_patch'}
        if request.method not in func_dict:
            ret['errorno'] = 2
        else:
            func_name = func_dict[request.method]
            _model = importlib.import_module('.%s' % self.impl, __name__.rsplit('.', 1)[0])
            importlib.reload(_model)
            if hasattr(_model, func_name):
                func = getattr(_model, func_name)
                if callable(func):
                    ret = func(request, args, kwargs)
        return ret


class ClearView(View):
    impl = ''

    def post(self, request, *args, **kwargs):
        ret = self._process(request, args, kwargs)
        return JsonResponse(ret)
    
    def _process(self, request, *args, **kwargs):
        ret = dict(errorno=0, date={})
        func_dict = {'GET':'get_data', 'POST':'do_post', 'PATCH':'do_patch'}
        if request.method not in func_dict:
            ret['errorno'] = 2
        else:
            func_name = func_dict[request.method]
            _model = importlib.import_module('.%s' % self.impl, __name__.rsplit('.', 1)[0])
            importlib.reload(_model)
            if hasattr(_model, func_name):
                func = getattr(_model, func_name)
                if callable(func):
                    ret = func(request, args, kwargs)
        return ret


class MailView(View):
    impl = ''

    def post(self, request, *args, **kwargs):
        ret = self._process(request, args, kwargs)
        return JsonResponse(ret)
    
    def _process(self, request, *args, **kwargs):
        ret = dict(errorno=0, date={})
        func_dict = {'GET':'get_data', 'POST':'do_post', 'PATCH':'do_patch'}
        if request.method not in func_dict:
            ret['errorno'] = 2
        else:
            func_name = func_dict[request.method]
            _model = importlib.import_module('.%s' % self.impl, __name__.rsplit('.', 1)[0])
            importlib.reload(_model)
            if hasattr(_model, func_name):
                func = getattr(_model, func_name)
                if callable(func):
                    ret = func(request, args, kwargs)
        return ret
