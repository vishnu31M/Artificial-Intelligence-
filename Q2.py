def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nq_util(board, col, n, solutions):
    if col >= n:
        solution = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(board[i][j])
            solution.append(row)
        solutions.append(solution)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nq_util(board, col + 1, n, solutions) or res
            board[i][col] = 0
    return res
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nq_util(board, 0, n, solutions)
    return solutions
def print_solution(solution):
    for row in solution:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()
def main():
    print("N-Queens Problem Solver")
    while True:
        try:
            n = int(input("Enter the number of queens (board size N x N, 1 < N < 20): "))
            if n <= 1 or n >= 20:
                print("Please enter a number between 2 and 19.")
                continue
            solutions = solve_n_queens(n)
            if not solutions:
                print(f"No solution exists for {n} queens.")
            else:
                print(f"\nFound {len(solutions)} solution(s) for {n} queens:")
                for i, solution in enumerate(solutions, 1):
                    print(f"Solution {i}:")
                    print_solution(solution)
            another = input("\nDo you want to solve for another N? (yes/no): ").lower()
            if another != 'yes':
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
