import glob, os, functools
import numpy as np
import pandas as pd
import SimpleITK as sitk

in_data = '/home/ubuntu/storage1/HECKTOR-2022/data/Task501_Hecktor/training/imagesTr'
in_label =  '/home/ubuntu/storage1/HECKTOR-2022/data/Task501_Hecktor/training/labelsTr'
ref_folder = '/home/ubuntu/storage1/HECKTOR-2022/nnUNet_raw_data/Task507_160x160x64/competition_data/'
names_path = '/home/ubuntu/storage1/HECKTOR-2022/data/Task501_Hecktor/testing/hecktor2022_clinical_info_testing.csv'
out_img = '/home/ubuntu/storage1/HECKTOR-2022/nnUNet_raw_data/Task507_160x160x64/competition_data/imagesTs'
out_temp = '/home/ubuntu/storage1/HECKTOR-2022/nnUNet_raw_data/Task507_160x160x64/competition_data/temp_folder/'
out_label = '/home/ubuntu/storage1/HECKTOR-2022/nnUNet_raw_data/Task507_160x160x64/labelsTr/'
out_trans = '/home/ubuntu/storage1/HECKTOR-2022/nnUNet_raw_data/Task507_160x160x64/competition_data/transforms'
df = pd.read_csv(names_path)
names = df['PatientID'].to_numpy()

code = 'HEK_'
#loop through patients
for i, name in enumerate(names):
    print("processing:",name)
    img_ct = sitk.ReadImage(os.path.join(in_data,name+'__CT.nii.gz'))
    img_pt = sitk.ReadImage(os.path.join(in_data,name+'__PT.nii.gz'))
    mask = sitk.ReadImage(os.path.join(in_label,name+'.nii.gz'))