def main(table):
    res = []

    for row in table:
        temp = []
        temp.append(row[0])
        temp[0] = temp[0].replace('[at]', '@')
        temp.append(row[1])
        day = temp[1][8:]
        year = temp[1][:4]
        month = temp[1][5:7]
        temp[1] = day + '/' + month + '/' + year
        temp.append(row[4])
        x = temp[2]
        temp[2] = str(round(float(x[:5]), 2))
        if (len(temp[2])) == 3:
            temp[2] = temp[2] + '0'
        x2 = f'({x[6:9]}) {x[10:]}'
        x2 = x2[:-2] + '-' + x2[-2:]
        temp.append(x2)
        res.append(temp)

    return res
