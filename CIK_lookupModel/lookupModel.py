import requests 
import json
from collections import namedtuple

Sec = namedtuple('Sec', ['name', 'ticker', 'cik_id'])

class SecEdgar:
    def _init_(self, fileUrl):
        self.fileUrl = fileUrl
        self.nameDict = {}
        self.ticherDict = {}

        header = { 'user-agent' : 'MLT IS isanchez@college.harvard.edu'}

        response = requests.get(url = self.fileUrl, headers=header)

        self.responseJson = response.json()

        self.json_to_dicts()

    def json_to_dicts(self):
        for _, value in self.responseJson:
            cik_id = value['cik_str']
            company_name = value['title']
            ticker = value['ticker']

            self.name_dict[company_name] = cik_id
            self.ticker_dict[ticker] = cik_id
            self.cik_dict[cik_id] = (company_name, ticker)
    
    def name_to_cik(self, name: str) -> list[tuple[str, int]]:
        if name not in self.name_dict:
            raise BaseException("Cant find requested company name in dictionary")

        cik_id = self.name_dict[name]
        _, ticker = self.cik_dict[cik_id]

        return Sec(name=name, ticker=ticker, cik_id=cik_id)

      
    def ticker_to_cik(self, ticker: str) -> list[tuple[str, int]]:
        if ticker not in self.ticker_dict:
            raise BaseException("Cant find requested ticker in dictionary")

        cik_id = self.ticker_dict[ticker]
        name, _ = self.cik_dict[cik_id]

        return Sec(name=name, ticker=ticker, cik_id=cik_id)


se = SecEdgar('https://www.sec.gov/files/company_tickers.json')
