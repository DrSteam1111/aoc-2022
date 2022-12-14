import sys;

def main():
    input_file = open('input.txt', 'r')
    lines = input_file.read()

    sys.setrecursionlimit(2000)
    end = findSubroutine(lines)
    print(end)
    

def findSubroutine(lines):
    start = 0
    end = 0
    found = False

    def find():
        nonlocal start
        nonlocal end
        nonlocal found

        local_tracker = 0
        char_array = []

        for char in lines[start:]:
            local_tracker += 1
            if char in char_array:
                start += 1
                break
            
            char_array.append(char)
            
            if local_tracker == 4:
                end = start + 4
                found = True
                break
        
        if found == False:
            find()

    find()
    return end


if __name__ == '__main__':
    main()