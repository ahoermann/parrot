from caproto import ChannelData, ChannelType
from caproto.server import (PVGroup, SubGroup, pvproperty, PvpropertyString,
                            PvpropertyInteger)


#@define
class Sample(PVGroup):
    """
    A group of PVs regarding the sample. 
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        

    samplename = pvproperty(
        value="default sample",
        name="samplename",
        doc="Sample name as given by the user",
        string_encoding="utf-8",
        report_as_string=True,
        max_length=255
        )


    sampleowner = pvproperty(
        value="",
        name="owner",
        string_encoding="utf-8",
        report_as_string=True,
        max_length=255
        )

    proposal = pvproperty(
        value="",
        name="proposal",
        string_encoding="utf-8",
        report_as_string=True,
        max_length=255,
        )

    sampleid = pvproperty(
        value="",
        name="sampleid",
        dtype=PvpropertyString,
        )

    samplepos = pvproperty(
        value="",
        name="sampos",
        dtype=PvpropertyString,
        )
