from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Karta:
    id: int
    jmeno: str
    tel: int
    mail: str

class AbstractObserver(ABC):   #načte id karty, vymysli zpravu rodicum
    @abstractmethod
    def vstup(self, id:int) -> bool:
        ...
    ...

class AbstractKontejner(ABC):   #z id karty zjistí ostatní údaje
    @abstractmethod
    def ctecka(self, id: int) -> Karta:
        ...
    ...

class AbstractNotifikator(ABC):   #napise zpravu rodicum, odesila zpravu rodicum
    @abstractmethod
    def zprava(self, mail: str, telo_zpravy: str) -> None: 
        ...
    ...
