from .base import Base


class Doc(Base):
    """
    获取文档信息
    """
    _docsUrl = '/repos/'    # 获取某个仓库的文档列表  注：需在最后加 仓库namespace/docs或id/docs
    _docDetailUrl = '/repos/'    # 获取单篇文档的详细信息 注：需在最后加 仓库namespace/docs/slug或repo_id/docs/id
    _docCreateUrl = '/repos/'    # 创建文档  注：需在最后加 仓库namespace/docs或id/docs
    _docUpdateUrl = '/repos/'    # 更新文档  注：需在最后加 仓库namespace/docs/id或repo_id/docs/id
    _docDeleteUrl = '/repos/'    # 删除文档  注：需在最后加 仓库namespace/docs/id或repo_id/docs/id

    def docs(self,namespace=None):
        """获取一个仓库的文档列表"""
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._docsUrl + self.namespace + '/docs'
        r = self._get(url=url)
        return r.json()

    def detail(self,id,namespace=None):
        """获取单篇文档的详细信息

        :param id: 文档的 id或slug
        """
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._docDetailUrl + self.namespace + '/docs/' + id
        r = self._get(url=url)
        return r.json()

    def create(self,title,body,slug=None,public=None,format='markdown',namespace=None):
        """创建文档

        :param title: 标题
        :param body: format 描述的正文内容，最大允许 5MB
        :param slug: 文档 slug
        :param public: 0 - 私密，1 - 公开
        :param format: 支持 markdown 和 lake，默认为 markdown
        """
        params = {
            'title': title,
            'slug': slug,
            'public': public,
            'format': format,
            'body': body
        }
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._docCreateUrl + self.namespace + '/docs'
        r = self._post(url=url,params=params)
        return r.json()

    def update(self,id,title=None,slug=None,public=None,body=None,namespace=None):
        """更新文档

        :param id: 文档的 id   不是 slug ！
        :param title: 标题
        :param slug: 文档 slug
        :param public: 0 - 私密，1 - 公开
        :param body: 描述的正文内容
        """
        params = {
            'title': title,
            'slug': slug,
            'public': public,
            'body': body
        }
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._docUpdateUrl + self.namespace + '/docs/' + id
        r = self._put(url=url,params=params)
        return r.json()

    def delete(self,id,namespace=None):
        """删除文档

        :param id: 文档的 id   不是 slug ！
        """
        self.namespace = namespace if namespace else self.namespace
        url = self._baseUrl + self._docDeleteUrl + self.namespace + '/docs/' + id
        r = self._delete(url=url)
        return r.json()