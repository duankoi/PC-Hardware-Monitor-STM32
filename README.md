# PC Hardware Monitor for STM32

A real-time PC hardware monitoring system based on **Python** and **STM32**.

The project reads hardware information (CPU, GPU, and RAM) from a Windows PC using **LibreHardwareMonitor**, parses the JSON data through an HTTP interface, and transmits the processed data to an STM32 microcontroller via UART. The STM32 receives, parses, and displays the information on an OLED screen in real time.

## Features

* Real-time CPU usage and temperature monitoring
* Real-time GPU usage and temperature monitoring
* Real-time RAM usage monitoring
* JSON data parsing
* UART communication between PC and STM32
* Custom serial communication protocol (`$...#`)
* STM32 interrupt-based UART reception
* OLED real-time display

## Technologies

* STM32F103C8T6
* Python
* PySerial
* Requests
* LibreHardwareMonitor
* UART Communication
* JSON Parsing
* SSD1306 OLED

## Project Structure

```
PC-Hardware-Monitor
├── Python/        # PC-side data acquisition and UART transmission
├── STM32/         # STM32 firmware
├── Docs/          # Project documentation
└── Images/        # Demo images and wiring diagrams
```

## Future Improvements

* Add GPU VRAM monitoring
* Fan speed monitoring
* LVGL graphical interface
* ESP32 Wi-Fi transmission
* Desktop executable (.exe)
* TFT LCD support
