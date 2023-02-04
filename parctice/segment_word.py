def sen2word(sentences,vocab,maxlen):
    #words 词表
    #maxlen 词的最大长度
    len_sen = len(sentences)
    head = 0
    tail = min(head+maxlen,len(sentences))
    words = []
    while(head<tail):
        word = sentences[head:tail]
        print(word)
        if(word in vocab) or (tail-head == 1):
            words.append(word)
            head = tail
            tail = min(head+maxlen,len(sentences))
        else:
            tail = tail-1
    return words

sentences = "今年世界杯的冠军是阿根廷队"
print(sen2word(sentences,["今年","世界杯","的","冠军","是","阿根廷队"],4))