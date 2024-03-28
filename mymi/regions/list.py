from enum import Enum

from mymi.types import PatientRegions
from mymi.utils import arg_to_list

class RegionList(list, Enum):
    # MICCAI 2015 dataset (PDDCA).
    MICCAI = ['Bone_Mandible', 'Brainstem', 'Glnd_Submand_L', 'Glnd_Submand_R', 'OpticChiasm', 'OpticNrv_L', 'OpticNrv_R', 'Parotid_L', 'Parotid_R']
    MICCAI_CVG_THRESHOLDS = [0.71, 0.66, 0.54, 0.54, 0.25, 0.40, 0.44, 0.63, 0.62]
    MICCAI_INVERSE_VOLUMES = [
        1.81605095e-05,
        3.75567497e-05,
        1.35979999e-04,
        1.34588032e-04,
        1.71684281e-03,
        1.44678695e-03,
        1.63991258e-03,
        3.45656440e-05,
        3.38292316e-05
    ]
    MICCAI_SHORT = ['BM', 'BS', 'SL', 'SR', 'OC', 'OL', 'OR', 'PL', 'PR']
    assert len(MICCAI) == len(MICCAI_CVG_THRESHOLDS) == len(MICCAI_INVERSE_VOLUMES) == len(MICCAI_SHORT)

    # PMCC dataset.
    PMCC = ['BrachialPlexus_L', 'BrachialPlexus_R', 'Brain', 'BrainStem', 'Cochlea_L', 'Cochlea_R', 'Lens_L', 'Lens_R', 'Mandible', 'OpticNerve_L', 'OpticNerve_R', 'OralCavity', 'Parotid_L', 'Parotid_R', 'SpinalCord', 'Submandibular_L', 'Submandibular_R']
    PMCC_CVG_THRESHOLDS = [0.31, 0.35, 0.78, 0.63, 0.27, 0.32, 0.36, 0.37, 0.71, 0.4, 0.42, 0.63, 0.62, 0.63, 0.53, 0.57, 0.58]
    PMCC_INVERSE_VOLUMES = [
        0.00011376029489088039,
        0.00011060966775471057,
        7.446522874686845e-07,
        3.964170420857003e-05,
        0.002744113436394272,
        0.0030073116457818953,
        0.002957342943345055,
        0.002988210189604558,
        1.3595619210428649e-05,
        0.000977472289486429,
        0.000962569199385967,
        9.200393030692723e-06,
        3.0352277602361224e-05,
        3.072187177824903e-05,
        3.976200542837415e-05,
        0.0001100993441549776,
        0.00010420091523896904
    ]
    PMCC_SHORT = ['BL', 'BR', 'B', 'BS', 'CL', 'CR', 'LL', 'LR', 'M', 'OL', 'OR', 'OC', 'PL', 'PR', 'SC', 'SL', 'SR']
    assert len(PMCC) == len(PMCC_CVG_THRESHOLDS) == len(PMCC_INVERSE_VOLUMES) == len(PMCC_SHORT)

# Behaves like 'arg_to_list', but also handles special 'RL:<region list>' format.
def region_to_list(region: PatientRegions, **kwargs) -> PatientRegions:
    if not isinstance(region, str) or not region.startswith('RL:'):
        return arg_to_list(region, str, **kwargs)

    # Get region list.
    rl_name = region.split(':')[-1]
    return list(getattr(RegionList, rl_name))
    