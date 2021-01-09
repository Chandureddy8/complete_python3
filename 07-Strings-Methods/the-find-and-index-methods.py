browser = "Google Chrome"

print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("G"))
print(browser.find("Z"))
print(browser.find("Zxy"))
print(browser.find("c"))

print()

print(browser.find("o"))
print(browser.find("o", 2))
print(browser.find("o", 5))

print("Ch" in browser)

print(browser.index("C"))
# print(browser.index("Z"))