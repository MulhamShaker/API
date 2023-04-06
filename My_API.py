from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Mulham API'})

@app.route('/users')
def get_users():
    users = [
        {'id': 1, 'name': 'Mulham'},
        {'id': 2, 'name': 'Wassem'},
        {'id': 3, 'name': 'Subhi'}
    ]
    return jsonify({'users': users})

@app.route('/lists')
def get_list():
    list = [
         {
        'id': 1, 'subject': 'subject data','noteText': 'note data'},
        {
        'id': 2, 'subject': 'subject data2', 'noteText': 'note data2'}
    ]
    return jsonify({'list': list})




if __name__ == '__main__':
    app.run(debug=True)

    