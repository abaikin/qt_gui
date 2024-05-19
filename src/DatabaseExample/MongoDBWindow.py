import sys 
import os

import pandas as pd
import pymongo

import pprint
from pymongo import MongoClient

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QFileDialog

from UI.MongoDBWindow_ui import Ui_Form

# Step 1. Install mongodb local server 
# https://www.mongodb.com/try/download/community

# Step 2.


class MongoDBDialog(qtw.QDialog, Ui_Form):

    # login_success = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.open_db)

    
    @qtc.Slot()
    def open_db(self):

        # Create connection
        client = MongoClient() # client = MongoClient("localhost", 27017)
        db = client.test_database # create database with name test_database
        collection = db.test_collection # createcollection inside databes with name test_collection

        #insert json of the object
        collection.insert_one( 
            {  
                "title": "Seven Brief Lessons on Physics", 
                "author": { 
                    "name": "Carlo Rovelli", 
                    "nationality": "Italian", 
                    "year-of-birth": 1956 
                }, 
                "publication-date": 2014, 
                "genre2323": "non-fiction" 
        }
        )
        #we do not need to save changes. They are saved automatically to mongo db

        print("OK")

        pprint.pprint(collection.find_one()) # for pretty print


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MongoDBDialog()
    window.show()
    sys.exit(app.exec())