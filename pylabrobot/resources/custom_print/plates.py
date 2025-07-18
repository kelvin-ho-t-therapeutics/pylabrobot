from pylabrobot.resources.height_volume_functions import (
  calculate_liquid_volume_container_2segments_square_vbottom,
)
from pylabrobot.resources.plate import Lid, Plate
from pylabrobot.resources.utils import create_ordered_items_2d
from pylabrobot.resources.well import (
  CrossSectionType,
  Well,
  WellBottomType,
)

def General_lid(name: str) -> Lid:
  """
  - 3D printed
  """
  return Lid(
    name=name,
    size_x=139.8,
    size_y=95.4,
    size_z=10.05,
    nesting_z_height=6.9,  # measure overlap between lid and plate
    model="General_lid",
  )