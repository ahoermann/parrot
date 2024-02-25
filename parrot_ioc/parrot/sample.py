from caproto import ChannelData, ChannelType
from caproto.server import (PVGroup, SubGroup, pvproperty, PvpropertyString)


#@define
class Sample(PVGroup):
    """
    A group of PVs regarding the sample. 
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        

    samplename = pvproperty(
        value=" ",
        name="samplename",
        doc="Sample name as given by the user",
        dtype=PvpropertyString,
        max_length=255
        )

    @samplename.putter
    async def samplename(self, instance: ChannelData, value: str):
        """Data was written over channel access."""
        if len(value) > 40:
            # 40 corresponds to the max length in bytes of 255 
            raise ValueError('Sample name too long')

        print(f'New sample name recorded as: {value}')
        return value


    sampleowner = pvproperty(
        value="",
        name="sampleowner",
        dtype=PvpropertyString,
        )

    proposal = pvproperty(
        value="",
        name="Proposal",
        dtype=PvpropertyString,        
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
