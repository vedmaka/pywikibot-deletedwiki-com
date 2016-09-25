# -*- coding: UTF-8 -*-

import mwclient


class SourceWiki:
    def __init__(self, url, prefix='/', user=False, password=False):
        self.url = url
        self.prefix = prefix
        self.user = user
        self.password = password
        self.site = mwclient.Site(url, prefix)
        if user:
            self.login()

    def login(self):
        self.site.login(self.user, self.password)

    def printinfo(self):
        print "{0} version is {1}".format(self.site.host, self.site.version)
