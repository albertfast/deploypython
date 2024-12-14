# Given a list of non-zero integers, find and print the first adjacent pair of elements that have the same sign. If there is no such pair, print 0.

a_list = [int(str_numbers) for str_numbers in input().split()]  # Input list


def same_sign(a_list):
    # Generate list of tuples of adjacent elements with the same sign
    pairs = [(a_list[i], a_list[i + 1]) for i in range(len(a_list) - 1) if (a_list[i] > 0 and a_list[i + 1] > 0) or (a_list[i] < 0 and a_list[i + 1] < 0)]

    if pairs:
        print(pairs[0][0], pairs[0][1])  # Print first pair
    else:
        print(0)  # No such pair

same_sign(a_list)

'''
def same_sign(a_list):
    for i in range(len(a_list) - 1):
        # Kontrol: İki yan yana elemanın işareti aynı mı?
        if (a_list[i] > 0 and a_list[i + 1] > 0) or (a_list[i] < 0 and a_list[i + 1] < 0):
            # Eğer aynı işarete sahipse çifti yazdır ve fonksiyondan çık
            print(a_list[i], a_list[i + 1])
            return
    
    # Eğer hiç aynı işarete sahip çift bulunmazsa 0 yazdır
    print(0)

same_sign(a_list)
'''