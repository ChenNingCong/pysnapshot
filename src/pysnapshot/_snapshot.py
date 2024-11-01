import sys

def install_exception_snapshot_hook(filename):
    import debuglater
    sys.excepthook = debuglater.excepthook_factory(filename, sys.excepthook)

def snapshot(filename, echo=True):
    import debuglater
    try:
        raise Exception('Snapshot')
    except Exception as e:
        _type, value, traceback = sys.exc_info()
    debuglater.run(filename, echo=True, type=_type, value=value, tb=traceback)
