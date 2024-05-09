m1 = [[0 for _ in range(21)] for _ in range(21)]


m2 = [list(i) for i in m1]



import tools.Tychonoff as t

print("Tychonoff : ",t.Linear_Tychonoff_Distance(m1, m2))
