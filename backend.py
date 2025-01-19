from flask import Flask, request, jsonify, session, render_template, flash,redirect, url_for
from flask_cors import CORS
import mysql.connector
import re

app = Flask(__name__)
CORS(app)
app.secret_key = "Hackathon_BNP_Paribas"

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Pheonix_A2",
    database="bnp_hack"
)
cursor = database.cursor()



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
        if request.method == 'POST':
            # Retrieve form data
            name = request.form['name']
            email = request.form['email']
            Pass = request.form['Pass']
            Confirm_pass = request.form['Confirm_pass']
            phonenum = request.form['Phone']

            # Validation checks
            if not all([name, email, Pass, Confirm_pass, phonenum]):
                flash("error: All fields are required!", "error")
                return redirect(url_for('signup'))  # Re-render the form with error

            if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                flash("error: Invalid email format!", "error")
                return redirect(url_for('signup'))  # Re-render the form with error

            if not Pass.isalnum():
                flash("error: Password must be alphanumeric!", "error")
                return redirect(url_for('signup'))  # Re-render the form with error

            if not phonenum.isdigit() or len(phonenum) != 10:
                flash("error: Invalid phone number format!", "error")
                return redirect(url_for('signup'))  # Re-render the form with error

            if Pass != Confirm_pass:
                flash("error: Passwords do not match!", "error")
                return redirect(url_for('signup'))  # Re-render the form with error

            # Check if the email or phone already exists
            cursor.execute("SELECT * FROM SignUp WHERE email = %s OR Phone = %s", (email, phonenum))
            if cursor.fetchone():
                flash("error: Email or phone number already exists!", "error")
                return redirect(url_for('signup'))  # Re-render the form with error

            # Insert new user into the database (Do not store Confirm_pass)
            signup_query = """
            INSERT INTO SignUp (Name, email, Pass, Phone)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(signup_query, (name, email, Pass, phonenum))
            database.commit()

            flash("success: Signup successful!", "success")
            return redirect(url_for('login'))  # Redirect to login page after successful signup

        # If GET request, render signup page (initial request)
        return render_template('signup.html')

      # Handle the error and re-render the form


@app.route('/login', methods=['GET', 'POST'])
def loginbtn():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['Pass']

            if not email or not password:
                flash("Email and Password shouldn't be empty", "error")
            else:
                # Check user credentials
                login_query = "SELECT * FROM SignUp WHERE email = %s AND Pass = %s"
                cursor.execute(login_query, (email, password))
                user = cursor.fetchone()

                if user:
                    session['email'] = email
                    flash("Login successful!", "success")
                    return redirect(url_for('dashboard'))  # Redirect to dashboard route
                else:
                    flash("Email or Password is incorrect!", "error")
        except Exception as e:
            flash(f"Login unsuccessful. Error: {e}", "error")

    return render_template('login.html')


@app.route('/')
def forgotpassword():
    return render_template('forgotpassword.html')

@app.route('/', methods=['GET', 'POST'])
def change():
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['Pass']
    cpass = request.form['Cpass']

    if not email or not phone:
        flash("Email and Phone shouldn't be empty", "error")
        return redirect(url_for('')) 
    else:
     
        query = "SELECT email, Pass FROM SignUp WHERE email = %s AND phone = %s"
        cursor.execute(query, (email, phone))
        correct = cursor.fetchone()

        if correct:
         
            query1 = "UPDATE SignUp SET Pass = %s, Confirm_Password = %s WHERE email = %s"
            cursor.execute(query1, (password, cpass, email))
            database.commit()

            flash('Password Changed Successfully', "success")
            return redirect(url_for(''))  
        else:
            flash('Email or Phone number is wrong!', "error")
            return redirect(url_for(''))  

            



    

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


 # Redirect to lc1 route


@app.route('/existing',methods=['GET','POST'])
def existing():
    return redirect(url_for('existingpage'))

@app.route('/templatebtn',methods=['GET','POST'])
def template():
    return redirect(url_for(''))



@app.route('/existingpage')
def existings():
    return render_template('existing.html') 



@app.route('/LC1')
def LC1():
    return render_template('LC1.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    try:
        types=request.form['types']
        issue_date=request.form['issue_date']
        credit_number=request.form['credit_number']
        expiry_date=request.form['expiry-date']
        expiry_place=request.form['expiry_place']
        applicant_address=request.form['applicant_address']
        beneficiary=request.form['beneficiary']
        currency_amount=request.form['currency_amount']
        variations=request.form['variations']
        credit_type=request.form['credit_type']
        credit_type1=request.form['credit_type1']
        credit_type2=request.form['credit_type2']
        credit_type3=request.form['credit_type3']
        usance=request.form['usance']
        port_loading=request.form['port_loading']
        Permit=request.form['Permit']
        Prohibit=request.form['Prohibit']
        shipment_from=request.form['shipment_from']       
        port_loading=request.form['port_loading']
        place1=request.form['place1']
        place2=request.form['place2']
        place3=request.form['place3']
        place=request.form['place']
        latest_shipment=request.form['latest_shipment']
        goods1=request.form['goods1']
        goods2=request.form['goods2']
        Desc1=request.form['Desc1']
        Desc2=request.form['Desc2']
        Desc3=request.form['Desc3']
        Desc4=request.form['Desc4']
        Desc5=request.form['Desc5']
        Desc6=request.form['Desc6']
        Desc7=request.form['Desc7']
        Desc8=request.form['Desc8']
        Desc9=request.form['Desc9']
        Desc10=request.form['Desc10']
        Desc11=request.form['Desc11']
        Desc12=request.form['Desc12'] 
        Desc13=request.form['Desc13'] 
        Desc14=request.form['Desc14']
        Desc15=request.form['Desc15']
        Desc16=request.form['Desc16']
        Desc17=request.form['Desc17']
        Desc18=request.form['Desc18']
        Desc19=request.form['Desc19']
        Desc20=request.form['Desc20']
        Desc21=request.form['Desc21']
        Desc22=request.form['Desc22']

        LC1query="""insert into LC_BANK (types,issue_date,credit_number,expiry_date,expiry_place,applicant_address,beneficiary,currency_amount,variations,credit_type,credit_type1,credit_type2,credit_type3,usance,port_loading,Permit,Prohibit,shipment_from,port_loading,place1,place2,place3,place,latest_shipment,goods1,goods2,Desc1,Desc2,Desc3,Desc4,Desc5,Desc6,Desc7,Desc8,Desc9,Desc10,Desc11,Desc12,Desc13,Desc14,Desc15,Desc16,Desc17,Desc18,Desc19,Desc20,Desc21,Desc22) """
        values1=(types,issue_date,credit_number,expiry_date,expiry_place,applicant_address,beneficiary,currency_amount,variations,credit_type,credit_type1,credit_type2,credit_type3,usance,port_loading,Permit,Prohibit,shipment_from,port_loading,place1,place2,place3,place,latest_shipment,goods1,goods2,Desc1,Desc2,Desc3,Desc4,Desc5,Desc6,Desc7,Desc8,Desc9,Desc10,Desc11,Desc12,Desc13,Desc14,Desc15,Desc16,Desc17,Desc18,Desc19,Desc20,Desc21,Desc22)
        cursor.execute(LC1query,values1)
        database.commit()
        flash('Submitted Successfully',"Success")
        return redirect(url_for('existing')) #next page

    except Exception as e:
        database.rollback()
        flash(f"Sorry Could't Submit. Error: {e}", "error")
        return redirect(url_for('LC1'))


@app.route('/logout')
def logout():
   
    session.clear()
    
    return redirect(url_for(''))




if __name__ == '__main__':
    app.run(debug=True)
