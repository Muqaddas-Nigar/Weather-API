import requests, os
from dotenv import load_dotenv
from argparse import ArgumentParser
os.system("cls" if os.name == "nt" else "clear")
load_dotenv()
KEY = os.getenv("API_KEY")
parser = ArgumentParser(description="CLI program for fetching weather.")
parser.add_argument("--city", default="karachi",
                    help= "Name of the city")
parser.add_argument("--units", choices=["standard", "metric", "imperial"], default="metric",
                    help="Units in standard, metric & imperial, default=metric")
temp_unit = {"metric": "C", "standard": "K", "imperial": "F"}

args = parser.parse_args()


unit = temp_unit[args.units]


url=f'https://api.openweathermap.org/data/2.5/weather?q={args.city}&units={args.units}&appid={KEY}'
try:
    r=requests.get(url)
    if r.status_code == 200:
        r_dict = r.json()
        print(
            f"City: {r_dict['name']}\n", 
            f"Description: {r_dict['weather'][0]['description'].title()}\n",
            f"Temperature: {r_dict['main']['temp']}{unit}\n", 
            f"Humidity: {r_dict['main']['humidity']}%\n"
        )
    else:
        print(r.status_code)
        print(r.json()["message"])
except requests.exceptions.RequestException:
    print("Please Check your connection and try again.")
