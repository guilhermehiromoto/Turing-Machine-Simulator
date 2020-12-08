## Author
## Guilherme Amaral Hiromoto 11218959
## Leandro Satoshi de Siqueira 10893103

## Classes
class state:
    def __init__(self, number):
        self.number = number
        self.transitions = []
        self.isInicial = False
        self.isAc = False
    
    def change_isInitial(self):
        self.isInicial = True
        
    def change_isAc(self):
        self.isAc = True
    
    def add_transition(self, transition):
        self.transitions.append(transition)
    
    def show(self):
        print("###################################")
        print("###################################")
        print(f"State: {self.number}")
        print(f"isInicial: {self.isInicial}")
        print(f"isAc: {self.isAc}\n")
        for i in range(len(self.transitions)):
            print("-----------------------------------")
            print (f"From: {self.transitions[i].from_}")
            print (f"To: {self.transitions[i].to_}")
            print (f"Symbol In: {self.transitions[i].symbol_in}")
            print (f"Symbol Out: {self.transitions[i].symbol_out}")
            print (f"Movement: {self.transitions[i].move}")

class transition:
    def __init__(self, from_, symbol_in, to_, symbol_out, move):
        self.from_ = from_
        self.to_ = to_
        self.symbol_in = symbol_in
        self.symbol_out = symbol_out
        self.move = move
        
    def print(self):
        print (f"From: {self.from_}")
        print (f"To: {self.to_}")
        print (f"Symbol In: {self.symbol_in}")
        print (f"Symbol Out: {self.symbol_out}")
        print (f"Movement: {self.move}\n")


## Functions
def read_states(turing_machine):
    #1
    n_states = int(input())             
    for i in range(n_states):
        newState = state(i)
        turing_machine.append(newState)
    #2
    line2 = input().split(" ")           
    n_symbols = int(line2[0])
    symbols = []
    for i in range(n_symbols):
        symbols.append(line2[i+1])
    #3
    line3 = input().split(" ")           
    n_symbols_ext = int(line3[0])
    symbols_ext = []
    for i in range(n_symbols_ext):
        symbols_ext.append(line3[i+1])
    
    #4
    turing_machine[0].change_isInitial()
    acc = int(input())
    turing_machine[5].change_isAc()

def read_transitions(turing_machine):
    #5-n
    n_transitions = int(input())
    for i in range(n_transitions):
        line6 = input().split(" ")
        newTransition = transition(int(line6[0]), line6[1], int(line6[2]), line6[3], line6[4])
        turing_machine[newTransition.from_].add_transition(newTransition)
        
  
#n+1-end
def check_valid_string(turing_machine, string):
    state = turing_machine[0]
    if dfs(turing_machine, state, string, 1):
        print("aceita")
    else:
        print("rejeita")
        
def dfs(turing_machine, state, string, pos):
    while True:
        if(state.isAc):
            return True
        flag = 0
        
        for transition in state.transitions:
            if transition.symbol_in == string[pos]:
                flag = 1
                string[pos] = transition.symbol_out
                if transition.move == 'R' and pos < len(string):
                    pos+=1
                if transition.move == 'L' and pos > 0:
                    pos-=1
                state = turing_machine[transition.to_]
                break
        if flag == 0:
            return False

def main():

	## Building Turing Machine
	turing_machine = []
	read_states(turing_machine)
	read_transitions(turing_machine)

	## Reading inputs for the tape
	for i in range(int(input())):
	    tape =  list('B' + input() + 'B')
	    check_valid_string(turing_machine,tape)
	
	return 0

if __name__ == "__main__":
    main()
