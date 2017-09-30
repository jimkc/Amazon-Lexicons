import json, os, sys, linecache, re, uuid, scipy
import numpy as np

class getdictxt:

    def __init__(self):
        self.src = sys.argv[1]

    def json_to_txt(self):

        for dirpath, dir_list, file_list in os.walk(self.src):
            #print "Walking into directory: " + str(dirpath)

            if len(file_list) > 0:
                #print "Files found: " + "\033[1m" + str(file_list) + "\033[0m"

                for f in file_list:
                    # in case there is a goddamn .DS_Store file
                    if str(f) == ".DS_Store":
                        print "Removing " + dirpath + "/" + str(f)
                        os.remove(dirpath+ "/"+ f)
                    else:
                       with open(dirpath + "/" + f) as file:
                           file_data = json.loads(file.read())
                           self.get_txt(file_data, f)



            else:
                print "No file is found"

            print "-"*80

    def get_txt(self, file_data, filename):
        lexicons = []
        with open(filename.split('.')[0]+".txt", "w") as output:
            for line in file_data["topN_sentiment_words"]:
                wordlist = ""
                for word in line['word']:
                    wordlist = wordlist + " " +word
                output.write(wordlist+"\n")

            output.close()


if __name__ == '__main__':
    gettxt = getdictxt()
    gettxt.json_to_txt()


