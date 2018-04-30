
import json
import bpy


def saveMat(name):
    if name not in bpy.data.materials:
        return False
    mat = bpy.data.materials[name]
    Mat = {}
    for m in dir(mat):
        prop = eval('bpy.data.materials[name].'+m)
        typ =  type(prop)
        if typ in [int, float, bool, str]:
            if m =='name':
                continue
            Mat[m]=prop
            #print('^^^ save mat ^^^',m,Mat[m])
            
                
        if str(typ)==("<class 'Color'>"):
            Mat[m]=list(prop)
            #print('>> save mat Color >>',str(m),Mat[str(m)])
    
    
    saveData = json.dumps(Mat)
    file = open("newfile.txt", "w") 
    file.write(saveData)
    return saveData
    
    
def loadMat(name):
    if name not in bpy.data.materials:
        print(False)
        return False
    mat = bpy.data.materials[name]
    
    file = open('newfile.txt', 'r')
    Mats=file.read()
    
    Mat = json.loads(Mats)

    dir_mat = dir(bpy.data.materials[name])
    for m in Mat.items():
        if m[0]not in dir_mat:
            continue
        
        prop_dest = eval('bpy.data.materials[name]')
        
        try:
            prop_dest.__setattr__(m[0],m[1])
            #print('!!! load !!!!!!!!!',m[0], m[1])
        except:
            #print('!!! only read',m[0], m[1])
            pass
        
        
       
        
    return True  
    
    


print('\n\n*************')

MM = saveMat('Material.002')
#print('MM',type(MM))
loadMat('Material')
