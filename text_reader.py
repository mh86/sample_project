import regex as re
import mmap as mm

txt_file = open('crch.txt', 'r')
txt_str = txt_file.read()
txt_file.close()

# print(type(txt_str))
# print(txt_str)
# pattern = re.compile('C')
# # matches = re.search(pattern, txt_str)
# print(type(matches))
# print(matches)


total = 0
a = [m.start() for m in re.finditer('C'+ str(1), txt_str)]
M = len(a)
b = [None] * M
for index in range(M):
		b[index] = txt_str[a[index]:].find(' ') + a[index]
#print(occurrence)
print(txt_str[a[0]:b[0]])
#for digit in range(10):
    # occurrence[digit] = [[m1.start(), m2.end()] for m1 in re.finditer('C' + str(digit), txt_str) for m2 in re.finditer(' ', txt_str)]
    # occurrence[digit] = [[m1.start() for m1 in re.finditer('C' + str(digit), txt_str)], [m2.end() for m2 in re.finditer(' ', txt_str)]]
    # occurrence[digit] = [[m1.start(), m2.end()] for [m1, m2] in zip(re.finditer('C' + str(digit), txt_str), re.finditer(' ', txt_str))]
#    occurrence1[digit] = [m.start() for m in re.finditer('C' + str(digit), txt_str)]
#    print(occurrence1[digit],'empty')
#    occurrence2[digit] = [m.start() for m in re.finditer(' ', txt_str[occurrence1[digit]:])]
#    occurrence[digit] = [occurrence1[digit], occurrence2[digit]]
#    counts[digit] = len(occurrence[digit])
#    print(counts[digit])
#    total += counts[digit]

#print(total)

#print(occurrence)
# print(txt_str[occurance[0][0][0], occurance[0][0][1]])
# print(occurance)
# N = len(occurance)
# print(N)
#
# for i in range(N):
#     print(txt_str[occurance[i]])
#     print('\n')