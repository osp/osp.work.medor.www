import os.path
from fabric.api import run, local, put, cd, sudo, env, prefix
from fabric.contrib.console import confirm


env.hosts = ['medor@92.243.16.55']
env.port = 2222
env.path = '/srv/data_rocamadour/www/coop.medor/app'


def deploy():
    """deploys to previously setup environment"""
    path_activate = '/srv/data_rocamadour/www/coop.medor/venv/bin/activate'
    path_wsgi = '/srv/data_rocamadour/www/coop.medor/app/medor/wsgi.py'

    with cd(env.path):
        run('git pull origin master')

        with prefix('source %s' % path_activate):
            run('python manage.py collectstatic --noinput')

    run('touch %s' % path_wsgi)
