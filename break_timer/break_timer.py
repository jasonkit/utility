#!/usr/bin/python
import sys
import os
import time
import signal

pid_file_name = "/tmp/break_timer.pid"

def daemonize():
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        sys.exit(1)

    os.chdir("/")
    os.setsid()
    os.umask(0)

    try:
        pid = os.fork()
        if pid > 0:
            pid_f = open(pid_file_name,"w+")
            pid_f.write(str(pid))
            pid_f.close()
            sys.exit(0)

    except OSError, e:
        sys.exit(1)

def main():
   
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print "usage: break_timer INTERVAL|stop [MESSAGE]"
        print "INTERVAL: [0-9]+[s|m|h]"
        sys.exit(1)

    if os.path.isfile(pid_file_name):
        pid_f = open(pid_file_name)
        pid = int(pid_f.read())
        pid_f.close()
        os.unlink(pid_file_name)
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError, e:
            sys.exit(1)

    if sys.argv[1] == "stop":
        sys.exit(0)

    daemonize()

    while True:
        interval = sys.argv[1]
        
        if interval[-1] == 'm':
            interval = int(float(interval[0:-1])*60)
        elif interval[-1] == 'h':
            interval = int(float(interval[0:-1])*3600)
        else:
            interval = int(interval)
        
        time.sleep(interval)

        msg = "Time to have a break!"

        if len(sys.argv) == 3:
            msg = sys.argv[2]

        os.system("terminal-notifier -message '%s' -title 'Break Timer' -sound 'default'"%msg)

if __name__ == "__main__":
    main()

