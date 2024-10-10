from caproto import ChannelData, ChannelType
from caproto.server import AsyncLibraryLayer, PVGroup, SubGroup, pvproperty, ioc_arg_parser
from sample import Sample
from experiment import Experiment
from config import Config
from sample_environment import SampleEnvironment
from sampleholder import SampleHolder_gisaxs5, MacroifiedNames
import yaml

class Parrot(PVGroup):
    """
    Parrot: an IOC to keep track of MOUSE measurement metadata.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Init here
        config_file = "sampleholders/gisaxs5.yaml"
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        

    sample = SubGroup(Sample, prefix="sample:")

    experiment = SubGroup(Experiment, prefix="exp:")

    instrument = SubGroup(Config, prefix="config:")

    sample_env = SubGroup(SampleEnvironment, prefix="environment:")

    
    sampleholder = SubGroup(SampleHolder_gisaxs5, prefix="sampleholder:")
    

    
