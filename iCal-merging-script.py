iCal1 = "TYPE FILE NAME HERE";
iCal2 = "TYPE FILE NAME HERE";
final_iCal = "TYPE FILE NAME HERE";

try:
        f1 = open(iCal1,"r");
except IOError:
	print '***** Could not open iCal-1 for reading *****';

try:
	f2 = open(iCal2,"r");
except IOError:
	print '***** Could not open iCal-2 for reading *****';

list1 = f1.readlines();
list2 = f2.readlines();

header = [];

i=0;
while i<len(list1):
	if "BEGIN:VEVENT" in list1[i]: 
		break;
	else:
		header.append(list1[i]);
		i=i+1;

final = [];

count1 = 0;
while 1:
	if "BEGIN:VEVENT" in list1[i]:
		f_elem = [];
		a = list1[i];
		b = list1[i+1];
		c = list1[i+2];
		d = list1[i+3];
                e = list1[i+4];
                f = list1[i+5];
		g = list1[i+6];
		f_elem.append(a);
		f_elem.append(b);
		f_elem.append(c);
		f_elem.append(d);
		f_elem.append(e);
		f_elem.append(f);
		f_elem.append(g);
		final.append(f_elem);
		count1=count1+1;
		i=i+7;
	else:
		break;

print '*****', count1, 'entries added from iCal-1 *****';

i=0
while i<len(list2):
        if "BEGIN:VEVENT" in list2[i]:
                break;
        else:
                i=i+1;

count2=0;
while 1:
        if "BEGIN:VEVENT" in list2[i]:
                f_elem = [];
                a = list2[i];
                b = list2[i+1];
                c = list2[i+2];
                d = list2[i+3];
                e = list2[i+4];
                f = list2[i+5];
                g = list2[i+6];
                f_elem.append(a);
                f_elem.append(b);
                f_elem.append(c);
                f_elem.append(d);
                f_elem.append(e);
                f_elem.append(f);
                f_elem.append(g);
		addflag=1;
		for x in final:
                	if f_elem[5] in x[5]:
				addflag=0;
		if addflag==1:
			final.append(f_elem);
			count2=count2+1;
                i=i+7;
        else:
		break;

print '*****', count2, 'entries added from iCal-2 *****';

print '***** Total', count1+count2, 'entries *****';

try:
	f3 = open(final_iCal,"w");
except IOError:
	print '***** Could not open final_iCal for writing. Check if you have write permissions *****';
	
for item in header:
	f3.write("%s" % item);
print '##### Saved headers to', final_iCal, '#####';

for x in final:
	for item in x:
		f3.write("%s" % item);
print '##### Saved', count1+count2, 'entries to', final_iCal, '#####';

f3.write("%s" % list1[len(list1)-1]);

f1.close();
f2.close();
f3.close();
