# This function changes the settings that can only have one option
import info


def change_setting(opt_list, value):
    choice = choose_option() - 1

    if 0 <= choice <= value - 1:
        for num in range(0, value):
            if num == choice:
                opt_list[num] = 'X'
            else:
                opt_list[num] = ' '

        print("Setting changed!\n")
    else:
        print("Invalid option!\n")


# This generic function asks the user to select an option
def choose_option():
    while True:
        try:
            option = int(input("Select your option: "))
        except ValueError:
            print("Must be an integer!\n")
        else:
            break
    return option


# This function determines if the user can start the game
def start_game(diff, dist):
    if 'X' in diff and 'X' in dist:
        print("Starting game...")
        return diff.index('X'), dist.index('X')
    else:
        print("You must select a Difficulty and a Distance first!\n")
    return -1, -1


# This function is where the user chooses the settings of a new game
def new_game():
    difficulty, distance, extra = [' '] * 3, [' '] * 3, [' '] * 2

    while True:
        print("\n" * 100)
        print("\nGAME SETTINGS:\n")
        print("— Game Difficulty:\n"
              f"Easy[{difficulty[0]}]     Normal[{difficulty[1]}]     Hard[{difficulty[2]}]\n")
        print("— Target Distance:\n"
              f"Near[{distance[0]}]     Average[{distance[1]}]     Far[{distance[2]}]\n")
        print("— Extra Settings (optional):\n"
              f"Overwater Modifier[{extra[0]}]     Hel Mode[{extra[1]}]\n")

        print("Change options: \n"
              "1. Start Game\n"
              "2. Difficulty\n"
              "3. Distance\n"
              "4. Modifiers (WIP)\n"
              "5. Help\n"
              "6. Credits\n"
              "7. Quit\n")

        match choose_option():
            case 1:
                game_settings = start_game(difficulty, distance)
                if 0 <= game_settings[0] <= 2 and 0 <= game_settings[1] <= 2:
                    return game_settings
            case 2:
                print("Change difficulty: \n"
                      "1. Easy\n"
                      "2. Normal\n"
                      "3. Hard\n")

                change_setting(difficulty, len(difficulty))
            case 3:
                print("Change distance: \n"
                      "1. Near\n"
                      "2. Average\n"
                      "3. Far\n")

                change_setting(distance, len(distance))
            case 4:
                print("Extra settings: \n"
                      "1. Overwater Modifier\n"
                      "2. Hel Mode\n")

                choice_extra = choose_option() - 1
                if 0 <= choice_extra <= len(extra) - 1:
                    if extra[choice_extra] == ' ':
                        extra[choice_extra] = 'X'
                        print("Modifier added!\n")
                    else:
                        extra[choice_extra] = ' '
                        print("Modifier removed!\n")
                else:
                    print("Invalid option!\n")
            case 5:
                info.tutorial()
            case 6:
                info.game_credits()
            case 7:
                quit()
            case _:
                print("Invalid option!\n")

        input("Press any key to continue")
