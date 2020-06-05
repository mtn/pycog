"""
Useful functions.

"""
import pickle
import errno
import os
import signal
import sys

def println(line):
    sys.stdout.write(line)
    sys.stdout.flush()

def print_settings(settings, indent=3, title="=> settings"):
    """
    Pretty print.

    """
    print(title)
    maxlen = max([len(s) for s in settings])
    for k, v in settings.items():
        print(indent*' ' + '| {}:{}{}'.format(k, (maxlen - len(k) + 1)*' ', v))
    sys.stdout.flush()

def get_here(file):
    return os.path.abspath(os.path.dirname(file))

def get_parent(dir):
    return os.path.abspath(os.path.join(dir, os.pardir))

def mkdir_p(path):
    """
    Portable mkdir -p

    """
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def dump(filename, obj):
    """
    Disable keyboard interrupt while pickling.

    """
    s = signal.signal(signal.SIGINT, signal.SIG_IGN)
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    signal.signal(signal.SIGINT, s)
