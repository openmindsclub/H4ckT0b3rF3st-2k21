from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.messagebox as ms
import os

import database


class RecordManagement(Frame):
    # Constructor Function
    def __init__(self, root):
        root.maxsize(560,500)
        root.minsize(560,500)
        root.wm_iconbitmap('RecordManager-icon.ico')
        # Initializing Master Frame and Tab notebook

        Frame.__init__(self)
        self.grid()
        self.master.title('Record Management')
        tabControl = ttk.Notebook(self)
        tabControl.configure(width=550, height=500)

        # Initializing Tab 1 --- "Student Registration Tab"
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Student Registration")
        tabControl.grid()
        self.tab1.configure(style='TFrame')

        # Initializing Tab 2 --- "Subject Allocation Tab"
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Subject Allocation")
        tabControl.grid()

        # Initializing Tab 3 --- "Marks Allocation Tab"
        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Marks Allocation")
        tabControl.grid()

        self.searchTab = ttk.Frame(tabControl)
        tabControl.add(self.searchTab, text="Search Database")
        tabControl.grid()

        # Initializing Top LabelFrame
        self.label_frame()
        # Constructing the GUI of 3 tabs
        self.tab_construct()

        self.mainloop()

    # Label Frame Construction
    def label_frame(self):
        # Initializing the LabelFrame for both 3 tabs
        self.labelFrame_tab1 = LabelFrame(self.tab1, text="Records Manager - Chitkara University", width=530, height=500)
        self.labelFrame_tab1.grid(row=0, column=0)
        self.labelFrame_tab1.grid_propagate(0)

        self.labelFrame_tab2 = LabelFrame(self.tab2, text="Records Manager - Chitkara University", width=580, height=500)
        self.labelFrame_tab2.grid(row=0, column=0)
        self.labelFrame_tab2.grid_propagate(0)

        self.labelFrame_tab3 = LabelFrame(self.tab3, text="Records Manager - Chitkara University", width=580, height=500)
        self.labelFrame_tab3.grid(row=0, column=0)
        self.labelFrame_tab3.grid_propagate(0)

        self.labelFrame_searchTab = LabelFrame(self.searchTab, text="Records Manager - Chitkara University", width=580, height=500)
        self.labelFrame_searchTab.grid(row=0, column=0)
        self.labelFrame_searchTab.grid_propagate(0)
    
    def top_label(self, labeltext, tab, topHeadingColumn=2, sticky="", columnspan=3):
        margin = Label(tab, width=2).grid(row=1, column=0)
        self.topLabel = Label(tab, text=labeltext,foreground='red', font="Helvetica 18 bold")
        self.topLabel.grid(row=0, column=topHeadingColumn, columnspan=columnspan, sticky=sticky)
        enter1 = Label(tab).grid(row=1, column=1)
        enter2 = Label(tab).grid(row=2, column=1)
    
    def bottom_label(self, tab, buttonText, startRow, entryList, optionCheck):
        enter1 = Label(tab).grid(row=startRow, column=1)
        enter2 = Label(tab).grid(row=startRow+1, column=1)
        submitButton = Button(tab, text=buttonText, command= lambda entryList=entryList, optionCheck=optionCheck: self.show_msg(entryList, optionCheck)).grid(row=startRow+2, column=2, columnspan=3)


    
    # 3 Tabs main GUI Construction 
    def tab_construct(self):
# ------------------------------------------------------- TAB 1 ------------------------------------------------------------------

        self.top_label("New Student Registration", self.labelFrame_tab1)
        
        nameLabel = Label(self.labelFrame_tab1, text="Name:", font="comicsansms 14").grid(row = 3, column=1, sticky="w") 
        self.nameEntry = Entry(self.labelFrame_tab1, width=45)
        self.nameEntry.grid(row = 3, column=3, columnspan=3)
        self.nameEntry.insert(0, "Student Name")
        self.nameEntry.bind('<FocusIn>', lambda event, entry=self.nameEntry, text="Student Name": self.on_click(event, entry, text))
        self.nameEntry.bind('<FocusOut>', lambda event, entry=self.nameEntry, text="Student Name": self.of_click(event, entry, text))
        self.nameEntry.configure(foreground='grey')

        RollNoLabel = Label(self.labelFrame_tab1, text="Roll No.:", font="comicsansms 14").grid(row = 4, column=1, sticky="w") 
        self.RollNoEntry = Entry(self.labelFrame_tab1, width=45)
        self.RollNoEntry.grid(row=4, column=3, columnspan=3)
        self.RollNoEntry.insert(0, "Student Roll No.")
        self.RollNoEntry.bind('<FocusIn>', lambda event, entry=self.RollNoEntry, text="Student Roll No.": self.on_click(event, entry, text))
        self.RollNoEntry.bind('<FocusOut>', lambda event, entry=self.RollNoEntry, text="Student Roll No.": self.of_click(event, entry, text))
        self.RollNoEntry.configure(foreground='grey')

        FatherLabel = Label(self.labelFrame_tab1, text="Father's Name:", font="comicsansms 14").grid(row = 5, column=1, sticky="w") 
        self.fatherEntry = Entry(self.labelFrame_tab1, width=45)
        self.fatherEntry.grid(row=5, column=3, columnspan=3)
        self.fatherEntry.insert(0, "Father's Name")
        self.fatherEntry.bind('<FocusIn>', lambda event, entry=self.fatherEntry, text="Father's Name": self.on_click(event, entry, text))
        self.fatherEntry.bind('<FocusOut>', lambda event, entry=self.fatherEntry, text="Father's Name": self.of_click(event, entry, text))
        self.fatherEntry.configure(foreground='grey')

        motherLabel = Label(self.labelFrame_tab1, text="Mother's Name:", font="comicsansms 14").grid(row = 6, column=1, sticky="w") 
        self.motherEntry = Entry(self.labelFrame_tab1, width=45)
        self.motherEntry.grid(row=6, column=3, columnspan=3)
        self.motherEntry.insert(0, "Mother's Name")
        self.motherEntry.bind('<FocusIn>', lambda event, entry=self.motherEntry, text="Mother's Name": self.on_click(event, entry, text))
        self.motherEntry.bind('<FocusOut>', lambda event, entry=self.motherEntry, text="Mother's Name": self.of_click(event, entry, text))
        self.motherEntry.configure(foreground='grey')
        

        mobileLabel = Label(self.labelFrame_tab1, text="Mobile No.:", font="comicsansms 14").grid(row = 7, column=1, sticky="w") 
        self.mobileEntry = Entry(self.labelFrame_tab1, width=45)
        self.mobileEntry.grid(row=7, column=3, columnspan=3)
        self.mobileEntry.insert(0, "Mobile No.")
        self.mobileEntry.bind('<FocusIn>', lambda event, entry=self.mobileEntry, text="Mobile No.": self.on_click(event, entry, text))
        self.mobileEntry.bind('<FocusOut>', lambda event, entry=self.mobileEntry, text="Mobile No.": self.of_click(event, entry, text))
        self.mobileEntry.configure(foreground='grey')

        courseLabel = Label(self.labelFrame_tab1, text="Course Interested: ", font="comicsansms 14").grid(row = 8, column=1, sticky="w") 
        self.option = StringVar()
        self.options = ("Select Course","Computer Science Engineering", "Electronics and Communcation Engineering", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Mechatronics")
        self.option.set("Select Course")
        self.optionMenu = OptionMenu(self.labelFrame_tab1, self.option, *self.options, command=self.func_tab1)
        self.optionMenu.grid(row=8, column=3, columnspan=3, sticky="ew")

        adressLabel = Label(self.labelFrame_tab1, text="Address:", font="comicsansms 14").grid(row = 9, column=1, sticky="w") 
        self.addressEntry1 = Entry(self.labelFrame_tab1, width=45)
        self.addressEntry1.grid(row=9, column=3, columnspan=3, sticky="w")
        self.addressEntry1.insert(0, "House No.\\Street Name\\Locality")
        self.addressEntry1.bind('<FocusIn>', lambda event, entry=self.addressEntry1, text="House No.\\Street Name\\Locality": self.on_click(event, entry, text))
        self.addressEntry1.bind('<FocusOut>', lambda event, entry=self.addressEntry1, text="House No.\\Street Name\\Locality": self.of_click(event, entry, text))
        self.addressEntry1.configure(foreground='grey')

        self.addressEntry2 = Entry(self.labelFrame_tab1, width=45)
        self.addressEntry2.grid(row=10, column=3, columnspan=3, sticky="w")
        self.addressEntry2.insert(0, "Colony\\Village\\Town")
        self.addressEntry2.bind('<FocusIn>', lambda event, entry=self.addressEntry2, text="Colony\\Village\\Town": self.on_click(event, entry, text))
        self.addressEntry2.bind('<FocusOut>', lambda event, entry=self.addressEntry2, text="Colony\\Village\\Town": self.of_click(event, entry, text))
        self.addressEntry2.configure(foreground='grey')
        
        self.addressEntry3 = Entry(self.labelFrame_tab1, width=45)
        self.addressEntry3.grid(row=11, column=3, columnspan=3, sticky="w")
        self.addressEntry3.insert(0, "City\\District")
        self.addressEntry3.bind('<FocusIn>', lambda event, entry=self.addressEntry3, text="City\\District": self.on_click(event, entry, text))
        self.addressEntry3.bind('<FocusOut>', lambda event, entry=self.addressEntry3, text="City\\District": self.of_click(event, entry, text))
        self.addressEntry3.configure(foreground='grey')

        self.entryList_tab1 = [self.RollNoEntry, self.nameEntry, self.fatherEntry, self.motherEntry, self.mobileEntry, self.addressEntry1, self.addressEntry2, self.addressEntry3]

        self.bottom_label(self.labelFrame_tab1, "Register Student", 12, self.entryList_tab1, True)

# -------------------------------------------------------------- TAB 2 ------------------------------------------------------------------

        self.top_label("Subject Allocation", self.labelFrame_tab2)

        RollNoLabel_tab2 = Label(self.labelFrame_tab2, text="Roll No.: ", font="comicsansms 14").grid(row = 3, column=1, sticky="w") 
        self.RollNoEntry_tab2 = Entry(self.labelFrame_tab2, width=45)
        self.RollNoEntry_tab2.grid(row=3, column=3, columnspan=3)
        self.RollNoEntry_tab2.insert(0, "Student Roll No.")
        self.RollNoEntry_tab2.bind('<FocusIn>', lambda event, entry=self.RollNoEntry_tab2, text="Student Roll No.": self.on_click(event, entry, text))
        self.RollNoEntry_tab2.bind('<FocusOut>', lambda event, entry=self.RollNoEntry_tab2, text="Student Roll No.": self.of_click(event, entry, text))
        self.RollNoEntry_tab2.configure(foreground='grey')
        
        subjectID = Label(self.labelFrame_tab2, text="Subject Id: ", font="comicsansms 14").grid(row = 4, column=1, sticky="w") 
        self.subjectId_entry = Entry(self.labelFrame_tab2, width=45)
        self.subjectId_entry.grid(row=4, column=3, columnspan=3)
        self.subjectId_entry.insert(0, "Subject ID")
        self.subjectId_entry.bind('<FocusIn>', lambda event, entry=self.subjectId_entry, text="Subject ID": self.on_click(event, entry, text))
        self.subjectId_entry.bind('<FocusOut>', lambda event, entry=self.subjectId_entry, text="Subject ID": self.of_click(event, entry, text))
        self.subjectId_entry.configure(foreground='grey')

        subject_name = Label(self.labelFrame_tab2, text="Subject Name: ", font="comicsansms 14").grid(row = 5, column=1, sticky="w") 
        self.subject_name_entry = Entry(self.labelFrame_tab2, width=45)
        self.subject_name_entry.grid(row=5, column=3, columnspan=3)
        self.subject_name_entry.insert(0, "Subject Name")
        self.subject_name_entry.bind('<FocusIn>', lambda event, entry=self.subject_name_entry, text="Subject Name": self.on_click(event, entry, text))
        self.subject_name_entry.bind('<FocusOut>', lambda event, entry=self.subject_name_entry, text="Subject Name": self.of_click(event, entry, text))
        self.subject_name_entry.configure(foreground='grey')

        credits = Label(self.labelFrame_tab2, text="Credits: ", font="comicsansms 14").grid(row = 6, column=1, sticky="w") 
        self.credits_entry = Entry(self.labelFrame_tab2, width=45)
        self.credits_entry.grid(row=6, column=3, columnspan=3)
        self.credits_entry.configure(foreground='grey')
        self.credits_entry.insert(0, "No. of Credits")
        self.credits_entry.bind('<FocusIn>', lambda event, entry=self.credits_entry, text="No. of Credits": self.on_click(event, entry, text))
        self.credits_entry.bind('<FocusOut>', lambda event, entry=self.credits_entry, text="No. of Credits": self.of_click(event, entry, text))

        self.entryList_tab2 = [self.RollNoEntry_tab2, self.subjectId_entry, self.subject_name_entry, self.credits_entry]

        self.bottom_label(self.labelFrame_tab2, "Allocate Subject", 7, self.entryList_tab2, False)

# ------------------------------------------------------------- TAB 3 ----------------------------------------------------------------

        self.top_label("Marks Allocation", self.labelFrame_tab3)

        RollNoLabel_tab3 = Label(self.labelFrame_tab3, text="Roll No.: ", font="comicsansms 14").grid(row = 3, column=1, sticky="w") 
        self.RollNoEntry_tab3 = Entry(self.labelFrame_tab3, width=45)
        self.RollNoEntry_tab3.grid(row=3, column=3, columnspan=3)
        self.RollNoEntry_tab3.insert(0, "Student Roll No.")
        self.RollNoEntry_tab3.bind('<FocusIn>', lambda event, entry=self.RollNoEntry_tab3, text="Student Roll No.": self.on_click(event, entry, text))
        self.RollNoEntry_tab3.bind('<FocusOut>', lambda event, entry=self.RollNoEntry_tab3, text="Student Roll No.": self.of_click(event, entry, text))
        self.RollNoEntry_tab3.configure(foreground='grey')
        
        subjectID = Label(self.labelFrame_tab3, text="Subject Id: ", font="comicsansms 14").grid(row = 4, column=1, sticky="w") 
        self.subjectId_entry_tab3 = Entry(self.labelFrame_tab3, width=45)
        self.subjectId_entry_tab3.grid(row=4, column=3, columnspan=3)
        self.subjectId_entry_tab3.insert(0, "Subject ID")
        self.subjectId_entry_tab3.bind('<FocusIn>', lambda event, entry=self.subjectId_entry_tab3, text="Subject ID": self.on_click(event, entry, text))
        self.subjectId_entry_tab3.bind('<FocusOut>', lambda event, entry=self.subjectId_entry_tab3, text="Subject ID": self.of_click(event, entry, text))
        self.subjectId_entry_tab3.configure(foreground='grey')

        subject_name_tab3 = Label(self.labelFrame_tab3, text="Subject Name: ", font="comicsansms 14").grid(row = 5, column=1, sticky="w") 
        self.subject_name_entry_tab3 = Entry(self.labelFrame_tab3, width=45)
        self.subject_name_entry_tab3.grid(row=5, column=3, columnspan=3)
        self.subject_name_entry_tab3.insert(0, "Subject Name")
        self.subject_name_entry_tab3.bind('<FocusIn>', lambda event, entry=self.subject_name_entry_tab3, text="Subject Name": self.on_click(event, entry, text))
        self.subject_name_entry_tab3.bind('<FocusOut>', lambda event, entry=self.subject_name_entry_tab3, text="Subject Name": self.of_click(event, entry, text))
        self.subject_name_entry_tab3.configure(foreground='grey')

        testTypeLabel = Label(self.labelFrame_tab3, text="Test Type: ", font="comicsansms 14").grid(row = 6, column=1, sticky="w")
        self.option_tab3 = StringVar()
        self.options_tab3 = ("Select Test Type","FA", "ST", "End Term", "Project Based")
        self.option_tab3.set("Select Test Type")
        self.optionMenu_tab3 = OptionMenu(self.labelFrame_tab3, self.option_tab3, *self.options_tab3, command=self.func_tab3)
        self.optionMenu_tab3.grid(row=6, column=3, columnspan=3, sticky="w")

        maxMarks = Label(self.labelFrame_tab3, text="Max Marks: ", font="comicsansms 14").grid(row = 7, column=1, sticky="w") 
        self.maxMarks_entry = Entry(self.labelFrame_tab3, width=45)
        self.maxMarks_entry.grid(row=7, column=3, columnspan=3)
        self.maxMarks_entry.insert(0, "Maximum Marks")
        self.maxMarks_entry.bind('<FocusIn>', lambda event, entry=self.maxMarks_entry, text="Maximum Marks": self.on_click(event, entry, text))
        self.maxMarks_entry.bind('<FocusOut>', lambda event, entry=self.maxMarks_entry, text="Maximum Marks": self.of_click(event, entry, text))
        self.maxMarks_entry.configure(foreground='grey')

        obtMarks = Label(self.labelFrame_tab3, text="Obtained Marks: ", font="comicsansms 14").grid(row = 8, column=1, sticky="w") 
        self.obtMarks_entry = Entry(self.labelFrame_tab3, width=45)
        self.obtMarks_entry.grid(row=8, column=3, columnspan=3)
        self.obtMarks_entry.insert(0, "Marks Obtained")
        self.obtMarks_entry.bind('<FocusIn>', lambda event, entry=self.obtMarks_entry, text="Marks Obtained": self.on_click(event, entry, text))
        self.obtMarks_entry.bind('<FocusOut>', lambda event, entry=self.obtMarks_entry, text="Marks Obtained": self.of_click(event, entry, text))
        self.obtMarks_entry.configure(foreground='grey')

        self.entryList_tab3 = [self.RollNoEntry_tab3, self.subjectId_entry_tab3, self.subject_name_entry_tab3, self.maxMarks_entry, self.obtMarks_entry]

        self.bottom_label(self.labelFrame_tab3, "Assign Marks", 9, self.entryList_tab3, True)
# ---------------------------------------------------------- SERACH TAB ------------------------------------------------------------------

        self.top_label("Search in Database", self.labelFrame_searchTab, 4)

        searchLabel = Label(self.labelFrame_searchTab, text="Roll No.: ", font="comicsansms 14").grid(row=1, column=1, sticky='w')

        space = Label(self.labelFrame_searchTab, width=15).grid(row=1, column=2)

        self.searchBar = Entry(self.labelFrame_searchTab, width=55)
        self.searchBar.grid(row=1, column=4, columnspan=5, sticky='e')
        self.searchBar.insert(0, "Enter the roll no of the student to get the data")
        self.searchBar.bind('<FocusIn>', lambda event, entry=self.searchBar, text="Enter the roll no of the student to get the data": self.on_click(event, entry, text))
        self.searchBar.bind('<FocusOut>', lambda event, entry=self.searchBar, text="Enter the roll no of the student to get the data": self.of_click(event, entry, text))
        self.searchBar.configure(foreground='grey')

        lineBreak = Label(self.labelFrame_searchTab).grid(row=2)

        self.radioVar = IntVar()
        radio1 = Radiobutton(self.labelFrame_searchTab, text="Personal Data", variable=self.radioVar , value=0).grid(row=3, column=2, columnspan=3,sticky='w')
        radio2 = Radiobutton(self.labelFrame_searchTab, text="Subject Data", variable=self.radioVar , value=1).grid(row=3, column=5, columnspan=2, sticky='w')
        radio3 = Radiobutton(self.labelFrame_searchTab, text="Marks Data", variable=self.radioVar , value=2).grid(row=3, column=7, columnspan=2, sticky='e')

        lineBreak = Label(self.labelFrame_searchTab).grid(row=4)

        searchButton = Button(self.labelFrame_searchTab, text='Search', command=self.search).grid(row=5, column=3, sticky='e', columnspan=2)

        lineBreak = Label(self.labelFrame_searchTab).grid(row=6)

        self.searchResult = Text(self.labelFrame_searchTab,state='disabled', wrap='none',height=17, width=62)
        # self.searchResult.grid(row=7, column=2, columnspan=4)


        self.scrollb = ttk.Scrollbar(self.labelFrame_searchTab, command=self.searchResult.yview)
        self.searchResult['yscrollcommand'] = self.scrollb.set

        self.scrollbh = ttk.Scrollbar(self.labelFrame_searchTab, orient='horizontal', command=self.searchResult.xview)
        self.searchResult['xscrollcommand'] = self.scrollbh.set
        # scrollbh.grid(row=8, column=1, sticky='nsew')





# ---------------------------------------------------------------------------------------------------------------------------------------
    # For getting the current value of option boxes present in 1st and 3rd tab
    def func_tab1(self, value):
        self.currentOption_tab1 = value
    
    def func_tab3(self, value):
        self.currentOption_tab3 = value

    # Event Binding Functions
    def on_click(self, event, entry, text):
        if entry.get() == text:
            entry.delete(0, "end")
            entry.configure(foreground='black')
            
    def of_click(self, event, entry, text):
        if entry.get() == "":
            entry.insert(0, text)
            entry.configure(foreground='grey')

    
    def check_empty(self, entryList, optionCheck):
        filled, rollnumber, mobileNo = True, True, True
        # Checking if there is any unfilled information present
        for i in range(len(entryList)):
            if str(entryList[i].cget('foreground')) == "grey":
                filled = False
                break
        # Checking if Option menu is filled or not
        if optionCheck:
            # For tab 1
            if len(entryList) == 8:
                try:
                    if str(self.currentOption_tab1) == "Select Course":
                        filled = False
                except Exception as e:
                    filled = False
            # For tab 2
            else:
                try:
                    if str(self.currentOption_tab3) == "Select Test Type":
                        filled = False
                except Exception as e:
                    filled = False
        # Checking if Roll No. given is in correct format or not
        # For tab 1
        if len(entryList) == 8:
            if (len(self.RollNoEntry.get()) != 10) or (not self.RollNoEntry.get().isdigit()):
                rollnumber = False
        # For tab 2
        elif len(entryList) == 4:
            if (len(self.RollNoEntry_tab2.get()) != 10) or (not self.RollNoEntry_tab2.get().isdigit()):
                rollnumber = False
        # for tab 3
        else:
            if (len(self.RollNoEntry_tab3.get()) != 10) or (not self.RollNoEntry_tab3.get().isdigit()):
                rollnumber = False
        
        # Checking if Mobile no. is given in correct format or not
        # For tab 1
        if len(entryList) == 8:
            if (len(self.mobileEntry.get()) != 10) or (not self.mobileEntry.get().isdigit()):
                mobileNo = False
                
        print(filled, rollnumber, mobileNo)
        return filled, rollnumber, mobileNo
    
    def checkCredits(self):
        if self.credits_entry.get().isdigit():
            return True
        else:       
            return False 
    def checkMarks(self):
        self.error = ""
        if self.maxMarks_entry.get().isdigit():
            if self.obtMarks_entry.get().isdigit():
                if int(self.maxMarks_entry.get())>=int(self.obtMarks_entry.get()):
                    return True
                else:
                    self.error = "Marks obtained cannot be greater than the Total marks"
                    return False
            else:
                self.error = "Please enter Obtained Marks correctly"
                return False
        else:
            self.error = "Please enter Max Marks correctly"
            return False

    def show_msg(self, entryList, optionCheck):
        filled, rollnumber, mobileNo = self.check_empty(entryList, optionCheck)
        if not filled:
            ms.showinfo('Information not filled ', 'Please fill up all the information', icon='error')
        else:
            Proceed = True
            if len(entryList) == 4:
                if not self.checkCredits():
                    ms.showinfo('Wrong Entry', 'Credits can only be number', icon='error')
                    Proceed = False
            elif len(entryList) == 5:
                if not self.checkMarks():
                    ms.showinfo('Wrong Entry', f"{self.error}", icon='error')
                    Proceed = False
            if Proceed:
                if not rollnumber:
                    ms.showinfo('Incorrect RollNo.', 'Please fill up the RollNo. correctly', icon='error')
                else:
                    if not mobileNo:
                        ms.showinfo('MobileNo. not correct', 'Please fill up the MobileNo. correctly', icon='error')
                    else:
                        msgbox = ms.askyesno('Do you want to add the data', 'Are you sure you want to add data into the database?', default='yes')
                        if msgbox:
                            isSuccess = self.update_data_to_backend(entryList)
                            if isSuccess == 'True':
                                ms.showinfo('Data added successfully', 'Your data has been successfully uploaded')
                            elif isSuccess == 'False_tab1':
                                ms.showinfo('User already exists', 'The user with this RollNo. already exists. If you want to edit the data for that user, you can go to the editing tab.', icon='error')
                            elif isSuccess == 'False_tab2':
                                ms.showinfo('Subject already exists', 'This subject already exists with the user you specified. If you want to edit the data, you can go to the editing tab.', icon='error')
                            elif isSuccess == 'False_tab3':
                                ms.showinfo('Marks already exists', f'The marks for the {self.currentOption_tab3} already exists for the given student. If you want to edit the data, you can go to the editing tab.', icon='error')
                            elif isSuccess == 'False_userNotFound':
                                ms.showinfo('User not found', 'Sorry, the Student with the given RollNo. not found', icon='error')
                            elif isSuccess == 'False_subjectNotFound':
                                ms.showinfo('Subject not found', 'Sorry, the Subject with given SubjectId not found', icon='error')

    def update_data_to_backend(self, entryList):
        get_data = database.Get_Data()
        write_data = database.Write_Data()
        
        # Initializing an empty dictionary for storing the data 
        data_dict = {}
        # Updating data of student file
        if len(entryList) == 8:
            if get_data.personal_data() == -1:
                data_dict = {str(self.RollNoEntry.get()): {'Name': self.nameEntry.get(), 'Father\'s Name': self.fatherEntry.get(), 'Mother\'s Name': self.motherEntry.get(), 'Mobile no.': self.mobileEntry.get(), 'Course Interested': self.currentOption_tab1, 'Address': {'Line 1': self.addressEntry1.get(), 'Line 2': self.addressEntry2.get(), 'Line 3': self.addressEntry3.get()}}}

                write_data.personal_data(data_dict)
                print(data_dict)
                return 'True'
            else:
                data_dict = get_data.personal_data()
                if str(self.RollNoEntry.get()) in data_dict:
                    return 'False_tab1'
                else:
                    new_student_info = {str(self.RollNoEntry.get()): {'Name': self.nameEntry.get(), 'Father\'s Name': self.fatherEntry.get(), 'Mother\'s Name': self.motherEntry.get(), 'Mobile no.': self.mobileEntry.get(), 'Course Interested': self.currentOption_tab1, 'Address': {'Line 1': self.addressEntry1.get(), 'Line 2': self.addressEntry2.get(), 'Line 3': self.addressEntry3.get()}}}

                    data_dict.update(new_student_info)
                    write_data.personal_data(data_dict)
                    return 'True'
        #  For updating the data of subject.json file 
        elif len(entryList) == 4:
            if not self.check_user_exist(self.RollNoEntry_tab2.get()):
                return 'False_userNotFound'
            if get_data.subject_data() == -1:
                data_dict = {str(self.RollNoEntry_tab2.get()): {self.subjectId_entry.get(): {'Subject Name': self.subject_name_entry.get(), 'Credits': self.credits_entry.get()}}}

                write_data.subject_data(data_dict)
                return 'True'
            else:
                data_dict = get_data.subject_data()
                if str(self.RollNoEntry_tab2.get()) in data_dict:
                    if self.subjectId_entry.get() not in data_dict[self.RollNoEntry_tab2.get()]:
                        new_subject = {str(self.subjectId_entry.get()): {'Subject Name': self.subject_name_entry.get(), 'Credits': self.credits_entry.get()}}

                        data_dict[self.RollNoEntry_tab2.get()].update(new_subject)
                        write_data.subject_data(data_dict)
                        return 'True'
                    else:
                        return 'False_tab2'
                else:
                    new_subject_info = {str(self.RollNoEntry_tab2.get()): {self.subjectId_entry.get(): {'Subject Name': self.subject_name_entry.get(), 'Credits': self.credits_entry.get()}}}

                    data_dict.update(new_subject_info)
                    write_data.subject_data(data_dict)
                    return 'True'
        #  For updating the data of marks.json file 
        else:
            if not self.check_user_exist(self.RollNoEntry_tab3.get()):
                return 'False_userNotFound'
            if not self.check_subject_exist(self.RollNoEntry_tab3.get(), self.subjectId_entry_tab3.get()):
                return 'False_subjectNotFound'
            if get_data.marks_data() == -1:
                data_dict = {str(self.RollNoEntry_tab3.get()): {self.subjectId_entry_tab3.get(): {self.currentOption_tab3: {'Subject Name': self.subject_name_entry_tab3.get(), 'Max Marks': self.maxMarks_entry.get(), 'Marks Obtained': self.obtMarks_entry.get()}}}}

                write_data.marks_data(data_dict)
                return 'True'
            else:
                data_dict = get_data.marks_data()
                if str(self.RollNoEntry_tab3.get()) in data_dict:
                    if self.subjectId_entry_tab3.get() in data_dict[self.RollNoEntry_tab3.get()]:
                        if self.currentOption_tab3 not in data_dict[self.RollNoEntry_tab3.get()][self.subjectId_entry_tab3.get()]:
                            new_fa_st = {self.currentOption_tab3: {'Subject Name': self.subject_name_entry_tab3.get(), 'Max Marks': self.maxMarks_entry.get(), 'Marks Obtained': self.obtMarks_entry.get()}}

                            data_dict[self.RollNoEntry_tab3.get()][self.subjectId_entry_tab3.get()].update(new_fa_st)
                            write_data.marks_data(data_dict)
                            return 'True'
                        else:
                            return 'False_tab3'
                    else:
                        new_subject_id = {self.subjectId_entry_tab3.get(): {self.currentOption_tab3: {'Subject Name': self.subject_name_entry_tab3.get(), 'Max Marks': self.maxMarks_entry.get(), 'Marks Obtained': self.obtMarks_entry.get()}}}

                        data_dict[self.RollNoEntry_tab3.get()].update(new_subject_id)
                        write_data.marks_data(data_dict)
                        return 'True'
                        
                else:
                    print(False)
                    new_subject_marks_info = {str(self.RollNoEntry_tab3.get()): {self.subjectId_entry_tab3.get(): {self.currentOption_tab3: {'Subject Name': self.subject_name_entry_tab3.get(), 'Max Marks': self.maxMarks_entry.get(), 'Marks Obtained': self.obtMarks_entry.get()}}}}

                    data_dict.update(new_subject_marks_info)
                    write_data.marks_data(data_dict)
                    return 'True'
    
    def check_user_exist(self, rollNo):
        get_data = database.Get_Data()
        student_data = get_data.personal_data()
        if student_data == -1:
            return False
        else:
            if rollNo in student_data:
                return True
            else:
                return False


    def check_subject_exist(self, rollNo, subjectId):
        get_data = database.Get_Data()
        subject_data = get_data.subject_data()
        if subject_data == -1:
            return False
        else:
            if subjectId in subject_data[rollNo]:
                return True
            else:
                return False

# ----------------------------- For Searching in the Database ------------------------------------------ 
    def search(self):
        search_data = database.Search_Data()
        get_data = database.Get_Data()
        def showError():
            ms.showinfo('Record not found', 'Sorry, the requested record not found', icon='error')
        
        def showData(filename):
            # Firstly Clearing all the previous data
            self.searchResult.delete('1.0', END)
            self.searchResult.grid_forget()
            self.scrollb.grid_forget()
            self.scrollbh.grid_forget()
            # Now writing the data found
            if search_data.searchAndWrite(filename, self.searchBar.get()) != -1:
                self.searchResult.grid(row=7, column=1, columnspan=9)
                self.scrollb.grid(row=7, column=9, sticky='nsew')
                self.scrollbh.grid(row=8, column=1, sticky='nsew', columnspan=9)
                self.searchResult.configure(state='normal')
                self.searchResult.delete('1.0', END)
                with open('f.json', 'r') as f:
                    self.searchResult.insert(INSERT, f.read())
                self.searchResult.configure(state='disabled')
                os.remove('f.json')
            else:
                showError()

        if self.radioVar.get() == 0:   # Searching the data in the Student File
           showData(get_data.personal_data()) 
        elif self.radioVar.get() == 1:
            showData(get_data.subject_data())
        elif self.radioVar.get() == 2:
            showData(get_data.marks_data())

        

                








        
                

        



if __name__ == '__main__':
    RecordManagement(Tk())
    
    


