1) To install the dependecies
# pip install --no-cache-dir -r requirements.txt


4) To run the test_framework file on local system 
# python test_framework.py

5) To check the coverage of test_framewok 
# coverage run -m unittest test_framework.py
# coverage report -m

6) To build test_framework in docker 
# docker build -t test_framewok .

7) To run test_framework in docker 
# docker run --rm test_framework

8) To run the automation file on local system 
# python automation.py

9) To check the coverage of automation 
# coverage run -m unittest automation.py