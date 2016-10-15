__author__ = 'Anupam Panwar'

def main(input_list):
    candy_list = [0]
    current_candies =1
    i =0
    while i < len(input_list)-1:
        if (input_list[i] < input_list[i+1]):
            candy_list[i]= current_candies
            candy_list.insert(i+1,current_candies+1)
            i = i+1
            current_candies =current_candies+1
        elif (input_list[i] > input_list[i+1]):
            candy_list[i]= current_candies
            candy_list.insert(i+1,current_candies)
            i = i+1
            current_candies =1
        elif (input_list[i] == input_list[i+1]):
            candy_list[i]=current_candies
            candy_list.insert(i+1,current_candies-1)
            i = i+1
    print sum(candy_list)



if __name__ == "__main__":
    t = int(raw_input().strip())
    input_list = list()
    for a0 in xrange(t):
        t1 = int(raw_input().strip())
        input_list.append(t1)
    main(input_list)