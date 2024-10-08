import re
from urllib import request as urllib_request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request

from wagtail.embeds.exceptions import EmbedNotFoundException
from wagtail.embeds.finders.base import EmbedFinder


class RtvEmbedFinder(EmbedFinder):
    def __init__(self, providers=None, options=None):
        self._endpoints = {}

        for provider in providers:
            patterns = []

            endpoint = provider["endpoint"]

            for url in provider["urls"]:
                patterns.append(re.compile(url))

            self._endpoints[endpoint] = patterns

    def _get_endpoint(self, url):
        for endpoint, patterns in self._endpoints.items():
            for pattern in patterns:
                if re.match(pattern, url):
                    return endpoint

    def accept(self, url):
        """
        Returns True if this finder knows how to fetch an embed for the URL.

        This should not have any side effects (no requests to external servers)
        """

        # check if url matches any of the providers
        return self._get_endpoint(url) is not None

    def find_embed(self, url, max_width=None):
        """
        Takes a URL and max width and returns a dictionary of information about the
        content to be used for embedding it on the site.

        This is the part that may make requests to external APIs.
        """

        return {
            "title": "",
            "author_name": "Multimedijski center RTV Slovenija",
            "provider_name": "RTVSLO.si",
            "type": "video",
            "thumbnail_url": "",
            "width": "",
            "height": "",
            "html": f'<iframe class="custom-video-embed" src="{url}"></iframe>',
        }
