"""
    Client for Instagram Basic Display API.
"""

from ...api.base_client import BaseBasicDisplayApi
from ...api.instagram_basic import resource as rs


class IGBasicDisplayApi(BaseBasicDisplayApi):
    """
    Api class for Instagram basic display api
    """

    user = rs.IGBasicUser()
    media = rs.IGBasicMedia()
