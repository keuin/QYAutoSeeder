# QingYing Auto Seeder
# Create:  Keuin
# Version: 1.0 alpha - only for test use

# TODO:
# 1. Get updates from spider.py
# 2. Send new tasks to taskpool.py
# 3. Retrieve finished tasks and get media info from infoman.py
# 4. Send to poster.py
# 5. Send to seeder.py

import json
import spider
import taskpool
import infoman
import poster
import seeder
import time


with open('seeder_settings.py', 'r') as f:
    config = json.loads(f.read())

tc_conf = {
    'address':'localhost',
    'port':9091,
    'user':None,
    'password':None
}

Spider = spider.QYSpider(spider.def_site_list, spider_callback)
Spider.activiate()
TaskPool = taskpool.QYTaskPool(tc_conf)
InfoMan = infoman.QYInfoMan()
# TaskPool.start_all()

def spider_callback(torrent_list):
    print('Got %d new torrent(s).' % len(torrent_list))
    # TODO(1)(2)
    TaskPool.add_tasks(torrent_list)


while True:
    new_finished = TaskPool.retrieve()
    for t in new_finished:
        
    time.sleep(1)