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
            run('pip install -r requirements.txt')
            run('python manage.py collectstatic --noinput')

    run('touch %s' % path_wsgi)


def download():
    """synchronizes the local db and media files from the remote ones"""
    foo = '/srv/data_rocamadour/www/coop.medor/'
    local('scp -P 2222 medor@medor.coop:%sdb/medor.db .' % foo)
    local("rsync -e 'ssh -p 2222' -avz --progress --stats medor@medor.coop:%sdocs/media ." % foo)

