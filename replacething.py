import os


# import fileinput
# import sys
# from shutil import copyfile
# import pathlib
# import getopt


class ReplaceThing:
    def __init__(self, OutputFile, InputFile):
        self.InputFile = InputFile
        self.OutputFile = OutputFile
        print("Input file: ", InputFile)
        print("Output file: ", OutputFile)

        FileExist = os.path.exists("./" + InputFile)
        if not FileExist:
            print("huh, file doesnt exist!")
            print("Will not try to open the Input File")
            self.Data = ""
        else:
            print("yay, no error!")
            f = open(InputFile, 'r')
            self.Data = f.read()
            f.close()

    def readf(self):
        f = open(self.InputFile, 'r')
        self.Data = f.read()
        f.close()
        Data = self.Data
        return Data

    def replacetext(self, infile, search):
        inp = open(infile, 'r')
        avar = inp.read()
        inp.close()
        self.Data = self.Data.replace(search, avar)
        Data = self.Data
        return Data

    def replacetextdirect(self, dathing, search):
        self.Data = self.Data.replace(search, dathing)
        Data = self.Data
        return Data

    def writef(self):
        f = open(self.OutputFile, 'w')
        f.write(self.Data)
        f.close()

    def writefdirect(self, dathing):
        f = open(self.OutputFile, 'a')
        f.write("\n")
        f.write(dathing)
        f.close()

    def Default(self):
        self.Data = self.replacetext('./var/startoffile.txt', 'sof')

        self.Data = self.replacetext('./var/1bitinput.txt', '1bi')

        self.Data = self.replacetext('./var/2bitinput.txt', '2bi')

        self.Data = self.replacetext('./var/inv.txt', 'inv')

        self.Data = self.replacetext('./var/buf.txt', 'buf')

        self.Data = self.replacetext('./var/nand.txt', 'nand')
        self.Data = self.replacetext('./var/xnor.txt', 'xnor')

        self.Data = self.replacetext('./var/nor.txt', 'nor')
        self.Data = self.replacetext('./var/and.txt', 'and')

        self.Data = self.replacetext('./var/xor.txt', 'xor')

        self.Data = self.replacetext('./var/or.txt', 'or')

        self.Data = self.replacetext('./var/endoffile.txt', 'eof')
        self.writef()
