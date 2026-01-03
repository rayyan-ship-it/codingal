def value_frequency_in_dict(data_dict, target_value):
    """
    Returns the frequency of target_value in the dictionary values.
    """
    if not isinstance(data_dict, dict):
        raise TypeError("First argument must be a dictionary.")

    
    return list(data_dict.values()).count(target_value)


if __name__ == "__main__":
    test_dict = {
        'a': 5,
        'b': 2,
        'c': 5,
        'd': 3,
        'e': 5,
        'f': 2
    }

    try:
        print("Test Dictionary:", test_dict)

        
        user_input = input("Enter the value to check frequency: ")
        try:
            if '.' in user_input:
                target_value = float(user_input)
            else:
                target_value = int(user_input)
        except ValueError:
            target_value = user_input

        freq = value_frequency_in_dict(test_dict, target_value)
        print(f"The value '{target_value}' appears {freq} time(s) in the dictionary.")

    except Exception as e:
        print("Error:", e)
