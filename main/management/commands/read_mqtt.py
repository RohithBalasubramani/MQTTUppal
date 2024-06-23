import os
import time
import json
import paho.mqtt.client as mqtt
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
from datetime import datetime

class Command(BaseCommand):
    help = 'Reads MQTT data and stores it in Django models'

    def handle(self, *args, **kwargs):
        # MQTT broker details
        broker = "broker.hivemq.com"
        port = 1883
        client_id = "asdas"  # Ensure this is unique for your client
        username = "admin"  # Public broker usually doesn't need this
        password = "admin"  # Public broker usually doesn't need this


        # Topics
        publish_topic = "SNEAPLuppalP"

        # Callback for connection
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected successfully")
                client.subscribe(publish_topic)
            else:
                print(f"Connection failed with return code {rc}")

        # Callback for receiving messages
        def on_message(client, userdata, msg):
            try:
                payload = json.loads(msg.payload.decode())
                data = payload["payload"][0]
                status = data["status"]
                timestamp = datetime.fromtimestamp(payload.get("time"))
                timestamp = timezone.make_aware(timestamp, timezone.get_default_timezone())


                # Create instances of each model with appropriate fields
                Skyd1Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("3F_SKYD1_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("3F_SKYD1_R-N_VOLTAGE"),
                    yn_voltage=status.get("3F_SKYD1_Y-N_VOLTAGE"),
                    bn_voltage=status.get("3F_SKYD1_B-N_VOLTAGE"),
                    avg_current=status.get("3F_SKYD1_AVG_CURRENT"),
                    r_current=status.get("3F_SKYD1_R-CURRENT"),
                    y_current=status.get("3F_SKYD1_Y-CURRENT"),
                    b_current=status.get("3F_SKYD1_B-CURRENT"),
                    hz=status.get("3F_SKYD1_HZ"),
                    kwh_eb=status.get("3F_SKYD1_KWH_EB"),
                    kvah_eb=status.get("3F_SKYD1_KVAH_EB"),
                    kwh_dg=status.get("3F_SKYD1_KWH_DG"),
                    kvah_dg=status.get("3F_SKYD1_KVAHDG")
                )

                Utility1st2ndFS2Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("Utility1st2ndF_S2_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("Utility1st2ndF_S2_R-N_VOLTAGE"),
                    yn_voltage=status.get("Utility1st2ndF_S2_Y-N_VOLTAGE"),
                    bn_voltage=status.get("Utility1st2ndF_S2_B-N_VOLTAGE"),
                    avg_current=status.get("Utility1st2ndF_S2_AVG_CURRENT"),
                    r_current=status.get("Utility1st2ndF_S2_R-CURRENT"),
                    y_current=status.get("Utility1st2ndF_S2_Y-CURRENT"),
                    b_current=status.get("Utility1st2ndF_S2_B-CURRENT"),
                    hz=status.get("Utility1st2ndF_S2_HZ"),
                    kwh_eb=status.get("Utility1st2ndF_S2_KWH_EB"),
                    kvah_eb=status.get("Utility1st2ndF_S2_KVAH_EB"),
                    kwh_dg=status.get("Utility1st2ndF_S2_KWH_DG"),
                    kvah_dg=status.get("Utility1st2ndF_S2_KVAHDG")
                )

                SpareStation3Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("Spare_Station3_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("Spare_Station3_R-N_VOLTAGE"),
                    yn_voltage=status.get("Spare_Station3_Y-N_VOLTAGE"),
                    bn_voltage=status.get("Spare_Station3_B-N_VOLTAGE"),
                    avg_current=status.get("Spare_Station3_AVG_CURRENT"),
                    r_current=status.get("Spare_Station3_R-CURRENT"),
                    y_current=status.get("Spare_Station3_Y-CURRENT"),
                    b_current=status.get("Spare_Station3_B-CURRENT"),
                    hz=status.get("Spare_Station3_HZ"),
                    kwh_eb=status.get("Spare_Station3_KWH_EB"),
                    kvah_eb=status.get("Spare_Station3_KVAH_EB"),
                    kwh_dg=status.get("Spare_Station3_KWH_DG"),
                    kvah_dg=status.get("Spare_Station3_KVAHDG")
                )

                ThirdFloorZohoS4Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("3rdFloor_Zoho_S4_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("3rdFloor_Zoho_S4_R-N_VOLTAGE"),
                    yn_voltage=status.get("3rdFloor_Zoho_S4_Y-N_VOLTAGE"),
                    bn_voltage=status.get("3rdFloor_Zoho_S4_B-N_VOLTAGE"),
                    avg_current=status.get("3rdFloor_Zoho_S4_AVG_CURRENT"),
                    r_current=status.get("3rdFloor_Zoho_S4_R-CURRENT"),
                    y_current=status.get("3rdFloor_Zoho_S4_Y-CURRENT"),
                    b_current=status.get("3rdFloor_Zoho_S4_B-CURRENT"),
                    hz=status.get("3rdFloor_Zoho_S4_HZ"),
                    kwh_eb=status.get("3rdFloor_Zoho_S4_KWH_EB"),
                    kvah_eb=status.get("3rdFloor_Zoho_S4_KVAH_EB"),
                    kwh_dg=status.get("3rdFloor_Zoho_S4_KWH_DG"),
                    kvah_dg=status.get("3rdFloor_Zoho_S4_KVAHDG")
                )

                SixthFloorS5Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("6thFloor_S5_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("6thFloor_S5_R-N_VOLTAGE"),
                    yn_voltage=status.get("6thFloor_S5_Y-N_VOLTAGE"),
                    bn_voltage=status.get("6thFloor_S5_B-N_VOLTAGE"),
                    avg_current=status.get("6thFloor_S5_AVG_CURRENT"),
                    r_current=status.get("6thFloor_S5_R-CURRENT"),
                    y_current=status.get("6thFloor_S5_Y-CURRENT"),
                    b_current=status.get("6thFloor_S5_B-CURRENT"),
                    hz=status.get("6thFloor_S5_HZ"),
                    kwh_eb=status.get("6thFloor_S5_KWH_EB"),
                    kvah_eb=status.get("6thFloor_S5_KVAH_EB"),
                    kwh_dg=status.get("6thFloor_S5_KWH_DG"),
                    kvah_dg=status.get("6thFloor_S5_KVAHDG")
                )

                SpareS6Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("Spare_S6_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("Spare_S6_R-N_VOLTAGE"),
                    yn_voltage=status.get("Spare_S6_Y-N_VOLTAGE"),
                    bn_voltage=status.get("Spare_S6_B-N_VOLTAGE"),
                    avg_current=status.get("Spare_S6_AVG_CURRENT"),
                    r_current=status.get("Spare_S6_R-CURRENT"),
                    y_current=status.get("Spare_S6_Y-CURRENT"),
                    b_current=status.get("Spare_S6_B-CURRENT"),
                    hz=status.get("Spare_S6_HZ"),
                    kwh_eb=status.get("Spare_S6_KWH_EB"),
                    kvah_eb=status.get("Spare_S6_KVAH_EB"),
                    kwh_dg=status.get("Spare_S6_KWH_DG"),
                    kvah_dg=status.get("Spare_S6_KVAHDG")
                )

                SpareS7Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("Spare_S7_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("Spare_S7_R-N_VOLTAGE"),
                    yn_voltage=status.get("Spare_S7_Y-N_VOLTAGE"),
                    bn_voltage=status.get("Spare_S7_B-N_VOLTAGE"),
                    avg_current=status.get("Spare_S7_AVG_CURRENT"),
                    r_current=status.get("Spare_S7_R-CURRENT"),
                    y_current=status.get("Spare_S7_Y-CURRENT"),
                    b_current=status.get("Spare_S7_B-CURRENT"),
                    hz=status.get("Spare_S7_HZ"),
                    kwh_eb=status.get("Spare_S7_KWH_EB"),
                    kvah_eb=status.get("Spare_S7_KVAH_EB"),
                    kwh_dg=status.get("Spare_S7_KWH_DG"),
                    kvah_dg=status.get("Spare_S7_KVAHDG")
                )

                ThirdFifthFloorKotakReading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    ln_avg_voltage=status.get("3rd5thFloor_Kotak_L-N_AVG_VOLTAGE"),
                    rn_voltage=status.get("3rd5thFloor_Kotak_R-N_VOLTAGE"),
                    yn_voltage=status.get("3rd5thFloor_Kotak_Y-N_VOLTAGE"),
                    bn_voltage=status.get("3rd5thFloor_Kotak_B-N_VOLTAGE"),
                    avg_current=status.get("3rd5thFloor_Kotak_AVG_CURRENT"),
                    r_current=status.get("3rd5thFloor_Kotak_R-CURRENT"),
                    y_current=status.get("3rd5thFloor_Kotak_Y-CURRENT"),
                    b_current=status.get("3rd5thFloor_Kotak_B-CURRENT"),
                    hz=status.get("3rd5thFloor_Kotak_HZ"),
                    kwh_eb=status.get("3rd5thFloor_Kotak_KWH_EB"),
                    kvah_eb=status.get("3rd5thFloor_Kotak_KVAH_EB"),
                    kwh_dg=status.get("3rd5thFloor_Kotak_KWH_DG"),
                    kvah_dg=status.get("3rd5thFloor_Kotak_KVAHDG")
                )

                DG2S3Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    phase_1_current=status.get("DG2_S3_PHASE-1_CURRENT"),
                    phase_2_current=status.get("DG2_S3_PHASE-2_CURRENT"),
                    phase_3_current=status.get("DG2_S3_PHASE-3_CURRENT"),
                    average_current=status.get("DG2_S3_AVERAGE_CURRENT"),
                    v1_voltage=status.get("DG2_S3_V1_VOLTAGE"),
                    v2_voltage=status.get("DG2_S3_V2_VOLTAGE"),
                    v3_voltage=status.get("DG2_S3_V3_VOLTAGE"),
                    ln_voltage=status.get("DG2_S3_L-N_VOLTAGE"),
                    kwh=status.get("DG2_S3_KWH"),
                    kvah=status.get("DG2_S3_KVAH")
                )

                EBS10Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    phase_1_current=status.get("EB_S10_PHASE-1_CURRENT"),
                    phase_2_current=status.get("EB_S10_PHASE-2_CURRENT"),
                    phase_3_current=status.get("EB_S10_PHASE-3_CURRENT"),
                    average_current=status.get("EB_S10_AVERAGE_CURRENT"),
                    v1_voltage=status.get("EB_S10_V1_VOLTAGE"),
                    v2_voltage=status.get("EB_S10_V2_VOLTAGE"),
                    v3_voltage=status.get("EB_S10_V3_VOLTAGE"),
                    ln_voltage=status.get("EB_S10_L-N_VOLTAGE"),
                    kwh=status.get("EB_S10_KWH"),
                    kvah=status.get("EB_S10_KVAH")
                )

                APFCS11Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    phase_1_current=status.get("APFC_S11_PHASE-1_CURRENT"),
                    phase_2_current=status.get("APFC_S11_PHASE-2_CURRENT"),
                    phase_3_current=status.get("APFC_S11_PHASE-3_CURRENT"),
                    average_current=status.get("APFC_S11_AVERAGE_CURRENT"),
                    v1_voltage=status.get("APFC_S11_V1_VOLTAGE"),
                    v2_voltage=status.get("APFC_S11_V2_VOLTAGE"),
                    v3_voltage=status.get("APFC_S11_V3_VOLTAGE"),
                    ln_voltage=status.get("APFC_S11_L-N_VOLTAGE"),
                    kwh=status.get("APFC_S11_KWH"),
                    kvah=status.get("APFC_S11_KVAH")
                )

                DG1S12Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    phase_1_current=status.get("DG1_S12_PHASE-1_CURRENT"),
                    phase_2_current=status.get("DG1_S12_PHASE-2_CURRENT"),
                    phase_3_current=status.get("DG1_S12_PHASE-3_CURRENT"),
                    average_current=status.get("DG1_S12_AVERAGE_CURRENT"),
                    v1_voltage=status.get("DG1_S12_V1_VOLTAGE"),
                    v2_voltage=status.get("DG1_S12_V2_VOLTAGE"),
                    v3_voltage=status.get("DG1_S12_V3_VOLTAGE"),
                    ln_voltage=status.get("DG1_S12_L-N_VOLTAGE"),
                    kwh=status.get("DG1_S12_KWH"),
                    kvah=status.get("DG1_S12_KVAH")
                )

                SolarS13Reading.objects.create(
                    timestamp=timestamp,
                    sub_device_id=data.get("subDeviceId"),
                    phase_1_current=status.get("Solar_S13_PHASE-1_CURRENT"),
                    phase_2_current=status.get("Solar_S13_PHASE-2_CURRENT"),
                    phase_3_current=status.get("Solar_S13_PHASE-3_CURRENT"),
                    average_current=status.get("Solar_S13_AVERAGE_CURRENT"),
                    v1_voltage=status.get("Solar_S13_V1_VOLTAGE"),
                    v2_voltage=status.get("Solar_S13_V2_VOLTAGE"),
                    v3_voltage=status.get("Solar_S13_V3_VOLTAGE"),
                    ln_voltage=status.get("Solar_S13_L-N_VOLTAGE"),
                    kwh=status.get("Solar_S13_KWH"),
                    kvah=status.get("Solar_S13_KVAH")
                )

                print(f"Saved values at {timestamp}")
            except Exception as e:
                print(f"Error processing message: {e}")

        # Setup MQTT client
        client = mqtt.Client(client_id=client_id)
        client.on_connect = on_connect
        client.on_message = on_message

        # Optional: Set username and password for the broker if required
        # client.username_pw_set(username, password)

        # Connect to the broker
        client.connect(broker, port, 60)

        # Start the loop to process callbacks and handle reconnections
        client.loop_start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            client.loop_stop()
            client.disconnect()
            print("Disconnected from MQTT broker")
