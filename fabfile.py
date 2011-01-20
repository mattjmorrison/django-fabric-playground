from fabric.api import env, run, cd

env.hosts = ["bowser"]

def deploy():
    try: #archive old one if it's already there
        run("mv something old_something")
    except:
        pass

    run('mkdir something')
    print run('ls -la')


