"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""


class Entry:
    """
    Utility class to load data.
    """
    
    def __init__(self,frame=-1,obj_type="unset",truncation=-1,occlusion=-1,\
                 obs_angle=-10,x1=-1,y1=-1,x2=-1,y2=-1,w=-1,h=-1,l=-1,\
                 X=-1000,Y=-1000,Z=-1000,yaw=-10,score=-1000,track_id=-1):
        """
        Constructor, initializes the object given the parameters.
        """
        
        # init object data
        self.frame      = frame
        self.track_id   = track_id
        self.obj_type   = obj_type
        self.truncation = truncation
        self.occlusion  = occlusion
        self.obs_angle  = obs_angle
        self.x1         = x1
        self.y1         = y1
        self.x2         = x2
        self.y2         = y2
        self.w          = w
        self.h          = h
        self.l          = l
        self.X          = X
        self.Y          = Y
        self.Z          = Z
        self.yaw        = yaw
        self.score      = score
        self.ignored    = False
        self.valid      = False
        self.tracker    = -1

    def __str__(self):
        """
        Print read data.
        """
        
        attrs = vars(self)
        return '\n'.join("%s: %s" % item for item in attrs.items())


def parse_label(filename):
    """
    Parse entries of a tracking label file.

    Parameters:
        filename(string): label file name.

    Returns:
        entries(list): a list of entries.
    """

    entries = []

    with open(filename, "r") as f:
        for line in f:
            # KITTI tracking benchmark data format:
            # (frame,tracklet_id,objectType,truncation,occlusion,alpha,x1,y1,x2,y2,h,w,l,X,Y,Z,ry)
            line = line.strip()
            fields = line.split(" ")

            # classes that should be loaded
            classes = ["car", "van", "dontcare"]

            if not any([s for s in classes if s in fields[2].lower()]):
                continue

            # get fields from table
            entry = Entry()
            entry.frame        = int(float(fields[0]))     # frame
            entry.track_id     = int(float(fields[1]))     # id
            entry.obj_type     = fields[2].lower()         # object type [car, pedestrian, cyclist, ...]
            entry.truncation   = int(float(fields[3]))     # truncation [-1,0,1,2]
            entry.occlusion    = int(float(fields[4]))     # occlusion  [-1,0,1,2]
            entry.obs_angle    = float(fields[5])          # observation angle [rad]
            entry.x1           = float(fields[6])          # left   [px]
            entry.y1           = float(fields[7])          # top    [px]
            entry.x2           = float(fields[8])          # right  [px]
            entry.y2           = float(fields[9])          # bottom [px]
            entry.h            = float(fields[10])         # height [m]
            entry.w            = float(fields[11])         # width  [m]
            entry.l            = float(fields[12])         # length [m]
            entry.X            = float(fields[13])         # X [m]
            entry.Y            = float(fields[14])         # Y [m]
            entry.Z            = float(fields[15])         # Z [m]
            entry.yaw          = float(fields[16])         # yaw angle [rad]

            entries.append(entry)

    return entries

