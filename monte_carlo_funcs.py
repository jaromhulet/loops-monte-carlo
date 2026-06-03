def create_strings(num_strings):

    '''
        Creates the 'box' of strings represented by string ends.
        Each element in the list of lists represents a string end.
        The first element represents the string number, the second element
        represents the end of the string (either 1 or 2).
        
        Inputs:
            num_strings (int) : number of strings in the box
        Output:
            strings (list) : 2d list with list for eact string end
    '''

    strings = []
    for i in range(num_strings):
        end_1 = [i,1]
        end_2 = [i,2]
        strings.append(end_1)
        strings.append(end_2)

    return strings


def select_ends(strings):

    '''
        Randomly selects two string ends
        
        Input:
            strings (list) : list of strings in the box
        Outputs:
            end_1 (list)   : first randomly selected string end
            end_2 (list)   : second randomly selected string end
            strings (list) : 2d list representing box, updated for ends that were removed 
    '''

    # select first end
    end_1 = strings.pop(random.randrange(len(strings)))
    # select second end
    end_2 = strings.pop(random.randrange(len(strings)))
    
    return end_1, end_2, strings


def tie_ends(strings, end_1, end_2):

    '''
        Logic to tie two ends together - if ends are from the same string,
        creates a circle, if they are not, tie them together and put them back in 
        strings list.
        
        Inputs:
            strings (list) : 2d list of strings in the box after ends have been removed
            end_1 (list)   : list that represents the first randomly selected end
            end_2 (list)   : list that represents the second randomly selected end

        Output:
            strings (list)    : 2d list with end added back if a circle was not made
            made_circle (bool) : True if a circle was made, False otherwise

    '''
  
    # if string id's are the same, show it made a circle
    if end_1[0] == end_2[0]:
        made_circle = True
    #if they are not the same 'tie' them
    else:
        # return first end back to list - arbitrary
        strings.append(end_1)

        # remove the end_2's other end from list
        end_2_str_num = end_2[0]
        strings = [x for x in strings if x[0] != end_2_str_num]

        made_circle = False
        
    return strings, made_circle
