import re

def generate_ngrams(text,n):

    tokens = re.split('\\s+',text)
    ngrams=[]
    print(tokens)

    for i in range(len(tokens-n+1)):
        temp = [tokens[j] for j in range(i,i+n)]
    ngrams.append("".join(temp))

    print(ngrams)
    return ngrams


generate_ngrams('hello  i am divyesh',5)