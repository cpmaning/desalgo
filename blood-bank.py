import PySimpleGUI as sg    #import that shows a UI 

def insertionSort(A):            #sort that will be used 
    arr = [str(x) for x in A]    
    for i in range(1, len(arr)): #traverse through 1 to the len of the arr
        key = arr[i] 
        j = i-1 
        #move elements of the arr, that are greater than key, to one position
        #ahead of their current position
        while j >= 0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return arr
#driver code of the insertion sort
def array_name(A,key):
    arrayName = insertionSort(A)
    s = '\n' .join([str(i) for i in arrayName])
    window.Element('INPUT').Update('')
    return window.Element(key).Update(s)
#tab layout declarion along with its key types and UI size
blood_A =  [[sg.T('Persons who have Blood Type A : '),sg.T('\n',key='type_A',size=(20,0))]]  
blood_AB = [[sg.T('Persons who have Blood Type AB: '),sg.T('\n',key='type_AB',size=(20,0))]]
blood_B = [[sg.T('Persons who have Blood Type B: '),sg.T('\n',key='type_B',size=(20,0))]]
blood_O= [[sg.T('Persons who have Blood Type O: '),sg.T('\n',key='type_O',size=(20,0))]]   

#dict for the every arr of blood types
bloods = {
    'A':  [],
    'B':  [],
    'AB': [],
    'O':  []
}

#layout of the tabs and buttons of the program
layout = [[sg.TabGroup([[sg.Tab('A', blood_A), sg.Tab('AB', blood_AB), sg.Tab('B', blood_B),
                         sg.Tab('O', blood_O)]])],
           [sg.InputText(key='BLOOD_TYPE'), sg.InputText(key='INPUT')],
          [sg.Button('Submit')],[sg.Button('Cancel')]]
#name of the window declaration 
window = sg.Window('Blood Bank', layout)    


while True:    
    event, values = window.Read()    
    if event is None or event == 'Cancel':
        break
    #appending the values inputted to the following assigned arr
    elif event == "Submit":
        if values['BLOOD_TYPE'] == 'A':
            bloods[values['BLOOD_TYPE']].append(values['INPUT'])
            array_name(bloods['A'],'type_A')
        elif values['BLOOD_TYPE'] == 'AB':
            bloods[values['BLOOD_TYPE']].append(values['INPUT'])
            array_name(bloods['AB'],'type_AB')
        elif values['BLOOD_TYPE'] == 'B':
            bloods[values['BLOOD_TYPE']].append(values['INPUT'])
            array_name(bloods['B'],'type_B')
        else:
            bloods[values['BLOOD_TYPE']].append(values['INPUT'])
            array_name(bloods['O'],'type_O')

window.Close()