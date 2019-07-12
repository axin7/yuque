from .base import Base


class User(Base):
    """
    获取用户信息
    """
    _userInfoUrl = '/users/'      # 获取单个用户信息   注：需在最后加 用户id或login      
    _userInfoAuthUrl = '/user'   # 获取认证的用户的个人信息  

    def info(self):
        """获取单个用户信息"""
        url = self._baseUrl + self._userInfoUrl + self.id
        r = self._get(url=url)
        return r.json()
            
    def info_auth(self):
        """获取认证用户的个人信息"""
        url = self._baseUrl + self._userInfoAuthUrl
        r = self._get(url=url)
        return r.json()

