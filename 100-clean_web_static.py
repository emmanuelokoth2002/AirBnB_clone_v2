#!/usr/bin/python3
# deletes out-of-date archives, using the function do_clean
from fabric.api import env, run, local
from fabric.context_managers import lcd
from datetime import datetime

# Define the remote hosts
env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """Delete out-of-date archives."""
    number = int(number)
    if number < 0:
        return
    elif number == 0 or number == 1:
        number = 2
    else:
        number += 2

    with lcd("versions"):
        local("ls -1t | tail -n +{} | xargs rm -f".format(number))

    with lcd("/data/web_static/releases"):
        run("ls -1t | tail -n +{} | xargs rm -rf".format(number))
