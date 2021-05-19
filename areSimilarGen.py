
import time
# a generator function that swaps every 2 elements within the given list 
def areSimilarIter(a, b):
    def swap(a):
        x = a[:]
        for i in range(len(a)):
            for j in range(len(a)):
                if  i>j:
                    s, ss= x[j], x[i]
                    x[i], x[j] = s ,ss
                    yield x
                    x = a[:]
    
#  check for matches for each permutation yielded by the generator function 
    def find_Match(a, b):
        g = swap(a)
        x =[]
        for i in g:
            if b == i:
                x.append(1)
                if len(x)>0:
                    return True
                else:
                    continue
#  perform the final check  
    if a == b:
        return True
    elif find_Match(a, b):
        return True
    else:
        return False

                

a= [905, 944, 570, 567, 880, 147, 791, 201, 829, 727, 687, 988, 691, 768, 726, 731, 666, 646, 621, 340, 372, 920, 473, 606, 721, 228, 984, 218, 948, 197, 87, 94, 425, 719, 293, 888, 610, 331, 67, 812, 107, 976, 724, 721, 459, 147, 201, 586, 611, 153, 93, 627, 358, 810, 459, 55, 317, 652, 726, 558, 302, 285, 370, 812, 866, 435, 266, 733, 578, 597, 13, 778, 453, 654, 297, 408, 257, 277, 503, 919, 874, 83, 566, 904, 866, 896, 462, 915, 124, 240, 947, 961, 724, 386, 870, 354, 122, 756, 103, 626]
b = [905, 944, 570, 567, 880, 147, 791, 201, 829, 727, 687, 988, 691, 768, 726, 731, 666, 646, 621, 340, 372, 920, 473, 606, 721, 228, 984, 218, 948, 197, 87, 94, 425, 719, 293, 888, 610, 331, 67, 812, 107, 976, 724, 721, 459, 147, 201, 586, 611, 153, 93, 627, 358, 810, 459, 55, 317, 652, 726, 558, 302, 285, 370, 812, 866, 435, 266, 733, 578, 597, 13, 778, 952, 654, 297, 408, 257, 277, 503, 919, 874, 83, 566, 904, 866, 896, 462, 915, 124, 240, 947, 961, 724, 386, 870, 354, 122, 756, 103, 626]


t1= time.time()
print(areSimilarIter(a, b))
t2= time.time()

print("time difference: %.6f" %(t2-t1))