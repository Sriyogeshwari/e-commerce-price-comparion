import requests as rq
import bs4 as bs4
import random
import prettytable as pt

class ProductScraper:
    def __init__(self, product_name):
        self.product_name = str(product_name).replace(" ", "+")

    def amazon_url(self):
        return f"https://www.amazon.in/s?k={self.product_name}"

    def flipkart_url(self):
        return f"https://www.flipkart.com/search?q={self.product_name}"

    def product_urls(self):
        return {"amazon": self.amazon_url(), "flipkart": self.flipkart_url()}

class WebScraper:
    def __init__(self, product_scraper):
        self.custom_headers_list = [
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0'},
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15'},
        ]
        self.urls = product_scraper.product_urls()
        self.htmls = self.get_htmls()

    def make_request(self):
        stat_codes = {}
        resp = {}
        for url in self.urls:
            req = rq.get(self.urls[url], headers=random.choice(self.custom_headers_list))
            resp[url] = req.content
            stat_codes[url] = req.status_code
        return {"status": stat_codes, "response": resp}

    def get_htmls(self):
        response = self.make_request()["response"]
        return {pf: bs4.BeautifulSoup(response[pf], "html.parser") for pf in response}

    def get_names(self):
        names = {"amazon": [], "flipkart": []}
        for platform, html in self.htmls.items():
            if platform == 'amazon':
                names[platform] = [tag.get_text() for tag in html.select('span.a-size-medium.a-color-base.a-text-normal')]
            elif platform == 'flipkart':
                names[platform] = [tag.get_text() for tag in html.find_all('div', {'class': '_4rR01T'})]
        return names

    def get_prices(self):
        prices = {"amazon": [], "flipkart": []}
        for platform, html in self.htmls.items():
            if platform == 'amazon':
                prices[platform] = [tag.get_text() for tag in html.select('span.a-price-whole')]
            elif platform == 'flipkart':
                prices[platform] = [tag.get_text() for tag in html.find_all('div', {'class': '_30jeq3'})]
        return prices

    def get_product_info(self):
        return {
            "amazon": {"name": self.get_names()["amazon"], "price": self.get_prices()["amazon"]},
            "flipkart": {"name": self.get_names()["flipkart"], "price": self.get_prices()["flipkart"]}
        }

class PriceComparison:
    @staticmethod
    def status_check(web_scraper):
        for site, status in web_scraper.make_request()["status"].items():
            print(f"{site} scraping status: {status}")

    @staticmethod
    def print_table(product_info, website):
        table = pt.PrettyTable(["S.NO", f"{website} Product Name", "Price (INR)"])
        names = product_info[website]["name"]
        prices = product_info[website]["price"]

        for idx, (name, price) in enumerate(zip(names, prices), start=1):
            table.add_row([idx, name, price if price else "Price not available"])

        print(table)

# Main Execution
if __name__ == "__main__":
    product_name = input("Enter Product name to search for: ")
    product_scraper = ProductScraper(product_name)
    web_scraper = WebScraper(product_scraper)

    PriceComparison.status_check(web_scraper)
    product_info = web_scraper.get_product_info()
    
    PriceComparison.print_table(product_info, "flipkart")
    PriceComparison.print_table(product_info, "amazon")
