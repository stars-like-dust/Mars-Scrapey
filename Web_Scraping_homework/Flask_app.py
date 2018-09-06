
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_info 
import pymongo


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.Mars_info_home
    

app = Flask(__name__)

app.route('/')
def home():

    Mars_22 = db.Mars_collection 
    return render_template('index.html', Mars_22=Mars_22)


app.route('/scrape')
def scrape():

    #scrape = scrape_info()



    # Create single dictionary
    Ultimate_Dic = {
    'results_1':['NASA Mars Title'],
    'results_2':['NASA MARS Paragraph'],
    'final_URL':['Featured Image'],
    'Planetdata':['Data List'],
    'text':['Mars Tweet']
    #Cerebus:scrapey_mars['Title1'] = 'Cerebus', cerberus_link,
    #Schiaparelli:['Title2'] = 'Schiaparelli', Schiaparelli
    #Sytris:['Title3'] = 'Syrtis', Syrtis
    #Valles[:'Title4'] = 'Valees', Valles
    }

    Ultimate_Dic

    #insert Ulitmate_Dic to pymongo

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.Mars_info_home
    collection = db['Mars_collection']
    collection.drop
    collection.insert_one(Ultimate_Dic)

    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=False)
