FROM python:3.9

WORKDIR /usr/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
RUN cythonize -a -i concat_impl.pyx

CMD ["fastapi", "run", "main.py", "--port", "8000"]