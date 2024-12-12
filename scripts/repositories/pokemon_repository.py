from decorators.singleton_decorator import singleton
from mysql.connector import MySQLConnection
from models.pokemon_model import PokemonModel


@singleton
class PokemonRepository:
    def __init__(self, connector: MySQLConnection):
        self.connector = connector

    def getPokemons(self) -> list[PokemonModel]:
        cursor = self.connector.cursor()

        query = ("SELECT num, forme FROM pokemons;")

        cursor.execute(query)
        pokemons = []
        
        for (num, forme) in cursor:
            pokemons.append(PokemonModel(num, forme))
        
        cursor.close()
        return pokemons
