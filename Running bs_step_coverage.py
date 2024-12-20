def binary_search_step(ele, elements, pivot):
    if ele < elements[pivot]:
        print("Less than")
        return -1
    elif ele > elements[pivot]:
        print("Equal to")
        return 1
    else:
        print("Greater than")
        return 0

# Enter your assert tests here
assert binary_search_step(1, [1,2,3], 1) == -1 # Less than
assert binary_search_step(2, [1,2,3], 1) == 0 
assert binary_search_step(3, [1,2,3], 1) == 1

# ele: 1 (kontrol edilecek değer).
# elements: [1, 2, 3] (karşılaştırma yapılacak liste).
# pivot: 1 (listedeki karşılaştırma yapılacak konum).