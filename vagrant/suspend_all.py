#!/usr/bin/env python

"""
Gracefully shuts down all running VMs.
"""

import contextlib
import os
import sys


@contextlib.contextmanager
def cwd(path):
    cur_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(cur_dir)


def main():
    for name in os.listdir('.'):
        if os.path.isdir(name):
            if os.path.isfile(os.path.join(name, 'Vagrantfile')):
                with cwd(name):
                    print(">>> suspend %s <<<" % name)
                    ret = os.system('vagrant suspend')
                    if ret != 0:
                        sys.exit(ret)


if __name__ == '__main__':
    main()