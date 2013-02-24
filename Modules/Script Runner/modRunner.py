import subprocess

'''modulePath: path to the module, arg: parameters to pass'''
def runner(modulePath, arg):

    print 'Runner.py started'
    print 'Running program:', str(modulePath), 'with arguements:', str(arg)
    subprocess.call(["C:\Python27\python.exe", modulePath, arg])