from typing import Optional

class PokemonModel:
    def __init__(self, num: int, forme: Optional[str]):
        self.num = num
        self.forme = forme

    def get_num(self) -> int:
        return self.num

    def get_forme(self) -> Optional[str]:
        return self.forme

    def __repr__(self):
        forme = self.forme if self.forme is not None else ""
        return f"{self.num} - {forme}"