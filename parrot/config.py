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

class HorizontalSlit(Slit):
    """
    A group of PVs describing the slit blades
    """
    left_blade = pvproperty(
        value=0.0,
        name="hl",
        doc="left blade position",
        )

    right_blade = pvproperty(
        value=0.0,
        name="hr",
        doc="left blade position",
        )
    
class VerticalSlit(Slit):
    """
    A group of PVs describing the slit blades
    """
    top_blade = pvproperty(
        value=0.0,
        name="top",
        doc="top blade position",
        )

    bottom_blade = pvproperty(
        value=0.0,
        name="bot",
        doc="bottom blade position",
        )

    
class Slits(PVGroup):
    """
    A group of PVs describing the positions of the slits 
    """
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    vertical1 = SubGroup(VerticalSlit, prefix="vertical1:")

    vertical2 = SubGroup(VerticalSlit, prefix="vertical2:")

    vertical3 = SubGroup(VerticalSlit, prefix="vertical3:")

    horizontal1 = SubGroup(HorizontalSlit, prefix="horizontal1:")

    horizontal2 = SubGroup(HorizontalSlit, prefix="horizontal2:")

    horizontal3 = SubGroup(HorizontalSlit, prefix="horizontal3:")


class Source(PVGroup):
    """
    A group of PVs describing source status (position and gap)
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    voltage = pvproperty(
        value=0.0,
        name="voltage",
        units="kV",
        doc="Voltage of the source."
    )

    current = pvproperty(
        value=0.35,
        name="current",
        units="mA",
        doc="Current of the source.",
    )

    shutter = pvproperty(
        enum_strings=("open", "closed", "unknown"),
        value="closed",
        name="shutter",
        string_encoding = "utf-8",
        doc="State of the safety shutter. One of 'open', 'closed', and 'unknown'.",
    )


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
    
    source_cu = SubGroup(Source, prefix="source_cu:")
    source_mo = SubGroup(Source, prefix="source_mo:")
    
    source = pvproperty(
        enum_strings=("source_cu", "source_mo", "unknown"),
        value="source_cu",
        name="source",
        doc="Source in use. Default: 'source_cu'. Value is one of 'source_cu', 'source_mo', and 'unknown'.",
        string_encoding = "utf-8",
    )

    dual = pvproperty(
        value=0.0,
        name="dual",
        dtype=PvpropertyDouble,
        units="mm",
        precision=2,  # check out motor specs
        doc="Position of the dual source translation stage.",
    )





