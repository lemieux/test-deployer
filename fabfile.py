from fabric.api import *

def bootstrap():
    print env.virtualenv_path
    print 'bootrapping!'

def local():
    print env.virtualenv_path
    print 'it is local!'

def deploy():
   print 'deploying!'
