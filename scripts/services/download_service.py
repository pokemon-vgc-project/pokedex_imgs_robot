import os

from concurrent.futures import ThreadPoolExecutor
from decorators.singleton_decorator import singleton
from infra.download import dowload_image
from repositories.pokemon_repository import PokemonRepository

@singleton
class DownloadService:
    def __init__(self, pokemonRepository: PokemonRepository):
        self.pokemonRepository = pokemonRepository
    
    def downloadPokemonImages(self, host:str, download_dir:str) -> None:
        pokemons = self.pokemonRepository.getPokemons()

        os.makedirs(download_dir, exist_ok=True)

        print("Started to Download")
        with ThreadPoolExecutor() as executor:
            futures = []
            for pokemon in pokemons:
                filename = pokemon.get_filename("png")
                url = pokemon.create_url(host, "png")
                save_path = os.path.join(download_dir, filename)
                futures.append(executor.submit(dowload_image, url, save_path))

            for future in futures:
                future.result()
            print("Finished to Download")

