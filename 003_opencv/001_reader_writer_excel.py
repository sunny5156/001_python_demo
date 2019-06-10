#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-6 下午7:00
# @Author  : Scheaven
# @File    : test_ecel.py
# @description: 

import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel("ErrorCode2.xls")
    df3 = pd.DataFrame()
    ff = open("f.csv",'w')
    cvalue_list = []
    fs = open("fs.csv", 'w')
    j=0;
    k=0
    i = 0;
    a = df.to_dict(orient="records")
    for line in a:
        n_line = "";
        flat = False
        top = ""
        n2_l = "";
        i+=1
        value_list = []
        for key,value in line.items():

            if (key == "Part" or key == "PartCode") and "/" in str(value):
                j+=1
                flat =True
                n_line +=str(value.split("/")[0]+value.split("/")[1][1:])+","
                n2_l +=str(value.split("/")[1])+","
                top = value.split("/")
            elif key == "ID":
                value = str(i);
                n_line += str(value) + ","
                n2_l += str(value) + ","
            elif key == "CodeDescription" or key == "PossibleReasion" or key == "Condition":
                if str(value) == "nan":
                    value = ""
                # print(str(value))
                value = str(value).replace("\n","")
                n_line += str(value) + ","
                n2_l += str(value) + ","
            else:
                if str(value) == "nan":
                    value = ""
                n_line+=str(value)+","
                n2_l +=str(value)+","

            if str(value) == "nan":
                value = ""
            value_list.append(value)

        # if i == 1777:
        #           break
        if flat:
            k+=1
            ff.write(n2_l+"\n")
            cvalue_list.append(value_list)
            # df2 = pd.concat(value_list).to_excel("Error.xls", index=False)

        ff.write(n_line+"\n")
    aaa = pd.DataFrame(cvalue_list, columns=list("abcdefghi"))
    aaa.to_excel("Error.xls", index=False)

    print(j,k)
