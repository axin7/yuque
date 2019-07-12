from functools import partial

import requests

class Base(object):
    """
    Base
    
    :param token: 用户token
    :param id: 用户的 login 或 id
    :param namespace: 仓库的 namespace或id
    """
    # 基本路径
    _baseUrl = 'https://www.yuque.com/api/v2'    

    def __init__(self,token=None,id=None,namespace=None):
        self.id = id.strip()
        self.namespace = namespace.strip()
        self._headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.46 Safari/537.36'
        }

        if token:
            self._headers.update({'X-Auth-Token':token.strip()})

        self._get = partial(requests.get,headers=self._headers)
        self._post = partial(requests.post,headers=self._headers)
        self._put = partial(requests.put,headers=self._headers)
        self._delete = partial(requests.delete,headers=self._headers)