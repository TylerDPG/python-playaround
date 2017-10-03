import urllib

def read_text():
    chkr = open("/Users/tylerrichendollar/Desktop/favorites.txt")
    contents_of_file = chkr.read()
    #print (contents_of_file)
    chkr.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print (output)
    connection.close()
    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
        print ("Good to go!")
    else:
        print ("Could not read document.")

read_text()
