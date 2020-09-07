def rev_sentence(sentence):
    words = sentence.split(' ')  
    reverse_sentence = ' '.join(reversed(words))  
    return reverse_sentence   
  

 str = input("Enter a sentence : \n")
 print("\n")
 print(rev_sentence(str)) 
