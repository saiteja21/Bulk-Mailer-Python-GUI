import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class Feedback:
    def __init__(self, master):
        self.header = ttk.Frame(master)
        self.header.pack()


        ttk.Label(self.header, text='WELCOME to Gen Next Mailer').grid(row=0, column=1)
        ttk.Label(self.header, wraplength=300,
                  text=("Thanks for using bulk mailer and spread a word about it :) just kidding  "
                        "Please tell us what your thoughts about our product.")).grid(row=1, column=1)


        self.frame_Mailer = ttk.Frame(master)
        self.frame_Mailer.pack()

        ttk.Label(self.frame_Mailer, text='To:').grid(row=0, column=0, padx=5)
        ttk.Label(self.frame_Mailer, text='Subject').grid(row=1, column=0, padx=5)
        ttk.Label(self.frame_Mailer, text='Upload:').grid(row=2, column=0, padx=5)
        ttk.Label(self.frame_Mailer, text='Message:').grid(row=3, column=0, padx=5)

        self.entry_mails = ttk.Entry(self.frame_Mailer, width=30)
        self.entry_subject = ttk.Entry(self.frame_Mailer, width=30)

        self.Message = Text(self.frame_Mailer, width=40, height=10)

        self.entry_mails.grid(row=0, column=1, padx=5,pady=5,sticky='w')
        self.entry_subject.grid(row=1, column=1, padx=5,pady=5,sticky='w')

        btnUpload = ttk.Button(self.frame_Mailer, text='Upload CSV', command =self.uploadCSV).grid(row=2, column=1, padx=5, pady=5, sticky='w')
        btnAttachments = ttk.Button(self.frame_Mailer, text='Attachments',command =self.uploadAttachments).grid(row=2, column=2, padx=5, pady=5,
                                                                                sticky='w')
        btnHTML = ttk.Button(self.frame_Mailer, text='HTML file',command =self.uploadHTML).grid(row=2, column=3, padx=5, pady=5, sticky='w')

        self.Message.grid(row=3, column=1, columnspan=2, padx=5)

        btnReset = ttk.Button(self.frame_Mailer, text='Reset').grid(row=4, column=2, padx=5, pady=5,sticky='w')

        btnSend = ttk.Button(self.frame_Mailer, text='Send').grid(row=4, column=3, padx=5, pady=5, sticky='w')

        self.frame_Extra = ttk.Frame(master)
        self.frame_Extra.pack()

        self.x = ttk.LabelFrame(self.frame_Extra, height=200, width=460, text="Last Activity Details",labelanchor='n',relief=RAISED).grid()


        # ttk.Label(self.frame_Extra, text='Subject').grid(row=0, column=1, padx=5)
        # ttk.Label(self.label_Frame, text='Upload:').grid(row=2, column=0, padx=5)
        # ttk.Label(self.label_Frame, text='Message:').grid(row=3, column=0, padx=5

    def uploadCSV(self):
        temp = Tk()
        temp.withdraw()
        file_path_csv = askopenfilename()
        self.processCSV(file_path_csv)

    def uploadAttachments(self):
        temp = Tk()
        temp.withdraw()
        file_path_attach = askopenfilename()

    def uploadHTML(self):
        temp = Tk()
        temp.withdraw()
        file_path_html = askopenfilename()

#mailing list process here 
    
    def processCSV(self,file_path_csv):
        import csv,sys,re
        file = open(file_path_csv,'rt')
        li = []
        mailStr = []
        mails = []
        try:
            reader = csv.reader(file)
            for row in reader:
                li.append(row)
            for text in li:
                mailStr.append(text[0])
                
        finally:
            file.close()
            
        for mail in mailStr:
            match = re.search(r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)',mail,re.M|re.I)
            mails.append(match.group())

        self.sendMails(mails)


    def sendMails(self,mails):
        import smtplib

        fromaddr = 'i4uhasai@gmail.com'
        msg = r'this is a test message for my project sai teja nagamothu.I respect you as my friend please ignore this'

            
        # Credentials (if needed)
        password = 'raviTEJA@#143'

        # The actual mail send

        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromaddr,password)
            for mail in mails:
                server.sendmail(fromaddr, mail, msg)    
        finally:
            server.quit()
            print('successful')

        

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()
