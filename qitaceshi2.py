# import re
s = "{\"loadStrategy\":\"FULL\",\"mode\":\"WIZARD\",\"name\":\"jicheng\",\"srcColumnIds\":[7631,7632,14174,14186,14187,14188,14189,14190,14191,14193,14194,14195,14196],\"srcDSId\":65,\"srcDSName\":\"test-lhq-in\",\"srcDSType\":\"DL\",\"srcModelId\":697,\"srcModelName\":\"datamodel_lhq_in\",\"targetDSId\":2,\"targetDSName\":\"cassandra\",\"targetDSType\":\"CDP\",\"targetDistinct\":true,\"targetModelId\":2475,\"targetModelName\":\"ods_datamodel_lhq_inin\"}"

s2 = s.split('targetModelName\":\"')
s3 = str(s2[1])
s3 = s3.split('"')
print(s2[1])
print(s3[0])


s4 = s.split('"')
print(len(s4))
print(s4[47])
print('-----5')

s="""{"loadStrategy":"FULL","mode":"WIZARD","name":"ihisq","srcColumnIds":[14552,14553,14554],"srcDSId":154,"srcDSName":"Lr","srcDSType":"DL","srcModelId":1174,"srcModelName":"autotest","targetDSId":2,"targetDSName":"cassandra","targetDSType":"CDP","targetDistinct":true,"targetModelId":2478,"targetModelName":"ods_xkgctmtfkcz"}"""
s5 = s.split('"')
print(len(s5))
print(s5[47])
