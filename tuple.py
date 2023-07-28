tuple01 = (10, 20, 30)
tuple01 = tuple01 + (40, )

print(tuple01)

#튜플 = 리스트
tuple02 = 1, 2, 3, 4
list02 = [1, 2, 3, 4]
tuple03 = tuple(list02)

if tuple02 == tuple03:
    print("equal")
else:
    print("not equal")

tuple04 = 1,2,3
tuple05 = 4,5,6
#튜플 합치기
tuple06 = tuple04 + tuple05
print(tuple06)

#튜플 반복
tuple07 = tuple04 * 4
print(tuple07)

# 튜플 스왑
a, b = 11, 22
a, b = b, a
print(a, b)