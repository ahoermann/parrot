from caproto import ChannelData, ChannelType
from caproto.server import (AsyncLibraryLayer, PVGroup, SubGroup, pvproperty, PvpropertyString, PvpropertyInteger)
import datetime 


class Experiment(PVGroup):
    """
    A group of PVs regarding the experiment. 
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        

    date = pvproperty(
        value=str(datetime.date.today()),
        name="date",
        doc="Date of measurement",
        dtype=PvpropertyString,
        )

    @date.scan(period=3600)
    async def date(self, instance: ChannelData, async_lib: AsyncLibraryLayer):
        await self.date.write(value=str(datetime.date.today()))
    
    logbook_date = pvproperty(
        value="",
        name="logbook_date",
        dtype=PvpropertyString,
        )

    operator = pvproperty(
        value="",
        name="operator",
        dtype=PvpropertyString,
        )

    protocol = pvproperty(
        value="",
        name="protocol",
        dtype=PvpropertyString,
        )

    procpipeline = pvproperty(
        value="",
        name="procpipeline",
        dtype=PvpropertyString,
        )

    batchnum = pvproperty(
        value=1,
        name="batchnum",
        dtype=PvpropertyInteger,
        )

    count_time = pvproperty(
        value=1,
        name="count_time",
        dtype=PvpropertyInteger,        
        )
    
    frame_time = pvproperty(
        value=10,
        name="frame_time",
        dtype=PvpropertyInteger,
        )

    repetitions = pvproperty(
        value=1,
        name="nrep",
        doc="number of repetitions",
        dtype=PvpropertyInteger,
        )

    additional_parameters = pvproperty(
        value="none",
        name="additional_parameters",
        doc="additional parameters defined in the logbook",
        record="waveform",
    )
