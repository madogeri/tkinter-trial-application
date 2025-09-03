
# project scope of work

# replace 115kV Vienna 1-phase CCVT and junction box - W.O. #C6MT200521
# - Mark #Q408 -                                                    
# - junction box PM2420 OPT A (2 conduit runs) on A phase

# replace 230kV Bienna 3-phase CCVT and junction Box         
# - Mark #Q701 - W.O. #C6MT200522
# - junction box PM2420 OPT B (5 conduits runs outdoor) on phase B - W.O. #C6MT200462
# - junction box PM2420 OPT C (indoor) // not to be installed 

# replace switch R1881 with motor operator - W.O. #C6MT200513
# 230kV 3000A CBS With 125vdc 9-10 sec operating time motor operated

# replace 63x relay on WX266 - W.O. #C6Ms200572
# install additional sudden pressure relay

# replace AUTO XFMR WX266 panel - W.O. #C6MT200422
# upgrade auto WX266 differential panel

# Major Materials: (Itemized list)
# Two (2) PM3507 OPT A3 Modified (SEL-411L and SEL-487E), 30”
# 230/115kV AUTO XFMR WX266 DIFF/VIENNA LN P1 PNL”
# 230/115kV AUTO XFMR WX266 DIFF/VIENNA LN P2 PNL”
# Two (2) 2000:5MR C800 Neutral window/donut CTs.
# One (1) Qualitrol Seal-In Relay (Model #909-300-01 and CatID #0032190635).
# One (1) Qualitrol Rapid Pressure Rise Relays.
# Gas space - CatID #0032163341). Confirm cable length during design.


import sys
import os
import math

def functional(data : str ) -> str:
    names = input(f"{data} your name: ")
    return names

information = functional("Please enter")

print(f"you entered: {information}")
print("testing this function")

testing_dict = {
    "Name" : "Michael Adogeri",
    "Age" : 39,
    "Occupation" : "Substation Design Engineer",
    "Degree" : ["Mechanical Engineer", "Computer Science"],
    "Degree Level" : ["Bachelor", "Master"],
}

valid = True
choices = ["Name", "Age", "Occupation", "Degree", "Degree Level"]
selection = ""

while valid:
    
    for index, choice in enumerate(choices):
        print("{}. {}".format(index + 1, choice))

    option = input("Select from one of the choices: ")

    if option.isdigit():
        option = int(option)
        if 1 <= option and option <= (len(choices) + 1):
           print(testing_dict[choice[option - 1]])
           selected = input("continue ? y for yes, other to continue: ")
           valid = False if selected == "y" else True
        else:
            print("invalid Selection")
    else:
        print("Enter a valid digit")