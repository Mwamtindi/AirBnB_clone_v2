#!/usr/bin/python3
"""
A Fabric script based on the file '2-do_deploy_web_static.py' that creates
+and distributes an archive to the web servers, using the function deploy
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['18.209.180.79', '100.25.152.221']


def do_pack():
    """generates a .tgz archive file"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_nam = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_nam))
        return file_nam
    except Exception:
        return None


def do_deploy(archive_path):
    """Function that distributes an archive to the web servers"""
    if not exists(archive_path):
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
    except Exception:
        return False


def deploy():
    """fxn that creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
