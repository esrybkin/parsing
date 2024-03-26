from lxml import etree

tree = etree.parse("src/web_page.html")

# title_element = tree.find("head/title")
# print(title_element.text)

# title_element = tree.find("body/titlep")
# print(title_element.text)

# list_item = tree.findall("body/li")

# for li in list_item:
#     a = li.find("a")
#     if a is not None:
#         print(f"{li.text.strip()} {a.text}")
#     else:
#         print(li.text)

# title_element = tree.xpath("//title/text()")[0]

# list_items = tree.xpath("//li")
# for li in list_items:
#     text = ''.join(map(str.strip, li.xpath(".//text()")))
#     print(text)

# list_items = tree.xpath("//ul/descendant::li")
# for li in list_items:
#     text = ''.join(map(str.strip, li.xpath(".//text()")))
#     print(text)

# css select
html = tree.getroot()
title_element = html.xcssselect("title")
print(title_element[0].text)