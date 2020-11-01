import unicodedata
import random
from collections import defaultdict

random.seed(42)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('ASCII')
    return only_ascii


def classify(src, tgt):
    src = src.replace(" <EOS>", "").replace("<F> ", "").replace("<M> ", "").replace("<N> ", "").strip()
    tgt = tgt.replace(" <EOS>", "").strip()
    src = remove_accents(src)
    tgt = remove_accents(tgt)
    #print(src, tgt)
    if tgt == src + ' n' or tgt == src + ' e n':
        noun_class = 1
    elif tgt == src + ' e':
        noun_class = 2
    elif tgt == src + ' e r':
        noun_class = 4
    elif tgt == src:
        noun_class = 3
    elif tgt == src + ' s':
        noun_class = 5
    else:
        noun_class = 6
    return noun_class


if __name__ == "__main__":
    data = []

    with open("unimorph_compound-src.txt", encoding="utf-8") as f_src, \
         open("unimorph_compound-tgt.txt", encoding="utf-8") as f_tgt:
        for src, tgt in zip(f_src, f_tgt):
            noun_class = classify(src, tgt)
            data.append((src.strip(), tgt.strip(), noun_class))

    with open("data.tsv", 'w', encoding="utf-8") as f:
        for src, tgt, noun_class in data:
            f.write(f"{src}\t{tgt}\t{noun_class}\n")

    random.shuffle(data)

    n = int(len(data) * 0.80)
    m = int(len(data) * 0.90)

    with open("train.src", 'w', encoding="utf-8") as f_src, \
         open("train.tgt", 'w', encoding="utf-8") as f_tgt:
        src, tgt, _ = zip(*data[:n])
        f_src.write("\n".join(src))
        f_tgt.write("\n".join(tgt))

    with open("val.src", 'w', encoding="utf-8") as f_src, \
         open("val.tgt", 'w', encoding="utf-8") as f_tgt:
        src, tgt, _ = zip(*data[n:m])
        f_src.write("\n".join(src))
        f_tgt.write("\n".join(tgt))

    with open("test.src", 'w', encoding="utf-8") as f_src, \
         open("test.tgt", 'w', encoding="utf-8") as f_tgt:
        src, tgt, _ = zip(*data[m:])
        f_src.write("\n".join(src))
        f_tgt.write("\n".join(tgt))
