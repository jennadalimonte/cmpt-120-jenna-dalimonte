# import your libraries here.
from datetime import datetime

currentTime = datetime.now()

# the name of the log file to write to.
log_file = "log-file-" + datetime.today().strftime('%Y-%m-%d') + ".log"


def log(text, log_file=log_file):
    # open up the log file in the correct mode.
    file = open(log_file, 'w')
    # create a string that has the current date and time in the beginning of the text.
    file.write(text)
    # Ensure the string ends with a new line character.
    # append the text to the end of the file.

    file.close()
    # close the file.


def dump(log_file=log_file):
    '''
    This function prints out each line in the log file to the console
    '''
    # open up the log file in the correct mode.
    file = open(log_file, 'r')
    # read the file into a list.
    # iterate through each item in the list and print out the results.
    for x in log_file:
        print(x)
    file.close()
    # close the file.
