tuple_example = ("cool", "you")
print("Hello, I think " +tuple_example[1] +" are " +tuple_example[0])

list_for_add = list(tuple_example)
list_for_add.append("done")
tuple_example = tuple(list_for_add)

print(tuple_example)

#Single cell tuple

single_cell = ("one",)
print(type(single_cell))