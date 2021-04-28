from itertools import permutations


def get_seat_perms(num_seats, num_starting_matches, num_matches_for_funded):
    '''Finds all of the seat permutations that match the given parameters.

    Returns
    -------
    successes : List<List<int>>

    Parameters
    ----------
    num_seats : int
        Number of seats at the table.
    num_starting_matches: int
        Number of people who sit down in the correct seat at the very beginning.
    num_matches_for_funded: int
        Number of matches required to be funded.
    '''
    placement = list(range(1, num_seats + 1))
    unlocked_seat_perms = list(permutations(
        range(num_starting_matches + 1, num_seats + 1)))
    seat_perms_as_lists = get_seat_perms_as_lists(
        unlocked_seat_perms, num_starting_matches)
    seat_perms_x_match = get_seat_perms_x_match(
        placement, seat_perms_as_lists, num_starting_matches)
    successes = get_successes(
        placement, seat_perms_x_match, num_matches_for_funded)

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


def get_successes(placement, seat_perms_x_match, num_matches_for_funded):
    '''Gets the number of successes after rotations

    Checks all rotations of the lists of interest to see if all rotations result in a match count lower than the
    num_matches_for_funded.  This can be better than checking if any match counts are greater than the
    num_matches_for_funded for diagnostic reasons, but is slower than using the any match check.

    Returns
    -------
    successes : List<List<int>>

    Parameters
    ----------
    placement: List<int>
        List of numbers from 1 to num_seats that represent the packages on the table.
    seat_perms_x_match : List<List<int>>
        All permutations of placements where starting matches equals num_starting_matches.
    num_matches_for_funded: int
        Number of matches required to be funded.
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
        if all(i < num_matches_for_funded for i in matching_amount_list):
            successes.append(list_to_check)
    return successes


def print_perms(seat_perms, num_matches_for_funded, num_to_print):
    '''Prints num_to_print number of seat_perms permutations.

    Parameters
    ----------
    seat_perms : List<List<int>>
        All of the permutations that were found to be successful for the orientation.
    number_to_print: int
        The number of permutations to print on screen.
    '''
    if num_to_print > len(seat_perms):
        num_to_print = len(seat_perms)

    print()
    if len(seat_perms) != 0:
        print("Seats")
        placement = list(range(1, len(seat_perms[0]) + 1))
        print(f"{placement}")
        print()
        print(f"First (or all available, if more were requested) {num_to_print} permutations with "
              f"less than {num_matches_for_funded} matches for all rotations (you don't get funded))")
        for i in range(num_to_print):
            print(seat_perms[i])
    else:
        print("No permutations exist for those conditions (always funded)!")


def validate_user_input(val, extra_check):
    '''Validates user input is an int and is less than extra_check.

    Returns
    -------
    bool

    Parameters
    ----------
    val : string
        The value being sent to see if it will parse to an integer.
    extra_check: int
        An extra limitation (integer) for the parsed value to be less than or equal to.
    '''
    try:
        val = int(val)
        if val < 0:
            return False
        if extra_check == None:
            return True
        else:
            if val <= extra_check:
                return True
            else:
                return False
    except:
        return False


def get_user_input(msg, extra_check):
    '''Gets user input to use for the parameters of the main function.

    Returns
    -------
    user_input : int

    Parameters
    ----------
    msg : string
        The display message for the user based on the value being requested.
    extra_check: int
        An extra limitation (integer) for the parsed value to be less than or equal to.
    '''
    valid = False
    while not valid:
        print(msg, end=": ")
        user_input = input()
        valid = validate_user_input(user_input, extra_check)
        if not valid:
            if extra_check == None:
                print("Invalid input. Please enter a positive integer.")
            else:
                print(
                    f"Invalid input. Please enter a positive integer less than or equal to {extra_check}")
    return int(user_input)


def main():

    num_seats = get_user_input("Enter the number of seats", None)
    num_starting_matches = get_user_input(
        "Enter the number of starting matches", num_seats)
    num_matches_for_funded = get_user_input(
        "Enter the minimum number of matches required to get funded", num_seats)
    maximum_num_perms_to_print = get_user_input(
        "Enter the maximum number of results to display", None)

    seat_perms = get_seat_perms(
        num_seats, num_starting_matches, num_matches_for_funded)
    print_perms(seat_perms, num_matches_for_funded, maximum_num_perms_to_print)


if __name__ == "__main__":
    main()
