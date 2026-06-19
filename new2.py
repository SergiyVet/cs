import requests
import re
import time

URL = "https://steamcommunity.com/market/listings/730/G183F20AB093004?appid=730&assetproperty=CAIVAAAAAB0K1yM9"

BOT_TOKEN = "7753495202:AAGc2mLnRDHkx0hVvgUWDpjSntB9bVk1eYs"
CHAT_ID = "858719081"

prn = 89
zns = 0.04

while True:

    html = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}).text
    html = html.replace("\xa0", " ")

    wear_matches = re.findall(
        r'(?:Wear Rating|Зношування).*?<span[^>]*>(\d+,\d+)',
        html,
        re.DOTALL | re.IGNORECASE
    )

    price_matches = re.findall(
        r'<span class="NI9oaXH36YQ-"[^>]*>\s*UAH\s*([0-9\s.,]+)',
        html
    )

    print("\n🔄 Перевірка...")

    min_len = min(len(price_matches), len(wear_matches))

    found = False

    for i in range(min_len):
        price = float(price_matches[i].strip().replace(" ", "").replace(",", "."))
        wear = float(wear_matches[i].replace(",", "."))

        print(f"💰 {price} UAH | 🔹 {wear}")

        if price <= prn and wear <= zns:
            found = True

            message = f"🔥 ЗНАЙДЕНО СКІН!\n💰 Ціна: {price} UAH\n🔹 Float: {wear}"

            requests.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                params={
                    "chat_id": CHAT_ID,
                    "text": message
                }
            )

    if not found:
        print("❌ Поки нічого не знайдено")

    time.sleep(20)