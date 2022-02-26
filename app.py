import time
import psycopg2
from database.DBConnection import *
from database.User import *
from flask import (
    Flask,
    g,
    render_template,
    url_for, 
    flash, 
    redirect, 
    request, 
    session, 
    abort
)

app = Flask(__name__)
app.secret_key = 'gpd'
#conn, cursor = None
#setup db connection
db = DBConnection('studyspacesboss', 'IPRO497gpd!!', 'studyspacesdbserver.postgres.database.azure.com', 5432, 'postgres')
conn = db.connect()
cursor = conn.cursor()
conn.autocommit = True
counter = 3

def add_reservation(reserve_id, user_id, room_id, equipment_id, status, group_size, start_time, end_time):
    query = f"insert into reservations values ({reserve_id}, {user_id}, {room_id}, {equipment_id}, '{status}', {group_size}, '{time.time()}', '{start_time}', '{end_time}')"
    cursor.execute(query)
    conn.commit()

# @app.before_request
# def before_request():
    
    
    # #check if user is in session and put it in 'g'
    # g.user = None
    # query = ''
    # cursor.execute(query)
    # conn.commit()
    # result_users = cursor.fetchall()
    
    # users_logged_in = [usr for usr in result_users if usr[1] == session['email']]
    # if users_logged_in:
    #     logged_in_user = users_logged_in[0]
    #     g.user = User(logged_in_user[0], logged_in_user[1], logged_in_user[2], logged_in_user[3], logged_in_user[5], logged_in_user[4])

# @app.teardown_request
# def after_request(error=None):
#     conn.close()
#     if error:
#         print(str(error))


@app.route('/')
def home():
    return render_template('headerfooter.html')

@app.route('/rooms', methods=['POST', 'GET'])
def rooms():
    return render_template('rooms.html')

@app.route('/room_info.html', methods=['POST', 'GET'])
def room():
    return render_template('room_info.html')

@app.route('/confirmation.html', methods=['POST', 'GET'])
def confirm():
    size = request.form.get("groupsize")
    time = request.form.get("time")
    time = time.split("-")
    start = time[0]
    end = time[1]
    add_reservation(3, 3, 3, 3, 'reserved', int(size), start, end)
    return render_template('confirmation.html')    

if __name__ == "__main__":
    app.static_folder='resources'
    app.run(debug=True)