class ArrayHandler:
    def __init__(self, array):
        self.array = array

    def filter_unique_records(self):
        """Create a dictionary to store unique entries by their id and fill the dictionary with unique entries, and convert the dictionary back to a list"""

        unique_dict = {item["id"]: item for item in self.array}
        unique_array = list(unique_dict.values())
        return unique_array

    def sort_array_by_id(self):
        """Sort the list by the key "id" """

        sorted_array = sorted(self.array, key=lambda x: x["id"])
        return sorted_array

    def filter_by_id(self, id):
        """Leaving only elements with id = 2"""

        filtered_array = [item for item in self.array if item["id"] == id]
        return filtered_array

    def convert_to_dictionary(self, key, value):
        """Convert the list into a dictionary, where "title" becomes the key and "id" becomes the value"""

        new_dict = {item[key]: item[value] for item in self.array}
        return new_dict


array = [
    {"id": 1, "create": "14.04.2023", "title": "array1"},
    {"id": 4, "create": "09.02.2023", "title": "array4"},
    {"id": 2, "create": "03.07.2023", "title": "array2"},
    {"id": 1, "create": "22.04.2023", "title": "array1"},
    {"id": 2, "create": "12.12.2023", "title": "array2"},
    {"id": 3, "create": "04.04.2023", "title": "array3"},
]

array_handler = ArrayHandler(array)

# 1.Unique records
unique_records = array_handler.filter_unique_records()
print("Unique Records: ", unique_records)

# 2.Sort Array
sorted_array = array_handler.sort_array_by_id()
print("Sorted Array: ", sorted_array)

# 3.Filter Array
filtered_array = array_handler.filter_by_id(2)
print("Filtered Array: ", filtered_array)

# 4.Convert to dictionary
converted_dict = array_handler.convert_to_dictionary("title", "id")
print("Transformed Dictionary: ", converted_dict)
