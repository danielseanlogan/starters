import math
import random

################################################################################

def declareWinner(name: str, num_votes_for: int, num_votes_total: int, round_number: int) -> None:
    ''' A helper function which prints an f-string to announce a winner if
        certain criteria are met.
    Parameters:
        name: the name of a given candidate
        num_votes_for: the number of votes which the given candidate recieved
        (as reflected in votes_counts)
        num_votes_total: the number of votes cast in the given election
        (as reflected by the len of the list of votes)
    Returns:
        None (prints a line, does not have a return)
    '''
    if num_votes_for > (num_votes_total / 2): # is not inclusive, as there may
    # be a need to distinguish an election between two candidates with half
    # of the votes each
        rounded_percentage = round((num_votes_for/num_votes_total) *100, 2)
        print(f"Candidate {name} wins in round {round_number} with {rounded_percentage}% of the vote")

def declareEliminated(name: str, num_votes_for: int, num_votes_total: int) -> None:
    ''' A helper function which prints out which candidate is eliminated at the
        end of a round and the percentage of the vote which that candidate
        recieved
    Parameters:
        name: the name of the candidate that has been eliminated
        num_votes_for: the number of votes which the eliminated candidate has
        recieved
        num_votes_total: the number of votes which were tallied in total during
        that round of the election
    Returns:
        None (prints a line)
    '''
    rounded_percentage = round((num_votes_for/num_votes_total)*100, 2) #will round to two significant figures
    print(f"Candidate {name} is eliminated with {rounded_percentage}% of the vote")


def printSlate(candidates: "list[str]", top_votes: "list[str]", second_votes: "list[str]", third_votes: "list[str]", round_number: int) -> None:
    ''' A helper function which creates a slate which presentes the round number
        and the preferences of voters
    Parameters:
        candidates: a list with str of all of the candidate's names who are
        still in the running
        top_votes: voters' first choices in the election
        second_votes: voters' second choices in the election
        third_votes: voters' third choices in the election
        round number: the number of rounds of voting which have taken place
        at the time of printing the slate
    Returns:
        None (prints 5 lines)
    '''
    print(f"----- ROUND {round_number} -----")
    print(f"Candidates:     {candidates}")
    print(f"Choice 1 votes: {top_votes}")
    print(f"Choice 2 votes: {second_votes}")
    print(f"Choice 3 votes: {third_votes}")

def copyList(list: list) -> list:
    ''' A helper function which will created a copy of a list
    Parameters:
        list: the list being copied
    Returns:
        a list which is a copy of the list put into the function
    '''
    new_list = [] #starting with an empty list to append to
    for i in range(len(list)): #using a for loop because lists are mutable
        new_list.append(list[i])
    return new_list

def findIndexOfMin(integer_list: "list[int]") -> int:
    ''' A helper function to find the index of the minimum value of the list (or
        the first minimum in the list if there are multiple)
    Parameters:
        integer_list: a list containing only integers
    Returns:
        the index of the minimum value of a given list
    '''
    min_value = integer_list[0] #starting off the min value as being the first
    #integer in the list
    for i in range(1, len(integer_list), 1):
        if integer_list[i] < min_value:
            min_value = integer_list[i] #if the value at i is less than the
            #current minimum value, it becomes the new minimum
    minimum_indexes = [] #creating a list to hold all minimums in the list
    for i in range(0, len(integer_list), 1): #creating another for loop for the
    #extra credit
        if integer_list[i] == min_value: #checks for all possition in the list
        #where the minimum is the value
            minimum_indexes.append(i)
    random_value = random.randint(0, len(minimum_indexes)-1) #picks a random
    #value of the minimum
    index = minimum_indexes[random_value]
    return index


def removeCandidate(candidates: "list[str]", index: int) -> "list[str]":
    ''' A helper function to remove a candidate (a string) from a list and to
        create a new list without that candidate
    Parameters:
        candidates: a list of all of the candidates still in the election
        index: the index in the list "candidates" which is to be removed
    Returns:
        a list of strings which is all of the candidates except for the candidate
        that was removed
    '''
    new_list = [] #starting with an empty list
    for i in range(0, len(candidates)):
        if i != index: #skipping only the index step
            new_list.append(candidates[i]) #creating a list with everything
            #except the index
    return new_list

def reassignTopChoices(current_top_choices: "list[str]", second_choices: "list[str]", third_choices: "list[str]", eliminated_candidate: str, new_candidates: "list[str]") -> "list[str]":
    ''' A helper function to take the new list of candidates and determine which
        have gained votes after the elimination of another candidate
    Parameters:
        current_top_choices: a list of strings representing the current list of
        votes prior to this reassignment
        second_choices: a list of strings which holds voters' second choices
        for candidates
        third_choices: a list of strings which holds voters' third choices for
        candidates
        eliminated_candidate: the name of the candidate which has been eliminated
        in this round of voting.
        new_candidates: a list of strings which represent the candidates which
        are still in the running
    Returns:
        a list of strings which represents the new vote count for every
        candidate still in the race
    '''
    new_top_choices = [] #a list to store the new top choices
    do_not_third = [] #a ticker to determine whether or not third choices should
    #be considered
    for i in range(len(current_top_choices)):
        do_not_third.append(0) #manually creating a list of zeros that has the
        #same length as current_top_choices
    for i in range(len(current_top_choices)):
        new_top_choices.append(current_top_choices[i]) #could have used the
        #copyList function, but decided to do it manually instead of calling a
        #helper within a helper
    for i in range(len(current_top_choices)):
        if current_top_choices[i] == eliminated_candidate:
            new_top_choices[i] = "holder" #using "holder" to mark the places
            #where there will either be a second choice, third choice, or
            #none of the above
    for i in range(len(current_top_choices)):
        if new_top_choices[i] == "holder" and do_not_third[i] == 0: #second part
        #of the if statement should always be true, but a good reminder
            for j in range(len(new_candidates)):
                if new_candidates[j] == second_choices[i]:
                    new_top_choices[i] = second_choices[i]
                    do_not_third[i] = "pass" #setting this so that there will
                    #not be a third choice overwriting the second choice.
                elif new_top_choices[i] == "holder" and do_not_third[i] != "pass":
                    #if there is a third choice but not a second choice, the
                    #elif should go through.
                    for k in range(len(new_candidates)):
                        if new_candidates[k] == third_choices[i]:
                            new_top_choices[i] = third_choices[i]
    return new_top_choices


def findCandidateIndex(candidates: list, which_candidate: str) -> int:
    ''' A function which Indexes the votes which particular candidates recieve
        into a single list where the number of votes which they recieve can be
        retrieved for other functions (in conjunction with countTheVotes).
    Parameters:
        candidates: The list of candidates in the given election
        which_candidate: the candidate which is being considered
    Returns:
        An integer which reflects the possition of which_candidate on the list
        of candidates.
    '''
    if which_candidate in candidates: #tried this with a number of for loops,
    #but it seems that an if statement is all that is needed.
        return candidates.index(which_candidate) #accessing the index of
        #which_candidate
    else:
        return None


def countTheVotes(candidates: "list[str]", votes: "list[str]") -> "list[int]":
    ''' A function which takes two lists and creates a list which tallys the
        number of votes for every candidate.
    Parameters:
        candidates: The list of candidates in any given election
        votes: The list of votes which each candidate recieves
    Returns:
        A list of integers which reflects the number of votes which each
        candidate recieved at the same index as that candidate
    '''
    votes_counts = [] #have to start with an empty list to append to
    for i in range(len(candidates)):
        count = 0 #starting with an empty count
        for j in range(len(votes)):
            if candidates[i] == votes[j]:
                count += 1
            else:
                pass
        votes_counts.append(count)
    return votes_counts #uses two different for loops in order to represent the
    #two parameter lists and to compare the values in each of the lists in every
    #possible point of comparison

def areAllEqual(votes_counts: list) -> bool:
    ''' A function which determines whether or not every candidate has recieved
        the exact same number of votes as every other candidate
    Parameters:
        votes_counts: a list generated by countTheVotes which represents the
        number of votes which each candidate has recieved
    Returns:
        True if all candidates recieved the same number of votes, false
        if any candidates do not have the same number of votes.
    '''
    checker = votes_counts[0]
    result = True
    for i in range(len(votes_counts)):
        if votes_counts[i] == checker: #comparing every element of the list with
        # the first element of the list to see if all elements of the list are
        # identical
            pass #keeping the value of result the same as it was prior to going
            #through this if statement
        else:
            result = False #this else statement only has to be reached a single
            #time to re-assign result to be false instead of true
    return result



def findSimpleMajorityWinner(votes_counts: "list[int]") -> int or None:
    ''' A function which takes votes_counts from the function countTheVotes
        and determines whether or not any candidate has recieved a majority of
        the votes in the election
    Parameters:
        votes_counts: a list of integers which is the number of votes which
        each candidate has recieved
    Returns:
        an integer which is the index of the candidate that has recieved more
        than half of the votes in the election if one exists. Otherwise, returns
        None.
    '''
    total_votes = 0 #start with 0 to add todo
    for i in range(len(votes_counts)):
        total_votes += votes_counts[i]
    holder = 0 #creating a value to hold the index of the value which has the
    #majority
    control = 0 #creating a ticker to note the number of times which the
    #function goes through the if statement
    for i in range(len(votes_counts)):
        if votes_counts[i] > (total_votes / 2):
            holder += i
            control += 1
    if control != 0:
        return holder
    else:
        return None #these last few lines are to ensure that if the index of the
        #majority candidate is 0, that will only be returned if the if statement
        #has been gone through.

def runElection(round1_candidates: "list[str]", choice1_votes: "list[str]", choice2_votes: "list[str]", choice3_votes: "list[str]", debug: bool = True) -> None:
    ''' A function which orders together all of the helper functions to run as
        election from start to finish
    Parameters:
        round1_candidates: a list of the candidates in the election
        choice1_votes: a list with the votes which each candidate has recieved
        as voters' first choices
        choice2_votes: a list with the votes which each candidate has recieved
        as voters' second choices
        choice3_votes: a list with the votes which each candidate has recieved
        as voters' third choices
        debug: debugs the election, when false, will not run
    Returns:
        None, but prints the winner of the election or a line reflecting that
        the election did not have a winner.
    '''
    if debug == True: #if this is not the case, the whole function can't work
        round_number = 1
        printSlate(round1_candidates, choice1_votes, choice2_votes, choice3_votes, round_number)
        round1_counts = countTheVotes(round1_candidates, choice1_votes)
        counts = copyList(round1_counts)
        candidates = copyList(round1_candidates)
        if areAllEqual(counts) == False and findSimpleMajorityWinner(counts) != None:
        #must meet both of these criteria, though the elif could make it so
        #the first part is redundant, but still not a bad idea
            winner = findSimpleMajorityWinner(counts)
            winningCandidate = round1_candidates[winner] #turns the index from the
            #function return above and turns it into the string to search
            winningIndex = findCandidateIndex(round1_candidates, winningCandidate) #searches for the
            #string which is to be printed.
            total_votes = 0
            for i in range(len(counts)):
                total_votes += counts[i] #tallying the total number of votes by
                #counting the votes for each candidate
            declareWinner(winningCandidate, counts[winner], total_votes, round_number)
            return None #returning None so that the rest of what is written won't
            #happen no matter what
        elif areAllEqual(counts) == True:
            random_index = random.randint(0, len(candidates)-1) #creating a random
            #candidate index to be the winner
            winner = candidates[random_index]
            rounded_percentage = round(1/len(candidates)*100, 2) #rounded to the
            #nearest two decimals
            print(f"Candidate {winner} wins in round {round_number} by lot with {rounded_percentage}% of the votes")
        elif areAllEqual(counts) == False: #this should always be true. could
        #also be an else statement
            eliminated_candidate_index = findIndexOfMin(counts) #since I don't
            #have the randomness, will be the first instance of the minimum that
            #gets returned
            eliminated_candidate = candidates[eliminated_candidate_index]
            eliminated_candidate_votes = counts[eliminated_candidate_index]
            total_votes = 0
            for i in range(len(counts)): #tallying the total votes to compare
            #with the votes fo the eliminated candidate
                total_votes += counts[i]
            declareEliminated(eliminated_candidate, eliminated_candidate_votes, total_votes)
            candidates             = removeCandidate(candidates, eliminated_candidate_index)
            votes                  = reassignTopChoices(choice1_votes, choice2_votes, choice3_votes, eliminated_candidate, candidates)
            round_number           += 1 #ticking the round number up before printing the Slate
            counts                 = countTheVotes(candidates, votes) #updating the counts before printing the Slate
            printSlate(candidates, choice1_votes, choice2_votes, choice3_votes, round_number)
            if areAllEqual(counts) == False and findSimpleMajorityWinner(counts) != None:
                winner = findSimpleMajorityWinner(counts)
                winningCandidate = round1_candidates[winner] #turns the index from the
                #function return above and turns it into the string to search
                findCandidateIndex(round1_candidates, winningCandidate) #searches for the
                #string which is to be printed.
                total_votes = 0
                for i in range(len(counts)):
                    total_votes += counts[i] #tallying the total votes to compare
                    #with the number of votes recieved by the winnner
                declareWinner(winningCandidate, counts[winner], total_votes, round_number)
                return None
            elif areAllEqual(counts) == True:
                random_index = random.randint(0, len(candidates)-1) #generating a random
                #winner among the remaining candidates
                winner = candidates[random_index]
                rounded_percentage = round(1/len(candidates)*100, 2) #rounding to
                #the nearest two decimal places
                print(f"Candidate {winner} wins in round {round_number} by lot with {rounded_percentage}% of the votes")
            elif areAllEqual(counts) == False and findSimpleMajorityWinner(counts) == None:
                eliminated_candidate_index = findIndexOfMin(counts) #another elimination
                eliminated_candidate = candidates[eliminated_candidate_index]
                eliminated_candidate_votes = counts[eliminated_candidate_index]
                total_votes = 0
                for i in range(len(counts)):
                    total_votes += counts[i]
                declareEliminated(eliminated_candidate, eliminated_candidate_votes, total_votes) #another declaration of an eliminated candidate
                candidates             = removeCandidate(candidates, eliminated_candidate_index)
                votes                  = reassignTopChoices(votes, choice2_votes, choice3_votes, eliminated_candidate, candidates)
                round_number           += 1 #ticking up to round 3 for the printSlate
                counts                 = countTheVotes(candidates, votes) #getting the new tallys for the printSlate
                printSlate(candidates, choice1_votes, choice2_votes, choice3_votes, round_number)
                if areAllEqual(counts) == False and findSimpleMajorityWinner(counts) != None:
                    winner = findSimpleMajorityWinner(counts)
                    winningCandidate = candidates[winner] #turns the index from the
                    #function return above and turns it into the string to search
                    findCandidateIndex(candidates, winningCandidate) #searches for the
                    #string which is to be printed.
                    total_votes = 0
                    for i in range(len(counts)):
                        total_votes += counts[i]
                    declareWinner(winningCandidate, counts[winner], total_votes, round_number)
                    return None
                elif areAllEqual(counts) == True: #if all candidates have the same votes in
                #round 3
                    random_index = random.randint(0, len(candidates)-1)
                    winner = candidates[random_index]
                    print(f"Candidate {winner} wins in round {round_number} by lot with {(1/len(candidates)*100):.3}% of the votes")
                    return None






################################################################################

def printTest(function_call_str: str, result: None, expected: None) -> None:
    ''' Streamlines regression testing calls, displaying the function call being
        made, the actual result, & the expected result. Not all typehints for
        this function are acurate to every function being tested, so I used the
        typehints which are accurate to runElection.
    Parameters:
        function_call_str: a string representing the function call, e.g.,
        "randomString(10)"
    result:
        the actual result of that function call (a list)
    expected:
        the expected result of that function call (a list)
    Returns:
        None -- just prints
    '''
    print(f"Testing {function_call_str}:")
    print(f"   Result:   {repr(result)}")
    print(f"   Expected: {repr(expected)}")

################################################################################

def main():

    #got rid of the tests from Lab2, as they were cluttering up the file, and
    #I know that the helper functions from back then work as intended

    #Tests for declareEliminated:

    name = "loser"
    num_votes_for = 1
    num_votes_total = 7
    declareEliminated(name, num_votes_for, num_votes_total)

    name = "bigLoser"
    num_votes_for = 0
    num_votes_total = 10
    declareEliminated(name, num_votes_for, num_votes_total)

    name = "closeLoser"
    num_votes_for = 3
    num_votes_total = 13
    declareEliminated(name, num_votes_for, num_votes_total)


    #Tests for printSlate

    Candidates = ['Fay', 'Jay', 'May']
    top_votes = ['Jay', 'Jay', 'Fay', 'Jay', 'May']
    second_votes = ['Fay', 'May', 'Fay', 'Jay', 'May']
    third_votes = ['May', 'Fay', 'Fay', 'Jay', 'May']
    round_number = 1
    printSlate(Candidates, top_votes, second_votes, third_votes, round_number)

    #Tests for copyList


    #testing for an empty list

    list = []
    printTest('copyList([])', copyList(list), [])


    #testing for a list of integers
    list = [1, 2, 5, 6, 12]
    printTest('copyList([1, 2, 5, 6, 12])', copyList(list), [1, 2, 5, 6, 12])

    #testing for a list of strings

    list = ['fi', 'fie', 'fo', 'fum']
    printTest("copyList(['fi', 'fie', 'fo', 'fum'])", copyList(list), ['fi', 'fie', 'fo', 'fum'])


    #Tests for findIndexOfMin:

    #testing for one integer in the list
    list = [1]
    printTest("findIndexOfMin([1])", findIndexOfMin(list), 0)


    #testing for a list with multiple of the same minimum
    random.seed(13632)
    list = [1, 1, 1, 1, 6]
    printTest("findIndexOfMin([1, 1, 1, 1, 6])", findIndexOfMin(list), 3)

    #testing for randomness

    random.seed(13013)
    printTest("findIndexOfMin([1, 1, 1, 1, 6])", findIndexOfMin(list), 0)


    random.seed(1231253)
    printTest("findIndexOfMin([1, 1, 1, 1, 6])", findIndexOfMin(list), 3)


    #testing for start of the list minimum
    list = [1, 2, 3, 4, 5]
    printTest("findIndexOfMin([1, 2, 3, 4, 5])", findIndexOfMin(list), 0)

    #testing for end of the list minimum
    list = [5, 4, 3, 2, 1]
    printTest("findIndexOfMin([5, 4, 3, 2, 1])", findIndexOfMin(list), 4)


    #testing removeCandidate
    candidates = ['James', 'John', 'Jill']
    index = 1
    printTest("removeCandidate(['James', 'John', 'Jill'], 1)", removeCandidate(candidates, index), ['James', 'Jill'])

    #testing removeCandidate at the front of a list
    candidates = ['James', 'John', 'Jill']
    index = 0
    printTest("removeCandidate(['James', 'John', 'Jill'], 0)", removeCandidate(candidates, index), ['John', 'Jill'])

    #testing removeCandidate at the back of a list

    candidates = ['James', 'John', 'Jill']
    index = 2
    printTest("removeCandidate(['James', 'John', 'Jill'], 2)", removeCandidate(candidates, index), ['James', 'John'])

    #testing removeCandidate in a list of one string

    candidates = ['James']
    index = 0
    printTest("removeCandidate([], 0)", removeCandidate(candidates, index), [])

    #testing reassignTopChoices
    #testing for replacing a vote at the back
    remaining_candidates = ["a", "b"]
    choices    = ["a", "a", "b", "c"]
    choice2    = ["c", "c", "a", "d"]
    choice3    = ["c", "c", "d", "a"]
    eliminated_candidate = "c"
    printTest('reassignTopChoices(["a", "a", "b", "c"], ["c", "c", "a", "d"], ["c", "c", "d", "a"], "c", ["a", "b"])', reassignTopChoices(choices, choice2, choice3, "c", ["a", "b"]), ['a', 'a', 'b', 'a'])


    #testing for replacing a vote at the front
    remaining_candidates    = ["a", "b"]
    choices                 = ["c", "a", "b", "a"]
    choices2                 = ["d", "b", "a", "b"]
    choices3                = ["a", "c", "c", "c"]
    eliminated_candidate    = "c"
    printTest('reassignTopChoices(["c", "a", "b", "a"], ["d", "b", "a", "b"], ["a", "c", "c", "c"], "c", ["a", "b"])' , reassignTopChoices(choices, choices2, choices3, eliminated_candidate, remaining_candidates), ["a", "a", "b", "a"])

    #testing for replacing a vote at the front and back
    remaining_candidates        = ["a", "b"]
    choices                     = ["c", "a", "b", "c"]
    choices2                    = ["d", "b", "a", "a"]
    choices3                    = ["a", "c", "c", "b"]
    eliminated_candidate        = "c"
    printTest('reassignTopChoices(["c", "a", "b", "c"], ["d", "b", "a", "a"], ["a", "c", "c", "b"], "c", ["a", "b"])' , reassignTopChoices(choices, choices2, choices3, eliminated_candidate, remaining_candidates), ["a", "a", "b", "a"])

    #testing for an eliminated second vote, but valid third vote
    remaining_candidates        = ["a", "b"]
    choices                     = ["a", "a", "b", "c"]
    choice2                     = ["c", "c", "a", "d"]
    choice3                     = ["c", "c", "d", "a"]
    eliminated_candidate        = "c"
    printTest('reassignTopChoices(["a", "a", "b", "c"], ["c", "c", "a", "d"], ["c", "c", "d", "a"], "c", ["a", "b"])', reassignTopChoices(choices, choice2, choice3, eliminated_candidate, remaining_candidates), ['a', 'a', 'b', 'a'])

    #testing for voters only listing their first candidate of choice
    remaining_candidates        = ["a", "b", "c"]
    choices                     = ["a", "a", "b", "c"]
    choice2                     = ["b", "b", "a", "x"]
    choice3                     = ["c", "c", "c", "x"]
    eliminated_candidate        = "c"
    printTest('reassignTopChoices(["a", "a", "b", "c"], ["b", "b", "a", "x"], ["c", "c", "c", "x"], "c", ["a", "b", "c"])', reassignTopChoices(choices, choice2, choice3, eliminated_candidate, remaining_candidates), ['a', 'a', 'b', 'holder'])

    #testing for voters listing only their first and third candidates of choice
    remaining_candidates        = ["a", "b", "c"]
    choices                     = ["a", "a", "b", "c"]
    choice2                     = ["b", "b", "a", "x"]
    choice3                     = ["c", "c", "c", "a"]
    eliminated_candidate        = "c"
    printTest('reassignTopChoices(["a", "a", "b", "c"], ["b", "b", "a", "x"], ["c", "c", "c", "a"], "c", ["a", "b", "c"])', reassignTopChoices(choices, choice2, choice3, eliminated_candidate, remaining_candidates), ['a', 'a', 'b', 'a'])

    #testing runElection
    candidates = ["a", "b", "c", "d"]
    choice1_votes = ["a", "a", "b", "c"]
    choice2_votes = ["b", "b", "a", "a"]
    choice3_votes = ["d", "d", "c", "d"]
    debug = True
    runElection(candidates, choice1_votes, choice2_votes, choice3_votes, debug)

def main_rcv_testing():

    # for the tests below, use any four names you like;
    # for "clean" printed output, you may want to make all entries the same
    #   width by including trailing spaces, as in "Alice" below;
    # include exactly four candidates

    names  = ["A", "B", "C", "D"]
    #names = ["Fay", "Jay", "May", "Ray"]
    #names = ["Alice   ", "Frankie ", "Franklin", "Snowball"]

    a,b,c,d = names  # short variables for (max 4) candidates will make list creation below convenient
    x = "x"          # x will indicate a vote that will not be considered in the process


    # <BEGIN> UNCOMMENT THIS BLOCK FOR THE ROUND 1 TESTING PHASE OF runElection

    # candidate B wins 1st round
    candidates = [a,b,c]     # three candidates
    choice1    = [b,b,a,b,b] # b wins in round 1
    choice2    = [x,x,x,x,x]
    choice3    = [x,x,x,x,x]
    runElection(candidates, choice1, choice2, choice3, debug = True)  # use after debugging added
    print("\t Expected: Candidate B wins 1st round w/ 80%")

    print('=' * 70)

    # random candidate wins 1st round
    candidates = [a,b,c]       # use three candidates
    choice1    = [b,b,a,a,c,c] # randomly-selected winner in round 1
    choice2    = [x,x,x,x,x,x]
    choice3    = [x,x,x,x,x,x]
    runElection(candidates, choice1, choice2, choice3, debug = True)  # use after debugging added
    print("\t Expected: Random candidate wins 1st round by lot w/ 33%")

    print('=' * 70)

    # <END> UNCOMMENT THIS BLOCK FOR THE ROUND 1 TESTING PHASE OF runElection



    # <BEGIN> UNCOMMENT THIS BLOCK FOR THE ROUND 2 TESTING PHASE OF runElection

    # candidate A wins 2nd round
    candidates = [a,b,c]      # three candidates
    choice1    = [a,b,c,a,b]  # c will be eliminated in round 1
    choice2    = [b,b,a,b,b]  # choice2[2] replaces choice1[2] --> a wins in round 2
    choice3    = [c,b,b,a,b]
    runElection(candidates, choice1, choice2, choice3, debug = True)  # use after debugging added
    print("\t Expected: Candidate A wins 2nd round w/ 60%")

    print('=' * 70)

    # candidate A or B wins 2nd round
    candidates = [a,b,c]        # three candidates
    choice1    = [a,b,c,a,b,b]  # c will be eliminated in round 1
    choice2    = [x,x,a,x,x,x]  # choice2[2] replaces choice1[2] --> a or b @ random in round 2
    choice3    = [x,x,x,x,x,x]
    runElection(candidates, choice1, choice2, choice3, debug = True)  # use after debugging added
    print("\t Expected: Random candidate A or B wins 2nd round by lot w/ 50%")

    print('=' * 70)

    # <END> UNCOMMENT THIS BLOCK FOR THE ROUND 2 TESTING PHASE OF runElection



    # <BEGIN> UNCOMMENT THIS BLOCK FOR THE ROUND 3 TESTING PHASE OF runElection

    # candidate C wins 3rd round w/ all choice2 replacements
    candidates = [a,b,c,d]            # four candidates
    choice1    = [a,a,b,b,b,c,c,c,d]  # d eleminated in round 1
    choice2    = [c,c,x,x,x,x,x,x,c]  # choice2[-1] replaces choice1[-1] --> still no winner in round 2
    choice3    = [x,x,x,x,x,x,x,x,x]  # choice2[0:2] replaces choice1[0:2] --> c wins round 3
    runElection(candidates, choice1, choice2, choice3, debug = True)  # use after debugging added
    print("\t Expected: Candidate C wins 3rd round w/ 66.67%")

    print('=' * 70)

    # candidate C wins 3rd round w/ replacements from choice2 and choice3
    candidates = [a,b,c,d]            # four candidates
    choice1    = [a,a,b,b,b,c,c,c,d]  # d eleminated in round 1
    choice2    = [d,d,x,x,x,x,x,x,c]  # choice2[-1] replaces choice1[-1] --> still no winner in round 2
    choice3    = [b,c,x,x,x,x,x,x,x]  # choice2[0:2] replaces choice1[0:2] --> c wins round 3
    runElection(candidates, choice1, choice2, choice3, debug = True)  # use after debugging added
    print("\t Expected: Candidate C wins 3rd round w/ 55.56%")

    # <END> UNCOMMENT THIS BLOCK FOR THE ROUND 3 TESTING PHASE OF runElection

    # My own additional tests

    # winner first round by majority vote

    candidates  = [a,b,c,d]
    choice1     = [a, a, a, b, a, c, d]
    choice2     = [x, x, x, x, x, x, x]
    choice3     = [x, x, x, x, x, x, x]
    runElection(candidates, choice1, choice2, choice3, debug = True)
    print("\t Expected: Candidate A wins first round with 57.14% of the vote")


    # winner first round by lot
    random.seed(313743131351342)
    candidates  = [a,b,c,d]
    choice1     = [a, a, b, b, c, c, d, d]
    choice2     = [x, x, x, x, x, x, x, x]
    choice3     = [x, x, x, x, x, x, x, x]
    runElection(candidates, choice1, choice2, choice3, debug = True)
    print("\t Expected: Candidate D wins in round 1 by lot with 25.0% of the vote")

    # winner second round by majority
    candidates  = [a,b,c,d]
    choice1     = [a, a, a, b, c, d]
    choice2     = [x, x, x, a, a, a]
    choice3     = [x, x, x, x, x, x]
    runElection(candidates, choice1, choice2, choice3, debug = True)
    print("\t Expected: Candidate A wins in round 2 with 66.67% of the vote")

    #winner second round by lot
    random.seed(23424475659)
    candidates  = [a,b,c,d]
    choice1     = [a, a, b, c, c, d]
    choice2     = [x, x, d, a, a, b]
    choice3     = [x, x, x, x, x, x]
    runElection(candidates, choice1, choice2, choice3, debug = True)
    print("\t Expected: Candidate C wins in round 2 by lot with 33.33% of the votes")

    #winner third round by majority
    candidates  = [a,b,c,d]
    choice1     = [a, a, b, c, c, c, d]
    choice2     = [c, c, a, a, a, a, c]
    choice3     = [b, b, c, d, d, b, a]
    runElection(candidates, choice1, choice2, choice3, debug = True)
    print("\t Expected: Candidate C wins in round 3 with 57.14% of the votes")

    #winnder third round by lots
    random.seed(3112)
    candidates  = [a,b,c,d]
    choice1     = [a, a, a, b, c, c, c, d]
    choice2     = [c, c, b, a, a, a, a, c]
    choice3     = [b, b, c, c, d, d, b, a]
    runElection(candidates, choice1, choice2, choice3, debug = True)
    print("\t Expected: Candidate C wins in round 3 by lot with 50.0% of the votes")

    runElection([p,q,r], [q,q,p,q,q], [0,0,0,0,0], [0,0,0,0,0])


main()

main_rcv_testing()   # UNCOMMENT THIS TO USE THE PROVIDED TESTS FOR runElection
