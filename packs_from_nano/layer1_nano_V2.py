# 增加登记模式
import cv2
import face.liveness as live
import time
from face.FWI_V2_nano import *
import finger.as608_combo_lib as as608
from finger.finger_nano import *


class layer1():
    def __init__(self):
        self.session = as608.connect_serial_session('/dev/ttyUSB0')
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        with open('/home/jetson/Desktop/layer-1_nano/face/name.txt', 'r+', encoding='utf-8') as source_file:
            lines = source_file.readlines()
            self.face_num = ['/home/jetson/Desktop/layer-1_nano/face/database/person{}.jpg'.format(i+1) for i in range(len(lines))]
            self.face_name = [line.strip() for line in lines]
            self.face_recognizer = FaceRecognizer()
            self.mode = 1

    def run(self, mode):
        # mode=1:带活体检测的人脸识别
        # mode=2:指纹识别
        # mode=3:人脸登记
        # mode=4:指纹登记
        if mode == 1 or mode == 3:
            self.face_recognizer.load_known_faces(self.face_num, self.face_name)
            start_time = 0
            mark1 = 0
            mark2 = 0
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    continue
                mark0 = self.face_recognizer.detect_faces(frame)
                _, shot = cv2.imencode('.jpg', frame)

                if mark0==1:
                    if mark1 == 0:
                        start_time = time.time()
                        mark1 = 1
                    else:
                        if mark2 == 1:
                            mark1 = 0
                            mark2 = 0
                            continue
                        sustain_time = time.time() - start_time
                        cv2.putText(frame, f"{int(4 - (time.time() - start_time))}", (frame.shape[1]-100, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
                        if sustain_time >= 3:
                            
                            if mode == 3:
                                # 保存图片至./database
                                cv2.imwrite(f'/home/jetson/Desktop/layer-1_nano/face/database/person{len(self.face_num)+1}.jpg', frame)
                                # 在name.txt新增一行人物姓名：test
                                with open('/home/jetson/Desktop/layer-1_nano/face/name.txt', 'a+', encoding='utf-8') as source_file:
                                    source_file.write('test\n')                       
                                return shot
                            
                            elif mode == 1:
                                if not live.face_api_invoke(shot):
                                    print("Fake face detected!")
                                    # break
                                else:
                                    print("Real face detected!")

                                    frame, final_result = self.face_recognizer.recognize_faces(frame)
                                    while final_result is None:
                                        frame, final_result = self.face_recognizer.recognize_faces(frame)
                                    if final_result == "Unknown":
                                        print("No registration!")
                                    else:
                                        print(f"Registerd successfully: {final_result}")
                        
                            break

                elif mark0==2:
                    mark2 = 1

                elif mark0==0:
                    mark2 = 1

                cv2.imshow('face', frame)
                if cv2.waitKey(1)==ord('q'):
                    break

        elif mode == 2 or mode == 4:
            if self.session:
                # 指纹登记模式
                if mode == 4:
                    as608.enroll_finger_to_device(self.session, as608,"lhr")
                    print("Registration completed!")

                # 指纹识别模式
                elif mode == 2:
                    as608.search_fingerprint_on_device(self.session, as608)

                    data = self.session.get_fpdata(sensorbuffer="image")
                    image_array = convert_4bit_to_8bit(data, 256, 288)
                    cv2.imshow('finger', image_array)

                # elif session.get_image() == as608.NOFINGER:
                #     print(".", end="", flush=True)
            else:
                print("AS608 connection error!")
    
    def off(self):
        self.cap.release()
        cv2.destroyAllWindows()    
        self.session.close_uart()

def main():
    mode = 3
    system = layer1()
    system.run(mode)
    system.off()

if __name__ == "__main__":
    main()