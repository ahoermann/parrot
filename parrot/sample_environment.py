from caproto import ChannelData, ChannelType
from caproto.server import (AsyncLibraryLayer, PVGroup, SubGroup,
                            pvproperty, PvpropertyString,
                            PvpropertyInteger, PvpropertyDouble)
import datetime 


class Motors(PVGroup):
    """
    A group of PVs describing the sample stage motor positions
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    ysam = pvproperty(
        value=0.0,
        name="ysam",
        units="mm",
        doc="horizontal position of the sample stage"
        )

    zsam = pvproperty(
        value=0.0,
        name="zsam",
        units="mm",
        doc="vertical position of the sample stage"
        )

    zheavy = pvproperty(
        value=0.0,
        name="zheavy",
        units="mm",
        doc="vertical position of the sample stage for heavy load (GISAXS)"
        )

    yawgi = pvproperty(
        value=0.0,
        name="yawgi",
        units="degree",
        doc="yaw angle of the sample stage (GISAXS)"
        )

    rollgi = pvproperty(
        value=0.0,
        name="rollgi",
        units="degree",
        doc="roll angle of the sample stage (GISAXS)"
        )

    pitchgi = pvproperty(
        value=0.0,
        name="pitchgi",
        units="degree",
        doc="pitch angle of the sample stage (GISAXS)"
        )    
    
    
    
    



class SampleEnvironment(PVGroup):
    """
    A group of PVs regarding the sample environment, including sample
    stage positions.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    environment_temperature = pvproperty(
        value=0.0,
        name="environment_temperature",
        doc="Temperature of the environment in degrees Celsius, from portenta:t0",
        units="°C",
        )

    stage_temperature = pvproperty(
        value=1.0,
        name="stage_temperature",
        units="°C",
        doc="Sample stage temperature in degrees Celsius, from portenta:t1",
    )

    chamber_pressure = pvproperty(
        value=0.0,
        name="pressure",
        doc="pressure in the sample chamber (inficon)",
        units="mbar",
        dtype=PvpropertyDouble,
        )

    motors = SubGroup(Motors, prefix="motors:")

    
