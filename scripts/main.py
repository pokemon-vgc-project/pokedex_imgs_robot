#!/usr/bin/env python3

import os
from infra import database
from dotenv import load_dotenv
from repositories.pokemon_repository import PokemonRepository
from services.download_service import DownloadService

load_dotenv()

config = {
    "host": os.getenv('DATABASE_HOST'),
    "user": os.getenv('DATABASE_USER'),
    "password": os.getenv('DATABASE_PASS'),
    "database": os.getenv('DATABASE_NAME'),
}

pokemon_image_host = os.getenv('POKEMON_IMAGE_HOST')
image_dir_path = os.getenv('IMAGE_DIR_PATH')

if __name__ == "__main__":
    connector = database.connect_to_mysql(config)
    
    repository = PokemonRepository(connector)
    service = DownloadService(repository)
    
    service.downloadPokemonImages(pokemon_image_host, image_dir_path)

    database.close_connection(connector)