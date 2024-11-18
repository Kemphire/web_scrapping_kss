import requests
from bs4 import BeautifulSoup
import csv


with requests.get("https://worldpopulationreview.com/countries") as web_page:
    soup_web_page = BeautifulSoup(web_page.text, "lxml")
    country_table = soup_web_page.find("table", class_="wpr-table !border-none")
    with open("data/data.csv", "w", newline="", encoding="utf-8") as csv_file:
        writter = csv.writer(csv_file, delimiter=",")

        headers = [
            th.div.div.text.strip()
            for th in country_table.find("thead").find("tr").find_all("th")
            if th.div.div.text.strip()
            != "Flag"  # To reason to not including "Flag" is the fact that it is a image path
        ]

        writter.writerow(headers)

        country_table_body = country_table.find("tbody")

        for row in (country_table_body_tr := country_table_body.find_all("tr")):
            list_of_tds = row.find_all("td")
            cells = [td.text.strip() for td in list_of_tds[:-1]]
            boolen_field_un_member = list_of_tds[-1]
            svg_element = boolen_field_un_member.find("svg")
            if svg_element and "tabler-icon-check" in svg_element.get("class", []):
                cells.append(True)
            else:
                cells.append(False)
            writter.writerow(cells)
