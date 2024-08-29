from typing import List, Optional

from typing_extensions import TypeAlias

# Because UUID has properties called int and bytes we need to rename these temporarily.
_Int: TypeAlias = int
_Bytes: TypeAlias = bytes
_FieldsType: TypeAlias = tuple[int, int, int, int, int, int]

class UUID:
    def __init__(
        self,
        hex: str | None = ...,
        bytes: _Bytes | None = ...,
        bytes_le: _Bytes | None = ...,
        fields: _FieldsType | None = ...,
        int: _Int | None = ...,
        version: _Int | None = ...,
    ) -> None: ...
    @property
    def int(self) -> _Int: ...
    @property
    def bytes(self) -> _Bytes: ...
    @property
    def bytes_le(self) -> _Bytes: ...
    @property
    def hex(self) -> str: ...
    @property
    def urn(self) -> str: ...
    @property
    def variant(self) -> str: ...
    @property
    def version(self) -> _Int | None: ...
    @property
    def fields(self) -> _FieldsType: ...
    @property
    def time_low(self) -> _Int: ...
    @property
    def time_mid(self) -> _Int: ...
    @property
    def time_hi_version(self) -> _Int: ...
    @property
    def clock_seq_hi_variant(self) -> _Int: ...
    @property
    def clock_seq_low(self) -> _Int: ...
    @property
    def time(self) -> _Int: ...
    @property
    def node(self) -> _Int: ...
    def __int__(self) -> _Int: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: UUID) -> bool: ...
    def __le__(self, other: UUID) -> bool: ...
    def __gt__(self, other: UUID) -> bool: ...
    def __ge__(self, other: UUID) -> bool: ...
    def __getstate__(self) -> _Bytes: ...
    def __setstate__(self, state: _Bytes) -> None: ...

def uuid1(node: Optional[int] = None, clock_seq: Optional[int] = None) -> UUID: ...
def uuid_v1mc() -> UUID: ...
def uuid3(namespace: UUID, name: str) -> UUID: ...
def uuid4() -> UUID: ...
def uuid4_bulk(n: int) -> List[UUID]: ...
def uuid4_as_strings_bulk(n: int) -> List[str]: ...
def uuid5(namespace: UUID, name: str) -> UUID: ...
def uuid7() -> UUID: ...
def uuid7_bulk(n: int) -> List[UUID]: ...
def uuid7_as_strings_bulk(n: int) -> List[str]: ...
