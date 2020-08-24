"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""
import context
import parse_data

filename = "/media/pengfei/New Volume/Data/KITTI/Tracking/data_tracking_label_2/training/label_02/0000.txt"
entries = parse_data.parse_label(filename)

print("Number of entries: ", len(entries))