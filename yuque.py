from functools import partial

import requests

# 基本路径
BASE_PATH = 'https://www.yuque.com/api/v2'    

# 用户路径
USER_INFO_PATH = '/users/'      # 获取单个用户信息   注：需在最后加 用户id或login      
USER_INFO_AUTH_PATH = '/user'   # 获取认证的用户的个人信息                           

# 组织路径
GROUP_GROUPS_PATH = '/users/'     # 获取某个用户的加入的组织列表  注：需在最后加 用户id/groups或login/groups
GROUP_GROUPS_PUBLIC_PATH = '/groups'    #获取公开组织列表
GROUP_CREATE_PATH = '/groups'    # 创建组织
GROUP_DETAIL_PATH = '/groups/'    # 获取单个组织的详细信息  注：需在最后加 用户id或login
GROUP_UPDATE_PATH = '/groups/'    # 更新单个组织的详细信息  注：需在最后加 用户id或login
GROUP_DELETE_PATH = '/groups/'    # 删除组织
GROUP_USERS_PATH = '/groups/'    # 获取组织成员信息  注：需在最后加 用户id/users或login/users
GROUP_UPDATE_USER_PATH = '/groups/'    # 增加或更新组织成员  注：需在最后加 用户group_login//users/login或:group_id/users/login
GROUP_DELETE_USER_PATH = '/groups/'    # 删除组织成员  注：需在最后加 用户group_login//users/login或:group_id/users/login

#仓库路径
REPO_REPOS_USER_PATH = '/users/'    # 获取某个用户的仓库列表  注：需在最后加 用户login/repos或id/repos
REPO_REPOS_GROUP_PATH = '/groups/'    # 获取某个组织的仓库列表  注：需在最后加 组织login/repos或id/repos
REPO_CREATE_USER_PATH = '/users/'    # 往自己下面创建仓库  注：需在后面加 用户login/repos或id/repos
REPO_CREATE_GROUP_PATH = '/users/'    # 往组织创建仓库  注：需在最后加 组织login/repos或id/repos
REPO_DETAIL_PATH = '/repos/'    # 获取仓库详情  注：需在最后加 仓库id或namespace
REPO_UPDATE_PATH = '/repos/'    # 更新仓库信息  注：需在最后加 仓库id或namespace
REPO_DELETE_PATH = '/repos/'    # 删除仓库  注：需在最后加 仓库id或namespace
REPO_TOC_PATH = '/repos/'    # 获取一个仓库的目录结构  注：需在最后加 仓库namespace/toc或id/toc 
REPO_SEARCH_PATH = '/search/repos'    # 基于关键字搜索仓库

# 请求头
HEADER = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

get = partial(requests.get,headers=HEADER)
post = partial(requests.post,headers=HEADER)
put = partial(requests.put,headers=HEADER)
delete = partial(requests.delete,headers=HEADER)


class User():
    """获取用户信息
    
    :param token: 用户token
    :param id: 用户的 login 或 id
    """

    def __init__(self,token=None,id=None):
        HEADER['X-Auth-Token'] = token
        self.id = id
        self.header = HEADER

    def info(self):
        """获取单个用户信息"""
        url = BASE_PATH + USER_INFO_PATH + self.id
        r = get(url=url,headers = self.header)
        return r.json()
            
    def info_auth(self):
        """获取认证的用户的个人信息"""
        url = BASE_PATH + USER_INFO_AUTH_PATH
        r = get(url=url,headers=self.header)
        return r.json()
    

class Group():
    """获取组织信息
    
    :param token: 用户token
    :param id: 用户的 login 或 id
    """

    def __init__(self,token=None,id=None):
        HEADER['X-Auth-Token'] = token
        self.id = id
        self.header = HEADER

    def groups(self):
        """获取某个用户的加入的组织列表"""
        url = BASE_PATH + GROUP_GROUPS_PATH + self.id + '/groups'
        r = get(url=url,headers=self.header)
        return r.json()

    def groups_public(self):
        """获取公开组织列表"""
        url = BASE_PATH + GROUP_GROUPS_PUBLIC_PATH
        r = get(url=url,headers=self.header)
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
        url = BASE_PATH + GROUP_CREATE_PATH
        r = post(url=url,headers=self.header,params=params)
        return r.json()

    def detail(self,groupid):
        """获取单个组织的详细信息
        
        :param groupid: 组织的login或id
        """

        url = BASE_PATH + GROUP_DETAIL_PATH + groupid
        r = get(url=url,headers=self.header)
        return r.json()

    def update(self,groupid,name=None,login=None,description=None):
        """更新单个组织的详细信息
        
        :param groupid: 组织的login或id
        :param name: 组织名称
        :param login: login
        :param description: 介绍
        """
        params = {
            'name': name,
            'login': login,
            'description': description
        }
        url = BASE_PATH + GROUP_UPDATE_PATH + groupid
        r = put(url=url,headers=self.header,params=params)
        return r.json()

    def delete(self,groupid):
        """删除组织

        :param groupid: 组织的login或id
        """
        url = BASE_PATH + GROUP_DELETE_PATH + groupid
        r = delete(url=url,headers=self.header)
        return r.json()

    def users(self,groupid):
        """获取组织成员信息

        :param groupid: 组织的login或id
        """
        url = BASE_PATH + GROUP_USERS_PATH + groupid + '/users'
        r = get(url=url,headers=self.header)
        return r.json()

    def update_user(self,groupid,login,role):
        """增加或更新组织成员
        
        :param groupid: 组织的login或id
        :param login: 用户的login
        :param role: 0 - 管理员, 1 - 普通成员
        """
        params = {
            'role': role
        }
        url = BASE_PATH + GROUP_UPDATE_USER_PATH + groupid + '/users/' + login
        r = put(url=url,headers=self.header,params=params)
        return r.json()

    def delete_user(self,groupid,login):
        """删除组织成员
        
        :param groupid: 组织的login或id
        :param login: 用户的login
        """
        url = BASE_PATH + GROUP_DELETE_USER_PATH + groupid + '/users/' + login
        r = delete(url=url,headers=self.header)
        return r.json()


class Repo():
    """获取仓库信息
    
    :params token: 用户token
    """

    def __init__(self,token=None):
        HEADER['X-Auth-Token'] = token
        self.header = HEADER

    def repos_user(self,id):
        """获取某个用户的仓库列表
        
        :params id: 用户的login或id
        """
        url = BASE_PATH + REPO_REPOS_USER_PATH + id + '/repos'
        r = get(url=url,headers=self.header)
        return r.json()

    def repos_group(self,groupid):
        """获取某个组织的仓库列表
        
        :params groupid: 组织的login或id
        """
        url = BASE_PATH + REPO_REPOS_GROUP_PATH + groupid +'/repos'
        r = get(url=url,headers=self.header)
        return r.json()

    def create(self,id,name=None,slug=None,description=None,public=None,type=None):
        """往自己下面创建仓库
        
        :params id: 用户的login或id
        :params name: 仓库名称
        :params slug: slug
        :params description: 说明
        :params public: 0 私密, 1 内网公开, 2 全网公开
        :params type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'name': name,
            'slug': slug,
            'description': description,
            'public': int(public),
            'type': type
        }
        url = BASE_PATH + REPO_CREATE_USER_PATH + id + '/repos'
        r = post(url=url,headers=self.header,params=params)
        return r.json()

    def create_group(self,groupid=None,name=None,slug=None,description=None,public=None,type=None):
        """往组织创建仓库
        
        :params groupid: 组织的login或id
        :params name: 仓库名称
        :params slug: slug
        :params description: 说明
        :params public: 0 私密, 1 内网公开, 2 全网公开
        :params type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'name': name,
            'slug': slug,
            'description': description,
            'public': int(public),
            'type': type
        }
        url = BASE_PATH + REPO_CREATE_GROUP_PATH + groupid + '/repos'
        r = post(url=url,headers=self.header,params=params)
        return r.json()

    def detail(self,id,type):
        """获取仓库详情
        
        :params id: 仓库的namespace或id
        :params type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'type': type
        }
        url = BASE_PATH + REPO_DETAIL_PATH + id
        r = get(url=url,headers=self.header,params=params)
        return r.json()

    def update(self,id=None,name=None,slug=None,toc=None,description=None,public=None):
        """更新仓库信息
        
        :params id: 仓库的namespace或id
        :params name: 仓库名称
        :params slug: slug
        :params toc: 更新文档仓库的目录信息
        :params description: 说明
        :params public: 0 私密, 1 内网公开, 2 全网公开
        """
        params = {
            'name': name,
            'slug': slug,
            'toc': toc,
            'description': description,
            'public': public
        }
        url = BASE_PATH + REPO_UPDATE_PATH + id
        r = put(url=url,headers=self.header,params=params)
        return r.json()

    def delete(self,id):
        """删除仓库
        
        :params id: 仓库的namespace或id
        """
        url = BASE_PATH + REPO_DELETE_PATH + id
        r = delete(url=url,headers=self.header)
        return r.json()

    def toc(self,id):
        """获取一个仓库的目录结构
        
        :params id: 仓库的namespace或id
        """
        url = BASE_PATH + REPO_TOC_PATH + id + '/toc'
        r = get(url=url,headers=self.header)
        return r.json()

    def search(self,keywords=None,type=None):
        """基于关键字搜索仓库
        
        :params: keywords: :仓库模糊搜索的关键词
        :params: type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'q': keywords,
            'type': type
        }
        url = BASE_PATH + REPO_SEARCH_PATH
        r = get(url=url,headers=self.header,params=params)
        return r.json()
