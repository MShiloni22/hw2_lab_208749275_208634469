from statistics import mean, median, variance, correlation
import csv


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    file_path = './winequality.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {:.2f}, Std: {:.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values)**0.5))

    strongest_pair = ["aaa", "bbb"]
    high_correlation = -0.9
    weakest_pair = ["aaa", "bbb"]
    low_correlation = 0.1
    # here you should compute correlations. Be careful, pair should be sorted before printing
    for i, keys1 in enumerate(data):
        for j, keys2 in enumerate(data):
            if j <= i:
                continue
            if correlation(data[keys1], data[keys2]) > high_correlation:
                if keys1 < keys2:
                    strongest_pair[0] = keys1
                    strongest_pair[1] = keys2
                else:
                    strongest_pair[0] = keys2
                    strongest_pair[1] = keys1
                high_correlation = correlation(data[keys1], data[keys2])
            if correlation(data[keys1], data[keys2]) < low_correlation:
                if keys1 < keys2:
                    weakest_pair[0] = keys1
                    weakest_pair[1] = keys2
                else:
                    weakest_pair[0] = keys2
                    weakest_pair[1] = keys1
                low_correlation = correlation(data[keys1], data[keys2])

    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))
    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use


if __name__ == '__main__':
    run_analysis()
