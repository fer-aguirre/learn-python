"""
A function to remove 
duplicates from a list
"""

# def remove_duplicates(list):
#     non_duplicates = []
#     for element in list:
#         if element not in non_duplicates:
#             non_duplicates.append(element)
#     return non_duplicates


# Function version with set()
def remove_duplicates(list):
    return set(list)
    

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))


if __name__ == "__main__":
    run()
