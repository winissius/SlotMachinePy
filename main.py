import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8 
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2 
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            # column[line] = symbol
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet    
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbol_count):
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    return columns

def show_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], end=" ")
        print()

def deposit():
    while True:
        amount = input("How much do you want deposit? $\n")
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("Please enter a deposit greater than 0\n")
            else:
                break
        else:
            print("Please enter a valid number")
    return amount

def get_number_lines():
    while True:
        lines = input("How much lines do you wana bet (1 - " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Please enter a valid number\n")
        else:
            print("Please enter a valid number")
    return lines

def get_bet():
    while True:
        bet = input("How much do you wanna bet in each line?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"The bet must be between ${MIN_BET} - ${MAX_BET}\n")
        else:
            print("Please enter a valid number")
    return bet

def spin(balance):
        lines = get_number_lines()
        while True:
            bet = get_bet()
            total_bet = lines * bet

            if total_bet > balance:
                print(f"You don't have enough money to do this bet. Your current balance is ${balance}")
            else:
                break

        print(f"You are betting ${bet} in {lines} lines. Total bet is ${total_bet}.")
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        show_slot_machine(slots)
        winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}")
        print(f"You won on lines: ", *winnings_lines)
        return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press enter to spin or press Q to quit")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left the game with ${balance}")


main()