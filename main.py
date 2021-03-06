import os
import Utils as u
from config import PATH_LOG, PATH_DIR


def get_conferma():
    message_conferma = " confermare? \n " + u.bcolors.WARNING + " y " + u.bcolors.END + \
                       " = yes, conferma -> " + u.bcolors.WARNING + " n " + u.bcolors.END + " = no \n"
    inpt = input(message_conferma)[0]
    if inpt == 'y':
        return True
    else:
        return False


def comunication_library(project_group_path):
    path_to_be_create = []
    project_group_path = project_group_path + ("/comunication")
    path_to_be_create.append(project_group_path)
    path_to_be_create.append(project_group_path + "/constants")
    path_to_be_create.append(project_group_path + "/dto")
    path_to_be_create.append(project_group_path + "/dto/filter")
    path_to_be_create.append(project_group_path + "/enums")
    # manca la cartella della security
    for path in path_to_be_create:
        if not os.path.exists(path):
            os.makedirs(path)


def create_folder(project_path, project_group_path, security):
    path_to_be_create = []

    path_to_be_create.append(project_path + "src/test")
    path_to_be_create.append(project_path + "src/main/resources")

    path_to_be_create.append(project_group_path)
    path_to_be_create.append(project_group_path + "/config")
    path_to_be_create.append(project_group_path + "/controller")
    path_to_be_create.append(project_group_path + "/enums")
    path_to_be_create.append(project_group_path + "/exception")
    path_to_be_create.append(project_group_path + "/model")
    path_to_be_create.append(project_group_path + "/repository")
    path_to_be_create.append(project_group_path + "/service")
    if security:
        path_to_be_create.append(project_group_path + "/security")

    # manca la cartella della security
    for path in path_to_be_create:
        if not os.path.exists(path):
            os.makedirs(path)
    comunication_library(project_group_path)

def add_security (project_group_path):
    source = "/Users/flaminiovilla/Desktop/Work Space/createJavaProject/security"
    destination = project_group_path + "/security"
    u.copytree(source,destination)

#def add_entity(project_group_path, entity_name):

def create_project():
    print("Inserire il" + u.bcolors.WARNING + " nome " + u.bcolors.END + "del progetto: ")
    project_name = input()
    print("Inserire il" + u.bcolors.WARNING + " group " + u.bcolors.END + "del progetto: ")
    print(u.bcolors.OKBLUE + " best practice = com.azienda" + u.bcolors.END)
    project_group = input()
    package_name = project_group + "." + project_name
    print("Il nome del package sar??: " + u.bcolors.WARNING + package_name + u.bcolors.END)
    project_path = PATH_DIR + project_name + "/"
    project_group_path = project_path + "src/main/java/" + project_group.replace(".", "/")
    if get_conferma():
        print("Aggiungere la security ?")
        if get_conferma():
            create_folder(project_path, project_group_path, True)
            add_security(project_group_path)
        else:
            create_folder(project_path, project_group_path, False)





if __name__ == '__main__':
    create_project()
