# Nancy Norton

import csv
from collections import deque

class NTM:
    def __init__(self, filename, max_steps=500, max_depth=50, max_transitions=500):
        self.transitions = {}
        self.states = []
        self.input_alphabet = []
        self.tape_alphabet = []
        self.start_state = ''
        self.accept_state = ''
        self.reject_state = ''
        self.max_steps = max_steps  # max number of steps
        self.max_depth = max_depth  # max depth of config tree
        self.max_transitions = max_transitions  # max num of transitions
        self.input_string = ''
        
        self.parse_input_file(filename)
        self.input_string = self.input_string
        #self.input_string = self.input_string + '_'  # adding blank to the end bc need it to reach the accept state 
        self.initial_configuration = (self.input_string, self.start_state, 0)  # tape, state, head pos

    def parse_input_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            lines = list(reader)
            
            # Read in the head of the csv 
            self.machine_name = lines[0][0]
            self.states = lines[1][0].split(',')
            self.input_alphabet = lines[2][0].split(',')
            self.tape_alphabet = lines[3][0].split(',')
            self.start_state = lines[4][0]
            self.accept_state = lines[5][0]
            self.reject_state = lines[6][0]
            self.input_string = lines[7][0]
            
            # Read in the transitions
            for line in lines[8:]:
                if len(line) != 5:
                    continue 
                state, char, next_state, write_char, direction = line
                if (state, char) not in self.transitions:
                    self.transitions[(state, char)] = []
                self.transitions[(state, char)].append((next_state, write_char, direction))
            return self.input_string

    def run(self):
        transition_tree = [[self.initial_configuration]]
        visited = set()
        total_transitions = 0
        accepting_depth = None
        num_steps = 0

        # print initial info 
        print(f"Machine: {self.machine_name}")
        print(f"Initial string: {self.input_string}")

        # run machine 
        for depth in range(self.max_depth):
            # if we exceed the max number of steps allowed, stop execution
            if num_steps >= self.max_steps:  
                print(f"Execution stopped after exceeding max steps of {self.max_steps}.")
                return
            # if finished processing configs 
            if depth >= len(transition_tree):
                break 

            current_level = transition_tree[depth]  # current level of configurations
            next_level = []  # holds  configurations for the next level

            for (tape, state, head_position) in current_level:
                num_steps += 1 
                if (tape, state, head_position) in visited:
                    continue
                visited.add((tape, state, head_position))

                # to print each config 
                left = tape[:head_position]
                head = tape[head_position]
                right = tape[head_position + 1:]
                print(f"Depth {depth}: {left}{state}|{head}|{right}")
                #print(f"Depth {depth}: left of head: {left}, state: {state}, head char: {head}, right of string: {right}")

                # check if it's in an accepting state
                if state == self.accept_state:
                    # save depth 
                    accepting_depth = depth
                    print(f"String accepted in {depth} transitions.")
                    break  # exit loop
            

                # check for all  transitions from the current state and the given symbol 
                if (state, tape[head_position]) in self.transitions:
                    for next_state, write_char, direction in self.transitions[(state, tape[head_position])]:
                        # update  tape with the written char
                        new_tape = tape[:head_position] + write_char + tape[head_position + 1:]
                        new_head_position = head_position + (1 if direction == 'R' else -1)

                        # out fo bounds checking for new head position
                        if new_head_position < 0:
                            new_tape = "_" + new_tape  # add a blank on the left 
                            new_head_position = 0
                        elif new_head_position >= len(new_tape):
                            new_tape = new_tape + "_"  # add a blank on the right

                        # create the new configuration
                        new_config = (new_tape, next_state, new_head_position)
                        next_level.append(new_config)
                        total_transitions += 1 # update total num of configs 

            # if maximum number of transitions is exceeded, stop execution
            if total_transitions > self.max_transitions:
                print(f"Execution stopped after exceeding max transitions of {self.max_transitions}.")
                return

            # if we find an accepting state, break
            if accepting_depth is not None:
                break 

            if next_level:
                transition_tree.append(next_level)  # add the next level of configurations
          

       # If no accept state found, check for reject
        if accepting_depth is None:
            print(f"String rejected in {self.max_depth} steps.")
            
        
        # display the total num of transitions 
        print(f"Total transitions simulated: {total_transitions}")

        #display depth of the tree
        print(f"Tree depth: {depth}")

        
def main():
    filename = 'inputs5.csv'  # update this with the current input file
    max_depth = 50  # max depth of the configuration tree we are allowing 
    max_transitions = 100  # max number of transitions we are allowing 

    ntm = NTM(filename, max_depth=max_depth, max_transitions=max_transitions) 
    ntm.run()

if __name__ == "__main__":
    main()
