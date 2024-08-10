#!/usr/bin/python3
"""
A Fabric script based on the file '1-pack_web_static.py' that distributes
+an archive to the web servers, using the function 'do_deploy'.
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['18.209.180.79', '100.25.152.221']


def do_deploy(archive_path):
    """Function that distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_nm = archive_path.split("/")[-1]
        no_extn = file_nm.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_extn))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_nm, path, no_extn))
        run('rm /tmp/{}'.format(file_nm))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extn))
        run('rm -rf {}{}/web_static'.format(path, no_extn))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extn))
        return True
    except:
        return False
