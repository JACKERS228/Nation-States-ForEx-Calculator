import requests as rq
import gzip as gz
import os
import sys
import json as js

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

URLS = ["https://www.nationstates.net/pages/nations.xml.gz","https://www.nationstates.net/pages/regions.xml.gz"]

DUMP_DIR = resource_path("dumps")

def download_daily_dumps(urls:list[str]=URLS,save_dir=DUMP_DIR,filename=None):
    print("Fetching daily dump files from NationStates...")
    os.makedirs(save_dir,exist_ok=True)
    for url in urls:
        try:
            filename = os.path.basename(url)
            save_path = os.path.join(save_dir,filename)

            response = rq.get(url,stream=True)
            response.raise_for_status()

            with open(save_path,"wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            
            print(f"File downloaded to {save_path}")
    
        except rq.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
        except Exception as e:
            print(f"Enexpected error: {e}")

def extract_data(files,extract_dirs:list[str]):
    print("Extracting XML data from dump files...")
    for file, dest in zip(files,extract_dirs):
        try:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with gz.open(file,"rb") as f_in:
                with open(dest,"wb") as f_out:
                    f_out.write(f_in.read())
        except FileNotFoundError:
            print(f"Source file not found at {file}")
        except Exception as e:
            print(f"An error occurred while extracting {file}: {e}")


def main():
    regions_zip_file_path = os.path.join(DUMP_DIR,"regions.xml.gz")
    nations_zip_file_path = os.path.join(DUMP_DIR,"nations.xml.gz")
    download_daily_dumps()

    extract_data(files=[nations_zip_file_path,regions_zip_file_path],extract_dirs=[os.path.join(DUMP_DIR,"nations.xml"),os.path.join(DUMP_DIR,"regions.xml")])
