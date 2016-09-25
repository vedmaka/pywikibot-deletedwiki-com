# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from pywikibot import family, config, deprecated

__version__ = '$Id$'

class Family(family.Family):

    def __init__(self):
        family.Family.__init__(self)

        #super(Family, self).__init__()
        self.name = 'deleted'

        #langlist = ['en'] #[ 'en', 'fr', 'fi', 'nl', 'de', 'es', 'it', 'pt', 'sv' ]
        #self.langs = { x: x for x in langlist }

        self.langs = {
            'en': 'deletedwiki.com',
        }

    def hostname(self, code):
        return 'deletedwiki.com'

    @deprecated('APISite.version()')
    def version(self, code):
        """Return the version for this family."""
        return "1.26.3"

    def scriptpath(self, code):
        """Return the script path for this family."""
        return ''

    def apipath(self, code):
        """Return the path to api.php for this family."""
        return '/api.php'
