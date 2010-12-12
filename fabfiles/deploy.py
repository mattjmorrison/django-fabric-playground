from fabric.api import env, run, cd

ip = "184.106.218.153"
user = "root"
password = "fabricsamplesR7gKg1Q1"

env.hosts = [ip]
env.user = user
env.password = password

def deploy():
    run('mkdir something')
    print run('ls -la')


