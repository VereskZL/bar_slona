def read_file():
    """Считывает построчно входящий файл."""

    file = open('input.txt', encoding='utf-8', mode='r')
    result = {}
    stroka = 1

    while True:
        line = file.readline()
        if not line:
            writen_exel(result)
            break
        words = line.split()
        try:
            num = float(words[-1])
            food =' '.join(line.split()[:-1]).lower()
            result = combination(result ,food, num)
        except ValueError:
            num = float(words[-2])
            food =' '.join(line.split()[:-2]).lower()
            result = combination(result ,food, num)
        except:
            food = f'строка "{stroka}" не читаетcя'
            result = combination(result ,food)
        stroka += 1
        file.close

def combination(result:dict, food:str, num:float=0)-> dict:
    """Объединяет одинаковые строчки"""

    if food not in result:
        result[food] = num
    else:
        result[food] += num
    return result

def writen_exel(result):
    f = open('calc.csv', encoding='utf-8', mode='w')
    for key in result:
        f.write(f'{key},{str(result[key])}\n')


def main():
    read_file()

if __name__ == "__main__":
    main()