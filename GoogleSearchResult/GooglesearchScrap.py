import json
from serpapi import GoogleSearch

def search_and_extract_links(q, num, start, output_json_file, output_text_file):
    params = {
        "api_key": "36e15307c600f96b9e26213ca81b7dcb1d8b7af5436029c85e6d7ff60ebe4136",
        "engine": "google",
        "q": f"site:facebook.com/groups/ {q}",
        "google_domain": "google.com.vn",
        "gl": "vn",
        "hl": "vi",
        "num": num,
        "start": start
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Export results as JSON
    with open(output_json_file, 'w') as f:
        json.dump(results, f, indent=4)

    # Extract links from JSON
    with open(output_json_file, 'r') as json_file:
        data = json.load(json_file)
        links = [result['link'] for result in data['organic_results']]
        with open(output_text_file, 'w') as output_file:
            for link in links:
                output_file.write(link + '\n')

    print(f"Results exported to {output_json_file} and links extracted to {output_text_file}")

if __name__ == "__main__":
    q = input("Enter search query (e.g., Nhà Đất): ")
    num = int(input("Enter number of results: "))
    start1 = int(input("Enter start value: "))
    start2 = start1 +100
    output_json_file1 = 'results1.json'
    output_text_file1 = 'links1.txt'
    output_json_file2 = 'results2.json'
    output_text_file2 = 'links2.txt'


    search_and_extract_links(q, num, start1, output_json_file1, output_text_file1)
    search_and_extract_links(q, num, start2, output_json_file2, output_text_file2)