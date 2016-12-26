"""
This file inherits the spirit of an Amazon article I read a while back about
how much Amazon communicates via APIs of all their team / services ... it forces them
to make well-thought APIs. Since I have a bit of historical data from Excel that I'm
importing - I had two options. 1) Just use django's native methods (get_or_create, etc)
or 2) eat my own dog food and use post/puts to create the historical data. I've tested
1) and I know it works ... but I've decided to with option 2 since empirically a
battle-tested API will make the eventual iOS / Android apps much easier to develop.
"""
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token

import requests


class BetterSelfAPIAdapter(object):
    """
    Takes a user, retrieves the token, accesses RESTful endpoints.
    """
    def __init__(self, domain, user):
        self.domain = domain
        self.user = user
        self.api_token = Token.objects.get_or_create(user=user)
        self.headers = {'Authorization': 'Token {}'.format(self.api_token.token)}

    def get_resource_endpoint_url(self, resource):
        url = reverse(resource.RESOURCE_NAME)
        return self.domain + url

    def get_resource(self, resource, parameters=None):
        resource_endpoint = self.get_resource_endpoint_url(resource)
        response = requests.get(resource_endpoint, params=parameters, headers=self.headers)