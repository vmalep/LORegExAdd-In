# LORegExAdd-In
Add-In for LibreOffice Calc providing fonctions using RegEx

So far, the only function is "regextract" that allows to extract some characters from a string according to a regex pattern.
This function takes 3 paramenters: the string to search into, the pattern in which each group to be extracted is put into brackets, and the number of the group to be displayed. I.e:
regextract("12 abc 12";"(\d+)\s(\D+)";1) = 12 and
regextract("12 abc 12";"(\d+)\s(\D+)";2) = abc

Suggestion are more than welcome.

Special thanks to Lorenzo Carbonell who helped me debugging this extension!
