import time
from pymodbus.client.sync import ModbusTcpClient
from django.core.management.base import BaseCommand
from main.models import (
    Skyd1Reading,
    Utility1st2ndFS2Reading,
    SpareStation3Reading,
    ThirdFloorZohoS4Reading,
    SixthFloorS5Reading,
    SpareS6Reading,
    SpareS7Reading,
    ThirdFifthFloorKotakReading,
    DG2S3Reading,
    EBS10Reading,
    APFCS11Reading,
    DG1S12Reading,
    SolarS13Reading
)
from django.utils import timezone
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

class Command(BaseCommand):
    help = 'Reads ModbusTCP data and stores it in Django models'

    def handle(self, *args, **kwargs):
        # Modbus server details
        server_ip = "192.168.1.21"
        port = 502

        # Data mapping
        data_mapping = [
            {"model": Skyd1Reading, "fields": [
                {"name": "ln_avg_voltage", "register": 0, "type": "float"},
                {"name": "rn_voltage", "register": 2, "type": "float"},
                {"name": "yn_voltage", "register": 4, "type": "float"},
                {"name": "bn_voltage", "register": 6, "type": "float"},
                {"name": "avg_current", "register": 8, "type": "float"},
                {"name": "r_current", "register": 10, "type": "float"},
                {"name": "y_current", "register": 12, "type": "float"},
                {"name": "b_current", "register": 14, "type": "float"},
                {"name": "hz", "register": 16, "type": "float"},
                {"name": "kwh_eb", "register": 18, "type": "float"},
                {"name": "kvah_eb", "register": 20, "type": "float"},
                {"name": "kwh_dg", "register": 22, "type": "float"},
                {"name": "kvah_dg", "register": 24, "type": "float"}
            ]},
            {"model": Utility1st2ndFS2Reading, "fields": [
                {"name": "ln_avg_voltage", "register": 26, "type": "float"},
                {"name": "rn_voltage", "register": 28, "type": "float"},
                {"name": "yn_voltage", "register": 30, "type": "float"},
                {"name": "bn_voltage", "register": 32, "type": "float"},
                {"name": "avg_current", "register": 34, "type": "float"},
                {"name": "r_current", "register": 36, "type": "float"},
                {"name": "y_current", "register": 38, "type": "float"},
                {"name": "b_current", "register": 40, "type": "float"},
                {"name": "hz", "register": 42, "type": "float"},
                {"name": "kwh_eb", "register": 650, "type": "float"},
                {"name": "kvah_eb", "register": 652, "type": "float"},
                {"name": "kwh_dg", "register": 48, "type": "float"},
                {"name": "kvah_dg", "register": 50, "type": "float"}
            ]},
            {"model": SpareStation3Reading, "fields": [
                {"name": "ln_avg_voltage", "register": 52, "type": "float"},
                {"name": "rn_voltage", "register": 54, "type": "float"},
                {"name": "yn_voltage", "register": 56, "type": "float"},
                {"name": "bn_voltage", "register": 58, "type": "float"},
                {"name": "avg_current", "register": 60, "type": "float"},
                {"name": "r_current", "register": 62, "type": "float"},
                {"name": "y_current", "register": 64, "type": "float"},
                {"name": "b_current", "register": 66, "type": "float"},
                {"name": "hz", "register": 68, "type": "float"},
                {"name": "kwh_eb", "register": 70, "type": "float"},
                {"name": "kvah_eb", "register": 72, "type": "float"},
                {"name": "kwh_dg", "register": 74, "type": "float"},
                {"name": "kvah_dg", "register": 76, "type": "float"}
            ]},
            {"model": ThirdFloorZohoS4Reading, "fields": [
                {"name": "ln_avg_voltage", "register": 78, "type": "float"},
                {"name": "rn_voltage", "register": 80, "type": "float"},
                {"name": "yn_voltage", "register": 82, "type": "float"},
                {"name": "bn_voltage", "register": 84, "type": "float"},
                {"name": "avg_current", "register": 86, "type": "float"},
                {"name": "r_current", "register": 88, "type": "float"},
                {"name": "y_current", "register": 90, "type": "float"},
                {"name": "b_current", "register": 92, "type": "float"},
                {"name": "hz", "register": 94, "type": "float"},
                {"name": "kwh_eb", "register": 96, "type": "float"},
                {"name": "kvah_eb", "register": 98, "type": "float"},
                {"name": "kwh_dg", "register": 100, "type": "float"},
                {"name": "kvah_dg", "register": 102, "type": "float"}
            ]},
            {"model": SixthFloorS5Reading, "fields": [
                {"name": "ln_avg_voltage", "register": 104, "type": "float"},
                {"name": "rn_voltage", "register": 106, "type": "float"},
                {"name": "yn_voltage", "register": 108, "type": "float"},
                {"name": "bn_voltage", "register": 110, "type": "float"},
                {"name": "avg_current", "register": 112, "type": "float"},
                {"name": "r_current", "register": 114, "type": "float"},
                {"name": "y_current", "register": 116, "type": "float"},
                {"name": "b_current", "register": 118, "type": "float"},
                {"name": "hz", "register": 120, "type": "float"},
                {"name": "kwh_eb", "register": 122, "type": "float"},
                {"name": "kvah_eb", "register": 124, "type": "float"},
                {"name": "kwh_dg", "register": 126, "type": "float"},
                {"name": "kvah_dg", "register": 128, "type": "float"}
            ]},
            {"model": SpareS6Reading, "fields": [
                {"name": "ln_avg_voltage", "register": 130, "type": "float"},
                {"name": "rn_voltage", "register": 132, "type": "float"},
                {"name": "yn_voltage", "register": 134, "type": "float"},
                {"name": "bn_voltage", "register": 136, "type": "float"},
                {"name": "avg_current", "register": 138, "type": "float"},
                {"name": "r_current", "register": 140, "type": "float"},
                {"name": "y_current", "register": 142, "type": "float"},
                {"name": "b_current", "register": 144, "type": "float"},
                {"name": "hz", "register": 146, "type": "float"},
                {"name": "kwh_eb", "register": 148, "type": "float"},
                {"name": "kvah_eb", "register": 150, "type": "float"},
                {"name": "kwh_dg", "register": 152, "type": "float"},
                {"name": "kvah_dg", "register": 154, "type": "float"}
            ]},
            {"model": SpareS7Reading, "fields": [
                {"name": "ln_avg_voltage", "register": 156, "type": "float"},
                {"name": "rn_voltage", "register": 158, "type": "float"},
                {"name": "yn_voltage", "register": 160, "type": "float"},
                {"name": "bn_voltage", "register": 162, "type": "float"},
                {"name": "avg_current", "register": 164, "type": "float"},
                {"name": "r_current", "register": 166, "type": "float"},
                {"name": "y_current", "register": 168, "type": "float"},
                {"name": "b_current", "register": 170, "type": "float"},
                {"name": "hz", "register": 172, "type": "float"},
                {"name": "kwh_eb", "register": 174, "type": "float"},
                {"name": "kvah_eb", "register": 176, "type": "float"},
                {"name": "kwh_dg", "register": 178, "type": "float"},
                {"name": "kvah_dg", "register": 180, "type": "float"}
            ]},
            {"model": ThirdFifthFloorKotakReading, "fields": [
                {"name": "ln_avg_voltage", "register": 182, "type": "float"},
                {"name": "rn_voltage", "register": 184, "type": "float"},
                {"name": "yn_voltage", "register": 186, "type": "float"},
                {"name": "bn_voltage", "register": 188, "type": "float"},
                {"name": "avg_current", "register": 190, "type": "float"},
                {"name": "r_current", "register": 192, "type": "float"},
                {"name": "y_current", "register": 194, "type": "float"},
                {"name": "b_current", "register": 196, "type": "float"},
                {"name": "hz", "register": 198, "type": "float"},
                {"name": "kwh_eb", "register": 654, "type": "float"},
                {"name": "kvah_eb", "register": 656, "type": "float"},
                {"name": "kwh_dg", "register": 658, "type": "float"},
                {"name": "kvah_dg", "register": 660, "type": "float"}
            ]},
            {"model": DG2S3Reading, "fields": [
                {"name": "phase_1_current", "register": 500, "type": "float"},
                {"name": "phase_2_current", "register": 502, "type": "float"},
                {"name": "phase_3_current", "register": 504, "type": "float"},
                {"name": "average_current", "register": 508, "type": "float"},
                {"name": "v1_voltage", "register": 510, "type": "float"},
                {"name": "v2_voltage", "register": 512, "type": "float"},
                {"name": "v3_voltage", "register": 514, "type": "float"},
                {"name": "ln_voltage", "register": 516, "type": "float"},
                {"name": "kwh", "register": 518, "type": "int"},
                {"name": "kvah", "register": 520, "type": "int"}
            ]},
            {"model": EBS10Reading, "fields": [
                {"name": "phase_1_current", "register": 522, "type": "float"},
                {"name": "phase_2_current", "register": 524, "type": "float"},
                {"name": "phase_3_current", "register": 526, "type": "float"},
                {"name": "average_current", "register": 530, "type": "float"},
                {"name": "v1_voltage", "register": 532, "type": "float"},
                {"name": "v2_voltage", "register": 534, "type": "float"},
                {"name": "v3_voltage", "register": 536, "type": "float"},
                {"name": "ln_voltage", "register": 538, "type": "float"},
                {"name": "kwh", "register": 540, "type": "int"},
                {"name": "kvah", "register": 542, "type": "int"}
            ]},
            {"model": APFCS11Reading, "fields": [
                {"name": "phase_1_current", "register": 544, "type": "float"},
                {"name": "phase_2_current", "register": 546, "type": "float"},
                {"name": "phase_3_current", "register": 548, "type": "float"},
                {"name": "average_current", "register": 552, "type": "float"},
                {"name": "v1_voltage", "register": 554, "type": "float"},
                {"name": "v2_voltage", "register": 556, "type": "float"},
                {"name": "v3_voltage", "register": 558, "type": "float"},
                {"name": "ln_voltage", "register": 560, "type": "float"},
                {"name": "kwh", "register": 562, "type": "int"},
                {"name": "kvah", "register": 564, "type": "int"}
            ]},
            {"model": DG1S12Reading, "fields": [
                {"name": "phase_1_current", "register": 566, "type": "float"},
                {"name": "phase_2_current", "register": 568, "type": "float"},
                {"name": "phase_3_current", "register": 570, "type": "float"},
                {"name": "average_current", "register": 574, "type": "float"},
                {"name": "v1_voltage", "register": 576, "type": "float"},
                {"name": "v2_voltage", "register": 578, "type": "float"},
                {"name": "v3_voltage", "register": 580, "type": "float"},
                {"name": "ln_voltage", "register": 582, "type": "float"},
                {"name": "kwh", "register": 584, "type": "int"},
                {"name": "kvah", "register": 586, "type": "int"}
            ]},
            {"model": SolarS13Reading, "fields": [
                {"name": "phase_1_current", "register": 587, "type": "float"},
                {"name": "phase_2_current", "register": 589, "type": "float"},
                {"name": "phase_3_current", "register": 591, "type": "float"},
                {"name": "average_current", "register": 595, "type": "float"},
                {"name": "v1_voltage", "register": 597, "type": "float"},
                {"name": "v2_voltage", "register": 599, "type": "float"},
                {"name": "v3_voltage", "register": 601, "type": "float"},
                {"name": "ln_voltage", "register": 603, "type": "float"},
                {"name": "kwh", "register": 605, "type": "int"},
                {"name": "kvah", "register": 607, "type": "int"}
            ]}
        ]

        def read_data(client, start_register, count):
            result = client.read_holding_registers(start_register, count)
            if not result.isError():
                return result.registers
            else:
                return None

        def decode_registers(registers, data_type):
            if data_type == "float":
                decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big, wordorder=Endian.Little)
                return decoder.decode_32bit_float()
            elif data_type == "int":
                decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big, wordorder=Endian.Little)
                return decoder.decode_32bit_int()
            return None

        # Create a ModbusTCP client
        client = ModbusTcpClient(server_ip, port=port)
        if not client.connect():
            print("Unable to connect to Modbus server")
            return

        while True:
            try:
                timestamp = timezone.now()

                for start_register in range(0, 1000, 125):  # Read registers in chunks of 125
                    registers = read_data(client, start_register, 125)
                    if registers is None:
                        continue

                    for mapping in data_mapping:
                        model = mapping["model"]
                        fields = mapping["fields"]
                        data = {"timestamp": timestamp, "sub_device_id": server_ip}

                        for field in fields:
                            register = field["register"]
                            data_type = field["type"]

                            if start_register <= register < start_register + 125:
                                start_index = register - start_register
                                field_registers = registers[start_index:start_index + 2]
                                data[field["name"]] = decode_registers(field_registers, data_type)

                        model.objects.create(**data)
                        print(f"Saved data for model {model.__name__} at {timestamp}")

                time.sleep(1)

            except Exception as e:
                print(f"Error reading Modbus data: {e}")

        client.close()
