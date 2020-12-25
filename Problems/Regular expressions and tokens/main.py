from nltk.tokenize import regexp_tokenize
str_in = input()
print(regexp_tokenize(str_in, r"[A-z'\-]+"))
