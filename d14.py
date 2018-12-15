def d14_1(num_recipes):
    recipes = [3, 7]
    elf_1 = 0
    elf_2 = 1
    done = False
    while not done:
        new_recipe = recipes[elf_1] + recipes[elf_2]
        recipes.extend([int(e) for e in str(new_recipe)])
        elf_1 = (elf_1 + recipes[elf_1] + 1) % len(recipes)
        elf_2 = (elf_2 + recipes[elf_2] + 1) % len(recipes)
        if len(recipes) > num_recipes + 10:
            done = True
    return "".join([str(e) for e in recipes[num_recipes:num_recipes + 10]])

def d14_2(sequence):
    recipes = [3, 7]
    elf_1 = 0
    elf_2 = 1
    done = False
    last_indx_checked = 0
    recipes_str = None
    while not done:
        new_recipe = recipes[elf_1] + recipes[elf_2]
        recipes.extend([int(e) for e in str(new_recipe)])
        elf_1 = (elf_1 + recipes[elf_1] + 1) % len(recipes)
        elf_2 = (elf_2 + recipes[elf_2] + 1) % len(recipes)
        if len(recipes) >= len(sequence):
            test_str = "".join(str(e) for e in recipes[last_indx_checked:])
            last_indx_checked = len(recipes) - len(sequence)
            if sequence in test_str:
                recipes_str = "".join(str(e) for e in recipes)
                seq_indx = recipes_str.index(sequence)
                done = True
    return len(recipes_str[:seq_indx])

# My input
data = 598701

# Part 1
# Test cases
print(f"Expected {'5158916779'} and got {d14_1(9)}")
print(f"Expected {'0124515891'} and got {d14_1(5)}")
print(f"Expected {'9251071085'} and got {d14_1(18)}")
print(f"Expected {'5941429882'} and got {d14_1(2018)}")

print(f"Part 1 {d14_1(data)}")

# Part 2
# Test cases
print(f"Expected {9} and got {d14_2('51589')}")
print(f"Expected {5} and got {d14_2('01245')}")
print(f"Expected {18} and got {d14_2('92510')}")
print(f"Expected {2018} and got {d14_2('59414')}")

print(f"Part 2 {d14_2(str(data))}")
