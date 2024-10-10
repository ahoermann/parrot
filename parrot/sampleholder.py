from caproto import ChannelData, ChannelType
from caproto.server import (PVGroup, SubGroup, pvproperty, PvpropertyString,
                            PvpropertyInteger, ioc_arg_parser)
from sample_environment import Motors
from sample import Sample
import yaml 


class MacroifiedNames(PVGroup):
    """
    An IOC with PVs that have macro-ified names.

    Required macros: "beamline" and "suffix"

    PVs
    ---
    {beamline}:{suffix}.VAL
    {beamline}:{suffix}.RBV
    """
    placeholder1 = pvproperty(value=0, name='{short_id}:{samplename}')

class SampleHolder(PVGroup):
    """
    A group of PVs that contains information on all loaded samples according to a config file.

    Information stored includes sample position and blank position as well as sample PV groups. 
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        # print(self.__dict__)
        # ids = [i["short_id"] for i in config['positions']]
        # for position in config['positions']:
            
        #     setattr(self, position["short_id"], SubGroup(Sample,
        #                                                  prefix=f'{self.prefix}{position["short_id"]}',
        #                                                  )
        #             )
            
        #     #print(self.__dict__['Cu GI3'].__dict__)
        #     #for key, value in position["sample"]:
        #     #    setattr(self, 

        

    name = pvproperty(value="solid48", name="sampleholdername")
        
    
    # method here to fill?

    #sample_location = SubGroup(Motors, prefix="location")
    #sample_blank = SubGroup(Motors, prefix="blank")


def getconfig():
    config_file = "sampleholders/gisaxs5.yaml"

    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config 

    
class SampleHolder_gisaxs5(PVGroup):
    """
    A group of PVs that contains information on all loaded samples according to a config file.

    Information stored includes sample position and blank position as well as sample PV groups. 
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.groups = {}
        
    

        
        #
        
 

    name = pvproperty(
        value="gisaxs5",
        name="name",
        doc="Short name of the sample holder",
        string_encoding="utf-8",
        report_as_string=True,
        max_length=255
        )
    

    
    config = getconfig()
    position1 = pvproperty(
        value = config["positions"][0]["short_id"],
        name = "position0",
        string_encoding="utf-8",
        report_as_string=True,
        max_length=255

        )

        
    for position in config["positions"]:
        for key, val in position.items():
            if type(val) is not dict:
                _ = pvproperty(
                    value=val,
                    name="position:"+key,
                )
                    


    #GI3 = SubGroup(Position, prefix="Cu_GI3"
    
    

    

class Position(PVGroup):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    ysam = pvproperty(
        value=0.0,
        name="ysam",
        units="mm",
        doc="horizontal position of the sample stage"
        )

    zheavy = pvproperty(
        value=0.0,
        name="zheavy",
        units="mm",
        doc="vertical position of the sample stage for heavy load (GISAXS)"
        )

    yawgi = pvproperty(
        value=0.0,
        name="yawgi",
        units="degree",
        doc="yaw angle of the sample stage (GISAXS)"
        )

    rollgi = pvproperty(
        value=0.0,
        name="rollgi",
        units="degree",
        doc="roll angle of the sample stage (GISAXS)"
        )

    pitchgi = pvproperty(
        value=0.0,
        name="pitchgi",
        units="degree",
        doc="pitch angle of the sample stage (GISAXS)"
        )    
