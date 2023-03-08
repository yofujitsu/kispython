def main(text):
    if ('\n' in text):
        text = text.replace('\n', '')
    text = text.replace(" ", '')
    text = text.replace("(", '')
    text = text.replace(")", '')
    open = text.count("[[")
    text = text.replace("[[", '')
    text = text.replace("]],", '<==')
    keys = []
    values = []
    text = text.split("<==")
    for i in range(open * 2):
        if (i % 2 == 0):
            keys.append(text[i])
        else:
            values.append(text[i])

    temp = dict(zip([data for data in keys], [data for data in values]))
    return temp


text1 = "( [[gean_230<== ceat_38 ]], [[ leisdi_38 <== teorbe]], )"
print(main(text1))

text2 = "([[ veorin<== onerat ]], [[ attere_901 <==teatqu_266 ]],[[raer<==raace_120 ]], [[ incece_291 <== rierle ]], )"
print(main(text2))
