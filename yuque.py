# coding = utf-8

import json

import requests


# 基本路径
BASE_PATH = 'https://www.yuque.com/api/v2'    

# 用户路径
USER_INFO_PATH = '/users/'      # 获取单个用户信息   注：需在最后加用户id或login       【无需认证】
USER_INFO_AUTH_PATH = '/user'   # 获取认证的用户的个人信息                           【需要认证】
USER_DOCS_PATH = '/user/docs'   # 获取用户创建的文档                                【需要认证】
USER_RENCENT_UPDATED_PATH = '/user/recent-updated'     # 获取最近参与的文档/知识库   【需要认证】

# 组织路径
GROUP_GROUPS_PATH = '/users/'     # 获取某个用户的加入的组织列表  注：需在最后加用户id/groups或login/groups
GROUP_GROUPS_PUBLIC_PATH = '/groups'    #获取公开组织列表
GROUP_CREATE_PATH = '/groups'    # 创建组织
GROUP_DETAIL_PATH = '/groups/'    #获取单个组织的详细信息  注：需在最后加用户id或login
GROUP_UPDATE_PATH = '/groups/'    #更新单个组织的详细信息  注：需在最后加用户id或login
GROUP_DELETE_PATH = '/groups/'    #删除组织
GROUP_USERS_PATH = '/groups/'    #获取组织成员信息  注：需在最后加用户id/users或login/users
GROUP_UPDATE_USER_PATH = '/groups/'    #增加或更新组织成员  注：需在最后加用户group_login//users/login或:group_id/users/login
GROUP_DELETE_USER_PATH = '/groups/'    #删除组织成员  注：需在最后加用户group_login//users/login或:group_id/users/login



# 请求头
HEADER = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}


class User():
    """获取用户信息
    
    :param 
    """

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
    """获取组织信息
    
    :param token: 用户token
    :param id: 用户的 login 或 id
    :param base_path: 基本路径
    :param group_groups_path: 获取某个用户的加入的组织列表路径
    :param group_groups_public_path: 获取公开组织列表路径
    :param group_create_path: 创建组织路径
    :param group_detail_path: 获取单个组织的详细信息路径
    :param group_update_path: 更新单个组织的详细信息路径
    :param group_delete_path: 删除组织路径
    :param group_users_path: 获取组织成员信息路径
    :param group_update_user_path: 增加或更新组织成员路径
    :param group_delete_user_path: 删除组织成员路径
    :param header: 请求头
    """

    def __init__(self,
                token=None,
                id=None,
                base_path=BASE_PATH, 
                group_groups_path=GROUP_GROUPS_PATH,
                group_groups_public_path=GROUP_GROUPS_PUBLIC_PATH,
                group_create_path=GROUP_CREATE_PATH,
                group_detail_path=GROUP_DETAIL_PATH,
                group_update_path=GROUP_UPDATE_PATH,
                group_delete_path=GROUP_DELETE_PATH,
                group_users_path=GROUP_USERS_PATH,
                group_update_user_path=GROUP_UPDATE_USER_PATH,
                group_delete_user_path=GROUP_DELETE_USER_PATH,
                header=HEADER):
        self.token = token
        self.id = id
        self.base_path = base_path
        self.group_groups_path = group_groups_path
        self.group_groups_public_path = group_groups_public_path
        self.group_create_path = group_create_path
        self.group_detail_path = group_detail_path
        self.group_update_path = group_update_path
        self.group_delete_path = group_delete_path
        self.group_users_path = group_users_path
        self.group_update_user_path = group_update_user_path
        self.group_delete_user_path = group_delete_user_path
        self.header = header

    def groups(self):
        """获取某个用户的加入的组织列表"""
        self.header['X-Auth-Token'] = self.token
        url = self.base_path + self.group_groups_path + self.id + '/groups'
        r = requests.get(url,headers=self.header)
        return r.json()

    def groups_public(self):
        """获取公开组织列表"""
        url = self.base_path + self.group_groups_public_path
        r = requests.get(url,headers=self.header)
        return r.json()

    def create(self,name,login,description=None):
        """创建 Group

        :param name: 组织名称
        :param login: login
        :param description: 介绍
        """
        params = {
            'name': name,
            'login': login,
            'description': description
        }
        self.header['X-Auth-Token'] = self.token
        url = self.base_path + self.group_create_path
        r = requests.post(url,headers=self.header,params=params)
        return r.json()

    def detail(self,groupid):
        """获取单个组织的详细信息
        
        :param groupid: 组织的 login 或 id
        """

        url = self.base_path + self.group_detail_path + groupid
        r = requests.get(url,headers=self.header)
        return r.json()

    def update(self,groupid,name=None,login=None,description=None):
        """更新单个组织的详细信息
        
        :param groupid: 组织的 login 或 id
        :param name: 组织名称
        :param login: login
        :param description: 介绍
        """
        params = {
            'name': name,
            'login': login,
            'description': description
        }
        self.header['X-Auth-Token'] = self.token
        url = self.base_path + self.group_update_path + groupid
        r = requests.put(url,headers=self.header,params=params)
        return r.json()

    def delete(self,groupid):
        """删除组织

        :param groupid: 组织的 login 或 id
        """
        self.header['X-Auth-Token'] = self.token
        url = self.base_path + self.group_delete_path + groupid
        r = requests.delete(url,headers=self.header)
        return r.json()

    def users(self,groupid):
        """获取组织成员信息

        :param groupid: 组织的 login 或 id
        """
        self.header['X-Auth-Token'] = self.token
        url = self.base_path + self.group_users_path + groupid + '/users'
        r = requests.get(url,headers=self.header)
        return r.json()

    def update_user(self,groupid,login,role):
        """增加或更新组织成员
        
        :param groupid: 组织的 login 或 id
        :param login: 用户的login
        :param role: 0 - 管理员, 1 - 普通成员
        """
        params = {
            'role': role
        }
        self.header['X-Auth-Token'] = self.token
        url = self.base_path + self.group_update_user_path + groupid + '/users/' + login
        r = requests.put(url,headers=self.header,params=params)
        return r.json()

    def delete_user(self,groupid,login):
        """删除组织成员
        
        :param groupid: 组织的 login 或 id
        :param login: 用户的login
        """

        self.header['X-Auth-Token'] = self.token
        url = self.base_path + self.group_delete_user_path + groupid + '/users/' + login
        r = requests.delete(url,headers=self.header)
        return r.json()
