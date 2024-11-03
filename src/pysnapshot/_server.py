import debuglater
import sys
from types import TracebackType
from typing import Any, Callable, Type
import debuglater
import debugpy

def debugpy_excepthook(
    endpoint,
    type_: Type[BaseException],
    value: BaseException,
    traceback: TracebackType,
) -> Any:
    """
    Callback called when an exception is hit and debugpy is enabled.
    """
    if not debugpy.is_client_connected():
        print("Exception thrown. Waiting for debugpy on port 5678.")
        debugpy.listen(endpoint)
        debugpy.wait_for_client()

    import pydevd
    import threading

    py_db = pydevd.get_global_debugger()
    thread = threading.current_thread()
    additional_info = py_db.set_additional_thread_info(thread)
    additional_info.is_tracing += 1
    try:
        arg = (type_, value, traceback)
        py_db.stop_on_unhandled_exception(py_db, thread, additional_info, arg)
    finally:
        additional_info.is_tracing -= 1

def tb_callback(_tb):
    global tb
    tb = _tb

def launch_debug_server(filename, endpoint):
    dump = debuglater.debug_dump(filename, tb_callback)
    debugpy_excepthook(endpoint, dump["type"], dump["value"], dump["traceback"])

