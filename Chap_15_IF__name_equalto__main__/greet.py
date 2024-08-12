# if __name__=="__main__":      -> used to avoid repetation from the imported file when they are run 


def welcome():
    print("Hello, Welcome")


print(__name__)                 #retuenn the value of the where from the file is used or imported

if __name__=="__main__":
    welcome()