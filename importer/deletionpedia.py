# -*- coding: UTF-8 -*-

# This script mirrors all normal pages from Deletionpedia.org to Deletedwiki.com

import mwclient
import codecs

our = mwclient.Site(('http', 'deletedwiki.com'), '/')
theirs = mwclient.Site(('http', 'deletionpedia.org'), '/w/')


our.login('Bot', '#PASSWORD_HERE#')

for page in theirs.pages:
    if page.namespace is not 0:
        continue
    print "Importing \"%s\"" % page.page_title
    ourPage = our.pages[page.page_title]
    ourPage.save(text=page.text(), summary='Imported from deletionpedia.org (en)')
