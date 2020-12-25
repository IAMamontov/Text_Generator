from nltk import WhitespaceTokenizer, BigramCollocationFinder, TrigramCollocationFinder
from nltk import bigrams
from nltk import collocations
import random
import re


if __name__ == '__main__':
    filename = input()
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            content = f.read()
        except OSError as e:
            print(e)
        finally:
            f.close()
    tokens = WhitespaceTokenizer().tokenize(content)
    content = ""
    # 1-5 stages
    # res_bigrams = dict(bigrams(tokens))
    # print(set(res_bigrams.keys()))
    # print(res_bigrams)
    # print(f"Number of bigrams: {len(res_bigrams)}")
    # find_dict = BigramCollocationFinder.from_words(tokens).ngram_fd
    # head = random.choice(list(finder.word_fd.keys()))
    # head = random.choice(list(set(res_bigrams.keys())))
    # head = random.choice(tokens)
    # print(head, end=" ")
    # print(find_dict.keys())
    find_dict3 = dict(TrigramCollocationFinder.from_words(tokens).ngram_fd)
    result = {}
    for i in range(10):
        j = 0
        while True:
            if j == 0:
                head3 = random.choice(list(find_dict3.keys()))
                head = (head3[0], head3[1])
                while re.match(r"[A-Z]\w*[^.!?]$", head[0]) is None:
                    head3 = random.choice(list(find_dict3.keys()))
                    head = (head3[0], head3[1])
                print(f"{head[0]} {head[1]}", end=" ")
            result.clear()
            for (_, __, ___) in find_dict3.keys():
                if (_, __) == head:
                    result[(___)] = find_dict3[(_, __, ___)]
            # print(result)
            if j > 0:
                text = random.choices(list(result.keys()), list(result.values()))[0]
                print(text, end=" ")
                head = (head[1], text)
            if j >= 3 and re.match(r".*[.!?]$", text) is not None:
                break
            j += 1
        print()

    # 3rd stage
    # str_in = input()
    # while str_in != "exit":
    #     result = {}
    #     print(f"Head: {str_in}")
    #     try:
    #         # index = int(str_in)
    #         for (_, __) in find_dict.keys():
    #             if _ == str_in:
    #                 result[__] = find_dict[(_, __)]
    #         if len(result) == 0:
    #             print("The requested word is not in the model. Please input another word.")
    #         else:
    #             for _ in result.keys():
    #                 print(f"Tail: {_} Count: {result[_]}")
    #     except ValueError:
    #         print("Type Error. Please input an integer.")
    #     except IndexError:
    #         print("Index Error. Please input an integer that is in the range of the corpus.")
    #     finally:
    #         str_in = input()
    # 1st stage
    # print("Corpus statistics")
    # print(f"All tokens: {len(tokens)}")
    # tokens_set = set(tokens)
    # print(f"Unique tokens: {len(tokens_set)}")
    # menu(res_bigrams)
