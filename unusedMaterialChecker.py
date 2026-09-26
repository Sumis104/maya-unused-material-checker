import maya.cmds as cmds

def check_unusedMaterial():
    cass = cmds.ls(type="aiStandardSurface")
    for surfacename in cass:
        sg = cmds.listConnections(surfacename,type="shadingEngine")[0]
        mesh = cmds.listConnections(sg,type="mesh")
        if mesh == None:
            print(surfacename + "is unused")

def main():
    check_unusedMaterial()

if __name__ == "__main__":
    main()