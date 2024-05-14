from requests_html import HTMLSession, AsyncHTMLSession

url = "https://www.pccomponentes.com/zotac-gaming-geforce-rtx-4060-ti-twin-edge-16gb-gddr6-dlss3"

session = HTMLSession()

r = session.get(url)

print(r)

