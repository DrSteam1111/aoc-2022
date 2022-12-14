import re
from dataclasses import dataclass

@dataclass
class Instruction:
    amount: int
    from_index: int
    to_index: int

    def __init__(self, instruction):
        regex = re.search('move (.*) from (.*) to (.*)', instruction)
        self.amount = int(regex.group(1))
        self.from_index = int(regex.group(2)) - 1
        self.to_index = int(regex.group(3)) - 1
        

def main():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    crates = parseCrates(lines)
    instructions = createInstructions(lines)
    
    movedCrates = doInstructions(crates, instructions)
    print(formatAnswer(movedCrates))

def parseCrates(lines):
    groups = [[] for i in range(9)]
    for i in range(8):
        strippedLine = lines[i].replace('\n', '')
        groupedLine = re.sub('    ', ' ', strippedLine);
        lineArray = re.split('\s', groupedLine);

        for idx, char in enumerate(lineArray):
            if char != '':
                groups[idx].append(char);
            
    return groups

def createInstructions(lines):
    instructions = []
    for line in lines[10:]:
        instructions.append(Instruction(line))

    return instructions

def doInstructions(crates, instructions):
    afterInst = crates
    for inst in instructions:
        for _ in range(inst.amount):
            to_move = afterInst[inst.from_index].pop(0)
            afterInst[inst.to_index].insert(0, to_move)
    return afterInst

def formatAnswer(movedCrates):
    stringAnswer = ''
    for m_crates in movedCrates:
        stringAnswer += m_crates[0]

    stringAnswer = re.sub('\[|\]', '', stringAnswer)

    return stringAnswer

if __name__ == '__main__':
    main()