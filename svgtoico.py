import os

pwd = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

for (path, dir, files) in os.walk("./"):
    
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.svg':
            svgPath = pwd + path.replace("\\","/")[1:] + '/' + filename
            icoPath = svgPath[:-4] + ".ico"

            cmd = f'magick -background transparent {svgPath} -define icon:auto-resize -colors 256 {icoPath}'
            os.system(cmd)
