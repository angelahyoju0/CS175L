#CS 175 L
#Angela An
#Expense Pie Chart

import matplotlib.pyplot as plt

def main():
    try:
        names = []
        expenses = []
        file = open('expenses.txt', 'r')
        x = 0
        for line in file:
            name = line.split('\t')[0]
            number = line.split('\t')[1].rstrip('\n')
            if number.isdigit():
                names.append(name)
                expenses.append(int(number))
                x += 1
        #print(names, expenses)
        plt.pie(expenses, labels = names)
        plt.title('Monthly Expenses')
        plt.show()

    except IOError:
        print ('An error occured trying to read the file.')

if __name__ == '__main__':
    main()
                            
