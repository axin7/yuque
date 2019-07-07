

class Base(object):
    # 基本路径
    _baseUrl = 'https://www.yuque.com/api/v2'    

    # 用户路径
    _userInfoUrl = '/users/'      # 获取单个用户信息   注：需在最后加 用户id或login      
    _userInfoAuthUrl = '/user'   # 获取认证的用户的个人信息                           

    # 组织路径
    _groupsUrl = '/users/'     # 获取某个用户的加入的组织列表  注：需在最后加 用户id/groups或login/groups
    _groupsPublicUrl = '/groups'    #获取公开组织列表
    _groupCreateUrl = '/groups'    # 创建组织
    _groupDetailUrl = '/groups/'    # 获取单个组织的详细信息  注：需在最后加 用户id或login
    _groupUpdateUrl = '/groups/'    # 更新单个组织的详细信息  注：需在最后加 用户id或login
    _groupDeleteUrl = '/groups/'    # 删除组织
    _groupUsersUrl = '/groups/'    # 获取组织成员信息  注：需在最后加 用户id/users或login/users
    _groupUpdateUsersUrl = '/groups/'    # 增加或更新组织成员  注：需在最后加 用户group_login//users/login或:group_id/users/login
    _groupDeleteUsersUrl = '/groups/'    # 删除组织成员  注：需在最后加 用户group_login//users/login或:group_id/users/login

    #仓库路径
    _reposUserUrl = '/users/'    # 获取某个用户的仓库列表  注：需在最后加 用户login/repos或id/repos
    _reposGroupUrl = '/groups/'    # 获取某个组织的仓库列表  注：需在最后加 组织login/repos或id/repos
    _repoUserCreateUrl = '/users/'    # 往自己下面创建仓库  注：需在后面加 用户login/repos或id/repos
    _repoGroupCreateUrl = '/users/'    # 往组织创建仓库  注：需在最后加 组织login/repos或id/repos
    _repoDetailUrl = '/repos/'    # 获取仓库详情  注：需在最后加 仓库id或namespace
    _repoUpdateUrl = '/repos/'    # 更新仓库信息  注：需在最后加 仓库id或namespace
    _repoDeleteUrl = '/repos/'    # 删除仓库  注：需在最后加 仓库id或namespace
    _repoTocUrl = '/repos/'    # 获取一个仓库的目录结构  注：需在最后加 仓库namespace/toc或id/toc 
    _repoSearchUrl = '/search/repos'    # 基于关键字搜索仓库

    #文档路径
    _docsUrl = '/repos/'    # 获取某个仓库的文档列表  注：需在最后加 仓库namespace/docs或id/docs
    _docDetailUrl = '/repos/'    # 获取单篇文档的详细信息 注：需在最后加 仓库namespace/docs/slug或repo_id/docs/id
    _docCreateUrl = '/repos/'    # 创建文档  注：需在最后加 仓库namespace/docs或id/docs
    _docUpdateUrl = '/repos/'    # 更新文档  注：需在最后加 仓库namespace/docs/id或repo_id/docs/id
    _docDeleteUrl = '/repos/'    # 删除文档  注：需在最后加 仓库namespace/docs/id或repo_id/docs/id

    # 请求头
    _headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }