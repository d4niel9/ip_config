import os
import time


def main():
    try:
        command_init = "kalitorify -t"
        os.popen(command_init)
        time.sleep(9) #Define switch init time in seconds
        while True:
            command_switch_ip = "kalitorify -r"
            os.popen(command_switch_ip)
            time.sleep(15) #Define renew time in seconds
    except KeyboardInterrupt as err:
        print("""Run "sudo kalitorify -c" manually to stop tor""")


if __name__ == "__main__":
    main()
