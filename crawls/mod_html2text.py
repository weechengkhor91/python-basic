import html2text


#print(dir(html2text))
h = html2text.HTML2Text()

h.ignore_links = True

print(h.handle("<p>Hello, <a href='https://www.google.com/earth/'>world</a>!"))