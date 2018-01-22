from dotenv import load_dotenv
from os.path import dirname, join

from framework.bootstrap import app

if __name__ == "__main__":
    # show the .env path
    dotenv_path = join(dirname('__file__'), '.env')
    # load the .env
    load_dotenv(dotenv_path)
    app.run(access_log=True)
