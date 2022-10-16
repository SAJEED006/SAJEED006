<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content=
"width=device-width, initial-scale=1.0">
<title>
Build a Survey Form using HTML and CSS
</title>

<style>

/* Styling the Body element i.e. Color,
Font, Alignment */
body {
background-color: #05c46b;
font-family: Verdana;
text-align: center;
}

/* Styling the Form (Color, Padding, Shadow) */
form {
background-color: #fff;
max-width: 500px;
margin: 50px auto;
padding: 30px 20px;
box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.5);
}

/* Styling form-control Class */
.form-control {
text-align: left;
margin-bottom: 25px;
}

/* Styling form-control Label */
.form-control label {
display: block;
margin-bottom: 10px;
}

/* Styling form-control input,
select, textarea */
.form-control input,
.form-control select,
.form-control textarea {
border: 1px solid #777;
border-radius: 2px;
font-family: inherit;
padding: 10px;
display: block;
width: 95%;
}

/* Styling form-control Radio
button and Checkbox */
.form-control input[type="radio"],
.form-control input[type="checkbox"] {
display: inline-block;
width: auto;
}

/* Styling Button */
button {
background-color: #05c46b;
border: 1px solid #777;
border-radius: 2px;
font-family: inherit;
font-size: 21px;
display: block;
width: 100%;
margin-top: 50px;
margin-bottom: 20px;
}
</style>
</head>

<body>
    <form method="post">
<h1>FORM</h1>

<!-- Create Form -->
<form id="form">

<!-- Details -->
<div class="form-control">
<label for="name" id="label-name">
Full Name
</label>

<!-- Input Type Text -->
<input type="text"
id="name"
name="name"
placeholder="Enter your name" />
</div>



<div class="form-control">
    <label for="name" id="label-name">
    Email
    </label>
    
    <!-- Input Type Text -->
    <input type="Email"
    id="Email"
    name="Email"
    placeholder="Enter your Email" />
    </div>


    <div class="form-control">
        <label for="name" id="label-name">
        Mobile Number
        </label>
        
        <!-- Input Type Text -->
        <input type="Mobile Number"
        id="Mobile Number"
        name="Mobile_Number"
        placeholder="Enter your Mobile Number" />
        </div>

        <div class="form-control">
            <label for="name" id="label-name">
            Gender
            </label>
            
            <!-- Input Type Text -->
            <input type="Gender"
            id="Gender"
            name="Gender"
            placeholder="Enter your Gender" />
            </div>

            <div class="form-control">
                <label for="name" id="label-name">
                Age
                </label>
                
                <!-- Input Type Text -->
                <input type="Age"
                id="Age"
                name="Age"
                placeholder="Enter your Age" />
                </div>


                <div class="form-control">
                    <label for="name" id="label-name">
                    Hobbies
                    </label>
                    
                    <!-- Input Type Text -->
                    <input type="Hobbies"
                    id="Hobbies"
                    name="Hobbies"
                    placeholder="Enter your Hobbies" />
                    </div>

                


<!-- Input Type Radio Button -->


<!-- Multi-line Text Input Control -->
<button type="submit" value="submit" name="submit">
Submit
</button>
</form>
</form>>
<?php
$con=mysqli_connect('localhost','root','','sajeed');
if(isset($_POST['submit']))
{
    $name=$_POST['name'];
    $email=$_POST['Email'];
    $mobilenumber=$_POST['Mobile_Number'];
    $gender=$_POST['Gender'];
    $age=$_POST['Age'];
    $hobbies=$_POST['Hobbies'];
    $query="INSERT INTO history(FULL_NAME,EMAIL,MOBILE_NUMBER,GENDER,AGE,HOBBIES)
    VALUES(' $name',' $email','$mobilenumber',' $gender','$age','$hobbies')";
    $run=mysqli_query($con,$query);
}
 
?>
</body>

</html>
