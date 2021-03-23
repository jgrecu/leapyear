#!/usr/bin/env python3


def sum_left_diagonal(matrice, n):
    left_diagonal_sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                left_diagonal_sum += int(matrice[i][j])
    return left_diagonal_sum


def sum_right_diagonal(matrice, n):
    right_diagonal_sum = 0
    for i in range(n):
        for j in range(n,-1,-1):
            if (i + j) == (n - 1):
                right_diagonal_sum += int(matrice[i][j])
    return right_diagonal_sum


def main():
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(input().strip().split())

    print('n:',n)
    print('matrice:', arr)
    
    left_sum = sum_left_diagonal(arr, n)
    right_sum = sum_right_diagonal(arr, n)
    absolute_diagonals_difference = abs(left_sum - right_sum)
    print('Absolute diagonals difference:', absolute_diagonals_difference)

if __name__ == "__main__":
    main()
