
def converter(val : str) -> float:
    start = val.find('(')
    end = val.find(')')
    rollno = val[:start].strip()
    return [rollno, float(val[start+1:end])]

def InsertionSortDesc(arr : list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[1] > arr[j][1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

with open('gpa.txt', 'r') as f:
    with open('desc.txt', 'w') as w:
        lines = f.readlines()
        students = []
        for line in lines:
            students.append(converter(line))
        sorted_students = InsertionSortDesc(students)
        for pos, student in enumerate(sorted_students):
            w.write(f"{pos+1} {student[0]} ({student[1]:.2f})\n")