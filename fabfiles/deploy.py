from fabric.api import env, run, cd

env.hosts = ["184.106.218.153"]
env.user = "root"
env.password = "fabricsamplesR7gKg1Q1"

def deploy():
    run('mkdir something')
    print run('ls -la')


