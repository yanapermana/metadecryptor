def decryptMorse(cipher):
	morse = ['.-','.---','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
	myList = cipher.split()
	myArr = []
	for i in range(0, len(myList), 1):
		for j in range(0, len(morse), 1):
			if myList[i] == morse[j]:
				myArr.append(alphabet[j])
	return ''.join(myArr)
	
if __name__ == '__main__':
	cipher = '- . --. .- .-.. / .-.. .- -.- .- / .-.. .- -.- .- / '
	print(decryptMorse(cipher))