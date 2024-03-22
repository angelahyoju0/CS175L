#Angela An
#CS 175L
#Average From Input File with Exception Handling

def main():
    total = 0
    count = 0

    try:
        with open('numbers.txt', 'r') as file:
            for line in file:
                try:
                    number = float(line)
                    count = count + 1
                    total = total + number
                    print(f'I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}')
                except ValueError:
                    print(f"Bad data: {line.strip()} skipping")
    except IOError:
        print("SystemExit: File not found: numbers.txt - exiting")
        raise SystemExit

    if count > 0:
        average = total / count
        print(f'Average: {average:.1f}')

if __name__ == "__main__":
    main()
