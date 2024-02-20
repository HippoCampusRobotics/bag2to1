from rosbags.typesys import get_types_from_msg
from rosbags.typesys.register import register_types

EVENT_PACKET_DEFINITION = """
std_msgs/Header header
uint32 height
uint32 width
uint64 seq
uint64 time_base
string encoding
bool is_bigendian
uint8[] events
"""

GANTRY_MOTOR_POSITION_DEFINITION = """
std_msgs/Header header
float64 position
int64 increments
"""

ALL_DEFINITIONS = {
    'event_camera_msgs/msg/EventPacket': EVENT_PACKET_DEFINITION,
    'gantry_msgs/msg/MotorPosition': GANTRY_MOTOR_POSITION_DEFINITION,
}


def register_all_msg_types():
    for msg_name in ALL_DEFINITIONS:
        register_types(get_types_from_msg(ALL_DEFINITIONS[msg_name], msg_name))
