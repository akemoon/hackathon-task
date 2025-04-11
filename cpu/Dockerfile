FROM python:3.11.9

WORKDIR /cpu
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5678
CMD ["python", "cpu.py"]