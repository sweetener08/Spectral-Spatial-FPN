_base_ = './mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        norm_cfg=dict(requires_grad=False),
        style='pytorch',
        init_cfg=dict(
            type='Pretrained',
            checkpoint='torchvision://resnet50')))

img_norm_cfg = dict(
    mean=[430.50096316, 840.02390591, 1496.18954706, 2176.41460541,
          2480.13549565, 2974.60737138, 3397.59235726, 3574.52421021,
          3533.25537136, 3586.58450401, 3562.23649622, 3751.78879719,
          3750.5874577, 3745.41968364, 3672.54947571, 3626.60555673,
          3522.66837151, 3492.61751108, 3351.41690583, 3286.72321578,
          3204.39773476, 3173.7480346, 2904.79222269, 3203.13652023,
          3523.80398441, 3742.41626093, 4242.01638768, 3692.96265732,
          3913.64171571, 4250.03127338, 4158.64935678, 3900.78717797,
          3748.84644999, 3843.73066701, 3660.382394, 3638.97604384,
          3668.9298373, 3142.10086936, 2837.70764051, 2280.28860456,
          1605.29572915, 1880.00084032, 2598.42307005, 3016.5130906,
          3163.43071949, 3197.33676535, 3210.32873343, 3218.27967091],
    std=[1.20540890e+02, 2.68908773e+02, 6.25245070e+02, 1.13380832e+03,
         1.44518744e+03, 1.86648522e+03, 2.24456431e+03, 2.45279672e+03,
         2.49702701e+03, 2.57883269e+03, 2.53874854e+03, 2.59465913e+03,
         2.54360639e+03, 2.54822321e+03, 2.56346554e+03, 2.60446435e+03,
         2.56915191e+03, 2.58872305e+03, 2.51505365e+03, 2.50033291e+03,
         2.47983086e+03, 2.48924973e+03, 2.22653879e+03, 2.20380419e+03,
         2.11436287e+03, 2.05527954e+03, 2.29311572e+03, 1.98108389e+03,
         2.10645085e+03, 2.29706335e+03, 2.24670830e+03, 2.09881783e+03,
         2.01040097e+03, 2.06805467e+03, 1.97101445e+03, 1.96709464e+03,
         1.98631471e+03, 1.68802991e+03, 1.51951385e+03, 1.21456197e+03,
         8.40274170e+02, 9.87885370e+02, 1.38598721e+03, 1.60921128e+03,
         1.68083586e+03, 1.68701809e+03, 1.68538369e+03, 1.66905812e+03],
    to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(
        type='Resize',
        img_scale=[(1333, 640), (1333, 672), (1333, 704), (1333, 736),
                   (1333, 768), (1333, 800)],
        multiscale_mode='value',
        keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    train=dict(pipeline=train_pipeline),
    val=dict(pipeline=test_pipeline),
    test=dict(pipeline=test_pipeline))