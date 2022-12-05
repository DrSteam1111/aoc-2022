def main():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    higest_calories = [];
    current_value = 0;

    for line in lines:
        if (line.isspace()):
            higest_calories.append(current_value);    
            current_value = 0;
            continue;
        current_value += int(line)

    quicksort(higest_calories)
    higest_calories.reverse()
    
    total_top_three = 0;
    for i in range(3):
        total_top_three += higest_calories[i]

    print (total_top_three)

def quicksort(a):
    def do_partition(a, start, end):

        pivot_idx = end
        pivot = a[pivot_idx]

        idx = start - 1
 
        def increment_and_swap(j):
            nonlocal idx
            idx += 1
            a[idx], a[j] = a[j], a[idx]
 
        [increment_and_swap(j) for j in range(start, end) if a[j] < pivot]
        a[idx+1], a[end] = a[end], a[idx+1]

        return idx+1
 
    def quicksort_helper(a, start, end):
        if start < end:
            pivot_idx = do_partition(a, start, end)
            quicksort_helper(a, start, pivot_idx-1)
            quicksort_helper(a, pivot_idx+1, end)
 
    quicksort_helper(a, 0, len(a)-1)

if __name__ == '__main__':
    main()