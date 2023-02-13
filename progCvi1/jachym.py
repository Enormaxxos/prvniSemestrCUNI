use = set()

def get_array(entry,arr,lenght,index):
    print(f"calling get_array({arr}) with index {index}")
    
    for i in range(0,lenght-index):
        
        if i == 0:
            print(f"adding str({arr})")
            use.add(str(arr))
            arr = [starter]
        
        elif i + index == lenght - 1:
            arr.append(entry[i + index])
            print(f"adding str({arr})")
            use.add(str(arr))
            arr = [starter]
        
        else:
            temp = arr[:]
            temp.append(entry[i + index])
            get_array(entry,temp,lenght,i + index)

numbers = [i for i in range(1,int(input()) + 1)] # vygeneruj list s cislama [1,...,n]

for starter in numbers:
    get_array(numbers,[starter],len(numbers),numbers.index(starter))

print(use)

# use = list(use)
# for i in use:
#     print((" ".join(str(i) for i in eval(i))))