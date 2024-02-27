from caproto import ChannelData, ChannelType
from caproto.server import AsyncLibraryLayer, PVGroup, SubGroup, pvproperty
from .sample import Sample
from .experiment import Experiment
from .config import Config
from .sample_environment import SampleEnvironment

class Parrot(PVGroup):
    """
    Parrot: an IOC to keep track of MOUSE measurement metadata.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Init here

    sample = SubGroup(Sample, prefix="sample:")

    experiment = SubGroup(Experiment, prefix="exp:")

    instrument = SubGroup(Config, prefix="config:")

    sample_env = SubGroup(SampleEnvironment, prefix="environment:")

