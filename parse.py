from html5print import HTMLBeautifier
from html5print import CSSBeautifier
from html5print import JSBeautifier

jsi = "alert("test");"
cssi = "p{color:#ff;}"
htmli = "<html><head>"

print(JSBeautifier.beautify(jsi, 4))
