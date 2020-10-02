import requests
import pandas as pd

# Enter csv source and desired filename
# example: https://raw.githubusercontent.com/PATH_TO_FILE.csv
url = str(input("Source url (github raw): \n"))
filename = str(input("Desired Filename (with extension): \n"))

# request file, open and write to desired file
res = requests.get(url, allow_redirects=True)
with open(filename,'wb') as file:
    file.write(res.content)
read_file = pd.read_csv(filename)
