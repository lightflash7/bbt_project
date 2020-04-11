import aiohttp
import asyncio
import io

ip_addr = "127.0.0.1"
remote_port = "8086"
mp_url_path = "/mp"
full_url = "http://" + ip_addr + ":" + remote_port + mp_url_path


async def request_http(data):
    async with aiohttp.ClientSession() as session:  # open a session
        with aiohttp.MultipartWriter() as mpwriter:  # make a multipart writer
            print("包裝 multipart 中：二進位")
            part = mpwriter.append(data)  # add a part include the photo data
            # part.set_content_disposition('binary')
            part.headers[aiohttp.hdrs.CONTENT_TYPE] = 'binary'
            print("包裝 multipart 中：字串")
            # mpwriter.append("the local size is " + str(len(data)))
            # use the default content type plain/text
            print("送出 multipart 中，，，")
            async with session.post(full_url, data=mpwriter) as resp:
                print("收取結果中，，，")
                code = resp.status
                result = await resp.text()
                return code, result


# def read_file():  # 輸入檔案路徑，將檔案存入記憶體，返回位元組數組
#     filename = input('copy your file uri here: ')
#     filename = filename.replace('\"','',2)
#     try:
#         file_handle = open(filename, 'br')
#     except Exception as esu:  # 嘗試二進位打開檔案
#         print(esu)
#         return None
#     finally:
#         data_read = bytearray(file_handle.read())
#         file_handle.close()
#         return data_read


def send_photo(file_stream):
    file_stream.seek(0)
    loop = asyncio.get_event_loop()
    result_code, result_text = loop.run_until_complete(request_http(file_stream))
    return result_code, result_text


if __name__ == '__main__':
    data = read_file()
    # print(len(data))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(request_http(data))
