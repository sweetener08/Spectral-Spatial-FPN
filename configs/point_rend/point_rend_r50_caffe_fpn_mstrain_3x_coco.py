_base_ = './point_rend_r50_caffe_fpn_mstrain_1x_coco.py'
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))
# learning policy
lr_config = dict(step=[240, 270])
runner = dict(type='EpochBasedRunner', max_epochs=300)
