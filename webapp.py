from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
post=[{'center_id': 394368,
       'name': 'Sevilimedu UPHC',
       'address': 'UPHC Road Street Sevilimedu Kancheepuram',
       'state_name': 'Tamil Nadu',
       'district_name': 'Kanchipuram',
       'block_name': 'Kancheepuram',
       'pincode': 631502,
       'from': '09:00:00',
       'to': '18:00:00',
       'lat': 12, 'long': 79,
       'fee_type': 'Free', 'session_id': '9d84f4bf-9565-486f-9346-b44e4f63fc77',
       'date': '18-05-2021', 'available_capacity_dose1': 30, 'available_capacity_dose2': 20,
       'available_capacity': 50, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVISHIELD',
       'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'center_id': 687772, 'name': 'Ayyampettai APHC Covaxin', 'address': 'APHC Thopu Street Ayyampettai Kancheepuram', 'state_name': 'Tamil Nadu', 'district_name': 'Kanchipuram', 'block_name': 'Walajabad', 'pincode': 631601, 'from': '09:00:00', 'to': '18:00:00', 'lat': 12, 'long': 79, 'fee_type': 'Free', 'session_id': 'be09311e-b156-410e-94ba-74f25238ae38', 'date': '18-05-2021', 'available_capacity_dose1': 79, 'available_capacity_dose2': 120, 'available_capacity': 199, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'center_id': 394576, 'name': 'Pillaiyarpalayam UPHC', 'address': 'UPHC Thiruvagamman Street Kancheepuram', 'state_name': 'Tamil Nadu', 'district_name': 'Kanchipuram', 'block_name': 'Kancheepuram', 'pincode': 631501, 'from': '09:00:00', 'to': '18:00:00', 'lat': 12, 'long': 79, 'fee_type': 'Free', 'session_id': 'b2208853-dcb8-46a5-86e9-705e6f8ebeda', 'date': '18-05-2021', 'available_capacity_dose1': 30, 'available_capacity_dose2': 20, 'available_capacity': 50, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'center_id': 247569, 'name': 'Panjupettai UPHC', 'address': 'UPHC Panjupettai Big Street Kancheepuram', 'state_name': 'Tamil Nadu', 'district_name': 'Kanchipuram', 'block_name': 'Kancheepuram', 'pincode': 631502, 'from': '09:00:00', 'to': '18:00:00', 'lat': 12, 'long': 79, 'fee_type': 'Free', 'session_id': '6c6160dc-b073-4bad-93bc-1b021cb64a49', 'date': '18-05-2021', 'available_capacity_dose1': 30, 'available_capacity_dose2': 20, 'available_capacity': 50, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'center_id': 247570, 'name': 'Chinna Kancheepuram UPHC', 'address': 'UPHC 61TK Nambi Street Chinna Kancheepuram', 'state_name': 'Tamil Nadu', 'district_name': 'Kanchipuram', 'block_name': 'Kancheepuram', 'pincode': 631501, 'from': '09:00:00', 'to': '18:00:00', 'lat': 12, 'long': 79, 'fee_type': 'Free', 'session_id': '97d3877a-7986-4768-a56f-611781ed1bc9', 'date': '18-05-2021', 'available_capacity_dose1': 30, 'available_capacity_dose2': 20, 'available_capacity': 50, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'center_id': 247571, 'name': 'Kancheepuram GH', 'address': 'GH Hospital Road Ennaikaran Kancheepuram', 'state_name': 'Tamil Nadu', 'district_name': 'Kanchipuram', 'block_name': 'Kancheepuram', 'pincode': 631501, 'from': '09:00:00', 'to': '18:00:00', 'lat': 12, 'long': 79, 'fee_type': 'Free', 'session_id': '80893ac8-c799-47bf-b409-c1c5fe242640', 'date': '18-05-2021', 'available_capacity_dose1': 59, 'available_capacity_dose2': 40, 'available_capacity': 99, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'center_id': 597616, 'name': 'Kancheepuram GH Covax', 'address': 'KPM GH COVAXIN', 'state_name': 'Tamil Nadu', 'district_name': 'Kanchipuram', 'block_name': 'Kancheepuram', 'pincode': 631501, 'from': '09:00:00', 'to': '18:00:00', 'lat': 12, 'long': 79, 'fee_type': 'Free', 'session_id': 'fe14fa19-5fed-4dae-8745-0b84c3146662', 'date': '18-05-2021', 'available_capacity_dose1': 71, 'available_capacity_dose2': 118, 'available_capacity': 189, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}]


@app.route("/")
def start():
    return  render_template("start.html")
@app.route("/",methods=["POST"])
def form():
       district=request.form["u"]
       date=request.form["d"]
       # val,date=input_val(district,date)


       return   render_template("index.html",posts=post)

@app.route("/")
def check():
       a=form()
       if a=="hi":
              return "HEllo guys"
       else:
              return  "NO"



if __name__=='__main__':
    app.run(debug=True)
