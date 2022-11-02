# A Tool parse image from https://www.instagram.com/
## Getting Started

These instructions will help you to run our unified discourse parser based on RST dataset.

### Prerequisites

```
* selenium
* Python 3
* wget

https://chromedriver.chromium.org/home
 download chromedriver, in local path: /usr/local/bin/chromedriver

```




## How To Run
* Parser: <br>
```
cd Parser/
python main.py
```
You can also control any other arguments. Please refer to `main.py`. By default, the parser will use the same parameters as described in the paper.

* Segmenter: <br>
```
cd parseimg
python3 main.py
```


Result:

![95822771_1148153855547538_2347966417961089731_n](/Users/apple/PycharmProjects/parseimg/explore/95822771_1148153855547538_2347966417961089731_n.jpg)