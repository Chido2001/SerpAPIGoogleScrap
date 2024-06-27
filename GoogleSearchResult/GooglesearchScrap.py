##Requirement: đã cài đặt google-search-results, cài đặt bằng lệnh pip install google-search-results
##Theo thông tin hiện tại, SerpAPI hỗ trợ 5000 lượt tìm kiếm thử miễn phí mỗi tháng, có thể cân nhắc nâng cấp hoặc tạo tài khoản mới và thay api_key mỗi khi api-key hết khả dụng
import json
from serpapi import GoogleSearch

def search_and_extract_links(q, num, start, output_json_file, output_text_file):
    params = {
        "api_key": "36e15307c600f96b9e26213ca81b7dcb1d8b7af5436029c85e6d7ff60ebe4136", ##Api_key sẽ được cấp phát khi người dùng đăng ký tài khoản trên https://serpapi.com/
        "engine": "google", ##Công cụ tìm kiếm được sử dụng để thu thập kết quả
        "q": f"site:facebook.com/groups/ {q}", ##Câu lệnh truy vấn dùng cho công cụ tìm kiếm, có thể tinh chỉnh dựa theo nhu cầu: vd: chỉnh từ pages -> groups
        "google_domain": "google.com.vn",
        "gl": "vn", ##Vùng quốc gia được tìm kiếm
        "hl": "vi",##Ngôn ngữ được sử dụng trong tìm kiếm
        "num": num,##Số kết quả hiện ra mỗi lần scarp, default là 10 ,SerpAPi chỉ có thể cho ra kết quả tối đa là 100 đối với mỗi lần 
        "start": start ##Vị trí bắt đầu scrap
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
    start2 = start1 +100 #Scrap 2 sẽ bắt đầu sau kết quả cuối cùng của scrap 1
    output_json_file1 = 'results1.json'
    output_text_file1 = 'links1.txt'
    output_json_file2 = 'results2.json'
    output_text_file2 = 'links2.txt'


    search_and_extract_links(q, num, start1, output_json_file1, output_text_file1)
    search_and_extract_links(q, num, start2, output_json_file2, output_text_file2)
