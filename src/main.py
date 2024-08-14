

base_url = 'https://www.olg.ca/en/winners/unclaimed-instant-prizes.html'

# def get_unclaimed_prices():
#     resp = requests.get(base_url)
#     #html = resp.content.decode('utf-8')
#     resp.encoding = resp.apparent_encoding
#     print(resp.text)
import requests
import lottery_oby

#map game_name: lottery obj
games_dict = {}



def get_unclaimed_prices():
    url = "https://gateway.wma.olg.ca/feeds/instant-unclaimed"

    payload = ""
    headers = {
        "cookie": "__cf_bm-gw=mkc%3A%3A2DC9B29381B8999561BE1BA40F77912E%3A%3AwBbdEk2B794b8SYBo7wYiXgw9XAdNPsQdJXJdrxnZTs-1723668615-1.0.1.1-cp7Y5sZ0Ck1WXCDT5bhQC8F1FS8NEnsGvK5itMGk6Ziimfg8a9NqxbPcVhA2bQXljZNrWgZgY9qsvmgsC4W14w; __cf_bm=wBbdEk2B794b8SYBo7wYiXgw9XAdNPsQdJXJdrxnZTs-1723668615-1.0.1.1-cp7Y5sZ0Ck1WXCDT5bhQC8F1FS8NEnsGvK5itMGk6Ziimfg8a9NqxbPcVhA2bQXljZNrWgZgY9qsvmgsC4W14w; __cf_bm=FgtR4XzqLN.Uy0_9Rj901XEGsDjK__7QncLLNvGfi3I-1723668615-1.0.1.1-V5aZpIFx6MX.Qtw5srEpia1yZZwOl9djoWYa7i5JGMrGT9ykU4uju00Dn_UmrPnNc647P5.QuZ326uO8nBKOAA",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "X-Site-Code": "playolg.ca",
        "X-Correlation-Token": "8c7eb206-2327-4226-83f8-0ac68c137143",
        "x-client-id": "rsH2esTpZdj4az96+sGDrojHaFNvf7eePkicOtsqAt1GUiF964HRvenqpP8JwfoJIkW3nQ8Jhaz8jm4PZwKLSg+Zfqo/GiDJ2jNNLVni/CoTdsAvwko/aw==",
        "Origin": "https://www.olg.ca",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.olg.ca/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    response = response.json()
    print(response)

    for i in response['response']['instantUnclaimedPrizes']['instantUnclaimedPrize']: 
        game_name = i['gameName']
        if (game_name in games_dict):
            games_dict[game_name].prizes.append(lottery_oby.Prize(i['prizeEN'], i['totalPrizes'], i['unclaimedPrizes']))
        else:
            games_dict[game_name] = lottery_oby.Lottery(i['gameName'],i['gameNumber'],i['gameCost'])

    print(games_dict)


def main():
    get_unclaimed_prices()

if __name__ == "__main__":
    main()