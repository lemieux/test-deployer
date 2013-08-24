from fabric import *

def bootstrap():
    print env.virtualenv_path
    print 'bootrapping!'

def local():
    print 'it is local!'

def deploy():
   print 'deploying!'
