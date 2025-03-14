# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    startState = problem.getStartState()

    from util import Stack
    stack = Stack()
    
    stack.push((startState, []))
    
    visited = set()

    while not stack.isEmpty():
        state, path = stack.pop()
        
        if problem.isGoalState(state):
            print path
            print len(path)
            return path
        
        if state not in visited:
            visited.add(state)
            
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    newPath = path + [action]
                    stack.push((successor, newPath))
    
    return []
    

def breadthFirstSearch(problem):
    from util import Queue
    startState = problem.getStartState()
    queue = Queue()
    queue.push((startState, []))
    visited = set()
    
    while not queue.isEmpty():
        state, path = queue.pop()
        
        if problem.isGoalState(state):
            print path
            print len(path)
            return path
        
        if state not in visited:
            visited.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    queue.push((successor, path + [action]))
    
    return []

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    
    Returns a list of actions that reaches the goal, using a graph search approach.
    
    Each element on the priority queue is a tuple: (state, path_taken).
    The priority is the total cost to reach that state.
    """
    from util import PriorityQueue
    
    startState = problem.getStartState()
    pq = PriorityQueue()
    pq.push((startState, []), 0)
    
    visited = {}
    visited[startState] = 0
    
    while not pq.isEmpty():
        current_state, path = pq.pop()
        
        if problem.isGoalState(current_state):
            return path
        
        for successor, action, step_cost in problem.getSuccessors(current_state):
            new_cost = visited[current_state] + step_cost
            # Only add the successor if it has not been visited or we found a cheaper path.
            if successor not in visited or new_cost < visited[successor]:
                visited[successor] = new_cost
                new_path = path + [action]
                pq.push((successor, new_path), new_cost)
    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    
    Returns a list of actions that reaches the goal.
    
    The function uses a priority queue to order nodes by (cost + heuristic),
    and employs a graph search strategy to avoid revisiting states.
    """
    from util import PriorityQueue

    startState = problem.getStartState()
    pq = PriorityQueue()
    # Each queue item is (state, path, cost); initial priority is just the heuristic value.
    pq.push((startState, [], 0), heuristic(startState, problem))
    
    # Dictionary mapping states to the best cost found so far.
    visited = {}
    visited[startState] = 0

    while not pq.isEmpty():
        state, path, cost = pq.pop()

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            newCost = cost + stepCost
            # Only add the successor if it has not been visited or we found a cheaper path.
            if successor not in visited or newCost < visited[successor]:
                visited[successor] = newCost
                newPath = path + [action]
                priority = newCost + heuristic(successor, problem)
                pq.push((successor, newPath, newCost), priority)

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
