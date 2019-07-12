from functools import partial

import requests

class Base(object):
    """
    Base
    
    :param token: 用户token
    :param id: 用户的 login 或 id
    :param name: 仓库的 namespace或id
    """
    # 基本路径
    _baseUrl = 'https://www.yuque.com/api/v2'    

    # 请求头
    _headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.46 Safari/537.36'
    }

    get = partial(requests.get,headers=_headers)
    post = partial(requests.post,headers=_headers)
    put = partial(requests.put,headers=_headers)
    delete = partial(requests.delete,headers=_headers)

    def __init__(self,token=None,id=None,name=None):
        if token:
            self._headers.update({'X-Auth-Token':token})
        self.id = id
        self.name = name
