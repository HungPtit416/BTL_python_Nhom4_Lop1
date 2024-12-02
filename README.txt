cài đặt python: https://blog.cloud365.vn/other/gioi-thieu-va-cai-dat-django/
pip install virtualenv
virtualenv env
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
env\Scripts\activate 
python -m pip install Django
pip install -r requirements.txt
python manage.py makemigrations
chạy thêm lệnh này:pip install mysqlclient --upgrade
để k bị _mysql not define
nếu có thêm lỗi pilow thì chạy:python -m pip install Pillow
nếu vẫn pilow thì xóa đi cài lại là ok :python -m pip uninstall Pillow
python -m pip install Pillow
python manage.py migrate 
python manage.py createsuperuser
python manage.py runserver
Note: Chỉnh sửa thông tin database trong file setting
