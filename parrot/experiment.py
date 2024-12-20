from caproto import ChannelData, ChannelType
from caproto.server import (AsyncLibraryLayer, PVGroup, SubGroup, pvproperty, PvpropertyString, PvpropertyInteger)
import datetime 

class ExperimentProgress(PVGroup):
    """
    A group of PVs to monitor experiment progress.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    measurements_overall = pvproperty(
        value=0,
        name="measurements_overall",
        doc="Number of measurements in the current measurement script. A measurement includes the direct beam and transmission measurement.",
        )

    measurements_completed = pvproperty(
        value=0,
        name="measurements_completed",
        doc="Number of measurements completed for the current measurement script. A measurement includes the direct beam and transmission measurement.",
        )

    ratio = pvproperty(value = 0.0, name="ratio",
                       doc = "ratio of measurements completed / measurements overall")

    estimated_completion_time = pvproperty(value=datetime.datetime(1970, 1, 1, 0, 0).isoformat(),
                                           name="estimated_completion_time",
                                           report_as_string=True,
                                           doc="Expected date and time for measurement completion"
                                           )

    @measurements_completed.putter
    async def measurements_completed(self, instance, value: int):
        """Calculate the ratio and remaining time after each update.

        This will be approximately correct if the parent count time is the
        measurement time. Measurement completion should be communicated to parrot
        before moving to the next direct beam exposure (with shorter count_time pv)"""
        if self.measurements_overall.value == 0:
            # measurement is complete if no measurements planned
            await self.ratio.write(1.0)
            await self.estimated_completion_time.write(datetime.datetime.now().isoformat())
            return

        await self.ratio.write(value / self.measurements_overall.value)
        # experimental overhead as observed on 2024-12-17
        overhead = datetime.timedelta(seconds=107.14)
        time_per_measurement = datetime.timedelta(seconds = self.parent.count_time.value) + overhead
        remaining_time = int(self.measurements_overall.value - value)*time_per_measurement
        await self.estimated_completion_time.write((datetime.datetime.now() + remaining_time).isoformat())
        return


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
        name="user",
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

    progress = SubGroup(ExperimentProgress, prefix="progress:",
                        )



