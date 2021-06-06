import requests
import os
s=['http://photo.colorweb.com.tw/DLphoto.php?file=All_photo/109/薇閣中學-2/0','-90','/90','/90','-1.jpg']

for _ in range(1,10):
    os.mkdir(str(_))
    for i in range(1,53):
        if i>=10:
            url=s[0]+str(_)+s[1]+str(_)+s[2]+str(_)+str(i)+s[3]+str(_)+str(i)+s[4]
        else:
            url=s[0]+str(_)+s[1]+str(_)+s[2]+str(_)+'0'+str(i)+s[3]+str(_)+'0'+str(i)+s[4]

        res=requests.get(url)
        re=url.split('/')[-1]
        print('suc'+str(url))
        with open(str(_)+'/'+re, 'wb') as f:
                f.write(res.content)
s=['http://photo.colorweb.com.tw/DLphoto.php?file=All_photo/109/薇閣中學-2/','-9','/9','/9','-1.jpg']

for _ in range(10,15):
    os.mkdir(str(_))
    for i in range(1,53):
        if i>=10:
            url=s[0]+str(_)+s[1]+str(_)+s[2]+str(_)+str(i)+s[3]+str(_)+str(i)+s[4]
        else:
            url=s[0]+str(_)+s[1]+str(_)+s[2]+str(_)+'0'+str(i)+s[3]+str(_)+'0'+str(i)+s[4]

        res=requests.get(url)
        re=url.split('/')[-1]
        print('suc'+str(url))
        with open(str(_)+'/'+re, 'wb') as f:
                f.write(res.content)


