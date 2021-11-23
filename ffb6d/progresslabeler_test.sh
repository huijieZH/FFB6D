model_sensor=D435
dataset_sensor=L515
checkpoint=train_log/ycb/checkpoints/FFB6D_fine_tune_$model_sensor.pth.tar
# checkpoint=train_log/ycb/checkpoints/FFB6D_baseline.pth.tar

echo "model_sensor: " $model_sensor ", dataset_sensor: " $dataset_sensor

# --test --sensor_name --template --ratio
python datasets/ycb/dataset_config/generate_list.py test $dataset_sensor test_scene1 1

python -m torch.distributed.launch --nproc_per_node=1 train_ycb.py --gpu 0 -eval_net -checkpoint $checkpoint -test -test_pose
# echo $tst_mdl 