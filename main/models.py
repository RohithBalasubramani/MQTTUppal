from django.db import models

class BaseModel(models.Model):
    timestamp = models.DateTimeField()
    sub_device_id = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Skyd1Reading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class Utility1st2ndFS2Reading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class SpareStation3Reading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class ThirdFloorZohoS4Reading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class SixthFloorS5Reading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class SpareS6Reading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class SpareS7Reading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class ThirdFifthFloorKotakReading(BaseModel):
    ln_avg_voltage = models.FloatField(null=True, blank=True)
    rn_voltage = models.FloatField(null=True, blank=True)
    yn_voltage = models.FloatField(null=True, blank=True)
    bn_voltage = models.FloatField(null=True, blank=True)
    avg_current = models.FloatField(null=True, blank=True)
    r_current = models.FloatField(null=True, blank=True)
    y_current = models.FloatField(null=True, blank=True)
    b_current = models.FloatField(null=True, blank=True)
    hz = models.FloatField(null=True, blank=True)
    kwh_eb = models.FloatField(null=True, blank=True)
    kvah_eb = models.FloatField(null=True, blank=True)
    kwh_dg = models.FloatField(null=True, blank=True)
    kvah_dg = models.FloatField(null=True, blank=True)


class DG2S3Reading(BaseModel):
    phase_1_current = models.FloatField(null=True, blank=True)
    phase_2_current = models.FloatField(null=True, blank=True)
    phase_3_current = models.FloatField(null=True, blank=True)
    average_current = models.FloatField(null=True, blank=True)
    v1_voltage = models.FloatField(null=True, blank=True)
    v2_voltage = models.FloatField(null=True, blank=True)
    v3_voltage = models.FloatField(null=True, blank=True)
    ln_voltage = models.FloatField(null=True, blank=True)
    kwh = models.FloatField(null=True, blank=True)
    kvah = models.FloatField(null=True, blank=True)


class EBS10Reading(BaseModel):
    phase_1_current = models.FloatField(null=True, blank=True)
    phase_2_current = models.FloatField(null=True, blank=True)
    phase_3_current = models.FloatField(null=True, blank=True)
    average_current = models.FloatField(null=True, blank=True)
    v1_voltage = models.FloatField(null=True, blank=True)
    v2_voltage = models.FloatField(null=True, blank=True)
    v3_voltage = models.FloatField(null=True, blank=True)
    ln_voltage = models.FloatField(null=True, blank=True)
    kwh = models.FloatField(null=True, blank=True)
    kvah = models.FloatField(null=True, blank=True)


class APFCS11Reading(BaseModel):
    phase_1_current = models.FloatField(null=True, blank=True)
    phase_2_current = models.FloatField(null=True, blank=True)
    phase_3_current = models.FloatField(null=True, blank=True)
    average_current = models.FloatField(null=True, blank=True)
    v1_voltage = models.FloatField(null=True, blank=True)
    v2_voltage = models.FloatField(null=True, blank=True)
    v3_voltage = models.FloatField(null=True, blank=True)
    ln_voltage = models.FloatField(null=True, blank=True)
    kwh = models.FloatField(null=True, blank=True)
    kvah = models.FloatField(null=True, blank=True)


class DG1S12Reading(BaseModel):
    phase_1_current = models.FloatField(null=True, blank=True)
    phase_2_current = models.FloatField(null=True, blank=True)
    phase_3_current = models.FloatField(null=True, blank=True)
    average_current = models.FloatField(null=True, blank=True)
    v1_voltage = models.FloatField(null=True, blank=True)
    v2_voltage = models.FloatField(null=True, blank=True)
    v3_voltage = models.FloatField(null=True, blank=True)
    ln_voltage = models.FloatField(null=True, blank=True)
    kwh = models.FloatField(null=True, blank=True)
    kvah = models.FloatField(null=True, blank=True)


class SolarS13Reading(BaseModel):
    phase_1_current = models.FloatField(null=True, blank=True)
    phase_2_current = models.FloatField(null=True, blank=True)
    phase_3_current = models.FloatField(null=True, blank=True)
    average_current = models.FloatField(null=True, blank=True)
    v1_voltage = models.FloatField(null=True, blank=True)
    v2_voltage = models.FloatField(null=True, blank=True)
    v3_voltage = models.FloatField(null=True, blank=True)
    ln_voltage = models.FloatField(null=True, blank=True)
    kwh = models.FloatField(null=True, blank=True)
    kvah = models.FloatField(null=True, blank=True)
