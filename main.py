import numpy
import time


def read_referencefiles():
    # Reading the reference files.
    print("Reading Reference Files")
    result=[]
    file_names = ("HapMap_r23a_CEP_C1_AllSNPs.txt", "HapMap_r23a_CEP_C2_AllSNPs.txt", "HapMap_r23a_CEP_C13_AllSNPs.txt", "HapMap_r23a_CEP_C14_AllSNPs.txt" , "HapMap_r23a_CEP_C15_AllSNPs.txt" , "HapMap_r23a_CEP_C16_AllSNPs.txt")
    for name in file_names :
        f = open(name)
        for i, line in enumerate(f):
            data = line.strip().split()#Format data taken from file
            result.append(data)
    return result
def readsample_file():
    f = open("genotype_inf.txt")
    result_sample=[]
    for i, line in enumerate(f):
        data = line.strip().split(r";")     #Format data taken from file (; removed by splitting
        result_sample.append(data)
    return result_sample

def operation(refer,sample):
    count=0
    result=[]
    refer_arr= numpy.array(refer)
    sort_indi = numpy.argsort(refer_arr[:, 0])
    sorted_refer_arr=refer_arr[sort_indi]
    #print(sorted_refer_arr)
    sample_arr = numpy.array(sample)
    sample_arr = sample_arr[2:]
    sort_indices = numpy.argsort(sample_arr[:, 0])
    sorted_sample_arr=sample_arr[sort_indices]

    #print(sorted_sample_arr)
    for i in range(len(sorted_refer_arr)):
         if sorted_refer_arr[i][0] == sorted_sample_arr[i][0]:

            if refer_arr[i][2]!=sample_arr[i][2]:
                    count=count+1
                    result.append(sample_arr[i][1])

    print(count)
    time.sleep(5)
    print("\nNumber of unique markers disregarding individuals are as follows")
    time.sleep(3)
    result=set(result)
    for i in result:
           print(i)

def read_testrefer():
    f = open("test_refer.txt")
    result_sample=[]
    for i, line in enumerate(f):
        data = line.strip().split()
        result_sample.append(data)
    return result_sample

def read_testsample():
    f = open("test_sample.txt")
    result_sample=[]
    for i, line in enumerate(f):
        data = line.strip().split(r";")
        result_sample.append(data)
    return result_sample




if __name__ == '__main__':
    print("This is a programme to compare sample genetic data to given reference data")
    sample=[]
    reference=[]
    reference=read_referencefiles()
    sample=readsample_file()
    #reference=read_testrefer()     #For reading self-test data
    #sample=read_testsample()       #For reading self-test data
    print("Number of pairs of individuals/markers where the allele result from the lab differed from the reference data are")
    operation(reference,sample)     #Operation to count result and unique markers


