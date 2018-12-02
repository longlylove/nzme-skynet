# -*- coding: utf-8 -*-
from nzme_skynet.core.api import helper
import logging

logger = logging.getLogger('ApiClient')

class Resource(object):
    """
    Resource request wrapper, creates new :class:`Resource` object

    :param uri: path to uri
    :param base_uri: (optional) base uri
    :param base_url: base url
    :param req: request session
    """

    def __init__(self, uri=None, base_uri=None, base_url=None, req=None):
        self._resource_url = helper.create_resource_url(base_url, uri, base_uri)
        self._req = req

    def get(self, **kwargs):
        """
        Sends a GET request

        :param kwargs: optional arguments to pass to request.get method
        :return: :class:`requests.Response` object.
        """
        return self._request('GET', self._resource_url, **kwargs)

    def post(self, **kwargs):
        """
        Send a POST request

        :param kwargs: optional arguments to pass to request.post method
        :return: :class:`requests.Response` object.
        """
        return self._request('POST', self._resource_url, **kwargs)

    def put(self, path=None, **kwargs):
        """
        Send a PUT request

        :param kwargs: optional arguments to pass to request.put method
        :return: :class:`requests.Response` object.
        """
        return self._request('PUT', self._append_path(path), **kwargs)

    def delete(self, path=None, **kwargs):
        """
        Send a POST request

        :param kwargs: optional arguments to pass to request.delete method
        :return: :class:`requests.Response` object.
        """
        return self._request('DELETE', self._append_path(path), **kwargs)

    def _request(self, method, url, **kwargs):
        logger.debug('(SENT REQUEST) Method: %s, URL: %s' % (method, self._resource_url))
        response =  self._req.request(method, url, **kwargs)
        logger.debug('(RECEIVED RESPONSE) Code: %s, URL: %s' % (response.status_code, self._resource_url))
        return response

    @property
    def resource_url(self):
        """
        Returns full url

        :return: full resource path
        """
        return self._resource_url

    def _append_path(self, path):
        """
        Append path to full url
        :param path: (string) path to add
        :return: full url
        """
        if path is not None:
            try:
                url = self.resource_url + path
            except Exception:
                raise Exception("path mus be of format: /path[../../]")
        return url