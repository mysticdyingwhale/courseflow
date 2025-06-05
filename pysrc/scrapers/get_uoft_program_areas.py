import requests
from bs4 import BeautifulSoup
import json
import re


def get_program_areas():
    uoft_program_areas = "https://artsci.calendar.utoronto.ca/listing-program-subject-areas"
    response = requests.get(uoft_program_areas)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        program_areas = []
        base = "https://artsci.calendar.utoronto.ca"

        for a_tag in soup.find_all('a'):
            href = a_tag.get('href')
            text = (a_tag.text.replace('\u00a0', ' ')
                    .replace('\u200b', '').strip())

            if ", Centre for" in text:
                text = text.split(", Centre for")[0]
            elif ", Center for" in text:
                text = text.split(", Center for")[0]

            if (href and href.startswith('/section/') and text
                    and "College" not in text):
                full_url = base + href
                program_areas.append({"text": text, "href": full_url})

        with open("../res/uoft_program_areas.json", "w", encoding="utf-8") as file:
            json.dump(program_areas, file, indent=2, ensure_ascii=False)

        print(f"Saved {len(program_areas)} program areas to uoft_program_areas.json")
    else:
        print(f"Failed to fetch page: {response.status_code}")
