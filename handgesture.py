import cv2
from djitellopy import tello
import threading
import motion


class Tello1:
    def __init__(self):
        self.me = tello.Tello()
        self.me.connect()
        self.me.streamon()
        self.me.takeoff()
        print(self.me.get_battery())

        self.motion_data_thread = threading.Thread(target=self.process_motion_data)
        self.motion_data_thread.start()

    def process_motion_data(self):
        try:
            while True:
                frame_read = self.me.get_frame_read()
                frame = frame_read.frame

                # 손 모션 감지 및 분석 (motion 모듈 사용)
                motion_data = motion.motion_set(frame)  # motion_set 함수를 사용하여 손 모션 분석

                # 드론 제어 (이 예시에서는 motion_data에 따라 드론을 움직임)
                self.me.send_rc_control(motion_data[0], motion_data[1], motion_data[2], motion_data[3])
                cv2.imshow('Tello Video Stream', frame)

                if cv2.waitKey(1) == ord('q'):
                    self.me.land()
                    break

        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == "__main__":
    tello1 = Tello1()
