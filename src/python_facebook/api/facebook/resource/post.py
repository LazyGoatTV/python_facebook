"""
    Apis for post.
"""

from typing import Dict, Optional, Union

from ....utils.constant import *
from ...base_resource import BaseResource
from ...facebook.common_edges import CommentsEdge
from ....models.post import Post
from ....utils.params_utils import enf_comma_separated


class FacebookPost(BaseResource, CommentsEdge):
    def get_info(
        self,
        post_id: Optional[str],
        fields: Optional[Union[str, list, tuple]] = None,
        return_json: bool = False,
    ) -> Union[Post, dict]:
        """
        Get information about a Facebook post

        :param post_id: ID for the post.
        :param fields: Comma-separated id string for data fields which you want.
            You can also pass this with an id list, tuple.
        :param return_json: Set to false will return a dataclass for post.
            Or return json data. Default is false.
        :return: Post information
        """

        if fields is None:
            fields = POST_PUBLIC_FIELDS + POST_CONNECTIONS_SUMMERY_FIELDS

        data = self.client.get_object(
            object_id=post_id, fields=enf_comma_separated(field="fields", value=fields)
        )
        if return_json:
            return data
        else:
            return Post.new_from_json_dict(data=data)

    def get_batch(
        self,
        ids: Optional[Union[str, list, tuple]],
        fields: Optional[Union[str, list, tuple]] = None,
        return_json: bool = False,
    ) -> Union[Dict[str, Post], dict]:
        """
        Get batch posts information by ids.

        :param ids: IDs for the posts.
        :param fields: Comma-separated id string for data fields which you want.
            You can also pass this with an id list, tuple.
        :param return_json: Set to false will return a dataclass for post.
            Or return json data. Default is false.
        :return: Posts information.
        """

        ids = enf_comma_separated(field="ids", value=ids)

        if fields is None:
            fields = POST_PUBLIC_FIELDS + POST_CONNECTIONS_SUMMERY_FIELDS

        data = self.client.get_objects(
            ids=ids, fields=enf_comma_separated(field="fields", value=fields)
        )
        if return_json:
            return data
        else:
            return {
                post_id: Post.new_from_json_dict(item) for post_id, item in data.items()
            }
