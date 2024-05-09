fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def distinguish(a):
    count = 0
    for fruit in fruits:
        if fruit == a:
            count += 1

    return count


print(f"배의 개수는? {distinguish('배')}개")