from app import create_app
from app.utils import load_into_db

app = create_app()

def main():
    with app.app_context():
        load_into_db(app.config['CSV_FILE_PATH'])
        app.run(debug=True)

if __name__ == '__main__':
    main()
