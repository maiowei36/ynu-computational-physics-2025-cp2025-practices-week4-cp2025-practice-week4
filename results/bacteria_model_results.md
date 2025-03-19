# 细菌生长模型研究结果

## 实验数据图

![实验数据图](path/to/bacteria_data.png)
![capture_20250319210041486 bmp](https://github.com/user-attachments/assets/9f7436fa-3ac9-489f-809e-2b08d2c94d1a)

## 模型拟合图

![模型拟合图](path/to/model_fit.png)
![capture_20250319210828625 bmp](https://github.com/user-attachments/assets/5106166f-9707-48ed-9dee-3665a3c7f40c)

## 分析与结论

- V模型与W模型的拟合效果比较。
- V模型是简单的指数模型，适用于初期的快速变化，但在tau=2.0后模型开始高于实验数据；W模型包含指数衰减和线性项，更加灵活，比V模型拟合程度高
- 参数估计结果。
- 可以使用最小二乘法来优化W模型使模型与实验数据更加吻合
