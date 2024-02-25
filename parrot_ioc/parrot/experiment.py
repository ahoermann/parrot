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
