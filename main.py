from unittest import result
import serial
import requests
import time
import re

# 串口
ser = serial.Serial(
    port='COM9',
    baudrate=9600,
    timeout=1
)

URL = "http://localhost:8085/data.json"


def find_sensor(node, name_keyword, unit):

    if isinstance(node, dict):

        text = node.get("Text", "")
        value = node.get("Value", "")

        if (
            name_keyword.lower() in text.lower()
            and unit in value
        ):
            return value

        for child in node.get("Children", []):

            result = find_sensor(
                child,
                name_keyword,
                unit
            )

            if result:
                return result

    return None


def get_number(text):

    if text is None:
        return "0"

    match = re.search(r'[\d.]+', text)

    if match:
        return match.group()

    return "0"


while True:


    try:
        # msg = "$ABC,DEF|123#"
        # print(list(msg.encode()))
        # ser.write(msg.encode())

        data = requests.get(
            URL,
            timeout=3
        ).json()

        # CPU
        cpu_temp = get_number(
            find_sensor(data, "CPU Package", "°C")
        )

        cpu_load = get_number(
            find_sensor(data, "CPU Total", "%")
        )

        # GPU
        gpu_temp = get_number(
            find_sensor(data, "GPU Core", "°C")
        )

        # gpu_load = get_number(
        #     find_sensor(data, "GPU Core", "%")
        # )

        # RAM
        ram_used = get_number(
            find_sensor(data, "Memory Used", "GB")
        )

        ram_load = get_number(
            find_sensor(data, "Memory", "%")
        )

        # # GPU显存
        # gpu_vram = get_number(
        #     find_sensor(data, "GPU Memory Used", "MB")
        # )
        #
        # # GPU功耗
        # gpu_power = get_number(
        #     find_sensor(data, "GPU Package", "W")
        # )

        # STM32通信格式
        msg = (
            f"${cpu_load},"
            f"{cpu_temp},"
            # f"{gpu_load},"
            f"{gpu_temp},"
            f"{ram_used},"
            f"{ram_load}#"
            # f"{gpu_vram},"
            # f"{gpu_power}#"
        )

        print("=" * 60)

        print(
            f"CPU : {cpu_load}%   {cpu_temp}°C"
        )

        print(
            f"GPU :  {gpu_temp}°C"
            # {gpu_load} %
        )

        print(
            f"RAM : {ram_used}GB   {ram_load}%"
        )

        # print(
        #     f"VRAM: {gpu_vram}MB"
        # )
        #
        # print(
        #     f"GPU Power: {gpu_power}W"
        # )

        print()

        print("发送数据:")
        print(msg)
        ser.write(msg.encode("utf-8"))
        # ser.write("$".encode())
        # ser.write(cpu_load.encode())
        # ser.write(cpu_temp.encode())
        # ser.write(gpu_load.encode())
        # ser.write(gpu_temp.encode())
        # ser.write("#".encode())
        time.sleep(1.5)

    except Exception as e:

        print("错误:", e)

        time.sleep(3)