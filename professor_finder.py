import os
from typing import List, Dict, Tuple, Set
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://www.southampton.ac.uk"


def get_people() -> None:
    people = set()
    print("Fetching people...")
    for i in tqdm(range(0, 443)):
        url = f"https://www.southampton.ac.uk/people/?page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for a in soup.find_all("a"):
            href = a.get("href")
            if href is None:
                continue
            if href.startswith("/people/"):
                people.add(href)
    print(f"Found {len(people)} people\n")
    for person in tqdm(people):
        response = requests.get(BASE_URL + person)
        soup = BeautifulSoup(response.text, "html.parser")
        # Collect only the text
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = "\n".join(chunk for chunk in chunks if chunk)
        with open(
            f"data/{person.split('/')[-2]}_{person.split('/')[-1]}.txt",
            "w",
            encoding="utf-8",
        ) as text_file:
            text_file.write(text)


def search_people(terms: List[str]) -> None:
    print(f"Searching people for {terms}...")
    people: Dict[str, Set[Tuple[str, str, int]]] = {}  # term: tuple(code, name, count)
    for file in tqdm(os.listdir("data")):
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            text = f.read().lower()
            for term in terms:
                if term in text:
                    people[term] = people.get(term, set())
                    prof_code = file.split("_")[0]
                    prof_name = file.split("_")[1][:-4]
                    count = text.count(term)
                    people[term].add((prof_code, prof_name, count))
    # Display
    for key, profs in people.items():
        print(key.upper())
        sorted_profs = sorted(list(profs), key=lambda x: x[2], reverse=True)
        for code, name, count in sorted_profs:
            pretty_name = name.replace("-", " ").title()
            url = BASE_URL + "/people/" + code + "/" + name
            print(f" - [{count}x] {pretty_name} ({url})")
        print("")


if __name__ == "__main__":
    # Updates cached data files (last updated 04/02/2024)
    # Takes a long time :)
    # get_people()

    # Finds professors relating to each term specified below
    TERMS = ["natural language processing", "cancer immunotherapy"]
    search_people(TERMS)
