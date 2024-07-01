# DA_SOICT

---

The research and development of a traffic vehicle classification solution in uncontrolled environments.

## I. Introduction

---

This project focuses on researching and developing a robust and reliable solution for detecting and classifying motorcycles in real traffic conditions in Vietnam. The solution utilizes advanced image preprocessing techniques and deep learning models for object detection and classification.

## II. Installation

---

1. Create a virtual environment (recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

or

```
conda create -m venv
conda activate venv
```

2.Install required libraries:

```
cd BKAI-Demo-Motorbike-PyQT
pip install -r requirements.txt
```

3. (Optional) Build Docker image:

```
docker build -t hungnk20/demo_motor_bk:0.0.1 .
```

## III. Data

---

- MCBK Dataset: This dataset was built specifically for this research and contains 91,838 motorcycle images labeled . You can download it from [here](https://husteduvn-my.sharepoint.com/:u:/g/personal/quan_dm210710_sis_hust_edu_vn/EW11l_Bn1G5OoPv_IawODJsBYphb8Lza5sehWSQZpSNoxw?e=gG7rbX).

- NOD and ExDark Datasets: These datasets are used to evaluate the model's performance in low-light conditions. You can download them from the following sources:
  - NOD: [link to NOD dataset](https://github.com/igor-morawski/NOD.git)
  - ExDark: [link to ExDark dataset](https://github.com/cs-chan/Exclusively-Dark-Image-Dataset.git)

## IV. How to Run

---

1. Dowload weight
   The weights file includes models for detection, tracking, classification, and image preprocessing. You can download it from [link](https://husteduvn-my.sharepoint.com/:u:/g/personal/quan_dm210710_sis_hust_edu_vn/EY61etcJ69FEijQjLr25jfoBxG9pj5yavCJgDTbO7U6Yww?e=hn5mbh)

2. Run the demo application

- Using Docker Compose

```
docker-compose up -d
```

- Running directly (without Docker):

```
python app.py
```
