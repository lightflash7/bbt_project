from io import BytesIO
from time import sleep
from picamera import PiCamera
from http_socket.http_client import send_photo


def capture_photo():
    # Create an in-memory stream
    my_stream = BytesIO()
    camera = PiCamera()
    camera.start_preview()
    # Camera warm-up time

    sleep(2)
    camera.capture(my_stream, 'jpeg')
    return my_stream


if __name__ == '__main__':
    the_stream = capture_photo()
    result_code, result_text = send_photo(the_stream)
    print(result_code, result_text)
