# Clone
Clone the repo
# cd into harifind-v3
```bash
cd harifind-v3
```
# Install requirements
```bash
pip install -r requirements.txt
```
# Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```
# Install tailwind
```bash
python manage.py tailwind install
```
# Install node dependencies
```bash
cd theme/static_src
npm install
cd ../../
```
# Run dev server
```bash
python manage.py tailwind start
```
```bash
python manage.py runserver
```
