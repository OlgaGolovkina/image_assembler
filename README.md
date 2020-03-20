# image_assembler
**Image Assembler App** is responsible for collecting the patches and reassembling them into the original image.
#
**BEFORE:** _Mixed Pieces_ -------------------------------------------------------------------------> **AFTER:** _Final Picture_
![image_assembler Logo](images/demo_pic.jpg)

* **Requirements**
    * install requirements
    * preferably using virtual environment 
```bash
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```
> Note: if you need additional effort in installing OpenCV and dependencies, you may explore this [post](https://medium.com/@nuwanprabhath/installing-opencv-in-macos-high-sierra-for-python-3-89c79f0a246a)

#
* **Example of Usage**
```bash
python run.py -i images/the_witcher.png -o poster.png -s 50
```
