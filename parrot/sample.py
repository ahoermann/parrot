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
        value=0,
        name="sampleid",
        )

    samplepos = pvproperty(
        value="",
        name="sampos",
        dtype=PvpropertyString,
        )

    matrixfraction = pvproperty(
        value=1.0,
        name="matrixfraction",
        )

    samplethickness = pvproperty(
        value=1e-4,
        name="samplethickness",
        )

    overall_mu = pvproperty(
        value=1.0,
        name="overall_mu",
        doc="X-ray absorption coefficient of the sample in 1/m",
        )
