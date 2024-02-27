from caproto import ChannelData, ChannelType
from caproto.server import (AsyncLibraryLayer, PVGroup, SubGroup,
                            pvproperty, PvpropertyString, PvpropertyInteger,
                            PvpropertyDouble)
import datetime 



class BeamStop(PVGroup):
    """
    A group of PVs describing the beam stop status 
    """
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    bstop = pvproperty(
        value=True,
        name="present",
        doc="Bool: beam stop present or not",
        )

    bsr = pvproperty(
        value=260.,
        name="bsr",
        doc="Position of the rotational beam stop axis",
        )

    bsz = pvproperty(
        value=0.,
        name="bsz",
        doc="Position of the vertical beam stop axis",
        )
    
class Slit(PVGroup):
    """
    A group of PVs describing slit status (position and gap)
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    position = pvproperty(
        value=0.0,
        name="position",
        doc="slit position",
        )

    gap = pvproperty(
        value=0.35,
        name="gap",
        doc="slit gap width",
        )

class Slits(PVGroup):
    """
    A group of PVs describing the positions of the slits 
    """
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    slit1 = SubGroup(Slit, prefix="slit1:")

    slit2 = SubGroup(Slit, prefix="slit2:")

    slit3 = SubGroup(Slit, prefix="slit3:")
    

class Config(PVGroup):
    """
    A group of PVs regarding the instrument configuration (beam,
    beam stop, and detector).
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        

    config_id = pvproperty(
        value=110,
        name="config_id",
        dtype=PvpropertyInteger,
        )

    detx = pvproperty(
        value=0.0,
        name="detx",
        dtype=PvpropertyDouble,
        units="mm",
        precision=2,  # check out motor specs
        )

    dety = pvproperty(
        value=0.0,
        name="dety",
        dtype=PvpropertyDouble,        
        units="mm",
        precision=2,  # check out motor specs
        )

    detz = pvproperty(
        value=0.0,
        name="detz",
        dtype=PvpropertyDouble,
        units="mm",
        precision=2,  # check out motor specs
        )    

    beamstop = SubGroup(BeamStop, prefix="beamstop:")

    slits = SubGroup(Slits, prefix="slits:")
    

    

        




