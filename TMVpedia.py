# Required Libraries
# To access wiki
import wikipedia as wikipedia
# To use google translate function
from googletrans import Translator

# To use Tkinter GUI library 
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox 

# To use timesleep function
import time

# To be create background images
from PIL import ImageTk,Image

#To convert text --> audio
import pyttsx3

# To use threading
import threading

# For speach audio control
from pygame import mixer

# OS 
import os

#LOADING SCREEN(LS)
LS = Tk()
LS.title('loading screen')
LS.config(bg="#01305E")
#position the app to the center of the screen
#app resolution
LS_w = 612
LS_h = 420
#screen resolution
screen_w = LS.winfo_screenwidth()
screen_h = LS.winfo_screenheight()
#coor of center
center_w = (screen_w/2)-(LS_w/2)
center_h = (screen_h/2)-(LS_h/2)
#LS geometry
LS.geometry(f'{LS_w}x{LS_h}+{int(center_w)}+{int(center_h)}')

#canvas
canvas_ls = Canvas(LS,width=612,height=433,border=0,highlightthickness=0,bg='black')
#Define background image for loading screen
bg_ls = ImageTk.PhotoImage(file ='resources/images/loadingscreen.png')
#add bg to canvas
canvas_ls.create_image(0,0,image= bg_ls,anchor=NW)
#hide the tittle bar
LS.overrideredirect(True)

#title bar frame
titlebar_frame = LabelFrame(LS,bg='black',highlightthickness=0,bd=0,cursor='diamond_cross')

#title loading screen
lbltitle = Label(titlebar_frame,text='Loading Screen',bg='black',fg='white'
,font=('',10))
#moving loading screen with titlbe bar hided
def move_ls(event):
    LS.geometry(f'+{event.x_root}+{event.y_root}')
#biding the function to the title of the loading screen 
lbltitle.bind("<B1-Motion>",move_ls)

#App icon(label icon)
app_icon = PhotoImage(file='resources/images/encyclopedia.png')
lbl_app_icon = Label(titlebar_frame,image=app_icon,bg='black')

#button exit
def exit():
    LS.destroy()
btn_exit = Button(titlebar_frame,text='X',font=('Black Ops One',8),fg='white',cursor='hand2'
                    ,bg='black',width=4,height=2,bd=0,command=exit)
def active_exit(e):
    btn_exit.config(bg='red')
def inactive_exit(e):
    btn_exit.config(bg='black')    
btn_exit.bind('<Enter>',active_exit)
btn_exit.bind('<Leave>',inactive_exit)

#running loadingbar(this is a function of btn launch app)
def loading():
#loading bar
 #create and place loading bar, text loading in loading screen
  #text 'loading'
    lblloading =canvas_ls.create_text(195,108,text='Loading......',font=('Black Ops One',10)
    ,fill='white')
  #loading bar
    loadingbar = ttk.Progressbar(LS,orient=HORIZONTAL,length=300,mode='determinate')
    canvas_ls.create_window(300,130,window=loadingbar)

    #lbl progress
    lbl_prog = Label(LS,text='',bg='#071216',font=('Black Ops One',7),fg='white',width=6,height=1
                    ,bd=0,highlightthickness=0)
    canvas_ls.create_window(435,112,window=lbl_prog)

 #Define how loading bar will run
    for i in range(100):
        loadingbar['value'] += 1
        lbl_prog.config(text=str(loadingbar['value'])+'%')
        LS.update_idletasks()
        time.sleep(0.02)
        if loadingbar['value'] == 100:
            LS.destroy()
    

#MAINSCREEN(ROOT) 

#TITLE BAR + APP RESOLUTION
    root = Tk()
    root.title('TMVPEDIA|DEV BY HOK_DAVID_VIET')
    root.iconbitmap('resources/icons/encyclopedia.ico')
    #position the app to the center of the screen
    # mainscreen resolution
    main_w = 760
    main_h = 760
    #screen resolution
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    #coor of center
    maincenter_w = (screen_w/2)-(main_w/2)
    maincenter_h = (screen_h/2)-(main_h/2)
    #mainscreen(root) geometry
    root.geometry(f'{main_w}x{main_h}+{int(maincenter_w)}+{int(maincenter_h)}')
    

#CANVAS
 #CANVAS
    canvas_root = Canvas(root,width=760,height=760,border=0,highlightthickness=0,bg='black')

 #BACKGROUND FOR CANVAS
  #define bg
    bg_root = ImageTk.PhotoImage(file ='resources/images/app_bg.png')     
  #add bg to canvas
    canvas_root.create_image(0,0,image= bg_root,anchor=NW)

 #LABEL APP NAME & COPYRIGHT
  #title(app name)
    lbl_app_name =canvas_root.create_text(700,70,anchor=CENTER,text='TMVPEDIA'
    ,font=('Transformers Movie',50),fill='#FFFDD0') 
  #copyright
    lblcopyright =canvas_root.create_text(700,685,anchor=CENTER
    ,text='Copyright © 2021 TMV Company. All rights reserved.',fill='#FFFDD0',font=('',10,BOLD)) 

 #FUNCTION FOR BG RESiZER(make bg fit to app frame)
    def resizer(e):
        global bg_root1,resized_bg,newbg
        #open image
        bg_root1=Image.open('resources/images/app_bg.png')
        #resize image
        resized_bg = bg_root1.resize((e.width,e.height),Image.LANCZOS)
        #Define the image again
        newbg = ImageTk.PhotoImage(resized_bg)
        #add the new image to canvas
        canvas_root.create_image(0,0,image= newbg,anchor=NW)
        #Readd the app name and copyright labels
        #app name
        canvas_root.create_text(700,70,anchor=CENTER,text='TMVPEDIA',font=('Transformers Movie',50)
                    ,fill='#FFFDD0')  
        #copyright
        canvas_root.create_text(700,685,anchor=CENTER,text='Copyright © 2021 TMV Company. All rights reserved.'
                    ,fill='#FFFDD0',font=('',10,BOLD))
    #binding resizer
    root.bind('<Configure>',resizer)


#CREATE FRAME
#Output box frame
    output_box_frame= LabelFrame(root,highlightthickness=1,highlightcolor='yellow')
 
 #list of search mode
    search_mode = ['MODE:Summary','MODE:Full Page']                #list of search mode
    list_searchmode_box = ttk.Combobox(output_box_frame,value = search_mode) #list box of search mode
    list_searchmode_box.current(0)
    
 #create scrollbar  
    scroll_txt_ver = Scrollbar(output_box_frame,orient=VERTICAL,width=20,cursor='hand2')
    scroll_txt_hor = Scrollbar(output_box_frame,orient=HORIZONTAL,width=20,cursor='hand2')

 #output box(outbox)
    output_box = Text(output_box_frame,yscrollcommand=scroll_txt_ver.set
                ,xscrollcommand=scroll_txt_hor.set,wrap='none',
                   width=70,height=20,font=('',16))

 #configure scrollbar to output box
    scroll_txt_ver.config(command=output_box.yview)
    scroll_txt_hor.config(command=output_box.xview)

# Utility bar frame
 #Define the functions for widgets in utility bar frame

  #Function for button speaker
   #Initialize speaker and text-->audio converter
    speaker = mixer.init()                     
    converter = pyttsx3.init()
    
   #Define function for speaker
    def speak_speaker():
    #Unload the currently loaded wav file to free up resources
        if os.path.exists('temp.wav'):
            mixer.music.unload()
            os.remove('temp.wav')
        else:
            pass

    #disable searchbtn during the search operation is running
        audiobtn['state']=DISABLED

    #Create a temporary .wav file 
        outfile  = 'temp.wav'

    #Get text from the outbox
        source=output_box.get(1.0,END)

    #Convert the text to audio
      #Then Save to the temp.wav file 
       #to the same directory with this python file/tmv.exe file 
        converter.save_to_file(source,outfile)

    #The converter stop the text-to-speech converting operation
        converter.runAndWait()

    #open the temp.wav file and play the audio which was converted from the text in outbox
      #Load the temp.wav file
        mixer.music.load(outfile)
      #Set the volume for the speaker
        mixer.music.get_volume()
        mixer.music.set_volume(1)
      #Play the file(LEFT MOUSE CLICK) 
        mixer.music.play()
        
    #When users want to pause(RIGHT MOUSE CLICK), unpause(X2 RIGHT MOUSE CLICK) stop(MIDDLE MOUSE CLICK) the speaker
      # the temp.wav will do exactly the same operation
        def stop_speaker(e):
            mixer.music.stop()
            #Unload the currently loaded music to free up resources
            if os.path.exists('temp.wav'):
                mixer.music.unload()
                os.remove('temp.wav')
            else:
                pass
        def pause_speaker(e):
            mixer.music.pause()
        def unpause_speaker(e):
            mixer.music.unpause()
        audiobtn.bind('<Button-2>',stop_speaker)
        audiobtn.bind('<Button-3>',pause_speaker)
        audiobtn.bind('<Double-Button-3>',unpause_speaker)

    #return the normal state for searchbtn to be able to be clicked again 
        audiobtn['state']=NORMAL


    

  #function for clear button
    def clear():
        entry_box.delete(0,END)
        output_box.delete(0.0,END)
        entry_box.insert(0,'Search something........')
     
  #function for search button
    def search():
            
    #disable searchbtn during the search operation is running
        searchbtn['state']=DISABLED
    
    # WHEN ENTRYBOX = "SEARCH SOMETHING...", clear the entrybox
        if entry_box.get()=='Search something........':
            entry_box.delete(0,END)
            entry_box.insert(0,'Please type something........')
            time.sleep(1)
            entry_box.delete(0,END)
            entry_box.insert(0,'Search something........')
            
    # WHEN ENTRYBOX EMPTY, request users to type something to the 
        elif entry_box.get()=='':
            #disable searchbtn during the operation is running
            searchbtn['state']=DISABLED
            entry_box.insert(0,'Please type something........')
            time.sleep(1)
            entry_box.delete(0,END)
            entry_box.insert(0,'Search something........')

    # WHEN REQUIREMENT MET(suitable info in entrybox) 
     # DO the search operation with mode
        else:
            #Define a new variable: user_input as what is typed in the entrybox
            user_input = entry_box.get() 
            
        #Summary mode
            if list_searchmode_box.get().lower() =='mode:summary':
            # if there is information available for what the user requested    
                try: 
                 #get input from entbox to sort out info from wiki 
                    data = wikipedia.summary(user_input,sentences=500
                            ,auto_suggest=False,redirect=True)
                 #output wiki result to outbox
                    output_box.delete(0.0,END)
                    output_box.insert(0.0,data)
            # if users type in a ambiguous words/phrases,
                # request them to try some of the following recommendations
                except wikipedia.DisambiguationError as e:
                 #Delete everything inside the outputbox, then insert a list of alter recommendations
                    output_box.delete(0.0,END)
                    output_box.insert(0.0,
                            '- Sorry!!!,there is no information for that'+'\n'
                            + f'- the word/phrase [{user_input}] may refer to:'
                            +'\n'+'- '+str(e.options))
            # if ther is no information available, inform user that there is NO PAGE FOUND               
                except wikipedia.PageError:
                 #Delete everything inside the outputbox,
                 #  then insert this prhase:"Sorry!!! NO PAGE FOUND"   
                    output_box.delete(0.0,END)
                    output_box.insert(0.0, f'- Sorry!!!,NO PAGE FOUND for [{user_input}]')

        #Full mode
            elif list_searchmode_box.get().lower() =='mode:full page':
            # if there is information available for what the user requested    
                try: 
                 #get input from entbox to sort out info from wiki 
                    data = wikipedia.page(user_input,auto_suggest=False, redirect=True)
                 #output wiki result to outbox
                    output_box.delete(0.0,END)
                    output_box.insert(0.0,data.content)

            # if users type in a ambiguous words/phrases,
                # request them to try some of the following recommendations
                except wikipedia.DisambiguationError as e:
                 #Delete everything inside the outputbox, then insert a list of recommendation   
                    output_box.delete(0.0,END)
                    output_box.insert(0.0,
                            '- Sorry!!!,there is no information for that'+'\n'
                            + f'- the word/phrase [{user_input}] may refer to:'
                            +'\n'+'- '+str(e.options))

            # if there is no information available, inform user that there is NO PAGE FOUND               
                except wikipedia.PageError:
                 #Delete everything inside the outputbox,
                 #  then insert this prhase:"Sorry!!! NO PAGE FOUND"   
                    output_box.delete(0.0,END)
                    output_box.insert(0.0, f'- Sorry!!!,NO PAGE FOUND for [{user_input}]')
                
    #return the normal state for searchbtn to be able to be clicked again 
        searchbtn['state']=NORMAL

  #function for info_guidance button
    def show_info():
        guidance = messagebox.showinfo(title='speaker use guidance',
        message='+ To play audio: left mouse click '+'\n'
                +'+ To pause audio: right mouse click '+'\n'
                +'+ To unpause audio: x2 right mouse click '+'\n'
                +'+ To stop audio: middle mouse click ') 
    show_info()

  #listlangbox function 
    def autotranslate(event):
        input=output_box.get(1.0,END)
        t=Translator()
        if listlangbox.get().lower() == 'language:default':
            a=t.translate(input,dest='en')
        if listlangbox.get().lower() == 'vietnamese':
            a=t.translate(input,dest='vi')
        elif listlangbox.get().lower() == 'spanish':
            a=t.translate(input,dest='es')
        elif listlangbox.get().lower() == 'chinese':
            a=t.translate(input,dest='zh-cn')
        elif listlangbox.get().lower() == 'indonesia':
            a=t.translate(input,dest='id')
        b=a.text
        output_box.delete(0.0,END)
        output_box.insert(0.0,b)
        
 # Display box frame
    utility_bar_frame = Frame(root)
   
  #entry box
    entry_box = Entry(utility_bar_frame,width=94,fg='grey')
    entry_box.insert(0,'Search something........')

   #binding effects for entrybox
    #KEYPRESS EVENT
    #when backspace is pressed
    def backspace_pressed(e):
        if entry_box.get()=='':
           entry_box.insert(0,'Search something.........') 
    entry_box.bind('<KeyPress-BackSpace>',backspace_pressed)
    #when any other keys is pressed
    def key_pressed(e):
        if entry_box.get()=='Search something........':
            entry_box.delete(0,END)
    entry_box.bind('<KeyPress>',key_pressed)

    #ENTBOX CLICKED EVENT
    def entbox_clicked(e):
        if entry_box.get()=='Search something........': 
            entry_box.delete(0,END)
    entry_box.bind('<Button-1>',entbox_clicked)



  #binding effect for utility_bar_frame
   #enter effect
    def utility_bar_frame_enter(e):
        utility_bar_frame.config(highlightthickness=1,highlightcolor='yellow')
    utility_bar_frame.bind('<Enter>',utility_bar_frame_enter)
   #Leave effect
    def utility_bar_frame_leave(e):
        if entry_box.get() == '':
            entry_box.insert(0,'Search something........')
        else:
            pass
    utility_bar_frame.bind('<Leave>',utility_bar_frame_leave)

  #button
   #icon for button
    #searchbtn_ico
    imgsearch_inactive = PhotoImage(file='resources/images/search_inactive.png') 
    imgsearch_active = PhotoImage(file='resources/images/search_active.png')
    #audiobtn_ico
    imgaudio_inactive = PhotoImage(file='resources/images/speaker_inactive.png') 
    imgaudio_active = PhotoImage(file='resources/images/speaker_active.png')

   #but audio(speaker)
    audiobtn = Button(utility_bar_frame,bd=0,highlightthickness=0,cursor='hand2'
    ,image = imgaudio_inactive,command=lambda:threading.Thread(target=speak_speaker).start())
    
   #but clear
    clearbtn = Button(utility_bar_frame,text='X',fg='grey',font=('Black Ops One',10),cursor='hand2'
              ,command=clear ,bd=0,highlightthickness=0,bg='#F0F0F0')
    
   #but search        
    searchbtn = Button(utility_bar_frame,bd=0,highlightthickness=0,cursor='hand2',image=imgsearch_inactive
                ,command=lambda:threading.Thread(target=search).start())
    
   #but info and guidance
    infobtn = Button(utility_bar_frame,text='i',fg='grey',font=('Black Ops One',10),cursor='hand2'
              ,command=show_info ,bd=0,highlightthickness=0,bg='#F0F0F0')

   #binding effect for btn
    #search btn
    def active_searchbtn(e):
        searchbtn.config(image=imgsearch_active)
    def inactive_searchbtn(e):
        searchbtn.config(image=imgsearch_inactive)
    searchbtn.bind('<Enter>',active_searchbtn)
    searchbtn.bind('<Leave>',inactive_searchbtn)

    #clear btn
    def active_clearbtn(e):
        clearbtn.config(fg='red')
    def inactive_clearbtn(e):
        clearbtn.config(fg='grey')
    clearbtn.bind('<Enter>',active_clearbtn)
    clearbtn.bind('<Leave>',inactive_clearbtn) 
            
    #audio btn
    def active_audiobtn(e):
        audiobtn.config(image=imgaudio_active)
    def inactive_audiobtn(e):
        audiobtn.config(image=imgaudio_inactive)
    audiobtn.bind('<Enter>',active_audiobtn)
    audiobtn.bind('<Leave>',inactive_audiobtn)

    #info btn
    def active_infobtn(e):
        infobtn.config(fg='blue')
    def inactive_infobtn(e):
        infobtn.config(fg='grey')
    infobtn.bind('<Enter>',active_infobtn)
    infobtn.bind('<Leave>',inactive_infobtn) 
    
  #listlangbox
    lang_opt = ['Language:Default','Vietnamese','Spanish','Chinese','Indonesia'] #list of languages
    listlangbox = ttk.Combobox(utility_bar_frame,value = lang_opt)                          #listlangbox
    listlangbox.current(0)
    listlangbox.bind('<<ComboboxSelected>>',autotranslate)

    
#PLACING OBJECTS(inside mainscreen)
    canvas_root.pack(fill='both',expand=True)
  #placing objects inside canvas
    utility_bar_frame_window = canvas_root.create_window(700,130,window=utility_bar_frame)
    outputbox_frame_window = canvas_root.create_window(700,410,window=output_box_frame)

  #placing objects inside utility bar frame
    entry_box.pack(side=LEFT)
    searchbtn.pack(side=LEFT,padx=12)
    clearbtn.pack(side=LEFT,padx=12)
    audiobtn.pack(side=LEFT,padx=12)
    infobtn.pack(side=LEFT,padx=12)
    listlangbox.pack(side=RIGHT)

  #placing objects inside output box frame
    list_searchmode_box.pack(side=TOP,fill=X)
    scroll_txt_ver.pack(fill=Y,side=RIGHT)
    scroll_txt_hor.pack(fill=X,side=BOTTOM)
    output_box.pack()
    root.mainloop()
    

#LOADING SCREEN WIDGET    
#BUTTON LAUNCH APP
#def active_btn_launch
def active_but(e):
    btnlaunch.config(bg='blue',fg='white')
#def inactive_but_launch
def inactive_but(e):
    btnlaunch.config(bg='white',fg='black')
#create button launch app
btnlaunch = Button(LS,text="LAUNCH",font=('Black Ops One',7),bg='white',fg='black',cursor='hand2'
,width=6,height=1,command=loading)
#binding button launch
btnlaunch.bind('<Enter>',active_but)
btnlaunch.bind('<Leave>',inactive_but)

##PLACING OBJECTS(inside loading screen)
#Not in frame
titlebar_frame.pack(side=TOP,fill=X,expand=1)
btnlaunch_window = canvas_ls.create_window(300,170,window=btnlaunch)
canvas_ls.pack(fill=BOTH,anchor=CENTER)

#inside title bar frame
lbl_app_icon.pack(side=LEFT)
lbltitle.pack(side=LEFT,fill=X,expand=True)
btn_exit.pack(side=RIGHT)


mainloop()
