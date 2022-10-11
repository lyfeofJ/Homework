import statistics
import math
def adding_numbers():
    my_list = [*range(1,100,1)]
    statistics.mean(my_list)
    statistics.stdev(my_list)
    math.fsum(my_list)
    print(statistics.mean(my_list))
    print(statistics.stdev(my_list))
    print(math.fsum(my_list))
    
    
adding_numbers()