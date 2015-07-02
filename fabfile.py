import os.path
from fabric.api import run, local, put, cd, sudo, env, prefix
from fabric.contrib.console import confirm


env.hosts = ['medor@92.243.16.55']
env.port = 2222
env.path = '/srv/data_rocamadour/www/coop.medor'


def remote_info():
    run('uname -a')


def deploy(branch='master'):
    """deploys to previously setup environment"""

    with cd('%(path)s/app' % env):
        run('git pull origin %s' % branch)

        with prefix('source %(path)s/venv/bin/activate' % env):
            run('pip install -r requirements.txt')
            run('python manage.py collectstatic --noinput')

    run('touch %(path)s/app/medor/wsgi.py' % env)


def migrate():
    """deploys to previously setup environment"""

    with cd('%(path)s/app' % env):
        with prefix('source %(path)s/venv/bin/activate' % env):
            run('python manage.py migrate')

    run('touch %(path)s/app/medor/wsgi.py' % env)


def download():
    """synchronizes the local db and media files from the remote ones"""
    local('scp -P %(port)s %(host)s:%(path)s/db/medor.db .' % env)
    local("rsync -e 'ssh -p %(port)s' -avz --progress --stats %(host)s:%(path)s/docs/media ." % env)
