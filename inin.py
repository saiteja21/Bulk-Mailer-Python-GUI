import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class E2mailer:
    
    def __init__(self, master):
        
        master.title('Gen Next Mailer')
        master.resizable(width=False, height=False)
        
        MyFont = font.Font(size=12)
        self.style = ttk.Style()
        
        self.style.configure('TButton',font=MyFont)
        self.style.configure('TLabel',font = ('Tahoma', 12))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.header = ttk.Frame(master)
        self.header.pack()


        ttk.Label(self.header, text='WELCOME to Gen Next Mailer').grid(row=0, column=1,pady=20)
        ttk.Label(self.header, wraplength=400,
                  text=("Thanks for using bulk mailer and spread a word about it :) just kidding  "
                        "Please tell us what your thoughts about our product.")).grid(row=1, column=1)
#---------------------------------------------------------------------------------------
        self.frame_Auth = ttk.Frame(master)
        self.frame_Auth.pack(padx=10,pady=15)
       
        ttk.Label(self.frame_Auth, text = 'SMTP Server:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_Auth, text = 'Port:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')

        self.entry_smtp = ttk.Entry(self.frame_Auth, width = 30)
        self.entry_smtp.grid(row = 1, column = 0, padx = 5)
        
        self.entry_port = ttk.Entry(self.frame_Auth, width = 30)
        self.entry_port.grid(row = 1, column = 1, padx = 5)
        
        ttk.Label(self.frame_Auth, text = 'Email:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_Auth, text = 'Password:').grid(row = 2, column = 1, padx = 5, sticky = 'sw')

        self.entry_email = ttk.Entry(self.frame_Auth, width = 30)
        self.entry_email.grid(row = 3, column = 0, padx = 5)
        
        self.entry_password = ttk.Entry(self.frame_Auth, width = 30,show = '*')
        self.entry_password.grid(row = 3, column = 1, padx = 5)
        
        btnSave = ttk.Button(self.frame_Auth, text='Save',command = self.writeAuthCSV).grid(row=4, column=0, padx=5, pady=5, sticky='E')
        self.saved = StringVar()
        ttk.Label(self.frame_Auth,textvariable=self.saved).grid(row = 4, column = 1, padx = 5, sticky = 'w')
        self.saved.set('not saved')
        self.setAuth()
        if self.entry_smtp.get() and self.entry_port.get() and self.entry_email.get() and self.entry_password.get():
            self.saved.set('values found')
            
#---------------------------------------------------------------------------------------
        
            
        self.frame_Mailer = ttk.Frame(master)
        self.frame_Mailer.pack(pady=20,fill=X)

         
        ttk.Label(self.frame_Mailer, text='To:').grid(row=0, column=0, padx=5)
        
        ttk.Label(self.frame_Mailer, text='Subject').grid(row=1, column=0, padx=5)

        ttk.Label(self.frame_Mailer, text='Upload:').grid(row=2, column=0, padx=5)

        ttk.Label(self.frame_Mailer, text='Message:').grid(row=3, column=0, padx=5)

        
        self.var = StringVar()
        self.found = tkinter.Label(self.frame_Mailer,textvariable=self.var).grid(row=4, column=3, padx=10, pady=10,sticky='w')
        self.var.set('0 mails found')

        
        self.entry_mails = ttk.Entry(self.frame_Mailer,width=50)
        self.entry_subject = ttk.Entry(self.frame_Mailer, width=50)
        self.entry_message = Text(self.frame_Mailer, width=40, height=10)


        self.entry_mails.grid(row=0, column=1, padx=5,pady=5,sticky='w',columnspan=2)
        self.entry_subject.grid(row=1, column=1, padx=5,pady=5,sticky='w',columnspan=2)

        btnUpload = ttk.Button(self.frame_Mailer, text='Upload CSV',command =self.uploadCSV).grid(row=2, column=1, padx=5, pady=5, sticky='w')
        btnAttachments = ttk.Button(self.frame_Mailer, text='Attachments',command =self.uploadAttachments).grid(row=2, column=2, padx=5, pady=5,
                                                                                sticky='w')
        

        self.entry_message.grid(row=3, column=1, columnspan=2, padx=5)

        btnReset = ttk.Button(self.frame_Mailer, text='Reset',command=self.restMails).grid(row=4, column=1, padx=5, pady=5,sticky='w')

        btnSend = ttk.Button(self.frame_Mailer, text='Send',command=lambda:self.sendMails(mails)).grid(row=4, column=2, padx=5, pady=5, sticky='w')
#--------------------------------------------------------------------------------------------------------------------------------
    def uploadCSV(self):
        temp = Tk()
        temp.withdraw()
        try:
            file_path_csv = askopenfilename()
            if file_path_csv:
                self.processCSV(file_path_csv)
        except:
            print('file not selected or some problem')

    def uploadAttachments(self):
        import os.path 
        temp = Tk()
        temp.withdraw()
        global file_path_attach
        global file_attach
        try:
            file_path_attach = askopenfilename()
            if file_path_attach:
                file_attach =os.path.basename(file_path_attach)
        except:
            print('file not selected or some problem')
        
    def writeAuthCSV(self):
        import csv
        smtp=self.entry_smtp.get()
        port=self.entry_port.get()
        email=self.entry_email.get()
        password=self.entry_password.get()
        save = dict()
        p = False 
        if smtp and port and email and password:
            save = {'smtp':smtp,'port':port,'email':email,'password':password}
            try:
                file = open('authentication.csv','w')
                wrt = csv.DictWriter(file, save.keys())
                wrt.writeheader()
                p = wrt.writerow(save)
                
            finally:
                file.close()
                
        #print(save)
        if p:
            self.saved.set('saved')
        else:
            self.saved.set('not saved')

    def setAuth(self):
        import csv
        try:
            input_file = open('authentication.csv','r')
            rd = csv.DictReader(input_file)
            for row in rd:
                self.entry_smtp.insert(0,row['smtp'])
                self.entry_port.insert(0,row['port'])
                self.entry_email.insert(0,row['email'])
                self.entry_password.insert(0,row['password'])
        except:
            print('')
        
        
   
#mailing list process here 
    
    def processCSV(self,file_path_csv):
        import csv,re

        global mails
        mails = []
        try:
            file = open(file_path_csv, 'rt')
            reader = csv.reader(file)
            for row in reader:
                    l = ''.join(row)
                    match = re.search(r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)',l, re.M | re.I)
                    mails.append(match.group())

        finally:
                self.getMails()
                s = str(len(mails)) + ' mails found'
                self.var.set(s)
                print(mails)
                file.close()

    def getMails(self):
        mailString = self.entry_mails.get()
        if mailString:
            match = re.search(r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)',mailString, re.M | re.I)
            if match:
                mails.append(match.group())   
                
    
        
    def sendMails(self,mails):
        import smtplib
        import email
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        smtp=self.entry_smtp.get() 
        port=self.entry_port.get()   
        fromaddr = self.entry_email.get()
        passw = self.entry_password.get()
         
        msg = MIMEMultipart()
         
        msg['From'] = fromaddr
        msg['Subject'] = self.entry_subject.get()
        
        body = self.entry_message.get('1.0',END)
         
        msg.attach(MIMEText(body, 'plain'))
        filename = file_attach 
        if filename:
            try:
                attachment = open(file_path_attach, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(part)
 
            except:
                print('attachment not found')
         
                
        server = smtplib.SMTP(smtp,port)
        server.ehlo()
        server.starttls()
        try:
            server.login(fromaddr, passw)
            text = msg.as_string()
        except:
            print('login failed bad network or something else')
        try:
            for mail in mails:
                server.sendmail(fromaddr, mail, text)
        finally:
            server.quit()


        
    def restMails(self):
        mails=[]
        s = str(0) + ' mails found'
        self.var.set(s)
        self.entry_mails.delete(0,END)
        self.entry_subject.delete(0,END)
        self.entry_message.delete(1.0,END)
                
   
        
    
def main():
    root = Tk()
    feedback = E2mailer(root)
    root.mainloop()


if __name__ == "__main__": main()
