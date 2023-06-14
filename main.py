# This is a sample Python script.
name1 = input("What is your name? \n")


name2 = input("What is their name? \n")

lower_name1=name1+name2
lowedition= lower_name1.lower()
t= lowedition.count("r") + lowedition.count("u") + lowedition.count("e") + lowedition.count("t")
l=lowedition.count("l") +lowedition.count("o") + lowedition.count("v") + lowedition.count("e")

strt=str(t)
strl=str(l)
all=strt+strl


allint=int(all)

if allint<10 or allint>90:
 print(f" Your score is {allint}, you go together like coke and mentos.")

elif allint>40 and allint<50:
    print(f" Your score is {allint}, you are alright together.")
else :
    print(f" your score is {allint} ")
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(ademusta):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

