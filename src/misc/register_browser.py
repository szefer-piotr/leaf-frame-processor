import webbrowser

print(webbrowser._browsers)



# webbrowser.open_new("https://www.google.com")


webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

# urL='https://www.google.com'
# # chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
# webbrowser.register('chrome', instance=None)
# webbrowser.get('chrome').open_new_tab(urL)