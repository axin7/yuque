from .base import Base


class Group(Base):
    """
    获取组织信息
    """
    _groupsUrl = '/users/'     # 获取某个用户的加入的组织列表  注：需在最后加 用户id/groups或login/groups
    _groupsPublicUrl = '/groups'    #获取公开组织列表
    _groupCreateUrl = '/groups'    # 创建组织
    _groupDetailUrl = '/groups/'    # 获取单个组织的详细信息  注：需在最后加 用户id或login
    _groupUpdateUrl = '/groups/'    # 更新单个组织的详细信息  注：需在最后加 用户id或login
    _groupDeleteUrl = '/groups/'    # 删除组织
    _groupUsersUrl = '/groups/'    # 获取组织成员信息  注：需在最后加 用户id/users或login/users
    _groupUpdateUsersUrl = '/groups/'    # 增加或更新组织成员  注：需在最后加 用户group_login//users/login或:group_id/users/login
    _groupDeleteUsersUrl = '/groups/'    # 删除组织成员  注：需在最后加 用户group_login//users/login或:group_id/users/login

    def groups(self):
        """获取某个用户的加入的组织列表"""
        url = self._baseUrl + self._groupsUrl + self.id + '/groups'
        r = self._get(url=url)
        return r.json()

    def groups_public(self):
        """获取公开组织列表"""
        url = self._baseUrl + self._groupsPublicUrl
        r = self._get(url=url)
        return r.json()

    def create(self,name,login,description=None):
        """创建组织

        :param name: 组织名称
        :param login: login
        :param description: 介绍
        """
        params = {
            'name': name,
            'login': login,
            'description': description
        }
        url = self._baseUrl + self._groupCreateUrl
        r = self._post(url=url,params=params)
        return r.json()

    def detail(self,groupid):
        """获取单个组织的详细信息
        
        :param groupid: 组织的login或id
        """

        url = self._baseUrl + self._groupDetailUrl + groupid
        r = self._get(url=url)
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
        url = self._baseUrl + self._groupUpdateUrl + groupid
        r = self._put(url=url,params=params)
        return r.json()

    def delete(self,groupid):
        """删除组织

        :param groupid: 组织的login或id
        """
        url = self._baseUrl + self._groupDeleteUrl + groupid
        r = self._delete(url=url)
        return r.json()

    def users(self,groupid):
        """获取组织成员信息

        :param groupid: 组织的login或id
        """
        url = self._baseUrl + self._groupUsersUrl + groupid + '/users'
        r = self._get(url=url)
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
        url = self._baseUrl + self._groupUpdateUsersUrl + groupid + '/users/' + login
        r = self._put(url=url,params=params)
        return r.json()

    def delete_user(self,groupid,login):
        """删除组织成员
        
        :param groupid: 组织的login或id
        :param login: 用户的login
        """
        url = self._baseUrl + self._groupDeleteUsersUrl + groupid + '/users/' + login
        r = self._delete(url=url)
        return r.json()