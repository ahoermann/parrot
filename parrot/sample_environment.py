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
        
    temperature = pvproperty(
        value=0,
        name="temperature",
        doc="temperature of the sample",
        units="K",
        dtype=PvpropertyDouble,
        )

    chamber_pressure = pvproperty(
        value=0,
        name="pressure",
        doc="pressure in the sample chamber (inficon)",
        units="mbar",
        dtype=PvpropertyDouble,
        )

    motors = SubGroup(Motors, prefix="motors:")

    
