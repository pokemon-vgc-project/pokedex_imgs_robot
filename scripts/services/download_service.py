import os
import time

from concurrent.futures import ThreadPoolExecutor
from decorators.singleton_decorator import singleton
from infra.download import dowload_image
from repositories.pokemon_repository import PokemonRepository
from models.pokemon_model import PokemonModel

@singleton
class DownloadService:
    def __init__(self, pokemonRepository: PokemonRepository):
        self.pokemonRepository = pokemonRepository
    
    def downloadPokemonImages(self, host:str, download_dir:str, batch_size: int = 10, delay: float = 10.0) -> None:
        pokemons = self.pokemonRepository.getPokemons()
        totalList = len(pokemons)
        print("Started")
        for i in range(0, totalList, batch_size):
            batch_pokemons = pokemons[i:i+batch_size]
            print(f"Started to download the batch {i // batch_size + 1}")

            #Execute
            self._download(batch_pokemons, host, download_dir)

            if i + batch_size < totalList:
                time.sleep(delay)
        print("Finished")

    def _download(self, pokemons: list[PokemonModel], host:str, download_dir:str, ) -> None:
        os.makedirs(download_dir, exist_ok=True)

        with ThreadPoolExecutor() as executor:
            futures = []
            for pokemon in pokemons:
                filename = pokemon.get_filename("png")
                url = pokemon.create_url(host, "png")
                save_path = os.path.join(download_dir, filename)
                futures.append(executor.submit(dowload_image, url, save_path))

            for future in futures:
                future.result()