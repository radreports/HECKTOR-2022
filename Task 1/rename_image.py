"""
This file renames PET/CT images to match the name convention used for nnU-Net.
"""

import os
join = os.path.join

root_path = "/home/ubuntu/storage1/HECKTOR-2022/data/hecktor2022_training/hecktor2022/labelsTr"

if os.path.exists(join(root_path, '.DS_Store')):
    os.remove(join(root_path, '.DS_Store'))

# print("processed in directory:",root_path)
for img in os.listdir(root_path):
    print("Processing:",img)
    if 'CT' in img:
        name = img.split('_CT')[0]
        os.rename(join(root_path, img), join(root_path, name + '0000.nii.gz'))
    elif 'PT' in img:
        name = img.split('_PT')[0]
        os.rename(join(root_path, img), join(root_path, name + '0001.nii.gz'))

print("processed in directory:",root_path)