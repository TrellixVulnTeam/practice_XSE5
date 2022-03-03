import sys
from _typeshed import FileDescriptorLike
from socket import socket
from typing import Any, overload

# cyclic dependence with asynchat
_maptype = dict[int, Any]
_socket = socket

socket_map: _maptype  # undocumented

class ExitNow(Exception): ...

def read(obj: Any) -> None: ...
def write(obj: Any) -> None: ...
def readwrite(obj: Any, flags: int) -> None: ...
def poll(timeout: float = ..., map: _maptype | None = ...) -> None: ...
def poll2(timeout: float = ..., map: _maptype | None = ...) -> None: ...

poll3 = poll2

def loop(timeout: float = ..., use_poll: bool = ..., map: _maptype | None = ..., count: int | None = ...) -> None: ...

# Not really subclass of socket.socket; it's only delegation.
# It is not covariant to it.
class dispatcher:

    debug: bool
    connected: bool
    accepting: bool
    connecting: bool
    closing: bool
    ignore_log_types: frozenset[str]
    socket: _socket | None
    def __init__(self, sock: _socket | None = ..., map: _maptype | None = ...) -> None: ...
    def add_channel(self, map: _maptype | None = ...) -> None: ...
    def del_channel(self, map: _maptype | None = ...) -> None: ...
    def create_socket(self, family: int = ..., type: int = ...) -> None: ...
    def set_socket(self, sock: _socket, map: _maptype | None = ...) -> None: ...
    def set_reuse_addr(self) -> None: ...
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def listen(self, num: int) -> None: ...
    def bind(self, addr: tuple[Any, ...] | str) -> None: ...
    def connect(self, address: tuple[Any, ...] | str) -> None: ...
    def accept(self) -> tuple[_socket, Any] | None: ...
    def send(self, data: bytes) -> int: ...
    def recv(self, buffer_size: int) -> bytes: ...
    def close(self) -> None: ...
    def log(self, message: Any) -> None: ...
    def log_info(self, message: Any, type: str = ...) -> None: ...
    def handle_read_event(self) -> None: ...
    def handle_connect_event(self) -> None: ...
    def handle_write_event(self) -> None: ...
    def handle_expt_event(self) -> None: ...
    def handle_error(self) -> None: ...
    def handle_expt(self) -> None: ...
    def handle_read(self) -> None: ...
    def handle_write(self) -> None: ...
    def handle_connect(self) -> None: ...
    def handle_accept(self) -> None: ...
    def handle_close(self) -> None: ...

class dispatcher_with_send(dispatcher):
    def __init__(self, sock: socket | None = ..., map: _maptype | None = ...) -> None: ...
    def initiate_send(self) -> None: ...
    def handle_write(self) -> None: ...
    # incompatible signature:
    # def send(self, data: bytes) -> int | None: ...

def compact_traceback() -> tuple[tuple[str, str, str], type, type, str]: ...
def close_all(map: _maptype | None = ..., ignore_all: bool = ...) -> None: ...

if sys.platform != "win32":
    class file_wrapper:
        fd: int
        def __init__(self, fd: int) -> None: ...
        def recv(self, bufsize: int, flags: int = ...) -> bytes: ...
        def send(self, data: bytes, flags: int = ...) -> int: ...
        @overload
        def getsockopt(self, level: int, optname: int, buflen: None = ...) -> int: ...
        @overload
        def getsockopt(self, level: int, optname: int, buflen: int) -> bytes: ...
        def read(self, bufsize: int, flags: int = ...) -> bytes: ...
        def write(self, data: bytes, flags: int = ...) -> int: ...
        def close(self) -> None: ...
        def fileno(self) -> int: ...

    class file_dispatcher(dispatcher):
        def __init__(self, fd: FileDescriptorLike, map: _maptype | None = ...) -> None: ...
        def set_file(self, fd: int) -> None: ...
