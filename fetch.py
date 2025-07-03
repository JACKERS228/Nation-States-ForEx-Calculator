import requests as rq
import gzip as gz
import os

URLS = ["https://www.nationstates.net/pages/nations.xml.gz","https://www.nationstates.net/pages/nations.xml.gz"]

def download_daily_dumps(urls:list[str],save_dir="dumps",filename=None):
    try:
        for url in urls:
            os.makedirs(save_dir,exist_ok=True)
            if filename is None:
                filename = os.path.basename(url)
                if not filename:
                    filename = "newest_dump"
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
    for file in files:
        with gz.open(file,"rb") as f_in:
            for extract_dir in extract_dirs:
                extract_dir = extract_dirs.pop(0)
                with open(extract_dir,"wb") as f_out:
                    f_out.write(f_in.read())
                print(f"Extracted data to: {extract_dir}")


def main():
    regions_zip_file_path = r"\dumps\regions.xml.gz"
    nations_zip_file_path = r"\dumps\nations.xml.gz"
    extract_dir = r"dumps\regions.xml"
    download_daily_dumps(urls=URLS)

    extract_data(files=[nations_zip_file_path,regions_zip_file_path],extract_dirs=[r"dumps\nations.xml",r"dumps\regions.xml"])

if __name__ == "__main__":
    main()
else:
    pass
