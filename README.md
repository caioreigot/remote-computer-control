To build the project:
pyinstaller --onefile --noconsole --icon="src\utils\logo.ico" --add-data="src\views\app\get\page.html;src\views\app\get" --name="Champignon"  app.py