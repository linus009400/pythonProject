# requests와 BeautifulSoup 모듈을 임포트합니다.
import requests
from bs4 import BeautifulSoup

# 환율 정보를 얻고 싶은 국가의 통화 코드를 입력합니다. 예: USD, EUR, JPY 등
currency = input("통화 코드: ")

# 네이버 금융 사이트에서 해당 통화의 환율 정보를 가져옵니다.
url = f"https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_{currency}KRW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 환율 정보가 담긴 테이블을 찾습니다.
table = soup.find("table", class_="tbl_exchange")

# 테이블에서 매매 기준율, 전일대비, 등락률을 추출합니다.
rate = table.find("span", class_="value").text  # 매매 기준율
change = table.find("span", class_="change").text  # 전일대비
updown = table.find("span", class_="blind").text  # 등락률

# 결과를 출력합니다.
print(f"{currency}/KRW 환율 정보")
print(f"매매 기준율: {rate} 원")
print(f"전일대비: {change} 원 ({updown})")
