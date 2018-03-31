def generate2(lst2):
    for sublst in lst2:
        try:
            for num in generate2(sublst):
                yield num
        except:
            yield sublst


lst2 = [1, [2, [3, 4]], 5, [6, [7, [8, 9]]]]
print(list(generate2(lst2)))
