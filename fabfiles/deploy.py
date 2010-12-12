from fabric.api import env, run, cd

env.hosts = ["ip"]
env.user = "user"
env.password = "password"

def deploy():
    try: #archive old one if it's already there
        run("mv something old_something")
    except:
        pass

    run('mkdir something')
    print run('ls -la')


