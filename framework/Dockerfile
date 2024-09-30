FROM python:3.13-rc-slim
 
WORKDIR /app
 
COPY . .
 
RUN pip install -r requirements.txt
 
# Install Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -f install -y \
    && rm google-chrome-stable_current_amd64.deb
 
ENV CHROME_DRIVER_VERSION=129.0.6668.70
 
# Install ChromeDriver
RUN wget -q "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_DRIVER_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip chromedriver-linux64.zip -d /usr/local/bin/ \
    && rm chromedriver-linux64.zip
 
# Ensure chromedriver is executable
RUN chmod +x /usr/local/bin/chromedriver-linux64/chromedriver
 
# Set environment variables for drivers
ENV CHROME_DRIVER_PATH=/usr/local/bin/chromedriver-linux64/chromedriver
ENV CHROME_BIN=/usr/bin/google-chrome
 
# CMD ["python", "-m", "unittest", "-b", "test_automation.py"]
 
# CMD ["coverage","run", "-m", "unittest", "-b", "test_framework.py"]
 
# # CMD ["coverage", "report"]
CMD ["sh", "-c", "coverage run -m unittest -b test_framework.py && coverage report"]