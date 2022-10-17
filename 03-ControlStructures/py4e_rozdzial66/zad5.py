str = 'X-DSPAM-Confidence:0.8475'
start = str.find(":")
nowystr = str[start+1:]
nowystr = float(nowystr)
print(nowystr)