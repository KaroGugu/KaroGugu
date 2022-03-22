import webbrowser as wb

def web_automation():
    chrom_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    URLS = ("google.com", "apple.com", "facebook.com")

    for url in URLS:
        print("Opening: " + url)
        wb.get(chrom_path).open(url)

web_automation()