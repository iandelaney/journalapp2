def main():
    print_header()
    run_event_loop()


def print_header():
    print("----------------------------------------")
    print("          JOURNAL APP")
    print("----------------------------------------")
    print()


def run_event_loop():
    print("What do you want to do with your journal?")
    cmd = None

    while cmd != "x":
        cmd = input("[L]ist entries, [A]dd an entry, or e[x]it: ")
        if cmd.lower() == "l":
            print("L")
        elif cmd.lower() == "a":
            print ("A")
        elif cmd.lower() != 'x':
            print("Sorry, we don't understand '{}'".format(cmd))


    print("Done. Goodbye.")


main()
