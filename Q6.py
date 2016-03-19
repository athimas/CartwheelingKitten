import sys
import os
print os.getcwd();
os.chdir("/home/samhita/Desktop/Ignite/new_file");
print os.getcwd();
para = open("new_file.txt","w");
para.write("Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d\n")
para.write("udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg\n")
para.write("<= 100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj.\n")
para.write("Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw\n")
para.write("vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu\n")
para.write("dojrulwkp");
para_modified = open("para_mod.txt","w");

with open("new_file.txt") as para:
  for line in  para:
	for c in line :
		case = ord(c);
		if case >= 68 and case <= 90:
			para_modified.write(chr(case -3));
		elif case >= 100 and case <= 122:
			para_modified.write(chr(case -3));
		elif case >= 65 and case<= 67:
			para_modified.write(chr(case +23));
		elif case >=97 and case <= 99:
			para_modified.write(chr(case +23));
		else :
			para_modified.write(c);
  para.close();
para_modified.close();
		
		
	