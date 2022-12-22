#!/usr/bin/python3
"""compress files and and deploy to servers"""
from fabric.api import local
from fabric.operations import run, env, put
import time
import os


env.user = 'ubuntu'
env.hosts = ['52.204.97.13', '35.174.207.85']


def do_pack():
    """compress files in web_static
       create directory versions to store compressed file"""
    dest = 'versions/web_static_{}.tgz'.format(time.strftime("%Y%m%d%H%M%S"))
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(dest))
    except Exception:
        return None
    return dest


def do_deploy(archive_path):
    """deploy local files to remote server"""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    remotefile = '/tmp/' + archive_path[9:]
    dest = '/data/web_static/releases/' + archive_path[9:-4]
    run("sudo mkdir -p {}".format(dest))
    run("sudo tar -xzvf {} -C {}".format(remotefile, dest))
    run("sudo rm -f {}".format(remotefile))
    run("sudo mv {}/web_static/* {}".format(dest, dest))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(dest))
    print('New version Deployed!')
    return True
