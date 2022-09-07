while True:
    base_num = input("Provide a number: ")
    try:
        base_num = float(base_num)

        if base_num > 50:
            print("Please use a number less than 50: ")
            continue
        currect_user_input = True

    except ValueError:
        currect_user_input = False
        message = "Use whole # or decimal, no spaces: >> "

    if currect_user_input:
        print(base_num)
        break