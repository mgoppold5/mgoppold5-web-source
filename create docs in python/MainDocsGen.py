#
# Copyright (c) 2019 Mike Goppold von Lobsdorf
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

def appendListBegin(outerStuff):
	return myCat2(outerStuff, "<ul>" + LINE_RETURN)

def appendListEnd(outerStuff):
	return myCat2(outerStuff, "</ul>" + LINE_RETURN)

def imageWrap(imgPath, altText, width, height):
	imgStr = ("<img class=" + QUOTE + "gray-border" + QUOTE + LINE_RETURN
		+ TAB + "src=" + QUOTE + imgPath + QUOTE + LINE_RETURN
		+ TAB + "alt=" + QUOTE + altText + QUOTE + LINE_RETURN
		+ TAB + "style=" + QUOTE
			+ "width: " + str(width) + "px;"
			+ " height: " + str(height) + "px;" + QUOTE + LINE_RETURN
		+ TAB + "/>")
	
	leftStr = "<a href=" + QUOTE + imgPath + QUOTE + "/>" + LINE_RETURN
	rightStr = "</a>" + LINE_RETURN
	myStr = myCat3(leftStr, imgStr, rightStr)
	return myStr

def mainWrap(contentStr, headerStr, titleStr):
	leftStr = ("<style"
		+ " type=" + QUOTE + "text/css" + QUOTE + ">" + LINE_RETURN)
	middleStr = (".gray-border {" + LINE_RETURN
		+ TAB + "border-width: 2px;" + LINE_RETURN
		+ TAB + "border-color: #777;" + LINE_RETURN
		+ TAB + "border-style: solid;" + LINE_RETURN
		+ "}" + LINE_RETURN)
	rightStr = "</style>" + LINE_RETURN
	myStr = myCat3(leftStr, middleStr, rightStr)

	leftStr = "<title>" + titleStr + "</title>" + LINE_RETURN
	headerWrapStr = myCat2(leftStr, myStr)
	headerWrapStr = myCat2(myStr, headerStr)
	
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
	myStr = myCat2(myStr, listItemWrap("Boot the cd or usb media"))
	
	os.system("mkdir -p docs/help/debian")
	
	os.system("cp"
		+ " picts/Debian-Boot-CD-BIOS.png"
		+ " docs/help/debian")
	os.system("cp"
		+ " picts/Debian-Boot-CD-UEFI.png"
		+ " docs/help/debian")
	
	myStr = appendListBegin(myStr)
	myStr = myCat2(myStr, listItemWrap(
		"If booting from BIOS, hit [ENTER] to choose <b>Graphical Install</b>."))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Boot-CD-BIOS.png", "BIOS boot screen", 320, 240)))
	myStr = myCat2(myStr, listItemWrap(
		"If booting from UEFI, hit [ENTER] to choose <b>Graphical Install</b>."))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Boot-CD-UEFI.png", "UEFI boot screen", 400, 300)))
	myStr = appendListEnd(myStr)
	
	myStr = myCat2(myStr, listItemWrap("Fill out the debian installer language forms"))

	os.system("cp"
		+ " picts/Debian-Installer-Language-1.png"
		+ " docs/help/debian")
	os.system("cp"
		+ " picts/Debian-Installer-Language-2.png"
		+ " docs/help/debian")
	os.system("cp"
		+ " picts/Debian-Installer-Language-3.png"
		+ " docs/help/debian")

	myStr = appendListBegin(myStr)
	myStr = myCat2(myStr, listItemWrap(
		"Choose <b>English</b> in the list box, and click <b>Continue</b>."))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Language-1.png",
			"Debian Installer Language Form 1", 400, 300)))
	myStr = myCat2(myStr, listItemWrap(
		"Choose <b>United States</b> in the list box, and click <b>Continue</b>."))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Language-2.png",
			"Debian Installer Language Form 2", 400, 300)))
	myStr = myCat2(myStr, listItemWrap(
		"Choose <b>American English</b> in the list box, and click <b>Continue</b>."))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Language-3.png",
			"Debian Installer Language Form 3", 400, 300)))
	myStr = appendListEnd(myStr)

	myStr = myCat2(myStr, listItemWrap("Fill out the debian installer network forms"))

	os.system("cp"
		+ " picts/Debian-Installer-Network-Hostname.png"
		+ " docs/help/debian")
	os.system("cp"
		+ " picts/Debian-Installer-Network-Domain-Name.png"
		+ " docs/help/debian")

	myStr = appendListBegin(myStr)
	myStr = myCat2(myStr, listItemWrap(
		"<p>A network hostname is the name" + LINE_RETURN
		+ " which your computer will show on the network." + LINE_RETURN
		+ " The default in the field is <b>debian</b>, which is just fine.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Network-Hostname.png",
			"Debian Installer Hostname Form", 400, 300)))
	myStr = myCat2(myStr, listItemWrap(
		"<p>A network domain name isnt necessary" + LINE_RETURN
		+ " for client computers for basic Internet access." + LINE_RETURN
		+ " It is used for servers, or utilized in large networks." + LINE_RETURN
		+ " The default in the field is a blank, which is just fine.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Network-Domain-Name.png",
			"Debian Installer Domain Name Form", 400, 300)))
	myStr = appendListEnd(myStr)

	myStr = myCat2(myStr, listItemWrap("Fill out the debian installer user forms"))

	os.system("cp"
		+ " picts/Debian-Installer-Users-Root-Password.png"
		+ " docs/help/debian")
	os.system("cp"
		+ " picts/Debian-Installer-Users-Full-Name.png"
		+ " docs/help/debian")
	os.system("cp"
		+ " picts/Debian-Installer-Users-Username.png"
		+ " docs/help/debian")
	os.system("cp"
		+ " picts/Debian-Installer-Users-Password.png"
		+ " docs/help/debian")

	myStr = appendListBegin(myStr)
	myStr = myCat2(myStr, listItemWrap(
		"<p>This form asks for the password for the root user." + LINE_RETURN
		+ " But Debian doesnt need a root user." + LINE_RETURN
		+ " You can leave this field blank, " + LINE_RETURN
		+ " and the installer will give admin privelages to the first user." + LINE_RETURN
		+ " The default in the field is blank, which is just fine.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Users-Root-Password.png",
			"Debian Installer Root's Password Form", 400, 300)))
	myStr = myCat2(myStr, listItemWrap(
		"<p>This form asks for your full name." + LINE_RETURN
		+ " The default in the field is blank, which is just fine.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Users-Full-Name.png",
			"Debian Installer Person Full Name Form", 400, 300)))
	myStr = myCat2(myStr, listItemWrap(
		"<p>This form asks for the username you will have." + LINE_RETURN
		+ " The system will most often use this to distinquish the user account." + LINE_RETURN
		+ " It's best if it has lowercase letters." + LINE_RETURN
		+ " Something simple like <b>debra</b> or <b>ian</b> is good.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Users-Username.png",
			"Debian Installer Username Form", 400, 300)))
	myStr = myCat2(myStr, listItemWrap(
		"<p>This form asks for your user's password." + LINE_RETURN
		+ " You will use this to log in." + LINE_RETURN
		+ " Type the same answer twice.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Users-Password.png",
			"Debian Installer Users Password Form", 400, 300)))
	myStr = appendListEnd(myStr)

	myStr = myCat2(myStr, listItemWrap(
		"Fill out the debian installer forms for the computer clock."))
	
	os.system("cp"
		+ " picts/Debian-Installer-Clock-Time-Zone.png"
		+ " docs/help/debian")

	myStr = appendListBegin(myStr)
	myStr = myCat2(myStr, listItemWrap(
		"<p>This form asks for the time zone." + LINE_RETURN
		+ " The system remembers this as an offset to Greenwich Mean Time." + LINE_RETURN
		+ " Select the correct value in the list box," + LINE_RETURN
		+ " to configure the clock correctly.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Clock-Time-Zone.png",
			"Debian Installer Clock Time Zone Form", 400, 300)))
	myStr = appendListEnd(myStr)

	myStr = myCat2(myStr, listItemWrap(
		"Fill out the debian installer forms to configure partitions."))

	os.system("cp"
		+ " picts/Debian-Installer-Disks-Partition-Strategy.png"
		+ " docs/help/debian")

	myStr = appendListBegin(myStr)
	myStr = myCat2(myStr, listItemWrap(
		"<p>This form has options to configure paritions." + LINE_RETURN
		+ " Select <b>Manual</b> in the list box." + LINE_RETURN
		+ " This gives the most freedom.</p>" + LINE_RETURN
		+ "<p>Click <b>Continue</b>.</p>" + LINE_RETURN))
	myStr = myCat2(myStr, listItemWrap(
		imageWrap("Debian-Installer-Disks-Partition-Strategy.png",
			"Debian Installer Disks Partition Strategy Form", 400, 300)))
	myStr = appendListEnd(myStr)

	myStr = appendListEnd(myStr)
	return myStr

def main():
	os.system("mkdir -p docs/help/debian")
	os.system("touch docs/help/debian/index.htm")

	f = open("docs/help/debian/index.htm", "r+")
	f.truncate(0)

	contentmyStr = bodyGen()
	headermyStr = ""
	titlemyStr = "Hi there"
	myStr = mainWrap(contentmyStr, headermyStr, titlemyStr)

	f.write(myStr)
	f.close()

main()
