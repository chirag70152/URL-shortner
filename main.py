import pyshorteners

url = input('Enter the link: ')

shortener = pyshorteners.Shortener()

a = shortener.tinyurl.short(url)

print(a)
