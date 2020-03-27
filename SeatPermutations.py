from itertools import permutations

def get_seat_perms(num_seats, num_starting_matches, num_maximum_allowed_matches):
    """Finds all of the seat permutations that match the given parameters.

    Returns
    -------
    successes : List<List<int>>

    Parameters
    ----------
    num_seats : int
        Number of seats at the table.
    num_starting_matches: int
        Number of people who sit down in the correct seat at the very beginning.
    num_maximum_allowed_matches: int
        Number of maximum allowable matches to check
        (e.g. 7 people, 1 person sits at the correct seat, if we want orientations that cannot have more than 1 person
        sitting in the correct seat no matter how the table is rotated after initial seating, then maximum allowable
        matches would be 1).
    """
    placement = list(range(1, num_seats + 1))
    seat_perms = list(permutations(range(num_starting_matches + 1, num_seats + 1)))
    seat_perms_as_lists = get_seat_perms_as_lists(seat_perms, num_starting_matches)
    seat_perms_x_match = get_seat_perms_x_match(placement, seat_perms_as_lists, num_starting_matches)
    successes = get_successes(placement, seat_perms_x_match, num_maximum_allowed_matches)

    return successes

def get_seat_perms_as_lists(seat_perms, num_starting_matches):
    '''Changes the list of permutation tuples to a list of lists.

    Returns
    -------
    seat_perms_as_lists : List<List<int>>

    Parameters
    ----------
    seat_perms : List<Tuple<int>>
        All permutations of non-fixed placements as tuples.
    num_starting_matches: int
        Number of people who sit down in the correct seat at the very beginning.
    '''
    seat_perms_as_lists = list()
    for perm in seat_perms:
        perms_as_list = list(perm)
        for i in range(num_starting_matches):
            perms_as_list.insert(i, i + 1)
        seat_perms_as_lists.append(perms_as_list)
    return seat_perms_as_lists

def get_seat_perms_x_match(placement, seat_perms_as_lists, num_starting_matches):
    '''Filter out permutations from seat_perms_as_lists that start with num_starting_matches match(es).

    Returns
    -------
    seat_perms_as_lists : List<List<int>>

    Parameters
    ----------
    placement: List<int>
        List of numbers from 1 to num_seats that represent the packages on the table.
    seat_perms_as_lists : List<List<int>>
        All permutations of initial placements as lists.
    num_starting_matches: int
        Number of people who sit down in the correct seat at the very beginning.
    '''
    seat_perms_x_match = list()
    for perm_list in seat_perms_as_lists:
        matching = 0
        for i in range(len(perm_list)):
            if perm_list[i] == placement[i]:
                matching = matching + 1
        if matching == num_starting_matches:
            seat_perms_x_match.append(perm_list)
    return seat_perms_x_match

def get_successes(placement, seat_perms_x_match, num_maximum_allowed_matches):
    '''Gets the number of successes after rotations

    Checks all rotations of the lists of interest to see if all rotations result in a match count lower than the
    num_maximum_allowed_matches.  This can be better than checking if any match counts are greater than the
    num_maximum_allowed_matches for diagnostic reasons, but is slower than using the any match check.

    Returns
    -------
    successes : List<List<int>>

    Parameters
    ----------
    placement: List<int>
        List of numbers from 1 to num_seats that represent the packages on the table.
    seat_perms_x_match : List<List<int>>
        All permutations of placements where starting matches equals num_starting_matches.
    num_maximum_allowed_matches: int
        Number of maximum allowable matches to check
        (e.g. 7 people, 1 person sits at the correct seat, if we want orientations that cannot have more than 1 person
        sitting in the correct seat no matter how the table is rotated after initial seating, then maximum allowable
        matches would be 1).
    '''
    successes = list()
    for list_to_check in seat_perms_x_match:
        matching_amount_list = list()
        for j in range(len(list_to_check)):
            matching = 0
            rotated_list = list_to_check[-j:] + list_to_check[:-j]
            for k in range(len(rotated_list)):
                if rotated_list[k] == placement[k]:
                    matching += 1
            matching_amount_list.append(matching)
        if all(i <= num_maximum_allowed_matches for i in matching_amount_list):
            successes.append(list_to_check)
    return successes

def print_perms(seat_perms, num_to_print = None):
    '''Prints num_to_print number of seat_perms permutations.

    Parameters
    ----------
    seat_perms : List<List<int>>
        All of the permutations that were found to be successful for the orientation
    number_to_print: int
        Number of permutations to print on screen
    '''
    if num_to_print == None or num_to_print > len(seat_perms):
        num_to_print = len(seat_perms)

    print()
    if len(seat_perms) != 0:
        print("Seats")
        placement = list(range(1, len(seat_perms[0]) + 1))
        print(f"{placement}")
        print()
        print("Permutations")
        for i in range(num_to_print):
            print(seat_perms[i])
    else:
        print("No permutations exist for those conditions!")


def main():

    num_seats = 7
    num_starting_matches = 1
    num_maximum_allowed_matches = 1
    maximum_num_perms_to_print = 3

    #TODO: Add user entry and validation for what the user enters. Can use the same validation for checking if ints
    #      Starting matches must be <= number of seats
    #      Allowed matches must <= number of starting matches
    #      All numbers must be ints
    #      Limit number of seats to something reasonable like 500 so computer can't crash

    seat_perms = get_seat_perms(num_seats, num_starting_matches, num_maximum_allowed_matches)
    print_perms(seat_perms, maximum_num_perms_to_print)

if __name__ == "__main__":
    main()