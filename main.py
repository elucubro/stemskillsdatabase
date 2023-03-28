# Importing Pandas to create DataFrame
import pandas as pd
import random


# Creating Empty DataFrame and Storing it in variable df
def init_database():
    df = pd.DataFrame(columns=['Names', 'Skills', 'Projects Completed', 'Projects In progress', 'UUID'])

    # Printing Empty DataFrame For Debugging Purposes
    print(df)
    df.to_csv("database.csv", index=False)


def init_user(name, initcomp, initprojects, initprogress, uuid):
    # When I get the nfc tags and stuff I'll probably make it randomize a UUID and
    # write it to the nfc tag at this point

    # Something like uuid = random.randint(100000, 999999)

    df = pd.read_csv("database.csv", index_col=False)
    df.loc[0] = [name, initcomp, initprojects, initprogress, uuid]
    print(df)
    df.to_csv("database.csv", index=False)


def add_skill(skill, uuid):
    df = pd.read_csv("database.csv", index_col=False)
    df.loc[df['UUID'] == uuid, 'Skills'] = df.loc[df['UUID'] == uuid, 'Skills'] + '+' + skill
    print(df.to_string())


if __name__ == "__main__":
    init_database()
    print("----------------------------")
    init_user("praseky", "laser cutting master", "cutmaster9000", "cutmaster9000v2", 2)#random.randint(100000, 999999))
    print("----------------------------")
    add_skill("annoying mr hawes professional", 2)
