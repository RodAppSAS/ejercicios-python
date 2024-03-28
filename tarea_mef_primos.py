primo = True
for i in range(2,101):
    for _ in range(i-1, 1, -1):
        if i % _ == 0:
            primo = False
            if primo == False:
                print(i, end=", ")
        

        
           
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]