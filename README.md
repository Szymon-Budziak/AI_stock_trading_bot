# Stock trading bot
AI stock trading bot written in Python that has an average accuracy of 55-60%. An example showing how the bot works is the Intel company.
It uses historical data provided by yfinance to predict next price moves. It is run and trained on 70 epochs you can change it to get a better accuracy. To run the model you just need to open `main.ipynb` file and run all the cells (do not forget about the requirements below).
**Important note**
I am not a financial advisor and you use this bot at your own risk.
## Prerequisites
Installation process shown on Linux Ubuntu 20.04 LTS:
1. Update system before installation:
```
sudo apt update
```
2. Check your Python version:
```
python3 --version
```
3. If your Python version is lower than 3.8, install a newer version:
```
sudo apt install python3.8
```
4. Validate python version:
```
python3.8 --version
```
5. Install `pip3`:
```
sudo apt install python3-pip
```
6. Validate `pip3` version:
```
pip3 --version
```
## Python lib requirements
**1. Pandas**

You can install pandas by using pip:
```
pip install pandas
```
or you can visit official Pandas website [here](https://pandas.pydata.org/docs/getting_started/install.html).

**2. Numpy**

Pip installation:
```
pip install numpy
```
official Numpy website [here](https://numpy.org/install/).

**3. Tensorflow**

You can install Tensorflow with pip and [here](https://www.tensorflow.org/install/pip) is the full instalation process on official Tensorflow website. I recommend installing it in virtual environment instead of system installation.

**4. Yahoo Finance**

Pip installation:
```
pip install yfinance --upgrade --no-cache-dir
```
also check out the pypi website [here](https://pypi.org/project/yfinance/) with yfinance quick start where you can check how to use it.

**5. Matplotlib**

If you want to visualize your predictions and price history then you can install it using pip:
```
python -m pip install -U matplotlib
```
You can find full installation process on official matplotlib website [here](https://matplotlib.org/stable/users/installing/index.html).

**6. Import_ipynb**

Pip installation:
```
pip install import-ipynb
```
pypi website [here](https://pypi.org/project/import-ipynb/).

## Conclusion
By using this bot for buying and trading assets, you do so at your own risk. This is not a financial advice to trade with it.
