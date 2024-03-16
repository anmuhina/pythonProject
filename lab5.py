import re

def check_domain(url):
    domain = r'^(https?://)([a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}(/)?$'
    if re.match(domain, url):
        return True
    else:
        return False


def get_domain(url):
    domain = r'^(https?://)([a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}(/)?$'
    match = re.match(domain, url)
    if match:
        return match.group()
    else:
        raise ValueError("Oops, not a domain :(")



url1 = "http://example.com"
url2 = "example.com"
url3 = "кремль.рф"
url4 = "https://ex.ru"
print("Проверка функции check_domain:")
print(url1+" - "+str(check_domain(url1))) #true
print(url2+" - "+str(check_domain(url2))) #false
print(url3+" - "+str(check_domain(url3))) #false
print(url4+" - "+str(check_domain(url4))) #true
print("\n")

print("Проверка функции get_domain:")
try:
    print(get_domain(url1))
    print(get_domain(url2)) #исключение
except ValueError as e:
    print(e)
