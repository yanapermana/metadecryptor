def decryptBacon(cipher):
		bacon = ['AAAAA','AAAAB','AAABA','AAABB','AABAA','AABAB','AABBA','AABBB','ABAAA','ABAAB','ABABA','ABABB','ABBAA','ABBAB','ABBBA','ABBBB','BAAAA','BAAAB','BAABA','BAABB','BABAA','BABAB','BABBA','BABBB']
		alphabet = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
		chunk_size = 5
		myList = [ cipher[i:i+chunk_size] for i in range(0, len(cipher), chunk_size) ]
		myArr = []
		out = ''
		for i in range(0, len(myList), 1):
			myList[i] = myList[i].upper()
			if any(myList[i] in s for s in bacon):
				for j in range(0, len(bacon), 1):
					if myList[i] == bacon[j]:
						myArr.append(alphabet[j])
			else:
				myArr.append("?")
		res = out.join(myArr)
		iv = res.replace('u','v')
		ju = res.replace('i','j')
		jv = res.replace('i','j').replace('u','v')

		print('[1]',res)
		print('[2]',iv)
		print('[3]',ju)
		print('[4]',jv)

if __name__ == '__main__':
	cipher = """BAAABABABAAABAAABBAABAABAAABAAABBAAAABBAABABBAAAAABAABBABAABAABAAABAAAABBABAABBAABAAAAAAAA"""
	decryptBacon(cipher)