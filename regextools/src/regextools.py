import uno
import unohelper
import re

from be.vmalep.libreoffice.Regextools import XRegextools

# RegExTools
# Extension created by Pierre van Male <vmalep@gmail.com>
# Inspired by Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>


class RegextoolsImpl(unohelper.Base, XRegextools):
    def __init__(self, ctx):
        self.ctx = ctx

# -------------------- Functions to modify -----------------------------

    def regextract(self, a, b, c):
        try:
            found = re.search(b, a).group(c)
        except AttributeError:
            # pattern not found in the original string
            found = 'N/A'  # return no answer
        return found

# ----------------------------------------------------------------------


def createInstance(ctx):
    return RegextoolsImpl(ctx)


g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance,
    "be.vmalep.libreoffice.Regextools.python.RegextoolsImpl",
    ("com.sun.star.sheet.AddIn",),)

if __name__ == '__main__':
    fi = RegextoolsImpl(None)
    print(fi.regextract('Words, words, words.',
                        '\W+'),
                        0)
