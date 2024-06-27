##Requirement: đã cài đặt google-search-results, cài đặt bằng lệnh pip install google-search-results
##Theo thông tin hiện tại, SerpAPI hỗ trợ 5000 lượt tìm kiếm thử miễn phí mỗi tháng, có thể cân nhắc nâng cấp hoặc tạo tài khoản mới và thay api_key
import json
from serpapi import GoogleSearch

params = {
  "api_key": "36e15307c600f96b9e26213ca81b7dcb1d8b7af5436029c85e6d7ff60ebe4136", ##Api_key sẽ được cấp phát khi người dùng đăng ký tài khoản trên https://serpapi.com/
  "engine": "google", ##Công cụ tìm kiếm được sử dụng để thu thập kết quả
  "q": "site:www.facebook.com/pages/ Bất+Động+Sản", ##Câu lệnh truy vấn dùng cho công cụ tìm kiếm, có thể tinh chỉnh dựa theo nhu cầu: vd: chỉnh từ pages -> groups
  "google_domain": "google.com.vn",
  "gl": "vn", ##Vùng quốc gia được tìm kiếm
  "hl": "vi", ##Ngôn ngữ được sử dụng trong tìm kiếm
  "num": "100", ##Số kết quả hiện ra mỗi lần scarp, default là 10 SerpAPi chỉ có thể cho ra kết quả tối đa là 100 đối với mỗi lần search
  "start": "0" ## "Bước nhảy" ở vị trí bắt đầu kết quả tìm kiếm, 0 sẽ là kết quả tìm kiếm ở trang đầu, các trang tiếp theo sẽ tùy thuộc theo công cụ tìm kiếm
}

search = GoogleSearch(params)
results = search.get_dict()

# Export results as JSON
with open('results.json', 'w') as f:
    json.dump(results, f)

print("Results exported to results.json")