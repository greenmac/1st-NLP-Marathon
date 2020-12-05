set1 = set()# 建立空的集合

set2 = {1, 2, 3, 4, 5}

# 從串列 (List) 來建立集合
set3 = set([i for i in range(20, 30)])

# 從數組 (Tuple) 來建立集合
set4 = set((10, 20, 30, 40, 50))

# 集合不會包含重複的資料, 你可以從 set5 印出來的結果得知
set5 = set((1, 1, 1, 2, 2, 3))

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)