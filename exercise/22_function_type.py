import shutil as st
width = st.get_terminal_size().columns
#function without argument and no return value 
def printLine():
    print('_'*width)
#function with argument and no retirn value
def printMessage(msg):
    print(msg.center(width))
#function with no argument but return value
def getPi():
    return 22/7
printLine()
printMessage('hello world')
printLine()
print(f"pi={getPi()}")
