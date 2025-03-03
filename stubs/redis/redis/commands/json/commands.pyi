from _typeshed import Incomplete

class JSONCommands:
    def arrappend(self, name: str, path: str | None = ..., *args) -> list[int | None]: ...
    def arrindex(
        self, name: str, path: str, scalar: int, start: int | None = None, stop: int | None = None
    ) -> list[int | None]: ...
    def arrinsert(self, name: str, path: str, index: int, *args) -> list[int | None]: ...
    def arrlen(self, name: str, path: str | None = ...) -> list[int | None]: ...
    def arrpop(self, name: str, path: str | None = ..., index: int | None = -1) -> list[str | None]: ...
    def arrtrim(self, name: str, path: str, start: int, stop: int) -> list[int | None]: ...
    def type(self, name: str, path: str | None = ...) -> list[str]: ...
    def resp(self, name: str, path: str | None = ...) -> list[Incomplete]: ...
    def objkeys(self, name, path=...): ...
    def objlen(self, name, path=...): ...
    def numincrby(self, name, path, number): ...
    def nummultby(self, name, path, number): ...
    def clear(self, name, path=...): ...
    def delete(self, key, path=...): ...
    forget = delete
    def get(self, name, *args, no_escape: bool = ...): ...
    def mget(self, keys, path): ...
    def set(self, name, path, obj, nx: bool = ..., xx: bool = ..., decode_keys: bool = ...): ...
    def set_file(self, name, path, file_name, nx: bool = ..., xx: bool = ..., decode_keys: bool = ...): ...
    def set_path(self, json_path, root_folder, nx: bool = ..., xx: bool = ..., decode_keys: bool = ...): ...
    def strlen(self, name, path: Incomplete | None = ...): ...
    def toggle(self, name, path=...): ...
    def strappend(self, name, value, path=...): ...
    def debug(self, subcommand, key: Incomplete | None = ..., path=...): ...
    def jsonget(self, *args, **kwargs): ...
    def jsonmget(self, *args, **kwargs): ...
    def jsonset(self, *args, **kwargs): ...
