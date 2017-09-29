import os
def setFont():
    """Obtain the nicest monospaced font present in the Window system folder and return it to use with GUI applications"""
    fonts=[]
    if os.name=="nt":
        try:
            osFonts=os.listdir("C:/WINDOWS/fonts")
            if "LiberationMono-Regular.ttf" in osFonts: fonts.append("Liberation Mono")
            if "DejaVuSansMono_0.ttf" in osFonts: fonts.append("DejaVu Sans Mono")
            if "lucon.ttf" in osFonts: fonts.append("Lucida Console")
            if "cousine-regular.ttf" in osFonts: fonts.append("Cousine")
            if "firamono-regular.ttf" in osFonts: fonts.append("Fira Mono")
            if "PTM55F.ttf" in osFonts: fonts.append("PT Mono")
            if "ubuntumono-r.ttf" in osFonts: fonts.append("Ubuntu Mono")            
        except: print("no good font found on Windows")
    fonts.append("Courier New")
    return fonts[0]

if __name__=="__main__":
    print(setFont())
