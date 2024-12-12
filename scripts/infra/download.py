import requests

def dowload_image(url: str, save_path: str) -> None:
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
    except requests.RequestException as e:
        print(f"Error when try to download the {url}: {e}")