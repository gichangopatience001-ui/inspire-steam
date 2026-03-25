"""
RoboDK Pick and Place Script
Task: Pick the Bottle (Plain) and place it inside the Box 12x10in (Open)
Robot: RoboDK RDK-COBOT-1200

Positions are based on the station setup visible in the screenshot:
  - Bottle (Plain)     : X=700, Y=-200, Z=0 mm (relative to New Station)
  - Box 12x10in (Open) : X=600, Y=70,   Z=0 mm (relative to New Station)
"""

from robodk.robolink import Robolink, ITEM_TYPE_ROBOT, ITEM_TYPE_OBJECT
from robodk.robomath import TxyzRxyz_2_Pose, transl, rotz, KUKA_2_Pose
import math

# ── 1. Connect to RoboDK ────────────────────────────────────────────────────
RDK = Robolink()

# ── 2. Grab items from the station tree ─────────────────────────────────────
robot  = RDK.Item('RoboDK RDK-COBOT-1200', ITEM_TYPE_ROBOT)
bottle = RDK.Item('Bottle (Plain)',         ITEM_TYPE_OBJECT)
box    = RDK.Item('Box 12x10in (Open)',     ITEM_TYPE_OBJECT)

# Validate that every item was found
for item, name in [(robot, 'Robot'), (bottle, 'Bottle (Plain)'), (box, 'Box 12x10in (Open)')]:
    if not item.Valid():
        raise RuntimeError(f"❌  Could not find '{name}' in the station. "
                           "Check the item name in the RoboDK tree.")

print("✅  All station items found.")

# ── 3. Configuration constants ───────────────────────────────────────────────
APPROACH_OFFSET_Z  =  150   # mm – how far above the object to hover before grasping
RETRACT_OFFSET_Z   =  200   # mm – safe lift height after grasping / releasing
SPEED_LINEAR       =  150   # mm/s  – Cartesian speed
SPEED_JOINTS       =   30   # deg/s – joint speed
BLEND_RADIUS       =   10   # mm    – corner rounding between waypoints

# Approximate table surface Z (station reference frame)
TABLE_Z            =    0   # mm  – adjust if your table surface is different

# Drop position *inside* the box (centre of box + small positive Z so it lands gently)
DROP_Z_OFFSET      =   30   # mm above box origin = inside the open box

# ── 4. Helper – build a pose from XYZ + Z-rotation (flat, top-down approach) ─
def flat_pose(x, y, z, rz_deg=0):
    """
    Returns a 4×4 pose matrix for a straight-down end-effector approach.
    rz_deg lets you rotate the tool around Z to avoid collisions.
    """
    # Tool pointing straight down → Rx=180°, Ry=0, Rz=rz_deg
    return TxyzRxyz_2_Pose([x, y, z,
                             math.pi,       # Rx – flip tool to face down
                             0,             # Ry
                             math.radians(rz_deg)])

# ── 5. Retrieve object positions from the station ───────────────────────────
bottle_pose = bottle.Pose()          # pose relative to its parent frame
box_pose    = box.Pose()

# Extract XY from the object poses (Z comes from TABLE_Z + offsets)
bx, by = bottle_pose[0, 3], bottle_pose[1, 3]
px, py = box_pose[0, 3],    box_pose[1, 3]

print(f"📍  Bottle centre  : X={bx:.1f}  Y={by:.1f}")
print(f"📍  Box centre     : X={px:.1f}  Y={py:.1f}")

# ── 6. Define key waypoints ──────────────────────────────────────────────────
# Home – joints (deg) – adjust to a safe starting posture for your robot
home_joints = [0, -45, 90, -45, -90, 0]

# Bottle approach (hover above)
bottle_approach = flat_pose(bx, by, TABLE_Z + APPROACH_OFFSET_Z)

# Bottle grasp (touch / close gripper here)
bottle_grasp    = flat_pose(bx, by, TABLE_Z + 10)   # 10 mm above table surface

# Bottle retract (lift straight up)
bottle_retract  = flat_pose(bx, by, TABLE_Z + RETRACT_OFFSET_Z)

# Box approach (hover above box)
box_approach    = flat_pose(px, py, TABLE_Z + APPROACH_OFFSET_Z)

# Box drop (lower into box)
box_drop        = flat_pose(px, py, TABLE_Z + DROP_Z_OFFSET)

# Box retract (lift away after release)
box_retract     = flat_pose(px, py, TABLE_Z + RETRACT_OFFSET_Z)

# ── 7. Motion program ────────────────────────────────────────────────────────
robot.setSpeed(SPEED_LINEAR, SPEED_JOINTS)
robot.setRounding(BLEND_RADIUS)

print("\n🤖  Starting pick-and-place sequence …\n")

# 7-a  Move to home
print("  → Moving to home position")
robot.MoveJ(home_joints)

# 7-b  Approach bottle
print("  → Approaching bottle")
robot.MoveJ(bottle_approach)   # joint move to approach (safer for long moves)

# 7-c  Descend to grasp
print("  → Descending to grasp bottle")
robot.MoveL(bottle_grasp)      # linear move for precision

# 7-d  Grasp (activate gripper / attach object)
print("  → Grasping bottle  [gripper CLOSE]")
robot.AttachClosest()           # attaches the nearest object to the robot TCP
# If you use a real I/O signal instead, replace with:
#   RDK.RunProgram('GripperClose')  or  robot.setDO(1, True)

# 7-e  Retract with bottle
print("  → Retracting with bottle")
robot.MoveL(bottle_retract)

# 7-f  Move over the box
print("  → Moving over the box")
robot.MoveJ(box_approach)

# 7-g  Descend into box
print("  → Lowering bottle into box")
robot.MoveL(box_drop)

# 7-h  Release
print("  → Releasing bottle  [gripper OPEN]")
robot.DetachAll()               # detaches all objects from the TCP
# If you use a real I/O signal instead, replace with:
#   RDK.RunProgram('GripperOpen')  or  robot.setDO(1, False)

# 7-i  Retract away from box
print("  → Retracting from box")
robot.MoveL(box_retract)

# 7-j  Return home
print("  → Returning to home position")
robot.MoveJ(home_joints)

print("\n✅  Pick-and-place complete!  Bottle is now inside the box.")