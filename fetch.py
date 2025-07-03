import requests as rq
import gzip as gz
import os

URLS = ["https://www.nationstates.net/pages/nations.xml.gz","https://www.nationstates.net/pages/regions.xml.gz"]
DUMP_DIR = "dumps"

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
            with gz.open(file,"rb") as f_in:
                with open(dest,"wb") as f_out:
                    f_out.write(f_in.read())
        except FileNotFoundError:
            print(f"Source file not found at {file}")
        except Exception as e:
            print(f"An error occurred while extracting {file}: {e}")


def main():
    regions_zip_file_path = r"dumps\regions.xml.gz"
    nations_zip_file_path = r"dumps\nations.xml.gz"
    download_daily_dumps()

    extract_data(files=[nations_zip_file_path,regions_zip_file_path],extract_dirs=[r"dumps\nations.xml",r"dumps\regions.xml"])
