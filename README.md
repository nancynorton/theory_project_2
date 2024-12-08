Theory Project 2
1. Team Name: NN
2. Team members names and netids Nancy Norton (nnorton2)
3. Overall project attempted, with sub-projects: Program 1: Tracing NTM Behavior 
4. Overall success of the project: Successful - I was able to sucessfully trace and generate results for each string I tested
5. Approximately total time (in hours) to complete: 
6. Link to github repository:  https://github.com/nancynorton/theory_project_2
7. List of included files (if you have many files of a certain type, such as test files of different sizes, list just the folder): (Add more rows as necessary). Add more rows as necessary.

   - Code Files
   
   theory_project_2/program.py   --> Code to trace NTM 

   - Test Files

   theory_project_2/inputs1.csv   --> CSV File with list of input info, containing the string instance to be tested by the machine. Results in outputs1.csv.

   theory_project_2/inputs2.csv   --> CSV File with list of input info, containing the string instance to be tested by the machine. Results in outputs2.csv.

   theory_project_2/inputs3.csv   --> CSV File with list of input info, containing the string instance to be tested by the machine. Results in outputs3.csv.

   theory_project_2/inputs4.csv   --> CSV File with list of input info, containing the string instance to be tested by the machine. Results in outputs4.csv.

   theory_project_2/inputs5.csv   --> CSV File with list of input info, containing the string instance to be tested by the machine. Results in outputs5.csv. 

   
   - Output Files
  
   theory_project_2/outputs1.csv   --> CSV File containing the ouputs of program.py for the input file inputs1.csv. 

   theory_project_2/outputs2.csv   --> CSV File containing the ouputs of program.py for the input file inputs2.csv.

   theory_project_2/outputs3.csv   --> CSV File containing the ouputs of program.py for the input file inputs3.csv.

   theory_project_2/outputs4.csv   --> CSV File containing the ouputs of program.py for the input file inputs4.csv.

   theory_project_2/outputs5.csv   --> CSV File containing the ouputs of program.py for the input file inputs5.csv.


9. Programming languages used, and associated libraries: Python, csv

10. Key data structures (for each sub-project): trees

11. General operation of code

    Hamiltonian Path
    - data_ham_paths_MNO.py goes through each graph instance provided by check_ham_paths_MNO.csv and determines if there is a Hamiltonian path, stopping at the first instance of one for each graph. Along the way it measures the execution time of searching for a Hamiltonian path and plots instances of size vs time for finding a Hamiltonian path.
    - graph_ham_paths_MNO.py graphs each instance provided in the input file check_ham_paths_MNO.csv using NetworkX
   
    Hamiltonian Cycle
    - data_ham_cycle_MNO.py goes through each graph instance provided by check_ham_cycle_MNO.csv and determines if there is a Hamiltonian cycle, stopping at the first instance found. It measures the time taken to find the first Hamiltonian cycle for each graph and plots the size vs time of each graph where the size is the number of vertices in the graph
    - graph_ham_cycle_MNO.py creates a graph for each graph input provided in check_ham_cycle_MNO.csv using NetworkX
   
    Traveling Salesman
    - data_TSP_MNO.py goes through each graph instance provided by check_TSP_MNO.csv and searches for the cycle that requires the minimum or shortest path in terms of weights between the edges. While it traverses all possible paths that the traveling salesman could take, it keeps track of the path that required the minimum amount of weight. This code does so by using the concept of backtracking via the graph, such that it explores all possibilities but also backtracks to other possibilities that allow us us to find the shortest minimum path

12. What test cases you used/added, why you used them, what did they tell you about the correctness of your code.
    
    Hamiltonian Path
    - Used the CSV file check_ham_paths_MNO.csv containing 9 instances of graphs. I used them to search for Hamiltonian paths and they successfully did so, allowing me to see that my code could properly identify a Hamiltonian path.

    Hamiltonian Cycle
    - check_ham_cycle_MNO.csv contains 19 different graphs that vary in the number of vertices, edges, and whether they contain a Hamiltonian cycle or not. Using lots of different graphs allowed me to verify the correctness of my code. I wanted a good amount of both graphs that had a Hamiltonian cycle and ones that didn’t as well as a variety of sizes so I could see the exponential growth in time to search the graphs.

    Traveling Salesman
    - Used the CSV file check_TSP_MNO.csv which contains 13 test cases of graphs of different lengths and directions. I used the to search for the traveling salesman solution but given that all graph inputs have different sizes, then the execution vs time for each of these test cases was different and in exponential growth.

13. How you managed the code development
    - We separated the project so we each completed one program to find either the hamiltonian path, cycle, or traveling salesman. We worked piece by piece, testing and generating various graph cases for each subproblem to ensure our code was accurate and working correctly.

14. Detailed discussion of results:
    
    Hamiltonian Path
    - The size vs time graph for Hamiltonian paths indicated that as the number of vertices and number of edges within a graph increase, the time it takes to find a Hamiltonian path increases as well. There is a clear exponential increase in the graph demonstrating this. Note that each red dot represents that a Hamiltonian path was not found, and there are a lot more of these than green dots because for each Hamiltonian path that was found, the program first checked a bunch of options that did not successfully return a Hamiltonian path. This accounts for some of the shorter execution times at large sizes that are represented by red dots. Looking at the trend of the green dots, however, the exponential growth in size vs time is clear. 
In creating test cases for this graph, I found it interesting that the execution time is more strongly correlated with the number of edges in a graph than the number of vertices. This makes sense though, since more edges require the program to spend more time checking different paths, whereas adding more vertices does not necessarily mean there are more paths to check. For example, a graph with 20 vertices all in a straight line, each with only one edge connecting them would have a faster execution time than a graph where there are 20 vertices and 4 edges connected to each vertice because there are a lot more potential paths to check in the second graph. Overall, this project was successful in showing the exponential growth in execution time of finding a Hamiltonian path as the size of a graph is increased. 

    Hamiltonian Cycle
    - I found that when plotting the time vs size results, graphs that don’t have a hamiltonian cycle take much longer because they need to go through each possible cycle, while the ones that have a hamiltonian cycle stop cycling through the graph as soon as it is found. I also found that as more vertices are added, it takes significantly longer to go through each cycle since there are more to visit. This is shown by the exponential growth of the graph, both for the red data points (no Hamiltonian cycle) and the green data points (at least 1 Hamiltonian cycle). The time it takes to cycle through the graph and identify a Hamiltonian cycle increases exponentially as the number of vertices is increased. I only went up to 20 vertices, but I can see how this would start taking a very long time as that number grows. I also found that adding edges significantly increased the time it took to execute, which also could have been plotted instead of vertices, but both show the same idea that the size of the graph has a large impact on the time it took to search for a Hamiltonian cycle.

    Traveling Salesman
    - In solving the Traveling Salesman Problem, I observed that as the number of cities increased, the time required to find the optimal solution grew exponentially, consistent with the NP-hard nature of the problem. I implemented the dynamic programming approach (Held-Karp algorithm), which significantly reduced the computational complexity compared to brute force methods. Despite the optimizations, the exponential growth in time became apparent as the problem size increased. Additionally, I noticed that the number of possible paths plays a key role in execution time, with more densely connected cities requiring the program to evaluate a larger number of potential solutions. Overall, this project highlighted the challenge of scaling algorithms for TSP while demonstrating the effectiveness of dynamic programming for smaller cases.

15. How team was organized:

    We split our team up so that we each worked on an individual part of the project. Nancy worked on everything for Hamiltonian paths, Olivia worked on everything for Hamiltonian Cycles, and Maria worked on everything for the Traveling Salesman.

16. What you might do differently if you did the project again

    - Create more long and heavier test cases that might take longer to run
    - Graph the number of edges as the size in the size vs time plot and compare to see the impact compared to the number of vertices
   
17. Any additional material:

    none
