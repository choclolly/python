import os
import datetime


def get():
    # service list
    service = ['Jps'
        , 'EmbeddedServer'
        , 'QuorumPeerMain'
        , 'NodeManager'
        , 'ResourceManager'
        , 'NameNode'
        , 'SecondaryNameNode'
        , 'HMaster'
        , 'HRegionServer'
        , 'RunJar'

               ]
    # Traversal list
    for i in service:
        a = "jps | awk '{print $2}'|grep " + i
        res = os.system(a)
        # Determine whether the service is running
        if res != 0:
            print
            "%s is not running!" % (i)
            if i == 'HMaster':
                os.system('start-hbase.sh')
            elif i == 'HRegionServer':
                os.system('local-regionservers.sh start 1')
            elif i == 'EmbeddedServer':
                os.system('ranger-admin start')
            elif i == 'QuorumPeerMain':
                os.system('zkServer.sh start')
            else:
                print
                'restart Hadoop !!!'


class CheckService(object):

    def __init__(self):
        pass

    def timer_fun(self, sched_timer):
        flag = 0
        while True:
            now = datetime.datetime.now()
            if now == sched_timer:
                get(self)
                flag = 1
            else:
                if flag == 1:
                    sched_timer = sched_timer + datetime.timedelta(hours=1)
                    flag = 0


if __name__ == "__main__":
    cs = CheckService()
    sched_Timer = datetime.datetime(2017, 7, 25, 9, 14)
    print
    'run the timer task at {0}'.format(sched_Timer)
    cs.timer_fun(sched_Timer)
