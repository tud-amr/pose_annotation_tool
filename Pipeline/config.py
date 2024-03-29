




### CHANGE THESE THREE DIRECTORIES

#location of this file
this_dir = '/home/jtverhoog/BEP/skeleton_annotation/Pipeline/config.py'

# location of mmdetection folder (don't end with a dash)
mmdet_folder = '/home/jtverhoog/BEP/skeleton_annotation/mmdetection'

# location of mmpose folder (don't end with a dash)
mmpose_folder = '/home/jtverhoog/BEP/skeleton_annotation/mmpose'






###############################################################################################################################
### More configuration possibilities

# device used, use cpu if no videocard available
device = 'cpu'

# detection threshold for person detection
det_threshold = 0.8

# model used for person detection
detection_model = 'mask-rcnn_r101-syncbn-gcb-r16-c3-c5_fpn_1x_coco'

# pose detection configuration file for Neural Network
config_file = f'{mmpose_folder}/configs/body_2d_keypoint/topdown_regression/coco/td-reg_res152_rle-8xb64-210e_coco-256x192.py'

# trained state of pose detection model
checkpoint_file = 'https://download.openmmlab.com/mmpose/top_down/deeppose/deeppose_res152_coco_256x192_rle-c05bdccf_20220615.pth'

# More options for visualisation of pose estimation
draw_heatmap = False          # Visualize the predicted heatmap
show_kpt_idx = False           # Whether to show the index of keypoints
skeleton_style = 'mmpose'     # Skeleton style selection, can be 'openpose' or 'mmpose'
kpt_thr = 0.5                 # Visualizing keypoint thresholds
radius = 2                    # Keypoint radius for visualization in pixels
thickness = 1                 # Link thickness for visualization in pixels
alpha = 1.0                   # The transparency of bboxes (between 0.0 and 1.0)
show = False                  # Whether to show img during processing
save_kpt_score = False        # Whether to save the numpy arrays of keypoint scores and indices

# LabelMe
add_skeleton = True           # If False, wil only print the keypoints in LabelMe. True adds keypoint connection


##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
import os


def get_directory_path(dir_name):
    base_path = os.path.dirname(__file__)  # Gets the current directory where this script is located
    dir_path = os.path.join(base_path, dir_name)
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
    return dir_path

# create all paths
get_directory_path('0_input_dataset')
get_directory_path('1_detection/preds')
get_directory_path('1_detection/vis')
get_directory_path('2_cut_out_bb')
get_directory_path('3_pose_annotation/preds_npy')
get_directory_path('3_pose_annotation/vis')
get_directory_path('4_labelme_readables')

def base_dir():
    return this_dir.split('config.py')[0]

def get_mmdet_folder():
    return mmdet_folder

def detection_threshold():
    return det_threshold

def get_mmpose_setup():
    cut_out_bb = get_directory_path('2_cut_out_bb')
    pose_npy_pred_out = get_directory_path('3_pose_annotation/preds_npy')
    pose_vis_out = get_directory_path('3_pose_annotation/vis')
    return config_file, checkpoint_file, pose_vis_out, pose_npy_pred_out, cut_out_bb

def get_vis_setup():
    return draw_heatmap, show_kpt_idx, skeleton_style, kpt_thr, radius, thickness, alpha, save_kpt_score, show, device, mmpose_folder

def get_json_setup():
    base_path = os.path.dirname(__file__)  
    full_labelme = os.path.join(base_path, 'skltn_labelme.json')
    base_labelme = os.path.join(base_path, 'kpt_labelme.json')
    cut_out_bb = get_directory_path('2_cut_out_bb')
    pose_npy_pred_out = get_directory_path('3_pose_annotation/preds_npy')
    output_labelme = get_directory_path('4_labelme_readables')
    return cut_out_bb, pose_npy_pred_out, base_labelme, full_labelme, output_labelme, add_skeleton, save_kpt_score

def get_detection_model():
    return detection_model, device

def print_separator():
    print('\n#############################################################################################################\n')

    


