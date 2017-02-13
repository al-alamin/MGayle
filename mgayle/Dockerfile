FROM alalamin19/mgayle
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
EXPOSE 80
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
