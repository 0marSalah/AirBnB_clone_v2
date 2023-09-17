#!/usr/bin/python3
"""a Fabric script (based on the file 3-deploy_web_static.py)"""

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['54.236.50.147	', '54.87.228.212']


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    ret = False
    if not os.path.exists(archive_path):
        return ret
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        ret = True
    except Exception:
        ret = False
    return ret


def deploy():
    """Archives and deploys the static files to the host servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
  archives = os.listdir("versions")
  if number is 2:
    for i in archives[2:]:
        os.unlink("versions/{}".format(i))
        run("rm -f versions/{}".format(i))
        run("rm -f /data/web_static/releases/{}".format(i))
        print("Clean is done successfully!")
  elif number is 1 or number is 0:
    for i in archives[1:]:
        os.unlink("versions/{}".format(i))
        run("rm -f versions/{}".format(i))
        run("rm -f /data/web_static/releases/{}".format(i))
        print("Clean is done successfully!")
