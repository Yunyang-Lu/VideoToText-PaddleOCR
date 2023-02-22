import paddle
# 加载预训练模型
all_params = paddle.load("output/best_accuracy.pdparams")
# 查看权重参数的keys
print(all_params.keys())
# 模型的权重提取
s_params = {key[len("Student."):]: all_params[key] for key in all_params if "Student." in key}
# 查看模型权重参数的keys
print(s_params.keys())
# 保存
paddle.save(s_params, "./student.pdparams")
#python tools/train.py -c configs/det/det_mv3_db.yml -o Global.pretrained_model=./pretrain_models/MobileNetV3_large_x0_5_pretrained
