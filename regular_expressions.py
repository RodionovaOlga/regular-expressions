from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

contacts_list.sort(key=lambda x: x[0])
dict_ = {}
pattern = r"\+?[78]\s?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})\s?\(?(\w*\.)?\s?(\d+)?\)?"

for idx, line in enumerate(contacts_list):
    line[:3] = " ".join(line[:3]).strip(" ").replace("  ", " ").split(" ")
    if line[2] == "":
        line.insert(2, "")
    line[5] = (re.sub(pattern, r"+7(\1)\2-\3-\4 \5\6", line[5])).strip(" ")
    if dict_.get(line[0]+line[1]) is None:
        dict_.setdefault(line[0]+line[1], line)
    for idx_, element in enumerate(dict_.get(line[0]+line[1])):
        if element == '':
            dict_.get(line[0]+line[1])[idx_] = line[idx_]

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(dict_.values())
print()






