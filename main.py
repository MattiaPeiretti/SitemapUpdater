import requests
import sys
import json
import os

JSON_SETTINGS_FILE = "config.json"


def load_json(file_path, custom_error="JSON file not found at: "):
    if not os.path.exists(file_path):
        raise ValueError("{} {}".format(custom_error, file_path))

    with open(file_path) as data_file:
        json_dict = json.load(data_file)
    print(f"Loading json file: {file_path}")
    print(json_dict)
    return json_dict


def get_XML_data(URI, obj_key):
    response = requests.get(URI)
    if (response.status_code != 200):
        print("Could not pull the data!!!")
        sys.exit()
    return response.json()[obj_key]


def write_sitemap_file(data, filename, file_location):
    with open(file_location + filename, 'w') as f:
        f.write(data)


def main():

    print("Sitemap Updated is starting...")
    print("Loading config...")

    settings = load_json(JSON_SETTINGS_FILE)

    print("Downloading up-to-date data from API endpoint...")
    data = get_XML_data(settings["XML_DATA_URI"], settings["XML_DATA_OBJ_KEY"])

    print("Data pulled successfully!")
    print("Writing new" + settings["SITEMAP_FILE_NAME"] + "file, at the location: " + settings["SITEMAP_FILE_LOCATION"] + "...")
    write_sitemap_file(data, settings["SITEMAP_FILE_NAME"], settings["SITEMAP_FILE_LOCATION"])

    print("File written successfully!")
    print("Exiting.")


if __name__ == "__main__":
    main()
