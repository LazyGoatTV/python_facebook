"""
    Base client for API.
"""
import inspect

from .graph import GraphAPI, BasicDisplayAPI
from .base_resource import BaseResource


def _is_resource_cls(obj):
    return isinstance(obj, BaseResource)


class BaseApi(GraphAPI):
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        resources = inspect.getmembers(cls, _is_resource_cls)
        for name, resource in resources:
            resource_cls = type(resource)
            resource = resource_cls(self)
            setattr(self, name, resource)
        return self


class BaseBasicDisplayApi(BasicDisplayAPI, BaseApi):
    ...
