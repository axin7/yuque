import json

import requests


# 基本路径
BASE_PATH = 'https://www.yuque.com/api/v2'    

# 用户路径
USER_INFO_PATH = '/users/'      # 获取单个用户信息   注：需在最后加用户id或login       【无需认证】
USER_INFO_AUTH_PATH = '/user'   # 获取认证的用户的个人信息                      【需要认证】
USER_DOCS_PATH = '/user/docs'   # 获取用户创建的文档                                【需要认证】
USER_RENCENT_UPDATED_PATH = '/user/recent-updated'     # 获取最近参与的文档/知识库   【需要认证】

# 组织路径
GROUP_USER_GROUPS_PATH = '/users/'    # 获取某个用户的加入的组织列表  注：需在最后加用户id/groups或login/groups
GROUP_GROUPS_PATH = '/groups'    #获取公开组织列表

# 请求头
HEADER = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}


class User():
    '''获取用户信息'''

    def __init__(self,
                token=None,
                id=None,
                base_path=BASE_PATH, 
                user_info_path=USER_INFO_PATH,
                user_info_auth_path=USER_INFO_AUTH_PATH,
                user_docs_path=USER_DOCS_PATH,
                header=HEADER):
        self.token = token
        self.id = id
        self.base_path = base_path
        self.user_info_path = user_info_path
        self.user_info_auth_path = user_info_auth_path
        self.user_docs_path = user_docs_path
        self.header = header

    def info(self):
        url = BASE_PATH + USER_INFO_PATH + self.id
        r = requests.get(url,headers = self.header)
        return r.json()
            
    def info_auth(self):
        self.header['X-Auth-Token'] = self.token
        url = BASE_PATH + USER_INFO_AUTH_PATH
        r = requests.get(url,headers=self.header)
        return r.json()

    def docs(self,keywords=None,offset=None):
        self.header['X-Auth-Token'] = self.token
        params = {
            'q': keywords,
            'offset': offset
        }
        url = BASE_PATH + USER_DOCS_PATH
        r = requests.get(url,headers=self.header,params=params)
        return r.json()

    def recent_updated(self,type,offset=None):
        params = {
            'type': type,
            'offset': offset
        }
        self.header['X-Auth-Token'] = self.token
        url = BASE_PATH + USER_RENCENT_UPDATED_PATH
        r = requests.get(url, headers=self.header,params=params)
        return r.json()
    

class Group():
    '''获取组织信息'''
    def __init__(self,token=None,
                ):
