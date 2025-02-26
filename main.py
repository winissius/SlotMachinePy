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


def main():
    balance = deposit()
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough money to do this bet. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} in {lines} lines. Total bet is ${total_bet}.")

# main()
get_slot_machine_spin(ROWS, COLS, symbol_count)