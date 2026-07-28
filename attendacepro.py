import cv2
import os ,csv
import face_recognition
import numpy as np
from datetime import datetime
from subprocess import call

images = []
classname = [] 
path = 'team'
mylist = os.listdir(path)


def run_database ():
    call(['python',"C:\\Users\\sarod\\coding material\\python\\pypr\\database.py"])

def findencoding(images):
    encodlist = []
    for img in images:
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if encode :
            encodlist.append(encode[0])
        else :
            print("NO face Detected in images.")

    return encodlist
 
def markattenance(name):  
    now = datetime.now()
    dtstring = now.strftime('%H:%M:%S')
    now_date = datetime.now()
    date = now.strftime('%Y-%m-%d')
    

    with open('Attendance.csv', 'r+') as f:
        csv_reader = csv.reader(f)
        next(csv_reader, None)

        for row in csv_reader:
            if row and len(row) >= 3 and row[0].strip() == name and row[2].strip() == date:
                print(f"Already marked for {name} at {dtstring} on {date} .")
                return
            
    


    
    with open('Attendance.csv', 'a', newline='') as f:
            
            if f.tell() == 0:
                f.write("Name,Time,Date\n")

            f.write(f"{name},{dtstring},{date}\n")
            print(f"Attendance marked for {name} at {dtstring} on {now_date}.")

            
for cl in mylist :
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classname.append(os.path.splitext(cl)[0])



encodelistkown = findencoding(images)
print( 'Encoding complete')


try:
    
    cap = cv2.VideoCapture(0)
    while True:
        success,img = cap.read()
        imgS = cv2.resize(img ,(0,0) ,None,0.25,0.25)
        imgS = cv2.cvtColor(imgS , cv2.COLOR_BGR2RGB)

        facescurframe = face_recognition.face_locations(imgS)
        encodecurframe = face_recognition.face_encodings(imgS , facescurframe)

        for encodeface,faceloc in zip(encodecurframe ,facescurframe) :
            matches = face_recognition.compare_faces(encodelistkown , encodeface)
            facedis = face_recognition.face_distance(encodelistkown , encodeface)
            
            matchind= np.argmin(facedis)

            if matches[matchind] :
                name = classname[matchind].upper()
                
                y1,x2,y2,x1 = faceloc
                y1,x2,y2,x1 = y1 * 4,x2 * 4,y2 * 4,x1 * 4
                cv2.rectangle(img ,(x1,y1),(x2,y2),(38, 159, 59),2)
                cv2.rectangle(img ,(x1,y2-35),(x2,y2),(38, 159, 59),cv2.FILLED)
                cv2.putText(img,name,(x1 + 6, y2 -6),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),1)
                markattenance(name)

        cv2.imshow('webcam',img)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
   

    run_database()
except Exception as e:
    print(f"An error occurred: {e}")


finally:
    cap.release()
    cv2.destroyAllWindows()
