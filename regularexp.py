import re


s = """Hello my birth"s year is 2025 , and last year was 2014"""
result = re.search("\d{4}",s)
print(result)

