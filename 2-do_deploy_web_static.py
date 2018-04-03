#!/usr/bin/python3
''' deploy code '''

from fabric.api import put, run, env
import os

env.hosts = ['34.228.66.63', '54.166.228.243']


def do_deploy(archive_path):
    ''' script that deploys package '''
    if not os.path.exists(archive_path):
        return False

    fileName = os.path.basename(archive_path)
    tmpPath = "/tmp/{}".format(fileName)
    name, ext = os.path.splitext(fileName)
    newPath = "/data/web_static/releases/{}/".format(name)
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(newPath))
        run("tar -xzf {} -C {}".format(tmpPath, newPath))
        run("rm {}".format(tmpPath))
        run("mv {}/web_static/* {}/".format(newPath, newPath))
        run("rm -rf {}/web_static".format(newPath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newPath))
        return True
    except:
        return False
