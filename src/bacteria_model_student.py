import numpy as np  #引入numpy用于数值计算
import matplotlib.pyplot as plt  #引入matplotlib的pyplot包用于绘图


class BacteriaModel:
    def __init__(self, A, tau):  #定义初始化模型参数，A是模型系数，控制W(t)曲线的幅度；tau是时间参数，控制生长速度
        self.A = A  #储存模型参数A
        self.tau = tau  #储存时间常数tau

    def v_model(self, t):  #定义V(t)的模型
        return 1 - np.exp(-t / self.tau)  #V(t)的函数

    def w_model(self, t):  #定义W(t)生长模型
        return self.A * (np.exp(-t / self.tau) - 1 + t / self.tau)  #W(t)的函数

    def plot_models(self, t):  #绘制两个生长模型的曲线图
        v = self.v_model(t)  #计算两个模型的输出
        w = self.w_model(t)

        plt.plot(t, v, label='V(t)')  #绘制V(t)曲线
        plt.plot(t, w, label='W(t)')  #绘制W(t)曲线
        plt.xlabel('Time')  #设置横坐标轴标签Time
        plt.ylabel('Response')  #设置纵坐标轴标签Response
        plt.title('Bacteria Growth Models')  #设置图标标题Bacteria Growth Models
        plt.legend()  #显示图例
        plt.show()


def load_bacteria_data(filepath):  #加载实验数据文件
    try:
        data = np.loadtxt(filepath, delimiter=',')  #尝试加载结构化的数据文件
        return data['time'], data['response']
    except:
        return np.loadtxt(filepath, delimiter=',', unpack=True)  #失败后就使用常规加载方式


def main():  #定义主程序
    # 初始化模型参数
    model = BacteriaModel(A=1.0, tau=2.0)

    # 生成时间序列
    t = np.linspace(0, 10, 100)  #0到10小时，100个数据点

    # 绘制模型曲线
    model.plot_models(t)

    # 加载实验数据
    time_data, response_data = load_bacteria_data(r"D:\HuaweiMoveData\Users\HUAWEI\Desktop\机器学习作业\g149novickA.txt")

    # 绘制实验数据
    plt.scatter(time_data, response_data, label='Experimental Data')
    plt.legend()
    plt.show()


if __name__ == "__main__":  #执行主程序
    main()
