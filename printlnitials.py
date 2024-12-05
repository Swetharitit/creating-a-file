def PrintInitials():
    initials = [
        ["M", "C", "W"]
    ]

    # Define pattern for 'M'
    M = [
        "*       *       *",
        "**     **       *",
        "* *   * *       *",
        "*  * *  *       *",
        "*   *   *       *",
        "*       *       *",
        "*       *       *",
        "*       *       *",
        "*       *       *"
    ]

    # Define pattern for 'C'
    C = [
        "  *****  ",
        " *     * ",
        "*        ",
        "*        ",
        "*        ",
        "*        ",
        "*        ",
        " *     * ",
        "  *****  "
    ]

    # Define pattern for 'W'
    W = [
        "*       *       *",
        "*       *       *",
        "*       *       *",
        "*       *       *",
        "*   *   *   *   *",
        "*  * *  *  * *  *",
        "* *   * * *   * *",
        "**     **     ** ",
        "*       *       *"
    ]

    # Printing all initials together
    for i in range(9):
        print(M[i], "   ", C[i], "   ", W[i])

# Run the program
PrintInitials()

