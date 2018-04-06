#!/usr/bin/python3
''' full deploy '''

do_pack = __import__('1-pack_web_static')
do_deploy = __import__('2-do_deploy_web_static')


def deploy():
    ''' deploy script '''
    file_path = do_pack.do_pack()
    if file_path is None:
        return False
    return do_deploy.do_deploy(file_path)
