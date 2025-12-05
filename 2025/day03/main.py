def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def part_one():
    final_count = 0
    lines = get_input()
    for line in lines:
        count = 0
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                value = int(line[i] + line[j])
                if value > count:
                    count = value
        final_count += count
    return final_count
# Index petit és el valor més petit de la meva llista
# Index numero és el índex del caracter que volem guardar al nostre vector
def fits_in_vector(list, index_petit, line, index_numero, m):
    numero_fins_final_llista = len(list) - index_petit
    numero_fins_final_linea = len(line) - index_numero
    # No tenim suficients elements.
    if numero_fins_final_linea < numero_fins_final_llista:
        return False, list, m
    mapping = {}
    index_list = index_petit
    for index_line in range(index_numero, index_numero + numero_fins_final_llista):
        list[index_list] = int(line[index_line])
        mapping[index_list] = index_line
        index_list += 1

    return True, list, mapping

def is_mapping_valid(old_map, new_map):
    for k, new_v in new_map.items():
        if k in old_map:
            if new_v < old_map[k]:
                return False
    return True

def part_two():
    lines = get_input()
    count = 0
    for line in lines:
        # Llista amb els 12 elements
        list = [0 for i in range(12)]
        mapping = {}
        for i,caracter in enumerate(line):
            caracter = int(caracter)
            if len(list) == 0:
                list.append(caracter)
            else:
                for j, _ in enumerate(list):
                    if list[j] < int(caracter):
                        condicio, new_list, new_mapping = fits_in_vector(list.copy(), j, line, i, mapping)
                        if condicio and is_mapping_valid(mapping, new_mapping):
                            mapping.update(new_mapping)
                            list = new_list
                            break
        result_str = ''.join(str(n) for n in list)
        print(f"The result is {result_str}")
        count += int(result_str)
    return count


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")