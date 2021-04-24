

def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2)    # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    result = 0
    if len(first_list_of_values) != len(second_list_of_values):    # checks both lists have same length
        return
    # covariance components:
    n = len(first_list_of_values)
    first_mean = mean(first_list_of_values)
    second_mean = mean(second_list_of_values)
    first_second = [first_list_of_values[i] * second_list_of_values[i] for i in range(n)]    # multiply x*y accordingly
    result += (sum(first_second) - n*first_mean * second_mean) / float(n-1)
    return result


def correlation(first_list_of_values, second_list_of_values):
    result = 0
    # correlation components:
    first_std = variance(first_list_of_values)**0.5
    second_std = variance(second_list_of_values)**0.5
    result += (covariance(first_list_of_values, second_list_of_values) / (first_std * second_std))
    return result
