# Importing Pandas to create DataFrame
import pandas as pd
import random
import ast

# Creating Empty DataFrame and Storing it in variable df
def init_database():
    df = pd.DataFrame(columns=['Names', 'Skills', 'Projects Completed', 'Projects In progress', 'UUID'])

    # Printing Empty DataFrame For Debugging Purposes
    print(df)
    df.to_csv("database.csv", index=False)


def init_user_exact(name, competency, finished_projects, underway_projects, uuid):
    # When I get the nfc tags and stuff I'll probably make it randomize a UUID and
    # write it to the nfc tag at this point

    # Something like uuid = random.randint(100000, 999999)

    df = pd.read_csv("database.csv", index_col=False)
    df.loc[0] = [name, competency, finished_projects, underway_projects, uuid]
    print(df)
    df.to_csv("database.csv", index=False)


def init_user_random(class_list):
    df = pd.read_csv("database.csv", index_col=False)
    num = random.randint(1000000, 9999999)
    num_list = []
    for student in class_list:
        while num in df['UUID'].values:
            num = random.randint(1000000, 9999999)
        df.loc[len(df)] = [student, '', '', '', num]
        num_list.append(num)
    print(df.to_string())
    return num_list


        #print(num)
        #print(df.to_string())


def add_skill(skill, uuid):
    df = pd.read_csv("database.csv", index_col=False)
    print(df['Skills'][df['UUID'] == uuid].values[0])

    old_value_string = (df['Skills'][df['UUID'] == uuid].values[0])
    current_value = ast.literal_eval(old_value_string)
    print(current_value)
    if skill in current_value:
        if current_value[skill] >= 4:
            pass
        else:
            current_value[skill] = current_value[skill] + 1
    else:
        current_value.update({skill: 1})
    # Selects value in row where UUID column equals param
    # And the column is equal to skills, then assigns to
    # Current value
    df['Skills'][df['UUID'] == uuid].loc[0] = current_value
    """print(current_value)"""
    # Finds the index of the aforementioned row
    index = df.UUID[df.UUID == uuid].index.values.astype(int)
    """print(int(index))"""
    current_value_string = str(current_value)
    df.at[int(index), 'Skills'] = current_value_string
    df.to_csv("database.csv", index=False)


if __name__ == "__main__":
    init_database()
    print("----------------------------")
    init_user_exact("praseky", '{"laser cutting master": 3}', "cutmaster9000", "cutmaster9000v2", 2)#random.randint(1000000, 9999999))
    print("----------------------------")
    add_skill("annoying mr hawes professional", 2)
    add_skill("annoying mr hawes professional", 2)
    print(init_user_random(['Alex', 'Dan']))
