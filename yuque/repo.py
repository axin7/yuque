from .base import Base


class Repo(Base):
    """
    获取仓库信息
    """
    _reposUserUrl = '/users/'    # 获取某个用户的仓库列表  注：需在最后加 用户login/repos或id/repos
    _reposGroupUrl = '/groups/'    # 获取某个组织的仓库列表  注：需在最后加 组织login/repos或id/repos
    _repoUserCreateUrl = '/users/'    # 往自己下面创建仓库  注：需在后面加 用户login/repos或id/repos
    _repoGroupCreateUrl = '/users/'    # 往组织创建仓库  注：需在最后加 组织login/repos或id/repos
    _repoDetailUrl = '/repos/'    # 获取仓库详情  注：需在最后加 仓库id或namespace
    _repoUpdateUrl = '/repos/'    # 更新仓库信息  注：需在最后加 仓库id或namespace
    _repoDeleteUrl = '/repos/'    # 删除仓库  注：需在最后加 仓库id或namespace
    _repoTocUrl = '/repos/'    # 获取一个仓库的目录结构  注：需在最后加 仓库namespace/toc或id/toc 
    _repoSearchUrl = '/search/repos'    # 基于关键字搜索仓库
    
    def repos_user(self,id=None):
        """获取某个用户的仓库列表
        
        :param id: 用户的login或id
        """
        self.id = id if id else self.id
        url = self._baseUrl + self._reposUserUrl + self.id + '/repos'
        r = self._get(url=url)
        return r.json()

    def repos_group(self,groupid):
        """获取某个组织的仓库列表
        
        :param groupid: 组织的login或id
        """
        url = self._baseUrl + self._reposGroupUrl + groupid +'/repos'
        r = self._get(url=url)
        return r.json()

    def create(self,id=None,name=None,slug=None,description=None,public=None,type=None):
        """往自己下面创建仓库
        
        :param id: 用户的login或id
        :param name: 仓库名称
        :param slug: slug
        :param description: 说明
        :param public: 0 私密, 1 内网公开, 2 全网公开
        :param type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'name': name,
            'slug': slug,
            'description': description,
            'public': int(public),
            'type': type
        }
        self.id = id if id else self.id
        url = self._baseUrl + self._repoUserCreateUrl + self.id + '/repos'
        r = self._post(url=url,params=params)
        return r.json()

    def create_group(self,groupid=None,name=None,slug=None,description=None,public=None,type=None):
        """往组织创建仓库
        
        :param groupid: 组织的login或id
        :param name: 仓库名称
        :param slug: slug
        :param description: 说明
        :param public: 0 私密, 1 内网公开, 2 全网公开
        :param type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'name': name,
            'slug': slug,
            'description': description,
            'public': int(public),
            'type': type
        }
        url = self._baseUrl + self._repoGroupCreateUrl + groupid + '/repos'
        r = self._post(url=url,params=params)
        return r.json()

    def detail(self,type,namespace=None):
        """获取仓库详情
        
        :param namespace: 仓库的namespace或id
        :param type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'type': type
        }
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._repoDetailUrl + self.namespace
        r = self._get(url=url,params=params)
        return r.json()

    def update(self,namespace=None,name=None,slug=None,toc=None,description=None,public=None):
        """更新仓库信息
        
        :param namespace: 仓库的namespace或id
        :param name: 仓库名称
        :param slug: slug
        :param toc: 更新文档仓库的目录信息
        :param description: 说明
        :param public: 0 私密, 1 内网公开, 2 全网公开
        """
        params = {
            'name': name,
            'slug': slug,
            'toc': toc,
            'description': description,
            'public': public
        }
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._repoUpdateUrl + self.namespace
        r = self._put(url=url,params=params)
        return r.json()

    def delete(self,namespace=None):
        """删除仓库
        
        :param namespace: 仓库的namespace或id
        """
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._repoDeleteUrl + self.namespace
        r = self._delete(url=url)
        return r.json()

    def toc(self,namespace=None):
        """获取一个仓库的目录结构
        
        :param namespace: 仓库的namespace或id
        """
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._repoTocUrl + self.namespace + '/toc'
        r = self._get(url=url)
        return r.json()

    def search(self,keywords,type=None):
        """基于关键字搜索仓库
        
        :param keywords: 仓库模糊搜索的关键词
        :param type: 类型，Book - 文档，Design - 画板
        """
        params = {
            'q': str(keywords),
            'type': type
        }
        url = self._baseUrl + self._repoSearchUrl
        r = self._get(url=url,params=params)
        return r.json()