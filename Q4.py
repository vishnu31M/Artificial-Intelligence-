from itertools import permutations
def solve_cryptarithmetic():
    print("Enter the cryptarithmetic puzzle in the format 'WORD1 + WORD2 = WORD3'")
    print("Example: SEND + MORE = MONEY")
    equation = input("Enter your equation: ").upper().replace(" ", "")
    try:
        parts = equation.split('+')
        word1 = parts[0]
        remaining = parts[1].split('=')
        word2 = remaining[0]
        word3 = remaining[1]
    except:
        print("Invalid equation format. Please use the format 'WORD1 + WORD2 = WORD3'")
        return
    all_letters = sorted(list(set(word1 + word2 + word3)))
    if len(all_letters) > 10:
        print("Error: Too many unique letters (maximum 10)")
        return    
    print(f"\nSolving: {word1} + {word2} = {word3}")
    print(f"Unique letters: {', '.join(all_letters)}")
    first_letters = {word1[0], word2[0], word3[0]}
    for digits in permutations('0123456789', len(all_letters)):
        if any(digits[all_letters.index(letter)] == '0' for letter in first_letters):
            continue 
        mapping = {letter: digit for letter, digit in zip(all_letters, digits)}
        try:
            num1 = int(''.join([mapping[c] for c in word1]))
            num2 = int(''.join([mapping[c] for c in word2]))
            num3 = int(''.join([mapping[c] for c in word3]))
        except KeyError:
            continue
        if num1 + num2 == num3:
            print("\nSolution found:")
            print(f"{word1} = {num1}")
            print(f"{word2} = {num2}")
            print(f"{word3} = {num3}")
            print("\nLetter assignments:")
            for letter in sorted(mapping.keys()):
                print(f"{letter}: {mapping[letter]}")
            return
    print("\nNo solution found for this equation.")

if __name__ == "__main__":
    solve_cryptarithmetic()
