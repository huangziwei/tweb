# tweb

A Python command line tool for downloading books from [http://taiwanebook.ncl.edu.tw/](http://taiwanebook.ncl.edu.tw/) (台湾华文电子书库).

下载 [台湾华文电子书库](http://taiwanebook.ncl.edu.tw/) PDF 的 Python 命令行工具。

## Why?

As stated on the website of 台湾华文电子书库：

> ... 鑑於國內許多的圖書館與文獻典藏單位典藏著1911-1949年出版品，該時期出版品記錄著臺灣歷史文化、人文地理、藝術文學、社會、政治、經濟等各面向資料，極具學術研究價值，成為臺灣研究的最佳資源。惟臺灣地區因溫、濕度偏高不利於圖書保存，多數圖書文獻典藏空間環境缺乏完善的溫溼度恆溫控制環境，圖書因年代久遠紙質酸化，往往禁不起翻閱而破損，或因損壞而被報廢，為達成保存文化與弘揚學術之任務，以數位化減少圖書因使用而損壞，得以數位形式備份保存，透過網路提供國內外讀者及研究人員查詢利用，延長這些實體圖書的保存壽命。

Yet, it only offers online browsing. The size of those books are big and it tooks a long time to load.  

## Requirements

- Python3
- requests
- BeautifulSoup4
- lxml

## Usage

	$ git clone https://github.com/huangziwei/tweb
	$ cd tweb
	$ pip install -r requirements.txt
	$ python tweb.py http://taiwanebook.ncl.edu.tw/zh-tw/book/NCL-000026558
	Downloading book:  亂世哲學
	Site:       ncl.edu.tw
	Title:      NCL-000026558
	Type:       Unknown type (pdf)
	Size:       17.68 MiB (18536765 Bytes)

	Downloading 亂世哲學.pdf ...
	 0.0% (  0.0/ 17.7MB) ├─────────────────────────────────────────┤[1/1]

## To Do

1. Extract book info from webpage and rename filenames into readable ones (✓);
2. Use other tools to download books instead of relying on built-in modules (✓);
3. ...
