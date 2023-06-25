<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="20008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="main.vi" Type="VI" URL="../main.vi"/>
		<Item Name="power_supply_server_2.vi" Type="VI" URL="../subvi/power_supply/power_supply_server_2.vi"/>
		<Item Name="public_device_occupy.vi" Type="VI" URL="../subvi/publi_device_occupy/public_device_occupy.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="instr.lib" Type="Folder">
				<Item Name="GPD-3303.lvlib" Type="Library" URL="/&lt;instrlib&gt;/GPD-3303/GPD-3303.lvlib"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="API Main.lvlib" Type="Library" URL="/&lt;vilib&gt;/NI/Modbus Library/API/Wrapper/API Main.lvlib"/>
				<Item Name="ASCII Data Unit.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Transmission Data Unit/ASCII/ASCII Data Unit.lvclass"/>
				<Item Name="Bits to Bytes.vi" Type="VI" URL="/&lt;vilib&gt;/NI/Modbus Library/Utility/Bits to Bytes.vi"/>
				<Item Name="Bytes to Bits.vi" Type="VI" URL="/&lt;vilib&gt;/NI/Modbus Library/Utility/Bytes to Bits.vi"/>
				<Item Name="Bytes to U16s.vi" Type="VI" URL="/&lt;vilib&gt;/NI/Modbus Library/Utility/Bytes to U16s.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Device Data Model.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Data Model/Device Data Model.lvclass"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Generate UUID.vi" Type="VI" URL="/&lt;vilib&gt;/NI/Modbus Library/Utility/Generate UUID.vi"/>
				<Item Name="IP Data Unit.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Transmission Data Unit/IP/IP Data Unit.lvclass"/>
				<Item Name="Master Function Definition.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Master Function Definition/Master Function Definition.lvclass"/>
				<Item Name="Modbus API.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/API/Modbus API.lvclass"/>
				<Item Name="Modbus Data Unit.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Modbus Data Unit/Modbus Data Unit.lvclass"/>
				<Item Name="Modbus Master.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/API/Master/Modbus Master.lvclass"/>
				<Item Name="Modbus Slave.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/API/Slave/Modbus Slave.lvclass"/>
				<Item Name="Network Master.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Network Master/Network Master.lvclass"/>
				<Item Name="Network Protocol.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Network Protocol.lvclass"/>
				<Item Name="Network Slave.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Network Slave/Network Slave.lvclass"/>
				<Item Name="RTU Data Unit.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Transmission Data Unit/RTU/RTU Data Unit.lvclass"/>
				<Item Name="Serial Data Unit.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Transmission Data Unit/Serial Interface/Serial Data Unit.lvclass"/>
				<Item Name="Serial Master.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Network Master/Serial/Serial Master.lvclass"/>
				<Item Name="Serial Shared Components.lvlib" Type="Library" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Serial Shared Components/Serial Shared Components.lvlib"/>
				<Item Name="Serial Slave.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Network Slave/Serial/Serial Slave.lvclass"/>
				<Item Name="Standard Data Model.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Data Model/Standard Data Model/Standard Data Model.lvclass"/>
				<Item Name="TCP Master.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Network Master/TCP/TCP Master.lvclass"/>
				<Item Name="TCP Shared Components.lvlib" Type="Library" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/TCP Shared Components/TCP Shared Components.lvlib"/>
				<Item Name="TCP Slave.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Network Protocol/Network Slave/TCP/TCP Slave.lvclass"/>
				<Item Name="Transmission Data Unit.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/NI/Modbus Library/Transmission Data Unit/Transmission Data Unit.lvclass"/>
				<Item Name="U16s to Bytes.vi" Type="VI" URL="/&lt;vilib&gt;/NI/Modbus Library/Utility/U16s to Bytes.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="VISA Flush IO Buffer Mask.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Flush IO Buffer Mask.ctl"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
			</Item>
			<Item Name="choose worker.vi" Type="VI" URL="../subvi/choose worker.vi"/>
			<Item Name="device log.vi" Type="VI" URL="../subvi/device log.vi"/>
			<Item Name="emergency stop.vi" Type="VI" URL="../subvi/status/emergency stop.vi"/>
			<Item Name="experiment_No.vi" Type="VI" URL="../subvi/status/experiment_No.vi"/>
			<Item Name="ExperimentNo.vi" Type="VI" URL="../subvi/API/experiment_No/ExperimentNo.vi"/>
			<Item Name="filter_vial_No.vi" Type="VI" URL="../subvi/status/filter_vial_No.vi"/>
			<Item Name="item name.vi" Type="VI" URL="../subvi/status/item name.vi"/>
			<Item Name="item name2.vi" Type="VI" URL="../subvi/status/item name2.vi"/>
			<Item Name="motor_all_shut_down.vi" Type="VI" URL="../subvi/motor/subvi/motor_all_shut_down.vi"/>
			<Item Name="motor_block1.vi" Type="VI" URL="../subvi/motor/subvi/motor_block1.vi"/>
			<Item Name="motor_block2.vi" Type="VI" URL="../subvi/motor/subvi/motor_block2.vi"/>
			<Item Name="motor_block3.vi" Type="VI" URL="../subvi/motor/subvi/motor_block3.vi"/>
			<Item Name="motor_choose_step.vi" Type="VI" URL="../subvi/motor/motor_choose_step.vi"/>
			<Item Name="motor_server.vi" Type="VI" URL="../subvi/motor/motor_server.vi"/>
			<Item Name="NoAndStatus.vi" Type="VI" URL="../subvi/API/write_No_status/NoAndStatus.vi"/>
			<Item Name="pause1.vi" Type="VI" URL="../subvi/status/pause1.vi"/>
			<Item Name="pause2.vi" Type="VI" URL="../subvi/status/pause2.vi"/>
			<Item Name="pause3.vi" Type="VI" URL="../subvi/status/pause3.vi"/>
			<Item Name="pause4.vi" Type="VI" URL="../subvi/status/pause4.vi"/>
			<Item Name="power_supply_choose_step.vi" Type="VI" URL="../subvi/power_supply/power_supply_choose_step.vi"/>
			<Item Name="power_supply_choose_step_2.vi" Type="VI" URL="../subvi/power_supply/power_supply_choose_step_2.vi"/>
			<Item Name="power_supply_main.vi" Type="VI" URL="../subvi/power_supply/subvi/power_supply_main.vi"/>
			<Item Name="power_supply_server_1.vi" Type="VI" URL="../subvi/power_supply/power_supply_server_1.vi"/>
			<Item Name="public_device_list.vi" Type="VI" URL="../subvi/status/public_device_list.vi"/>
			<Item Name="public_device_occupy_choose_step.vi" Type="VI" URL="../subvi/publi_device_occupy/public_device_occupy_choose_step.vi"/>
			<Item Name="public_device_occupy_server.vi" Type="VI" URL="../subvi/publi_device_occupy/public_device_occupy_server.vi"/>
			<Item Name="public_device_unoccupy_choose_step.vi" Type="VI" URL="../subvi/public_device_unoccupy/public_device_unoccupy_choose_step.vi"/>
			<Item Name="pump_choose_step.vi" Type="VI" URL="../subvi/pump/pump_choose_step.vi"/>
			<Item Name="pump_close.vi" Type="VI" URL="../subvi/pump/subvi/pump_close.vi"/>
			<Item Name="pump_initial.vi" Type="VI" URL="../subvi/pump/subvi/pump_initial.vi"/>
			<Item Name="pump_main.vi" Type="VI" URL="../subvi/pump/subvi/pump_main.vi"/>
			<Item Name="pump_server.vi" Type="VI" URL="../subvi/pump/pump_server.vi"/>
			<Item Name="relay_block1.vi" Type="VI" URL="../subvi/relay/subvi/relay_block1.vi"/>
			<Item Name="relay_block2.vi" Type="VI" URL="../subvi/relay/subvi/relay_block2.vi"/>
			<Item Name="relay_block3.vi" Type="VI" URL="../subvi/relay/subvi/relay_block3.vi"/>
			<Item Name="relay_choose_step.vi" Type="VI" URL="../subvi/relay/relay_choose_step.vi"/>
			<Item Name="relay_close.vi" Type="VI" URL="../subvi/relay/subvi/relay_close.vi"/>
			<Item Name="relay_initial.vi" Type="VI" URL="../subvi/relay/subvi/relay_initial.vi"/>
			<Item Name="relay_server.vi" Type="VI" URL="../subvi/relay/relay_server.vi"/>
			<Item Name="robot change attitude.vi" Type="VI" URL="../subvi/robot/subvi/Robot-HL/small_scara_interface/VIs/robot change attitude.vi"/>
			<Item Name="robot check done.vi" Type="VI" URL="../subvi/robot/subvi/Robot-HL/small_scara_interface/VIs/robot check done.vi"/>
			<Item Name="robot set efg state.vi" Type="VI" URL="../subvi/robot/subvi/Robot-HL/small_scara_interface/VIs/robot set efg state.vi"/>
			<Item Name="robot_choose_step.vi" Type="VI" URL="../subvi/robot/robot_choose_step.vi"/>
			<Item Name="robot_efg_choose_step.vi" Type="VI" URL="../subvi/robot_efg/robot_efg_choose_step.vi"/>
			<Item Name="robot_efg_server.vi" Type="VI" URL="../subvi/robot_efg/robot_efg_server.vi"/>
			<Item Name="robot_initial.vi" Type="VI" URL="../subvi/robot/subvi/robot_initial.vi"/>
			<Item Name="robot_main.vi" Type="VI" URL="../subvi/robot/subvi/robot_main.vi"/>
			<Item Name="robot_server.vi" Type="VI" URL="../subvi/robot/robot_server.vi"/>
			<Item Name="small_scara_interface.dll" Type="Document" URL="../subvi/robot/subvi/Robot-HL/small_scara_interface/small_scara_interface.dll"/>
			<Item Name="small_scara_interface.lvlib" Type="Library" URL="../subvi/robot/subvi/Robot-HL/small_scara_interface/small_scara_interface.lvlib"/>
			<Item Name="status of power_supply1.vi" Type="VI" URL="../subvi/status/status of power_supply1.vi"/>
			<Item Name="status of power_supply2.vi" Type="VI" URL="../subvi/status/status of power_supply2.vi"/>
			<Item Name="status of power_supply3.vi" Type="VI" URL="../subvi/status/status of power_supply3.vi"/>
			<Item Name="status of power_supply4.vi" Type="VI" URL="../subvi/status/status of power_supply4.vi"/>
			<Item Name="status of pump.vi" Type="VI" URL="../subvi/status/status of pump.vi"/>
			<Item Name="status of relay.vi" Type="VI" URL="../subvi/status/status of relay.vi"/>
			<Item Name="status of robot.vi" Type="VI" URL="../subvi/status/status of robot.vi"/>
			<Item Name="status of worker1.vi" Type="VI" URL="../subvi/status/status of worker1.vi"/>
			<Item Name="status of worker2.vi" Type="VI" URL="../subvi/status/status of worker2.vi"/>
			<Item Name="status of worker3.vi" Type="VI" URL="../subvi/status/status of worker3.vi"/>
			<Item Name="status of worker4.vi" Type="VI" URL="../subvi/status/status of worker4.vi"/>
			<Item Name="stop software.vi" Type="VI" URL="../subvi/status/stop software.vi"/>
			<Item Name="time1.vi" Type="VI" URL="../subvi/status/time1.vi"/>
			<Item Name="time2.vi" Type="VI" URL="../subvi/status/time2.vi"/>
			<Item Name="time3.vi" Type="VI" URL="../subvi/status/time3.vi"/>
			<Item Name="time4.vi" Type="VI" URL="../subvi/status/time4.vi"/>
			<Item Name="wait1.vi" Type="VI" URL="../subvi/wait/wait1.vi"/>
			<Item Name="wait2.vi" Type="VI" URL="../subvi/wait/wait2.vi"/>
			<Item Name="wait3.vi" Type="VI" URL="../subvi/wait/wait3.vi"/>
			<Item Name="wait4.vi" Type="VI" URL="../subvi/wait/wait4.vi"/>
			<Item Name="worker1.vi" Type="VI" URL="../subvi/worker1.vi"/>
			<Item Name="worker2.vi" Type="VI" URL="../subvi/worker2.vi"/>
			<Item Name="worker3.vi" Type="VI" URL="../subvi/worker3.vi"/>
			<Item Name="worker4.vi" Type="VI" URL="../subvi/worker4.vi"/>
			<Item Name="xlsx_to_JSON.vi" Type="VI" URL="../subvi/API/JSON/xlsx_to_JSON.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
