import requests
import xml.etree.ElementTree as ET
import os
import json
from dotenv import load_dotenv
from ai21 import Client

load_dotenv()

A21_API_KEY = os.getenv("A21_API_KEY")

sitemap_url = "https://gamersplane.com/sitemap.xml"
start_url = "https://gamersplane.com/forums/9091"
output_file = "url-list.md"


def extract_sitemap_urls(sitemap_url, start_url, output_file):
    """
    Extracts URLs from a sitemap XML file that start with a specific URL and writes them to an output file.

    Parameters:
        sitemap_url (str): The URL of the sitemap XML file.
        start_url (str): The URL that the extracted URLs should start with.
        output_file (str): The path to the output file where the extracted URLs will be written.

    Returns:
        None
    """
    response = requests.get(sitemap_url)
    root = ET.fromstring(response.content)
    urls = []

    for child in root:
        if child.tag.endswith("url"):
            loc = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
            if loc.startswith(start_url):
                urls.append(loc)

    with open(output_file, "w") as file:
        for url in urls:
            file.write(url + "\n")


def segment_urls(output_file):
    """
    Segments the text of the URLs in the input file and writes the results to JSON files.

    Parameters:
        None

    Returns:
        None
    """

    # Read the list of URLs from the file
    with open(output_file, "r") as f:
        urls = f.read().splitlines()

    # Initialize the AI21 client
    client = Client(api_key=A21_API_KEY)

    # Loop through each URL and call the text segmentation API
    for url in urls:
        # Get the difference between the URL and the start URL
        filename = url.replace(start_url, "").strip("/")
        # Call the text segmentation API
        response = client.segment(url=url)
        # Save the result as a JSON file
        with open(os.path.join("jsonoutputs", f"{filename}.json"), "w") as f:
            json.dump(response, f)
