# -*- coding: utf-8 -*-

u"""Framework do pobierania metadanych specyficznych dla danego typu pliku.

Można utworzyć instancję odpowiedniej klasy podając jej nazwę pliku w konstruktorze.
Zwrócony obiekt zachowuje się jak słownik posiadający parę klucz-wartość
dla każdego fragmentu metadanych.

    import fileinfo
    info = fileinfo.MP3FileInfo("/music/ap/mahadeva.mp3")
    print "\\n".join(["%s=%s" % (k, v) for k, v in info.items()])

Lub użyć funkcji listDirectory, aby pobrać informacje o wszystkich plikach w katalogu.
    for info in fileinfo.listDirectory("/music/ap/", [".mp3"]):
        ...

Framework może być rozszerzony poprzez dodanie klas dla poszczególnych typów plików, np.:
HTMLFileInfo, MPGFileInfo, DOCFileInfo.  Każda klasa jest całkowicie odpowiedzialna
za właściwe sparsowanie swojego pliku; zobacz przykład MP3FileInfo.
"""

import os
import sys


def stripnulls(data):
    u"usuwa białe znaki i nulle"
    return data.replace("\00", " ").strip()


class FileInfo(dict):
    u"przechowuje metadane pliku"

    def __init__(self, filename=None):
        dict.__init__(self)
        self["plik"] = filename


class MP3FileInfo(FileInfo):
    u"przechowuje znaczniki ID3v1.0 MP3"
    tagDataMap = {u"tytuł": (3, 33, stripnulls),
                  "artysta": (33, 63, stripnulls),
                  "album": (63, 93, stripnulls),
                  "rok": (93, 97, stripnulls),
                  "komentarz": (97, 126, stripnulls),
                  "gatunek": (127, 128, ord)}

    def __parse(self, filename):
        u"parsuje znaczniki ID3v1.0 z pliku MP3"
        self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == 'TAG':
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            pass

    def __setitem__(self, key, item):
        if key == "plik" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)


def listDirectory(directory, fileExtList):
    u"zwraca listę obiektów zawierających metadane dla plików o podanych rozszerzeniach"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList \
                if os.path.splitext(f)[1] in fileExtList]

    def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
        u"zwraca klasę metadanych pliku na podstawie podanego rozszerzenia"
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo

    return [getFileInfoClass(f)(f) for f in fileList]


if __name__ == "__main__":
    for info in listDirectory("E:/mp3/", [".mp3"]):  # (1)
        print "\n".join("%s=%s" % (k, v) for k, v in info.items())
        print