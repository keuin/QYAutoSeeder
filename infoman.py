# QY Infoman: Get media information from given sites, 
# generate snapshots from specific movie or music file.

# Written by: Keuin

# TODO:
# 1. Get media info from imdb.com.
# 2. Take snapshots or music clips.
# 3. Return to taskpool.py.


import urllib

class QYInfoMan:
    def search(self,keyword):
        url = 'https://www.imdb.com/find?q=%s' % urllib.parse.quote(keyword)
        # TODO: Get information from imdb.com webpage

