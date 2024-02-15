import sys

def readCsv(path):
    
    next(path)
    modalidades = []
    aptos = 0
    inaptos = 0
    distribuicao = {}

    for line in path:
        row = line.rstrip().split(',')
        if row[8] not in modalidades:
            modalidades.append(row[8])
        if row[12] == 'true':
            aptos +=1
        else:
            inaptos +=1
        idade = int(row[5])
        key = (idade//5)*5 
        nome = row[3] + ' ' + row[4]
        if key not in distribuicao:
            distribuicao[key] = (1,[nome])
        else:
            totaln, nomes = distribuicao[key]
            distribuicao[key] = (totaln + 1, nomes + [nome])

    modalidades_sort = sorted(list(set(modalidades)))

    total = aptos + inaptos
    percent_aptos = (aptos / total) * 100
    percent_inaptos = (inaptos / total) * 100

    return modalidades_sort, percent_aptos, percent_inaptos, distribuicao

def main():
    
        modalidades_sort, percent_aptos, percent_inaptos, distribuicao = readCsv(sys.stdin)
        
        print("Modalidades desportivas ordenadas:", modalidades_sort)
        print("\n")
        print("Percentagem de atletas aptos:", percent_aptos)
        print("\n")
        print("Percentagem de atletas inaptos:", percent_inaptos)
        print("\n")
        for i in range(0, 100, 5):
            if i in distribuicao: 
                print(f"[{i}-{i+4}]:", distribuicao[i])
                print("\n")
        print("\n")
        
if __name__ == "__main__":
    main()