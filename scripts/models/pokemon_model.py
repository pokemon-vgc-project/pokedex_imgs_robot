from typing import Optional

class PokemonModel:
    def __init__(self, num: int, forme: Optional[str]):
        self.num = num
        self.forme = forme if forme is not None else ""
        self.formeDic = {
            "10%": "10",
            "Alola": "a",
            "Alola-Totem": "a",
            "Antique": "f",
            "Ash": "a",
            "Attack": "a",
            "Belle": "belle",
            "Black": "b",
            "Blade": "b",
            "Bloodmoon": "b",
            "Blue": "b",
            "Blue-Striped": "b",
            "Bond": "a",
            "Burn": "f",
            "Bug": "bug",
            "Busted": "b",
            "Busted-Totem": "b",
            "Cornerstone": "c",
            "Cornerstone-Tera": "cmt",
            "Chill": "i",
            "Complete": "c",
            "Crowned": "c",
            "Dada": "d",
            "Dark": "dark",
            "Dawn-Wings": "dw",
            "Dragon": "dragon",
            "Defense": "d",
            "Douse": "w",
            "Dusk": "d",
            "Dusk-Mane": "dm",
            "Electric": "electric",
            "Eternal": "e",
            "Eternamax": "e",
            "F": "f",
            "Fairy": "fairy",
            "Fan": "s",
            "Fancy": "f",
            "Fighting": "fighting",
            "Fire": "fire",
            "Flying": "flying",
            "Four": "f",
            "Frost": "f",
            "Galar": "g",
            "Galar-Zen": "gz",
            "Ghost": "ghost",
            "Gmax": "gi",
            "Gorging": "go",
            "Grass": "grass",
            "Ground": "ground",
            "Gulping": "gu",
            "Hangry": "h",
            "Heat": "h",
            "Hearthflame": "h",
            "Hearthflame-Tera": "hmt", 
            "Hero": "h",
            "Hisui": "h",
            "Hoenn": "hoenn",
            "Ice": "ice",
            "Kalos": "kalos",
            "Large": "l",
            "Libre": "libre",
            "Low-Key": "l",
            "Low-Key-Gmax": "gi",
            "Mega": "m",
            "Mega-X": "mx",
            "Mega-Y": "my",
            "Midnight": "m",
            "Mow": "m",
            "Noice": "n",
            "Origin": "o",
            "Original": "original",
            "Partner": "partner",
            "Pa'u": "pau",
            "Paldea":"p",
            "Paldea-Aqua": "a",
            "Paldea-Blaze": "b",
            "Paldea-Combat": "p",
            "Pom-Pom": "p",
            "PhD": "phd",
            "Pirouette": "s",
            "Pokeball": "pb",
            "Pop-Star": "popstar",
            "Poison": "poison",
            "Primal": "m",
            "Psychic": "psychic",
            "Rainy": "r",
            "Rapid-Strike": "r",
            "Rapid-Strike-Gmax": "rgi",
            "Resolute": "r",
            "Rock": "rock",
            "Roaming": "r",
            "Sandy": "c",
            "School": "s",
            "Sensu": "s",
            "Shadow": "s",
            "Shock": "e",
            "Sky": "s",
            "Sinnoh": "sinnoh",
            "Small": "s",
            "Snowy": "s",
            "Speed": "s",
            "Spiky-eared": "s",
            "Steel": "steel",
            "Stellar": "s",
            "Sunny": "s",
            "Sunshine": "s",
            "Super": "h",
            "Teal-Tera": "tmt",
            "Terastal": "t",
            "Therian": "s",
            "Three-Segment": "t",
            "Trash": "t",
            "Unova": "unova",
            "Unbound": "u",
            "Ultra": "m",
            "Wash": "w",
            "Water": "water",
            "Wellspring": "w",
            "Wellspring-Tera": "wmt",
            "White": "w",
            "White-Striped": "w",
            "World": "world",
            "Yellow": "y",
            "Zen": "z",
        }

    def get_filename(self, format:str) -> str :
        forme = self.forme if self.forme == "" else "_" + self.forme
        return f"{self.num}{forme}.{format}"
    
    def create_url(self, host:str, format:str) -> str :
        forme = self._get_url_forme_name()
        num = self._get_img_num()
        return f"{host}/{num}{forme}.{format}"

    def _get_url_forme_name(self) -> str :
        if self.num == 133 and self.forme == "Starter": return ""

        if self.forme in self.formeDic:
            if self.num == 898 and self.forme == "Ice": return "-i"
            elif self.num == 25 and self.forme == "Alola": return "-alola"
            return "-"+self.formeDic[self.forme]
        return ""
    
    def _get_img_num(self) -> str :
        if self.num < 10 : return f"00{self.num}"
        elif self.num < 100 : return f"0{self.num}"
        return f"{self.num}"
        
    def __repr__(self):
        return f"{self.num} - {self.forme}"