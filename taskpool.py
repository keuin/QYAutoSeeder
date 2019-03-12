# QY Taskpool: Control Transmission via RPC, download torrents,
# get media info from infoman.py and talk to poster.py

# Written by: Keuin

# TODO:
# 1. Download torrents.
# 2. Get information.
# 3. Send to poster.py.

import transmissionrpc


class QYTaskPool:

    def QYTaskPool(self, transmission_rpc_configure):
        self.__tc = transmissionrpc.Client(
            transmission_rpc_configure['address'],
            transmission_rpc_configure['port'],
            transmission_rpc_configure['user'],
            transmission_rpc_configure['password'])

    def add_tasks(task_list):
        for t in task_list:
            self.__tc.add_torrent(t)
            print('torrent "%s" added.' % t)

    def start_all(self):
        if hasattr(self,'__tc'):
            self.__tc.start_all()

    def retrieve(self): # Get new finished tasks
        # TODO
        return []