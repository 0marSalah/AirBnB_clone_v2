#!/usr/bin/python3
"""
a Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives,
using the function do_clean.
"""

from os import listdir
from fabric.api import put, run, env

env.hosts = ['54.236.50.147', '54.87.228.212']

def do_clean(number=0):
  l = listdir("versions")
  if number is 2:
    for i in l[2:]:
        run("rm -f versions/web_static_{}".format(i))
        run("rm -f /data/web_static/releases/web_static_{}".format(i))
        print("Clean is done successfully!")
