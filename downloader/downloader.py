from bing_image_downloader import downloader

query = "araba"

downloader.download(query, limit=30, output_dir="data", timeout=60, verbose=True)