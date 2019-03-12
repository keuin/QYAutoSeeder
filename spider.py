# QY Spider: Automatically grab torrents from selected sites and send to download list (taskpool.py).

# Written by: Keuin

# TODO:
# 1. Login to given PT sites.
# 2. Automatically check changes.
# 3. Add updates to our task list.

import threading

TORRENT_DIR = '.\\torrents'

def_site_list = {
    'something':'here'
}

class QYSpider:
    def QYSpider(self, site_list, callback_function):
        self.site_list = site_list
        self.cb_func = callback_function

    def activiate(self):
        self.__th = QYSpiderThread(self)
        self.__th.start()

    def join(self):
        if hasattr(self, '__th') and self.__th != None:
            self.__th.join()


class QYSpiderThread(threading.Thread):
    def QYSpiderThread(self, spider_body):
        self.__spider = spider_body

    def run(self):
        pass
        # TODO
        torrent_list = [] # A torrent filename list


        # finish:
        self.__spider.cb_func([TORRENT_DIR + '\\' + torrent for torrent in torrent_list])
