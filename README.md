# **Automated robotic electrosynthesis platform based on Wi-eChem devices**
Automated control code for multi-channel electroscreening system
## **Install procedures**
1. Install LabvIEW 2020 (Only tested on 2020)
2. Install Python 3.7-3.11 (only tested on 3.7 and 3.11)
3. Put instr.lib folder from this repo to "...\National Instruments\LabVIEW 2020\instr.lib\" (... is where your LabVIEW is installed, unzip before using it)
4. Install the Python environment
5. Run "Wi-eChem-automation/main.lvproj" from this repo to access all the functions.

## **How to use**
1. Put the experimental parameters into user.xls 
2. Run "Wi-eChem-automation/Main.vi"
3. Select user.xls and the corresponding Python version
4. Set the device port, etc.
