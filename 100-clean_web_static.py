#!/usr/bin/python3
""" Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean
"""

import os
from fabric.api import *

env.hosts = ['3.84.238.29', '18.210.33.105']

def do_clean(number=0):
    """ protoype to delete out of date archiives
    args:
    number:number of the archives, including the most recent, to keep
    If number is 0 or 1, keep only the most recent version of your archive.
    f number is 2, keep the most recent, and second most recent versions of your archive
    """
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for x in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

with cd("/data/web_static/releases"):
    archives = run("ls -tr").split()
    archives = [a for a in archives if "web_static_" in a]
    [archives.pop() for i in range(number)]
    [run("rm -rf ./{}".format(a)) for a in archives]
