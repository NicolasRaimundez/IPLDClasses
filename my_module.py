nums_list = [1, 2, 4, 6, 8]
start = 2
stop = 7

# result = 2*4*6 = 48

def multiply_in_range(nums_list, start, stop):
    final_prod = None  # you put none in case that there are no numbers in range 

    for num in nums_list:
        if start <= num < stop:
        #if start <= num and num < stop:    --- another way of doing the last line
        
            if not final_prod:
                final_prod = 1

            final_prod *= num
            print(final_prod)

    return final_prod


multiply_in_range([1, 2, 4, 6, 8], 2, 7)
