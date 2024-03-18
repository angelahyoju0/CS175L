#Angela An
#CS 175L
#Average from Input File



def main():
    total = 0
    count = 0

    with open('numbers.txt', 'r') as file:
        for line in file:
            number = float(line)
            count = count + 1
            total = total + number
            print(f'I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}')

    if count > 0:
        average = total / count
        print(f'Average: {average:.1f}')

if __name__ == "__main__":
    main()
