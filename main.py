import requests
import fake_useragent
import os
from bs4 import BeautifulSoup


def clear() -> None:
    if os.path.isfile("youtube.txt"):
        os.remove("youtube.txt")


def search() -> None:
    clear()

    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}

    page = 1
    last_page = 10
    link = f"https://modrinth.com"

    while page <= last_page:
        print(f"{page}|{last_page}")
        try:
            page_response = (20 * page - 20)
            response = requests.get(f"{link}/mods?o={page_response}&v=1.20.2", headers=header).text
            soup = BeautifulSoup(response, "html.parser")

            # page
            if page == 1:
                last_page = soup.find("a", class_="shrink").text
                last_page = int(last_page)

            block = soup.find("div", class_="search-results-container").find("div", id="search-results")

            for i in block.find_all("article", role="listitem"):
                name = i.find("h2", class_="name").text
                # Environments = i.find("span", class_="environment").text
                text = f"{name}"
                print(text)

                with open("youtube.txt", "a", encoding="UTF-8") as MyFile:
                    MyFile.write(text + "\n")
            page += 1
        except AttributeError:
            #page_response = (20 * page - 20)
            #response = requests.get(f"{link}/mods?o={page_response}&v=1.20.2", headers=header).text
            #soup = BeautifulSoup(response, "lxml")
            #anti = soup.find("input", type="checkbox")
            break


if __name__ == "__main__":
    search()
