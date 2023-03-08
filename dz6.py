s = ({"JFLEX", 1962, 2003},
     {"JFLEX", 1962, 1992, 1978},
     {"JFLEX", 1962, 1992, 2015},
     {"JFLEX", 1962, 1992, 2020},
     {"JFLEX", 1990, 1978, "MUF"},
     {"JFLEX", 1990, 1978, "TWIG"},
     {"JFLEX", 1990, 1978, "KICAD"},
     {"JFLEX", 1990, 2015, "MUF"},
     {"JFLEX", 1990, 2015, "TWIG"},
     {"JFLEX", 1990, 2015, "KICAD"},
     {"JFLEX", 1990, 2020},
     {"JFLEX", 1981},
     {"NUMPY"},
     {"SHEN"})


def main(x):
    s1 = set(x)
    return [i for i in range(len(s))
            if not (len(s[i] - s1))][0]

# print(main(['TWIG', 1981, 2003, 2020, 'JFLEX']))
# print(main(['TWIG', 1962, 2003, 1978, 'JFLEX']))
# print(main(['MUF', 1990, 2003, 2015, 'SHEN']))
# print(main(['TWIG', 1981, 1992, 1978, 'NUMPY']))
# print(main(['TWIG', 1962, 1992, 2020, 'JFLEX']))
