def get_input():
    with open("example.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def part_one():
    count = 0
    dial = 50
    lines = get_input()
    for line in lines:
        number = line[1:]
        if line[0] == "L":
            dial -= int(number)
        else:
            dial += int(number)
        dial = dial % 100
        print(dial)
        if dial == 0:
            count += 1
    return count


def part_two():
    count = 0
    dial = 50
    lines = get_input()
    for line in lines:
        number = line[1:]
        #print(f"Dial {dial}")
        #print(f"Linia {line}")
        if line[0] == "L":
            if dial - int(number) <= 0 and dial != 0:
                print("Underflow")
                nou_dial = dial - int(number)
                print(f"Count: {nou_dial // 99}")
                count += abs(nou_dial // 99)
                if nou_dial == 0:
                    count+=1
                print(count)
            dial -= int(number)
        else:
            if dial + int(number) > 99:
                print("Overflow")
                nou_dial = dial + int(number)
                print(f"Count: {nou_dial // 99}")
                count += abs(nou_dial // 99)
                if nou_dial == 0:
                    count+=1
                print(count)
            dial += int(number)
        #test = dial / 100
        #print(f"Dial:{test}")
        #if test > 0:
        #    count += test // 1
        #else:
        #    count += -1*(test // 1)
        dial = dial % 100
    return count


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")