






def Up(x,y,w,h,swap):
    y-=h-1
    if swap:
        h=int(h/2)
    return x, y, w, h

def Right(x,y,w,h,swap):
    x+=w-1
    if swap:
        w=int(w/2)
    return x, y, w, h

def Down(x,y,w,h,swap):
    y+=h-1
    if swap:
        h=int(h/2)
    return x, y, w, h

def Left(x,y,w,h,swap):
    x-=w-1
    if swap:
        w=int(w/2)
    return x, y, w, h

def Up_Right(x,y,w,h,swap):
    x, y,w,h =  Up(x,y,w,h,swap)
    return Right(x,y,w,h,swap)

def Up_Left(x,y,w,h,swap):
    x, y,w,h =  Up(x,y,w,h,swap)
    return Left(x,y,w,h,swap)

def Down_Right(x,y,w,h,swap):
    x, y,w,h =  Down(x,y,w,h,swap)
    return Right(x,y,w,h,swap)

def Down_Left(x,y,w,h,swap):
    x, y,w,h =  Down(x,y,w,h,swap)
    return Left(x,y,w,h,swap)

swith = {'U':Up, 'UR': Up_Right, 'R': Right, 'DR': Down_Right,
 'D': Down, 'DL': Down_Left, 'L': Left, 'UL':Up_Left}

print(swith['U'](2,3))


# U (Up)
# UR (Up-Right)
# R (Right)
# DR (Down-Right)
# D (Down)
# DL (Down-Left)
# L (Left)
# UL (Up-Left)
