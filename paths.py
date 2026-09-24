import os
import sys


def root():
    """Returns the project's root folder.

    Works both when running via 'python pricing_pipeline.py' (or any individual
    script) and via an executable built with PyInstaller, and does not
    depend on the current working directory (cwd) at runtime -- that's
    why it's safe to call this from inside a .bat file, Task Scheduler,
    or anywhere else.
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def path(env_var, default):
    """Resolves a path coming from .env relative to the project root.

    If the value stored in .env is already an absolute path (e.g. you
    want to store Ars on another drive), it's used as-is, unmodified.
    If it's relative (e.g. 'Ars', 'instantclient_23_0'), it's resolved
    from the project root -- not from the cwd.
    """
    value = os.getenv(env_var, default)
    if os.path.isabs(value):
        return value
    return os.path.join(root(), value)
