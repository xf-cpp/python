def Calculate_the_sum_of_the_squares_of_the_first_n_numbers(n):
    sum = 0
    for i in range(n+1):
        sum +=  i**2
    return sum

if __name__=="__main__":
    print(Calculate_the_sum_of_the_squares_of_the_first_n_numbers( int(input("n") )))