def count_integer(numbers, integer):
    count = 0
    for i in numbers:
        if i == integer:
            count = count + 1

    if count > 0:
        print("The occurence of the integer", x, "is: ")
        return count
    else:
        return 42


list_num = [1, 2, 3, 4, 7, 6, 8, 7]
x = 7
print(count_integer(list_num, x))


def list_func(numbers, integer):
    count = 0
    for index, value in enumerate(numbers):
        #print("index: {0}, Value: {1}".format(index, value))
        if numbers[index] == integer:
           numbers[index] = 6
           count = count + 1

    if count > 0:
        new_list = numbers.copy()
        new_list.reverse()
        print(new_list)
        return numbers
    else:
        return []


list = [1, 2, 3, 4, 5]
int = 3
new_list = []
print(list_func(list, int))


def compare_lists(list1, list2):
    count = 0
    for i in list1:
        #print(i)
        for x in list2:
            #print(x)
            if i == x:
                count = count + 1
                new_list.append(i)      # genera new list, append jedes i das gleich x ist

    if count > 0:
        return new_list
    else:
        return []


a = [1, 2, 3, 4]
b = [4, 5, 1, 6]
new_list = []
print(compare_lists(a, b))


def remove_duplicates(lst):

    for i in lst:
        #print(i)
        if i not in new_list:
            new_list.append(i)
    if len(new_list) == 0:
        return lst
    else:
        return new_list


my_list = [1, 2, 3, 1, 2, 3, 4]
new_list = []
print(remove_duplicates(my_list))


def dict_func(dictionary):

    deftype = dictionary.get("Type", "unknown type")
    defbrand = dictionary.get("Brand", "unknown brand")
    defprice = dictionary.get("Price", "unknown price")

    if deftype == "unknown type" or defbrand == "unknown brand" or defprice == "unknown price":
        new_dict = {
            "Type": deftype,
            "Brand": defbrand,
            "Price": defprice
        }
        print("You have a", new_dict["Type"], "from", new_dict["Brand"], "that costs", new_dict["Price"])
        return new_dict

    else:
        print("You have a", dictionary["Type"], "from", dictionary["Brand"], "that costs", dictionary["Price"])
        dictionary["OS"] = "Linux"
        print(dictionary)


my_dict = {
    "Type": "Notebook",
    "Brand": "Lenovo",
    "Price": 500
}
new_dict = {}
dict_func(my_dict)