from nltk.tokenize import regexp_tokenize
str_in = input()
x = int(input())
result = regexp_tokenize(str_in, r"[A-Za-z]+")
print(result[x])