from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process the form data
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        message = request.form.get('message')
        gender = request.form.get('gender')
        hobbies = request.form.getlist('hobbies')
        country = request.form.get('country')

        # Connect to the MySQL database
       
        conn = mysql.connector.connect(
             host="127.0.0.1",
             user="root",
             password="jay81",
             database="voice_assistant"
)

        # Create a cursor object
        cursor = conn.cursor()

        # SQL query to insert data
        sql = "INSERT INTO form_data (f_name,l_name,message,gender,intrests,country) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, message, gender, ', '.join(hobbies), country)

        # Execute the query
        cursor.execute(sql, values)

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

        return "Form submitted successfully!"
    return render_template('from.html')

if __name__ == '__main__':
    app.run(debug=True)
