#
# Copyright (c) 2019-2020 Mike Goppold von Lobsdorf
#
# This program is free software; you can redimyStribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is dimyStributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin myStreet, Fifth Floor, Boston, MA 02110-1301 USA.
#

#
# This is a script that generates a howto
#

import os

QUOTE = "\""
LINE_RETURN = "\n"
TAB = "\t"

def myCat3(left, middle, right):
	myStr = ""	
	if(left != None): myStr += left
	if(middle != None): myStr += middle
	if(right != None): myStr += right
	return myStr

def myCat2(left, right):
	myStr = ""
	if(left != None): myStr += left
	if(right != None): myStr += right
	return myStr

def unorderedListWrap(innerStuff):
	return myCat3("<ul>", innerStuff, "</ul>")

def listItemWrap(innerStuff):
	return myCat3("<li>", innerStuff, "</li>" + LINE_RETURN)

def appendListItemBegin(outerStuff):
	return myCat2(outerStuff, "<li>" + LINE_RETURN)

def appendListItemEnd(outerStuff):
	return myCat2(outerStuff, "</li>" + LINE_RETURN)

def appendListBegin(outerStuff):
	return myCat2(outerStuff, "<ul>" + LINE_RETURN)

def appendListEnd(outerStuff):
	return myCat2(outerStuff, "</ul>" + LINE_RETURN)

def imageWrap(imgPath, altText, width, height):
	imgStr = ("<img class=" + QUOTE + "pict-preview" + QUOTE + LINE_RETURN
		+ TAB + "src=" + QUOTE + imgPath + QUOTE + LINE_RETURN
		+ TAB + "alt=" + QUOTE + altText + QUOTE + LINE_RETURN
		+ TAB + "style=" + QUOTE
			+ "width: " + str(width) + "px;"
			+ " height: " + str(height) + "px;" + QUOTE + LINE_RETURN
		+ TAB + "/>")
	
	leftStr = "<a href=" + QUOTE + imgPath + QUOTE + ">" + LINE_RETURN
	rightStr = "</a>" + LINE_RETURN
	myStr = myCat3(leftStr, imgStr, rightStr)
	return myStr

def appendTerminalBoxBegin(prevContent):
	myStr = myCat2(prevContent,
		"<div style=" + QUOTE
		+ "border: 2pt solid black;" + LINE_RETURN
		+ "background: #afa;"
		+ "font-family: monospace;"
		+ QUOTE + ">"
		+ "<div style=" + QUOTE
		+ "border: 2pt solid white;" + LINE_RETURN
		+ QUOTE + ">")
	return myStr

def appendTerminalBoxEnd(prevContent):
	myStr = myCat2(prevContent,
		"</div>" + LINE_RETURN
		+ "</div>" + LINE_RETURN)
	return myStr

def appendTextEditorBoxBegin(prevContent):
	myStr = myCat2(prevContent,
		"<div style=" + QUOTE
		+ "border: 2pt solid black;" + LINE_RETURN
		+ "background: #ffd;"
		+ "font-family: monospace;"
		+ QUOTE + ">"
		+ "<div style=" + QUOTE
		+ "border: 2pt solid white;" + LINE_RETURN
		+ QUOTE + ">")
	return myStr

def appendTextEditorBoxEnd(prevContent):
	myStr = myCat2(prevContent,
		"</div>" + LINE_RETURN
		+ "</div>" + LINE_RETURN)
	return myStr

def mainWrap(contentStr, headerStr, titleStr):
	leftStr = ("<style"
		+ " type=" + QUOTE + "text/css" + QUOTE + ">" + LINE_RETURN)
	#middleStr = (".gray-border {" + LINE_RETURN
	#	+ TAB + "border-width: 2px;" + LINE_RETURN
	#	+ TAB + "border-color: #777;" + LINE_RETURN
	#	+ TAB + "border-style: solid;" + LINE_RETURN
	#	+ "}" + LINE_RETURN)
	middleStr = (
		"@import url(docs-style.css);" + LINE_RETURN)
	rightStr = "</style>" + LINE_RETURN
	myStr = myCat3(leftStr, middleStr, rightStr)

	leftStr = "<title>" + titleStr + "</title>" + LINE_RETURN
	headerWrapStr = myCat3(leftStr, myStr, headerStr)
	
	leftStr = "<head>" + LINE_RETURN
	rightStr = "</head>" + LINE_RETURN
	headerWrapStr = myCat3(leftStr, headerWrapStr, rightStr)
	
	leftStr = "<body>" + LINE_RETURN
	rightStr = "</body>" + LINE_RETURN
	myStr = myCat3(leftStr, contentStr, rightStr)

	myStr = myCat3(headerWrapStr, myStr, None)

	leftStr = (
		"<html"
			+ " xmlns=" + QUOTE + "http://www.w3.org/1999/xhtml" + QUOTE
			+ " xml:lang=" + QUOTE + "en" + QUOTE
			+ " lang=" + QUOTE + "en" + QUOTE
			+ ">" + LINE_RETURN
		)
	rightStr = "</html>" + LINE_RETURN
	myStr = myCat3(leftStr, myStr, rightStr)

	leftStr = (
		"<!DOCTYPE html PUBLIC " + LINE_RETURN
			+ TAB + QUOTE
				+ "-//W3C//DTD XHTML Basic 1.1//EN"
			+ QUOTE + LINE_RETURN
			+ TAB + QUOTE
				+ "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd"
			+ QUOTE + ">" + LINE_RETURN
		)
	myStr = myCat3(leftStr, myStr, None)

	leftStr = (
		"<?xml"
			+ " version=" + QUOTE + "1.0" + QUOTE
			+ " encoding=" + QUOTE + "UTF-8" + QUOTE
			+ "?>" + LINE_RETURN
		)
	myStr = myCat3(leftStr, myStr, None)

	return myStr

def bodyGen():
	#myStr = "<p>Hi there!</p>" + LINE_RETURN
	myStr = ""
	myStr = appendListBegin(myStr)
	
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr, "Run the CSV test of ObjectAccessNow.")
	
	os.system("mkdir -p docs/help/csv")

	os.system("cp"
		+ " css/docs-style.css"
		+ " docs/help/csv")
	
	#os.system("cp"
	#	+ " picts/Debian-Boot-CD-BIOS.png"
	#	+ " docs/help/debian")
	#os.system("cp"
	#	+ " picts/Debian-Boot-CD-UEFI.png"
	#	+ " docs/help/debian")
	
	myStr = appendListBegin(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Open a terminal and clone the ObjectAccessNow repo.</p>")
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>git clone https://github.com/mgoppold5/objectaccessnow</b>" + "<br>" + LINE_RETURN
		+ "Cloning into 'objectaccessnow'..." + "<br>" + LINE_RETURN
		+ "remote: Enumerating objects: 820, done." + "<br>" + LINE_RETURN
		+ "remote: Counting objects: 100% (820/820), done." + "<br>" + LINE_RETURN
		+ "remote: Compressing objects: 100% (355/355), done." + "<br>" + LINE_RETURN
		+ "remote: Total 820 (delta 425), reused 755 (delta 360), pack-reused 0" + "<br>" +	LINE_RETURN
		+ "Receiving objects: 100% (820/820), 356.29 KiB | 517.00 KiB/s, done." + "<br>" + LINE_RETURN
		+ "Resolving deltas: 100% (425/425), done." + "<br>" + LINE_RETURN
		+ "COMMAND> <b>cd objectaccessnow</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Move the " + QUOTE + "test java compiler csv"
			+ QUOTE + " folder, out of the "
			+ QUOTE + "extra" + QUOTE + " folder, into the top level repo folder.</p>")
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>mv " + QUOTE + "extra/test java compiler csv"
			+ QUOTE + " .</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Make a test folder in the top level repo folder.</p>")
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>mkdir " + QUOTE + "test"
			+ QUOTE + "</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Copy in " + QUOTE + "ProjectInfo" + QUOTE + LINE_RETURN
		+ " and " + QUOTE + "Tools" + QUOTE + LINE_RETURN
		+ " from the " + QUOTE + "test java compiler" + QUOTE + " folder.</p>" + LINE_RETURN)
	myStr = myCat2(myStr,
		"<p>And copy in " + QUOTE + "ProjectInfo" + QUOTE + LINE_RETURN
		+ " and " + QUOTE + "Tools" + QUOTE + LINE_RETURN
		+ " from the " + QUOTE + "test java compiler csv" + QUOTE + " folder.</p>" + LINE_RETURN)
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>cp -r " + QUOTE + "test java compiler/ProjectInfo"
			+ QUOTE + " " + QUOTE + "test" + QUOTE + "</b>" + "<br>" + LINE_RETURN
		+ "COMMAND> <b>cp -r " + QUOTE + "test java compiler/Tools"
			+ QUOTE + " " + QUOTE + "test" + QUOTE + "</b>" + "<br>" + LINE_RETURN
		+ "COMMAND> <b>cp -r " + QUOTE + "test java compiler csv/ProjectInfo"
			+ QUOTE + " " + QUOTE + "test" + QUOTE + "</b>" + "<br>" + LINE_RETURN
		+ "COMMAND> <b>cp -r " + QUOTE + "test java compiler csv/Tools"
			+ QUOTE + " " + QUOTE + "test" + QUOTE + "</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Get a prompt in the " + QUOTE + "test" + QUOTE + " folder.</p>" + LINE_RETURN)
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>cd " + QUOTE + "test" + QUOTE + "</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Set the environment variables "
		+ QUOTE + "JDK_HOME" + QUOTE
		+ " and " + QUOTE + "JRE_HOME" + QUOTE
		+ " to where your java development kit is located.</p>" + LINE_RETURN)
	myStr = myCat2(myStr,
		"<p>For example, in Debian, use the "
		+ QUOTE + "/usr/lib/jvm/default-java" + QUOTE + " folder.</p>" + LINE_RETURN)
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>export JDK_HOME=/usr/lib/jvm/default-java</b>" + "<br>" + LINE_RETURN
		+ "COMMAND> <b>export JRE_HOME=/usr/lib/jvm/default-java</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Execute the "
		+ QUOTE + "testMerge.py" + QUOTE
		+ " and " + QUOTE + "testCompile.py" + QUOTE + " programs.</p>" + LINE_RETURN)
	myStr = myCat2(myStr,
		"<p>The merge operation copies all the files"
		+ " from all the necessary top level folders,"
		+ " into the test folder, overwriting everything.</p>" + LINE_RETURN
		+ "<p>The compile operation compiles the java source code.</p>" + LINE_RETURN)
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>python3 Tools/testMerge.py</b>" + "<br>" + LINE_RETURN
		+ "COMMAND> <b>python3 Tools/testCompile.py</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Now you are ready to run the test program.</p>" + LINE_RETURN
		+ "<p>There is a program to run a command called "
		+ QUOTE + "testCommand1.py" + QUOTE + ".</p>")
	myStr = myCat2(myStr,
		"<p>Run off a copy of the original,"
		+ " since the original gets overwritten with each merge operation.</p>" + LINE_RETURN
		+ "<p>Now edit the copy."
		+ " The copy will stay in the " + QUOTE + "test" + QUOTE + " folder.</p>")
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>cp Tools/testCommand1.py Tools/testCommandTemp.py</b>" + "<br>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Edit the program to run the command,"
		+ " enabling the action to occur.</p>" + LINE_RETURN)
	myStr = appendTextEditorBoxBegin(myStr)
	myStr = myCat2(myStr,
		"EDIT> change <b>False</b> to <b>True</b> in the <b>if</b> statement.</b>" + "<br>" + LINE_RETURN
		+ "from" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;if(False):" + "<br/>" + LINE_RETURN
		+ "to" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;if(True):" + "<br/>" + LINE_RETURN
		+ "EDIT>" + "<br/>" + LINE_RETURN)
	myStr = appendTextEditorBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	myStr = appendListItemBegin(myStr)
	myStr = myCat2(myStr,
		"<p>Now run the program with the command.</p>" + LINE_RETURN)
	myStr = appendTerminalBoxBegin(myStr)
	myStr = myCat2(myStr,
		"COMMAND> <b>python3 Tools/testCommandTemp.py</b>" + "<br>" + LINE_RETURN
		+ "File: test1.csv" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;Outputing tree" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;GRAM_XML_CONTENT ()" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_STRING_SPAN (one)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_COMMA (,)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;GRAM_XML_CONTENT ()" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_STRING_SPAN (two)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_COMMA (,)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;GRAM_XML_CONTENT ()" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_STRING_SPAN (three)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_LINE_RETURN (" + "<br/>" + LINE_RETURN
		+ ")" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;GRAM_XML_CONTENT ()" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_STRING_SPAN (four)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_COMMA (,)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;GRAM_XML_CONTENT ()" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_STRING_SPAN (five)" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;TOKEN_END_OF_STREAM" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;Outputing module info" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;module CharReader" + "<br/>" + LINE_RETURN
		+ "&nbsp;&nbsp;&nbsp;&nbsp;module CsvBaseReader" + "<br/>" + LINE_RETURN
		+ "COMMAND>" + "<br>" + LINE_RETURN)
	myStr = appendTerminalBoxEnd(myStr)
	myStr = appendListItemEnd(myStr)
	#myStr = appendListItemBegin(myStr)
	#myStr = myCat2(myStr,
	#	imageWrap("Debian-Boot-CD-BIOS.png", "BIOS boot screen", 320, 240))
	#myStr = appendListItemEnd(myStr)
	

	myStr = appendListEnd(myStr)
	return myStr

def main():
	os.system("mkdir -p docs/help/csv")
	os.system("touch docs/help/csv/index.htm")

	f = open("docs/help/csv/index.htm", "r+")
	f.truncate(0)

	contentMyStr = bodyGen()
	headerMyStr = ""
	titleMyStr = "Hi there"
	myStr = mainWrap(contentMyStr, headerMyStr, titleMyStr)

	f.write(myStr)
	f.close()

main()
