import numpy

testing_data = numpy.array([
  [0,697,38,3,2],
  [2,636,601,155,2],
  [5,862,28,0,2],
  [0,280,418,32,2],
  [5,724,1023,0,2],
  [11,1023,207,77,2],
  [6,1023,850,0,2],
  [47,523,953,258,2],
  [27,266,97,0,2],
  [5,542,0,0,2],
  [15,587,0,0,2],
  [44,316,0,8,2],
  [11,15,8,57,2],

  [0,0,302,76,3],
  [58,19,235,70,3],
  [26,24,313,12,3],
  [63,27,217,24,3],
  [31,18,265,40,3],
  [0,0,497,0,3],
  [120,266,811,101,3],
  [160,0,422,113,3],
  [160,120,941,57,3],
  [105,95,478,115,3],
  [6,0,297,2,3],
  [55,78,466,47,3],
  [57,21,531,58,3],
  [8,0,223,84,3],
  [0,60,435,170,3]
])

features = testing_data[:,0:4]
labels = testing_data[:,4].T