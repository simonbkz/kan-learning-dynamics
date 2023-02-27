import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.family':'Times New Roman', 'font.size': 15})

### This script just replots the dense and split network performance together on the same plot ###

dense_sys_train_mean = np.mean(np.genfromtxt('dense/train_accs_sys.txt'), axis=0)
dense_non_train_mean = np.mean(np.genfromtxt('dense/train_accs_non.txt'), axis=0)
split_sys_train_mean = np.mean(np.genfromtxt('split/train_accs_sys.txt'), axis=0)
split_non_train_mean = np.mean(np.genfromtxt('split/train_accs_non.txt'), axis=0)
dense_sys_train_std = np.std(np.genfromtxt('dense/train_accs_sys.txt'), axis=0)
dense_non_train_std = np.std(np.genfromtxt('dense/train_accs_non.txt'), axis=0)
split_sys_train_std = np.std(np.genfromtxt('split/train_accs_sys.txt'), axis=0)
split_non_train_std = np.std(np.genfromtxt('split/train_accs_non.txt'), axis=0)

dense_sys_test_mean = np.mean(np.genfromtxt('dense/test_accs_sys.txt'), axis=0)
dense_non_test_mean = np.mean(np.genfromtxt('dense/test_accs_non.txt'), axis=0)
split_sys_test_mean = np.mean(np.genfromtxt('split/test_accs_sys.txt'), axis=0)
split_non_test_mean = np.mean(np.genfromtxt('split/test_accs_non.txt'), axis=0)
dense_sys_test_std = np.std(np.genfromtxt('dense/test_accs_sys.txt'), axis=0)
dense_non_test_std = np.std(np.genfromtxt('dense/test_accs_non.txt'), axis=0)
split_sys_test_std = np.std(np.genfromtxt('split/test_accs_sys.txt'), axis=0)
split_non_test_std = np.std(np.genfromtxt('split/test_accs_non.txt'), axis=0)

epochs = 301
plt.plot(np.arange(epochs), dense_sys_train_mean, label='Dense Compositional Error')
plt.fill_between(np.arange(epochs), dense_sys_train_mean - dense_sys_train_std, dense_sys_train_mean + dense_sys_train_std, alpha=0.5)
plt.plot(np.arange(epochs), dense_non_train_mean, label='Dense Non-compositional Error')
plt.fill_between(np.arange(epochs), dense_non_train_mean - dense_non_train_std, dense_non_train_mean + dense_non_train_std, alpha=0.5)
plt.plot(np.arange(epochs), split_sys_train_mean, label='Split Compositional Error')
plt.fill_between(np.arange(epochs), split_sys_train_mean - split_sys_train_std, split_sys_train_mean + split_sys_train_std, alpha=0.5)
plt.plot(np.arange(epochs), split_non_train_mean, label='Split Non-compositional Error')
plt.fill_between(np.arange(epochs), split_non_train_mean - split_non_train_std, split_non_train_mean + split_non_train_std, alpha=0.5)
#plt.title('Train Normalized Error')
plt.xlabel('Epoch Number')
plt.ylabel('Normalized Error')
plt.legend(loc='upper left', bbox_to_anchor=(0.05, 0.5, 0.5, 0.5))
plt.grid()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.savefig('cmnist_train.pdf')
plt.close()

plt.plot(np.arange(epochs), dense_sys_test_mean, label='Dense Compositional Error')
plt.fill_between(np.arange(epochs), dense_sys_test_mean - dense_sys_test_std, dense_sys_test_mean + dense_sys_test_std, alpha=0.5)
plt.plot(np.arange(epochs), dense_non_test_mean, label='Dense Non-compositional Error')
plt.fill_between(np.arange(epochs), dense_non_test_mean - dense_non_test_std, dense_non_test_mean + dense_non_test_std, alpha=0.5)
plt.plot(np.arange(epochs), split_sys_test_mean, label='Split Compositional Error')
plt.fill_between(np.arange(epochs), split_sys_test_mean - split_sys_test_std, split_sys_test_mean + split_sys_test_std, alpha=0.5)
plt.plot(np.arange(epochs), split_non_test_mean, label='Split Non-compositional Error')
plt.fill_between(np.arange(epochs), split_non_test_mean - split_non_test_std, split_non_test_mean + split_non_test_std, alpha=0.5)
#plt.title('Test Normalized Error')
plt.xlabel('Epoch Number')
plt.ylabel('Normalized Error')
plt.legend(loc='upper left', bbox_to_anchor=(0.05, 0.1, 0.5, 0.5))
plt.grid()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.savefig('cmnist_test.pdf')
