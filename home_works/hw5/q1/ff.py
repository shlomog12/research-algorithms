def all_subsets_sorted_by_sum(my_list):
    # Get the first subset
    subset = []

    # Yield each subset in ascending order of its sum
    while True:
        yield sorted(subset, key=lambda x: sum(x))

        # Generate the next subset by adding the next item to the current subset
        subset += [my_list[len(subset)]]


# for s in all_subsets_sorted_by_sum(list(range(100))):
#     print(s)        

# Create the list
my_list = [1, 2, 3, 4]

# Get all subsets of the list sorted by their sum
all_subsets = all_subsets_sorted_by_sum(my_list)

# Print the subsets
for subset in all_subsets:
    print(subset)
