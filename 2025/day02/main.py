def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def part_one():
    count = 0
    lines = get_input()
    for line in lines:
        ranges = line.split(",")
        for r in ranges:
            start, end = map(int, r.split("-"))
            for i in range(start, end + 1):
                str_i = str(i)
                half = len(str_i) / 2
                if str_i[0:int(half)] == str_i[int(half):len(str_i)]:
                    count += i
    return count



def part_two():
    count = 0
    lines = get_input()
    for line in lines:
        ranges = line.split(",")
        for r in ranges:
            start, end = map(int, r.split("-"))
            print(f"Rang {start} - {end}")
            for value in range(start, end + 1):
                racha = False
                i = 0
                list = []
                to_check = []
                char_index = 0
                #print(f"Value: {value}")
                for character in str(value):
                    #print(f"Character: {character}")
                    #print(f"i: {i}")
                    #print(f"Mida del vector {len(list)}")
                    #print(f"Char index: {char_index}")
                    # Començem amb la llista
                    if not list:
                        #print("Llista buida, començem")
                        list.append(character)
                        #print(f"La llista és {list}")
                    # El character no correspon amb el ítem de la llista. Perdem la racha però mantenim la llista
                    elif list[i] != character and racha:
                        to_check = list.copy()
                        #print(f"El character {character} no correspon amb {list[i]}, NO RACHA")
                        list.append(character)
                        racha = False
                        i = 0
                        if list[i] == character:
                            i+=1
                            racha = True
                    # No estem en racha, afegim el valor
                    elif list[i] != character and not racha:
                        list.append(character)
                        #print(f"La llista és {list}")
                    # Si són iguals, afegim el següent character a comparar i incrementem 1.
                    elif list[i] == character and not racha:
                        #print(f"El character {character} correspon amb {list[i]}, RACHA")
                        to_check = list.copy()
                        list.append(character)
                        racha = True
                        i += 1
                    elif list[i] == character:
                        list.append(character)
                        racha = True
                        i += 1
                    # Estem al final del número i de la llista.
                    if racha and char_index+1 == len(str(value)) and len(list) == len(str(value)) and (len(list))/2 <= i:
                        #print(f"Valor extrany: {(len(list))/2}")
                        if i % len(to_check) != 0:
                            break
                        count += value
                        print(f"Donem aquesta solució per bona: {value}. Resultat: {count}")
                        break
                    # Si no estem al final de la llista, hem de comprovar si els nombres propers són iguals o no 4343[43]
                    char_index += 1
                    # Si estem en racha i hem arribat al final del vector ho donem per bo
                    #for i in range(1, longitud+1):
                    #    for items in list:
                    #        pass

            print("--------")
    return count


if __name__ == "__main__":
    #print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")