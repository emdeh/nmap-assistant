import os
from nmap_analysis import run_analysis

def display_ascii_art():
    print("""
                    Welcome to Nmap Assistant
                    -------------------------
                        created by @emdeh
                        Find me at emdeh.com
.-. .-..-.  .-.  .--.  .-.-.       .--.   .----. .----..-. .----..-----. 
|  \{ |}  \/  { / {} \ | } }}___  / {} \ { {__-`{ {__-`{ |{ {__-``-' '-' 
| }\  {| {  } |/  /\  \| |-'{___}/  /\  \.-._} }.-._} }| }.-._} }  } {   
`-' `-'`-'  `-'`-'  `-'`-'       `-'  `-'`----' `----' `-'`----'   `-'   
    """)

def get_openai_api_key():
    while True:
        api_key = input("Please enter your OpenAI API key: ").strip()
        if api_key:
            return api_key
        else:
            print("API key cannot be empty. Please try again.")

def get_xml_file_path():
    while True:
        file_path = input("Please enter the path to your Nmap output XML file: ").strip()
        if os.path.exists(file_path):
            if not file_path.endswith(".xml"):
                print("File must be an XML file. Please try again.")
            else:
                return file_path
        else:
            print(f"File not found at {file_path}. Please try again.")

def main():
    display_ascii_art()
    api_key = get_openai_api_key()

    # Set the API key as an environment variable
    os.environ["OPENAI_API_KEY"] = api_key

    xml_file_path = get_xml_file_path()

    # Call the main analysis function with the collected data
    run_analysis(api_key, xml_file_path)

try:
    main()
except KeyboardInterrupt:
    print("\n\nProgram interrupted by user. Exiting the program. Have a great day!")
    exit()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

if __name__ == "__main__":
    main()


