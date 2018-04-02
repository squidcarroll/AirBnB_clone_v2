#!/usr/bin/python3
''' package into tar '''

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    ''' runs the command '''
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")

    version = "versions/web_static_{}.tgz".format(date)
    try:
        local("tar -cvzf {} web_static".format(version))
        return version
    except:
        return None
