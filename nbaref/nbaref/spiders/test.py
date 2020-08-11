def euclidean (p,q,features):
    d=0
    for i in range(features):
        d +=(p[i]-q[i])**2
    d = sqrt(d)
    return d


# test_data is new data introduced to the problem
#training_data is data already classified
#training_labels are labels given to test_Data once classified
def knnclassify(test_data,training_data, training_labels, K=1):
    sizet = len(test_data)
    classified = []
    for i in range (len(test_data)):
        data = [] 
        closest_distance = math.inf
        for j in range((training_data)):
            measure = euclidean(test_data[i],training_data[j],4)
            data.append([measure,training_data[j]])
            if measure<closest_distance:
                    closest_distance=measure
                    closest=training_data[j]
        sorted(data,key=lambda l:l[1])
        temp = []
        for l in range (K):
            temp.append(training_labels[data[l]])
        result = counter (temp)
        classified.append(result.most_common(1)[0][0])
    return classified



        
    