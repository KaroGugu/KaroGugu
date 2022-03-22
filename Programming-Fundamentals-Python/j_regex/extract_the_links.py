import re

pattern = r'((www)\.([a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*(\.[a-z]+)+))'
some_sentences = input()
valid_urls = []

while some_sentences != "":
    matches = re.finditer(pattern, some_sentences)
    for match in matches:
        valid_urls.append(match.group(1))

    some_sentences = input()

for valid_url in valid_urls:
    print(valid_url)


